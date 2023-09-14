from models.player_profile import PlayerProfile
from models.player_bowling_stats import PlayerBowlingStats
from models.player_batting_fielding_stats import PlayerBattingFieldingStats
from models.csv_writer import CsvWriter
class PlayerDetailed:
    def __init__(
            self, 
            player_profile:PlayerProfile,
            player_bowling_stats:[PlayerBowlingStats],
            player_batting_fielding_stats : [PlayerBattingFieldingStats]
        ):
        self.player_profile : PlayerProfile = player_profile
        self.player_bowling_stats : [PlayerBowlingStats] = player_bowling_stats
        self.player_batting_fielding_stats : [PlayerBattingFieldingStats] = player_batting_fielding_stats
    
    @staticmethod
    def split_career_stats(career_stats_json):
        bowling_stats_json,batting_stats_json = [],[]
        for stat in career_stats_json:
            stat_type = str(stat.get('type'))
            if stat_type == 'BATTING':
                batting_stats_json.append(stat)
            elif stat_type == 'BOWLING':
                bowling_stats_json.append(stat)
        return {
            'batting':batting_stats_json,
            'bowling':bowling_stats_json
        }
    @staticmethod
    def parse_bowling_stats(bowling_stats_json)->[PlayerBowlingStats]:
        player_bowling_stats = []
        
        if not bowling_stats_json:
            return []
        
        for stat in bowling_stats_json:
            bowling_stat = PlayerBowlingStats.from_json(stat)
            player_bowling_stats.append(bowling_stat)

        return player_bowling_stats

    @staticmethod
    def parse_batting_stats(batting_stats_json)->[PlayerBattingFieldingStats] :
        if not batting_stats_json:
            return []
        
        player_batting_fielding_stats = []
        for stat in batting_stats_json:
            batting_stat = PlayerBattingFieldingStats.from_json(stat)
            player_batting_fielding_stats.append(batting_stat)
        
        return player_batting_fielding_stats


    @staticmethod
    def from_json(player_json):
        player_profile_json = player_json.get('player')
        career_stats_json = player_json.get('content').get('careerAverages').get('stats')
        
        player_profile = PlayerProfile.from_json(player_profile_json)
        
        stats = PlayerDetailed.split_career_stats(career_stats_json)
        
        bowling_stats_json = stats.get('bowling')
        batting_stats_json = stats.get('batting')
        
        player_batting_fielding_stats = PlayerDetailed.parse_batting_stats(batting_stats_json)
        player_bowling_stats = PlayerDetailed.parse_bowling_stats(bowling_stats_json)

        return PlayerDetailed(
            player_profile=player_profile,
            player_batting_fielding_stats=player_batting_fielding_stats,
            player_bowling_stats=player_bowling_stats
            )
    

    @staticmethod
    def write_profile_header(file_name:str = 'player_profiles.csv',header:list = None):
        csv_writer = CsvWriter(file_name)
        if not header:
            header = ['id','long_name','gender','image_url','headshot_image_url','dob','dod','country_team_id']
        
        csv_writer.write_header(header=header)

    def write_profile_to_csv(self, file_name:str = 'player_profiles.csv'):
        csv_writer = CsvWriter(file_name)
        profile_data = [
            self.player_profile.id,
            self.player_profile.long_name,
            self.player_profile.gender,
            self.player_profile.image_url,
            self.player_profile.headshot_image_url,
            self.player_profile.dob,
            self.player_profile.dod,
            self.player_profile.country_team_id
        ]
        csv_writer.write_row(profile_data)

    @staticmethod
    def write_bowling_stats_header(file_name:str = 'bowling_stats.csv', header:list = None):
        csv_writer = CsvWriter(file_path=file_name)
        if not header:
            header = [
               'player_id', 'match_format','matches',
               'innings','balls','runs','wickets',
               'best_bowling_innings','best_bowling_match',
               'average','economy','strike_rate',
               'four_wicket_hauls','five_wicket_hauls','ten_wicket_hauls'
            ]
        csv_writer.write_header(header=header)

    
    def write_bowling_stats_to_csv(self,file_name:str = 'bowling_stats.csv'):
        csv_writer = CsvWriter(file_path=file_name)
        player_bowling_stats = [
            [self.player_profile.id, bowling_stats.match_format, bowling_stats.matches,
             bowling_stats.innings, bowling_stats.balls,bowling_stats.runs,
             bowling_stats.wickets, bowling_stats.best_bowling_innings,bowling_stats.best_bowling_match,
             bowling_stats.average, bowling_stats.economy, bowling_stats.strike_rate,
             bowling_stats.four_wicket_hauls, bowling_stats.five_wicket_hauls, bowling_stats.ten_wicket_hauls
             ] 
            for bowling_stats in self.player_bowling_stats
        ]
        csv_writer.write_rows(player_bowling_stats)

    @staticmethod
    def write_batting_stats_header(file_name:str = 'batting_stats.csv', header:list = None):
        csv_writer = CsvWriter(file_path=file_name)
        if not header:
            header = [
                'player_id','match-format','matches',
                'innings','notouts','runs',
                'hi_score','average','balls_faced',
                'strike_rate','hundreds','fifties',
                'fours','sixes','catches','stumps'
            ]

        csv_writer.write_header(header=header)

    def write_batting_stats_to_csv(self,file_name:str = 'batting_stats.csv'):
        csv_writer = CsvWriter(file_path=file_name)
        player_batting_stats = [
            [
                self.player_profile.id, batting_stats.match_format, batting_stats.matches,
                batting_stats.innings, batting_stats.notouts, batting_stats.runs,
                batting_stats.hi_score, batting_stats.average, batting_stats.balls_faced,
                batting_stats.strike_rate, batting_stats.hundreds, batting_stats.fifties,
                batting_stats.fours, batting_stats.sixes, batting_stats.catches, batting_stats.stumps
            ] for batting_stats in self.player_batting_fielding_stats
        ]

        csv_writer.write_rows(player_batting_stats)