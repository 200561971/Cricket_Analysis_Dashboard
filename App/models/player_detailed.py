from models.player_profile import PlayerProfile
from models.player_bowling_stats import PlayerBowlingStats
from models.player_batting_fielding_stats import PlayerBattingFieldingStats

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
        