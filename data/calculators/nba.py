import data.validators.nba as nba_validators


DRAFTKINGS_SCORING_VALUES = {
    'DOUBLE_DOUBLE': 1.5,
    'TRIPLE_DOUBLE': 3,
    'POINT': 1,
    'MADE_THREE_POINT_SHOT': 0.5,
    'REBOUND': 1.25,
    'ASSIST': 1.5,
    'STEAL': 2,
    'BLOCK': 2,
    'TURNOVER': -0.5
}


def calculate_draftkings_points(box_score):
    score = 0
    if nba_validators.is_double_double(box_score=box_score):
        score += DRAFTKINGS_SCORING_VALUES['DOUBLE_DOUBLE']
    elif nba_validators.is_triple_double(box_score=box_score):
        score += DRAFTKINGS_SCORING_VALUES['TRIPLE_DOUBLE']

    if hasattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['POINTS']):
        score += DRAFTKINGS_SCORING_VALUES['POINT'] * float(getattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['POINTS']))

    elif hasattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['THREE_POINT_FIELD_GOALS']):
        score += DRAFTKINGS_SCORING_VALUES['MADE_THREE_POINT_SHOT'] * float(getattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['THREE_POINT_FIELD_GOALS']))

    elif hasattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['TOTAL_REBOUNDS']):
        score += DRAFTKINGS_SCORING_VALUES['REBOUND'] * float(getattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['TOTAL_REBOUNDS']))

    elif hasattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['ASSISTS']):
        score += DRAFTKINGS_SCORING_VALUES['ASSIST'] * float(getattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['ASSISTS']))

    elif hasattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['STEALS']):
        score += DRAFTKINGS_SCORING_VALUES['STEAL'] * float(getattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['STEALS']))

    elif hasattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['BLOCKS']):
        score += DRAFTKINGS_SCORING_VALUES['BLOCK'] * float(getattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['BLOCKS']))

    elif hasattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['TURNOVERS']):
        score += DRAFTKINGS_SCORING_VALUES['TURNOVER'] * float(getattr(box_score, nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['TURNOVERS']))

    return score