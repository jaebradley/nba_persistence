import data.translators.nba as nba_translators
import data.validators.nba as nba_validators
from data.models import BoxScore


def insert_box_score(box_score):
    translated_box_score = nba_translators.translate_box_score(box_score=box_score)
    BoxScore.objects.update_or_create(
            player=translated_box_score.player,
            game=translated_box_score.game,
            seconds_played=translated_box_score.seconds_played,
            field_goals=translated_box_score.field_goals,
            field_goal_attempts=translated_box_score.field_goal_attempts,
            three_point_field_goals=translated_box_score.three_point_field_goals,
            three_point_field_goal_attempts=translated_box_score.three_point_field_goal_attempts,
            free_throws=translated_box_score.free_throws,
            free_throw_attempts=translated_box_score.free_throw_attempts,
            offensive_rebounds=translated_box_score.offensive_rebounds,
            defensive_rebounds=translated_box_score.defensive_rebounds,
            total_rebounds=translated_box_score.total_rebounds,
            assists=translated_box_score.assists,
            steals=translated_box_score.steals,
            blocks=translated_box_score.blocks,
            turnovers=translated_box_score.turnovers,
            fouls_committed=translated_box_score.personal_fouls,
            points=translated_box_score.points,
            draftkings_points=translated_box_score.draftkings_points
        )


def insert_box_scores(minimum_date, maximum_date):
    for date in nba_translators.translate_date_range_to_distinct_start_days(minimum_date=minimum_date,
                                                                            maximum_date=maximum_date):
        for box_score in nba_translators.translate_date_to_box_scores(start_day=date):
            insert_box_score(box_score=box_score)


