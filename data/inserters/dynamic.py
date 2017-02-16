# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import logging
import logging.config
import os
from django.db.utils import IntegrityError

from nba_data import Client as NbaClient, Season as NbaSeason, DateRange as NbaDateRange

from data.models import Team as TeamModel, Season as SeasonModel, Player as PlayerModel, \
    Game as GameModel, GamePlayerBoxScore as NbaGamePlayerBoxScoreModel, TeamPlayer as PlayerTeamModel

logging.config.fileConfig(os.path.join(os.path.dirname(__file__), '../../logging.conf'))
logger = logging.getLogger('inserter')

# TODO: @jbradley refactor all of this ASAP


def insert_players():
    logger.info('Inserting NBA players')
    for season in SeasonModel.objects.order_by('start_time'):
        logger.info('Fetching players from NBA API for season: %s' % season)
        query_season = NbaSeason.get_season_by_start_and_end_year(start_year=season.start_time.year,
                                                                  end_year=season.end_time.year)
        for player in NbaClient.get_players(season=query_season):
            logger.info('Player: %s' % player.__dict__)
            try:
                player_model_object, created = PlayerModel.objects.get_or_create(name=player.name.strip(),
                                                                                 source_id=player.player_id)
                logger.info('Created: %s | Player: %s', created, player_model_object)
            except IntegrityError:
                logger.error('Player with same source id: %s but different name: %s', player.player_id, player.name.strip())


def insert_games():
    logger.info('Insert NBA games')
    for season in SeasonModel.objects.order_by('start_time'):
        logger.info('Season: %s' % season)
        game_counts = NbaClient.get_game_counts_in_date_range(NbaDateRange(start=season.start_time.date(),
                                                                           end=season.end_time.date()))
        for date_value, game_count in game_counts.items():
            logger.info('%s games on %s', game_count, date_value)
            for game in NbaClient.get_games_for_date(date_value=date_value):
                logger.info('Inserting game: %s' % game.__dict__)
                # TODO: @jbradley deal with All Star game
                if game.matchup.home_team is not None and game.matchup.away_team is not None:
                    logger.info('Game Id: %s' % game.game_id)
                    logger.info('Home Team: %s vs. Away Team: %s @ %s',
                                game.matchup.home_team, game.matchup.away_team, game.start_time)
                    home_team = TeamModel.objects.get(name=game.matchup.home_team.value)
                    away_team = TeamModel.objects.get(name=game.matchup.away_team.value)
                    game, created = GameModel.objects.get_or_create(home_team=home_team, away_team=away_team,
                                                                    season=season, start_time=game.start_time,
                                                                    source_id=game.game_id)
                    logger.info('Created: %s | Game: %s', created, game)


def insert_box_scores():
    for season in SeasonModel.objects.order_by('start_time'):
        for game in GameModel.objects.filter(start_time__lte=season.end_time).filter(start_time__gte=season.start_time):
            logger.info('Getting traditional box score for: %s', game.source_id)
            traditional_box_score = NbaClient.get_traditional_box_score(game_id=str(game.source_id))
            for player_box_score in traditional_box_score.player_box_scores:
                player_name = player_box_score.player.name.strip()
                player_id = player_box_score.player.id
                team_player_name = player_box_score.player.team.value
                team = TeamModel.objects.get(name=team_player_name)
                try:
                    player, created = PlayerModel.objects.get_or_create(name=player_name, source_id=player_id)
                    logger.info('Created: %s | Player: %s', created, player)
                except IntegrityError:
                    logger.error('Player with same source id: %s but different name: %s', player_id, player_name)
                    player = PlayerModel.objects.get(source_id=player_id)
                team_player, created = PlayerTeamModel.objects.get_or_create(player=player, team=team)
                logger.info('Created:%s | Team Player: %s', created, team_player)
                box_score, created = NbaGamePlayerBoxScoreModel.objects.get_or_create(
                        game=game, team_player=team_player, status=player_box_score.player.status.type.value,
                        explanation=player_box_score.player.status.comment,
                        seconds_played=player_box_score.seconds_played,
                        field_goals_made=player_box_score.field_goals_made,
                        field_goals_attempted=player_box_score.field_goal_attempts,
                        three_point_field_goals_made=player_box_score.three_point_field_goals_made,
                        three_point_field_goals_attempted=player_box_score.three_point_field_goal_attempts,
                        free_throws_made=player_box_score.free_throws_made,
                        free_throws_attempted=player_box_score.free_throw_attempts,
                        offensive_rebounds=player_box_score.offensive_rebounds,
                        defensive_rebounds=player_box_score.defensive_rebounds,
                        assists=player_box_score.assists, steals=player_box_score.steals,
                        blocks=player_box_score.blocks, turnovers=player_box_score.turnovers,
                        personal_fouls=player_box_score.personal_fouls,
                        plus_minus=player_box_score.plus_minus)
                logger.info('Created: %s | Box Score: %s', created, box_score)