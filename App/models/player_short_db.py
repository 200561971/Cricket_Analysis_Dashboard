import requests
import json
from utils.constants import Urls
from models.player_short import PlayerShort
class PlayersShortDatabase:
    
    def __init__(self,team_id):
        self.team_id = team_id
        self.players_short_db = []
        self.total_players = 0
        self.records_per_page = 40
    
    def get_page_records(self,page_num):
        page_num = page_num
        records = self.records_per_page
        base_url = Urls.player_query_url
        params = {
            'mode':'BOTH',
            'page':page_num,
            'records':records,
            'filterActive':'false',
            'filterTeamId': self.team_id,
            'filterFormatLevel':"INTERNATIONAL",
            'sort':'ALPHA_ASC'
        }

        response = requests.get(base_url,params=params)
        data = None
        if response.status_code == 200:
            data = json.loads(response.content)
        else:
            print(f"There was error gathering data from page:{page_num}.\nStatusCode:{response.status_code}\n{str(response.content)}")
        return data
    
    def get_total_players(self):
        content = self.get_page_records(page_num=1)
        self.total_players = content.get('total')
        return self.total_players
    
    def get_total_page_nums(self):
        self.get_total_players()
        total_pages = (self.total_players // self.records_per_page) + 1
        return total_pages
    
    def parse_player_data_from_records(self,records:list):
        for player in records:
            self.players_short_db.append(PlayerShort.from_json(player))
    
    def insert_records(self):
        page_nums = self.get_total_page_nums()
        for page_num in range(1, page_nums+1):
            print(f"Gathering data from page:{page_num}".ljust(35," "),end="\r")
            player_data = self.get_page_records(page_num=page_num)
            records = player_data.get('results')
            self.parse_player_data_from_records(records)
        print(f"Gathered ids of {len(self.players_short_db)} of {self.total_players} players")
        