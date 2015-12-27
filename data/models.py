from __future__ import unicode_literals

from django.db.models import Model, IntegerField, CharField, DateTimeField, FloatField, ForeignKey, CASCADE


class Position(Model):

    name = CharField(max_length=50)
    abbreviation = CharField(max_length=10)

    class Meta:
        unique_together = ('name', 'abbreviation')


class Team(Model):

    name = CharField(max_length=200)
    abbreviation = CharField(max_length=100)

    class Meta:
        unique_together = ('name', 'abbreviation')


class Season(Model):

    start_year = IntegerField(unique=True)


class Game(Model):

    home_team = ForeignKey(Team, on_delete=CASCADE, related_name='home_team')
    away_team = ForeignKey(Team, on_delete=CASCADE, related_name='away_team')
    start_time = DateTimeField()
    season = ForeignKey(Season, on_delete=CASCADE)

    class Meta:
        unique_together = ('home_team', 'away_team', 'start_time')


class Player(Model):

    first_name = CharField(max_length=250)
    last_name = CharField(max_length=250)
    team = ForeignKey(Team, on_delete=CASCADE)
    position = ForeignKey(Position, on_delete=CASCADE)

    class Meta:
        unique_together = ('first_name', 'last_name', 'team', 'position')


class DraftkingsPlayerSalary(Model):

    game = ForeignKey(Game, on_delete=CASCADE)
    player = ForeignKey(Player, on_delete=CASCADE)
    salary = FloatField()

    class Meta:
        unique_together = ('game', 'player', 'salary')


class BoxScore(Model):

    player = ForeignKey(Player, on_delete=CASCADE)
    game = ForeignKey(Game, on_delete=CASCADE)
    seconds_played = IntegerField()
    field_goals = IntegerField()
    field_goal_attempts = IntegerField()
    three_point_field_goals = IntegerField()
    three_point_field_goal_attempts = IntegerField()
    free_throws = IntegerField()
    free_throw_attempts = IntegerField()
    offensive_rebounds = IntegerField()
    defensive_rebounds = IntegerField()
    total_rebounds = IntegerField()
    assists = IntegerField()
    steals = IntegerField()
    blocks = IntegerField()
    turnovers = IntegerField()
    fouls_committed = IntegerField()
    points = IntegerField()
    draftkings_points = FloatField()

    class Meta:
        unique_together = ('player', 'game')
