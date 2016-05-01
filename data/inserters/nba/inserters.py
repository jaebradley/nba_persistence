import data.translators.nba as nba_translators
from data.models import BoxScore


def insert_box_score(box_score):
    BoxScore.objects.update_or_create(
            player=box_score.player,
            game=box_score.game,
            seconds_played=box_score.seconds_played,
            field_goals=box_score.field_goals,
            field_goal_attempts=box_score.field_goal_attempts,
            three_point_field_goals=box_score.three_point_field_goals,
            three_point_field_goal_attempts=box_score.three_point_field_goal_attempts,
            free_throws=box_score.free_throws,
            free_throw_attempts=box_score.free_throw_attempts,
            offensive_rebounds=box_score.offensive_rebounds,
            defensive_rebounds=box_score.defensive_rebounds,
            total_rebounds=box_score.total_rebounds,
            assists=box_score.assists,
            steals=box_score.steals,
            blocks=box_score.blocks,
            turnovers=box_score.turnovers,
            fouls_committed=box_score.personal_fouls,
            points=box_score.points,
            draftkings_points=box_score.draftkings_points
        )


def insert_box_scores(minimum_date, maximum_date):
    for date in nba_translators.translate_date_range_to_distinct_start_days(minimum_date=minimum_date,
                                                                            maximum_date=maximum_date):
        for box_score in nba_translators.translate_date_to_box_scores(start_day=date):
            insert_box_score(box_score=box_score)


