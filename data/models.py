from __future__ import unicode_literals

# Create your models here.


from django.db.models import Model, BigIntegerField, CharField, DateTimeField, ForeignKey, \
    CASCADE


class Position(Model):
    name = CharField(max_length=100, unique=True)

    def __unicode__(self):
        return '{0}'.format(self.name)


class Season(Model):
    start_time = DateTimeField(unique=True)
    end_time = DateTimeField(unique=True)

    def __unicode__(self):
        return '{0} - {1}'.format(self.start_time, self.end_time)


class Team(Model):
    name = CharField(max_length=100, unique=True)

    def __unicode__(self):
        return '{0}'.format(self.name)


class Player(Model):
    name = CharField(max_length=250)
    source_id = CharField(max_length=250, unique=True)

    class Meta:
        unique_together = ('name', 'source_id')

    def __unicode__(self):
        return '{0} - {1}'.format(self.name, self.source_id)


class TeamPlayer(Model):
    team = ForeignKey(Team, on_delete=CASCADE)
    player = ForeignKey(Player, on_delete=CASCADE)

    class Meta:
        unique_together = ('team', 'player')

    def __unicode__(self):
        return '{0} - {1}'.format(self.team, self.player)


class Game(Model):
    home_team = ForeignKey(Team, on_delete=CASCADE, related_name='home_team')
    away_team = ForeignKey(Team, on_delete=CASCADE, related_name='away_team')
    season = ForeignKey(Season, on_delete=CASCADE)
    start_time = DateTimeField()
    source_id = CharField(max_length=250, unique=True)

    class Meta:
        unique_together = ('home_team', 'away_team', 'season', 'start_time')

    def __unicode__(self):
        return '{0} - {1} - {2} - {3} - {4}'.format(self.home_team, self.away_team, self.season, self.start_time, self.source_id)


class GamePlayerBoxScore(Model):
    game = ForeignKey(Game, on_delete=CASCADE)
    team_player = ForeignKey(TeamPlayer, on_delete=CASCADE)
    status = CharField(max_length=100)
    explanation = CharField(max_length=250, default=None, null=True)
    seconds_played = BigIntegerField(null=True)
    field_goals_made = BigIntegerField(null=True)
    field_goals_attempted = BigIntegerField(null=True)
    three_point_field_goals_made = BigIntegerField(null=True)
    three_point_field_goals_attempted = BigIntegerField(null=True)
    free_throws_made = BigIntegerField(null=True)
    free_throws_attempted = BigIntegerField(null=True)
    offensive_rebounds = BigIntegerField(null=True)
    defensive_rebounds = BigIntegerField(null=True)
    assists = BigIntegerField(null=True)
    steals = BigIntegerField(null=True)
    blocks = BigIntegerField(null=True)
    turnovers = BigIntegerField(null=True)
    personal_fouls = BigIntegerField(null=True)
    plus_minus = BigIntegerField(null=True)

    class Meta:
        unique_together = ('game', 'team_player')

    def __unicode__(self):
        return '{0} - {1}'.format(self.game, self.team_player)
