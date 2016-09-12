double_calculation_statistical_categories = ['total_rebounds', 'assists', 'steals', 'blocks', 'points']
statistical_categories_not_used_for_calculation = {
    'SECONDS_PLAYED': 'seconds_played',
    'FIELD_GOALS': 'field_goals',
    'THREE_POINT_FIELD_GOAL_ATTEMPTS': 'three_point_field_goal_attempts',
    'FREE_THROWS': 'free_throws',
    'FREE_THROW_ATTEMPTS': 'free_throw_attempts',
    'OFFENSIVE_REBOUNDS': 'offensive_rebounds',
    'DEFENSIVE_REBOUNDS': 'defensive_rebounds',
    'TOTAL_REBOUNDS': 'total_rebounds',
    'PERSONAL_FOULS': 'personal_fouls'
}
STATISTICAL_CATEGORIES_USED_FOR_DOUBLE_DOUBLE_CALCULATION = {
    'TOTAL_REBOUNDS': 'total_rebounds',
    'ASSISTS': 'assists',
    'STEALS': 'steals',
    'BLOCKS': 'blocks',
    'POINTS': 'points'
}
STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION = STATISTICAL_CATEGORIES_USED_FOR_DOUBLE_DOUBLE_CALCULATION.copy()
STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['TURNOVERS'] = 'turnovers'
STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['THREE_POINT_FIELD_GOALS'] = 'three_point_field_goals'
STATISTICAL_CATEGORIES = statistical_categories_not_used_for_calculation.copy()
STATISTICAL_CATEGORIES.update(STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION.copy())


def is_valid_box_score(box_score):
    for statistical_category in STATISTICAL_CATEGORIES:
        if statistical_category not in box_score:
            return False

    return True


def count_doubles(box_score):
    double_count = 0
    for statistic in double_calculation_statistical_categories:
        if getattr(box_score, statistic) > 9:
            double_count += 1

    return double_count


def is_triple_double(box_score):
    return count_doubles(box_score=box_score) > 2


def is_double_double(box_score):
    return count_doubles(box_score=box_score) == 2
