from utils.helpers import get_format_by_id
from models.csv_writer import CsvWriter
class PlayerBattingFieldingStats:
    def __init__(
        self,
        match_format = '',
        matches = 0,
        innings = 0,
        notouts = 0,
        runs = 0,
        hi_score = 0,
        average = 0,
        balls_faced = 0,
        strike_rate = 0,
        hundreds = 0,
        fifties = 0,
        fours = 0,
        sixes = 0,
        catches = 0 ,
        stumps = 0
    ) -> None:
        self.match_format = match_format
        self.matches = matches
        self.innings = innings
        self.notouts = notouts
        self.runs = runs
        self.hi_score = hi_score
        self.average = average
        self.balls_faced = balls_faced
        self.strike_rate = strike_rate
        self.hundreds = hundreds
        self.fifties = fifties
        self.fours = fours
        self.sixes = sixes
        self.catches = catches
        self.stumps = stumps
    
    def from_json(json):
        return PlayerBattingFieldingStats(
            match_format= get_format_by_id(json.get('cl')),
            matches=json.get('mt'),
            innings=json.get('in'),
            notouts=json.get('no'),
            runs = json.get('rn'),
            hi_score=json.get('hs'),
            average= json.get('avg'),
            balls_faced= json.get('bl'),
            strike_rate = json.get('sr'),
            hundreds=json.get('hn'),
            fifties= json.get('ft'),
            fours= json.get('fo'),
            sixes=json.get('si'),
            catches = json.get('ct'),
            stumps= json.get('st')
        )
    
    def __repr__(self):
        return (
            f"PlayerBattingFieldingStats("
            f"match_format={self.match_format!r}, "
            f"matches={self.matches}, "
            f"innings={self.innings}, "
            f"notouts={self.notouts}, "
            f"runs={self.runs}, "
            f"hi_score={self.hi_score}, "
            f"average={self.average}, "
            f"balls_faced={self.balls_faced}, "
            f"strike_rate={self.strike_rate}, "
            f"hundreds={self.hundreds}, "
            f"fifties={self.fifties}, "
            f"fours={self.fours}, "
            f"sixes={self.sixes}, "
            f"catches={self.catches}, "
            f"stumps={self.stumps})"
        )

    def __str__(self):
        return (
            f"Player Batting & Fielding Stats:\n"
            f"Match Format: {self.match_format}\n"
            f"Matches: {self.matches}\n"
            f"Innings: {self.innings}\n"
            f"Not Outs: {self.notouts}\n"
            f"Runs: {self.runs}\n"
            f"Highest Score: {self.hi_score}\n"
            f"Average: {self.average}\n"
            f"Balls Faced: {self.balls_faced}\n"
            f"Strike Rate: {self.strike_rate}\n"
            f"Hundreds: {self.hundreds}\n"
            f"Fifties: {self.fifties}\n"
            f"Fours: {self.fours}\n"
            f"Sixes: {self.sixes}\n"
            f"Catches: {self.catches}\n"
            f"Stumps: {self.stumps}"
        )


