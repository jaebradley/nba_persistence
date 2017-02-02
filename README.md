# DEPRECATED

# NBA Data API

## Purpose
For a lot of different projects, I find myself needing NBA box score data (estimating daily fantasy sports performance, for example). This project currently tries to capture box score data found on [basketball-reference.com](http://www.basketball-reference.com/friv/dailyleaders.cgi?lid=header_dateoutput&month=01&day=02&year=2016) and create queryable API endpoints for public consumption.

## API
Here's a sample of what the box score API endpoint looks like ![alt text](https://i.imgur.com/4Ipx4LL.png)

* Endpoints
  * [Positions](https://nba-persistence.herokuapp.com/positions/) 
  * [Teams](https://nba-persistence.herokuapp.com/teams/)
  * [Seasons](https://nba-persistence.herokuapp.com/seasons/)
  * [Games](https://nba-persistence.herokuapp.com/games/)
  * [Players](https://nba-persistence.herokuapp.com/players/)
  * [Box Scores](https://nba-persistence.herokuapp.com/box_scores/)
  * [Daily Fantasy Sports Sites](https://nba-persistence.herokuapp.com/daily_fantasy_sports_sites/) (BETA!)
  * [Player Salaries](https://nba-persistence.herokuapp.com/player_salaries/) (BETA!)

* Caveats (Because there always are...)
  * This project is in active development and I make no guarantees as to the accuracy or the service's uptime.
  * Currently only data from 2015-2016 season
  * Because `basketball-reference.com` posts their box score data the day after, this is non-live box score data.
  * There are some known issues with the calculation of `draftkings_points` in the box score endpoint - however, I think the scores are 90% accurate.

