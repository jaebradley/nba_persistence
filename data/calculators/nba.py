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
    if not nba_validators.is_valid_box_score(box_score):
        raise ValueError('illegal boxscore')
    else:
        score = 0
        if nba_validators.is_double_double(box_score=box_score):
            score += DRAFTKINGS_SCORING_VALUES['DOUBLE_DOUBLE']
        elif nba_validators.is_triple_double(box_score=box_score):
            score += DRAFTKINGS_SCORING_VALUES['TRIPLE_DOUBLE']

        for key, value in box_score.iteritems():
            multiplier = None
            if key is nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['POINTS']:
                multiplier = DRAFTKINGS_SCORING_VALUES['POINT']

            elif key is nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['THREE_POINT_FIELD_GOALS']:
                multiplier = DRAFTKINGS_SCORING_VALUES['MADE_THREE_POINT_SHOT']

            elif key is nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['TOTAL_REBOUNDS']:
                multiplier = DRAFTKINGS_SCORING_VALUES['REBOUND']

            elif key is nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['ASSISTS']:
                multiplier = DRAFTKINGS_SCORING_VALUES['ASSIST']

            elif key is nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['STEALS']:
                multiplier = DRAFTKINGS_SCORING_VALUES['STEAL']

            elif key is nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['BLOCKS']:
                multiplier = DRAFTKINGS_SCORING_VALUES['BLOCK']

            elif key is nba_validators.STATISTICAL_CATEGORIES_USED_FOR_DRAFTKINGS_CALCULATION['TURNOVERS']:
                multiplier = DRAFTKINGS_SCORING_VALUES['TURNOVER']

            if multiplier is not None:
                score *= float(multiplier) * value

        return score