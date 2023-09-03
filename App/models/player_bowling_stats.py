from utils.helpers import get_format_by_id
class PlayerBowlingStats:
    def __init__(
        self,
        match_format = '',
        matches = 0,
        innings = 0,
        balls = 0,
        runs = 0,
        wickets = 0,
        best_bowling_innings='',
        best_bowling_match ='',
        average = 0,
        economy = 0,
        strike_rate =0,
        four_wicket_hauls =0,
        five_wicket_hauls = 0,
        ten_wicket_hauls = 0
    ) -> None:
        self.match_format = match_format
        self.matches = matches
        self.innings = innings
        self.balls = balls
        self.runs = runs
        self.wickets = wickets
        self.best_bowling_innings = best_bowling_innings
        self.best_bowling_match = best_bowling_match
        self.average = average
        self.economy = economy
        self.strike_rate = strike_rate
        self.four_wicket_hauls = four_wicket_hauls
        self.five_wicket_hauls = five_wicket_hauls
        self.ten_wicket_hauls  = ten_wicket_hauls

    def from_json(json):
        return PlayerBowlingStats(
            match_format= get_format_by_id(json.get('cl')),
            matches= json.get('mt'),
            innings=json.get('in'),
            balls=json.get('bl'),
            runs=json.get('rn'),
            wickets = json.get('wk'),
            best_bowling_innings= json.get('bbi'),
            best_bowling_match= json.get('bbm'),
            average = json.get('avg'),
            economy= json.get('bwe'),
            strike_rate= json.get('sr'),
            four_wicket_hauls= json.get('fwk'),
            five_wicket_hauls= json.get('fw'),
            ten_wicket_hauls= json.get('tw')
        )
    def __repr__(self):
        return (
            f"PlayerBowlingStats("
            f"match_format={self.match_format!r}, "
            f"matches={self.matches}, "
            f"innings={self.innings}, "
            f"balls={self.balls}, "
            f"runs={self.runs}, "
            f"wickets={self.wickets}, "
            f"best_bowling_innings={self.best_bowling_innings!r}, "
            f"best_bowling_match={self.best_bowling_match!r}, "
            f"average={self.average}, "
            f"economy={self.economy}, "
            f"strike_rate={self.strike_rate}, "
            f"four_wicket_hauls={self.four_wicket_hauls}, "
            f"five_wicket_hauls={self.five_wicket_hauls}, "
            f"ten_wicket_hauls={self.ten_wicket_hauls})"
        )

    def __str__(self):
        return (
            f"Player Bowling Stats:\n"
            f"Match Format: {self.match_format}\n"
            f"Matches: {self.matches}\n"
            f"Innings: {self.innings}\n"
            f"Balls: {self.balls}\n"
            f"Runs: {self.runs}\n"
            f"Wickets: {self.wickets}\n"
            f"Best Bowling (Innings): {self.best_bowling_innings}\n"
            f"Best Bowling (Match): {self.best_bowling_match}\n"
            f"Average: {self.average}\n"
            f"Economy: {self.economy}\n"
            f"Strike Rate: {self.strike_rate}\n"
            f"Four Wicket Hauls: {self.four_wicket_hauls}\n"
            f"Five Wicket Hauls: {self.five_wicket_hauls}\n"
            f"Ten Wicket Hauls: {self.ten_wicket_hauls}"
        )

