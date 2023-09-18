from utils.constants import Constants
import time
import requests
from models.player_detailed_db import PlayerDetailedDb
from models.player_short_db import PlayersShortDatabase
from models.teams_db import TeamsDatabase
from utils.constants import Urls
from models.player_detailed import PlayerDetailed
import pandas as pd
import json
import concurrent.futures

class Repository:
    def __init__(self) -> None:
        self.teams_db = TeamsDatabase()
        self.players_short_db = []
        self.players_detailed_db = PlayerDetailedDb()
        self.players_json = []
        #self.add_teams_data()
        #self.teams_db.write_csv()
        #self.add_players_short_data()
        #self.write_player_short_data()
        self.get_player_detailed_json()
        self.add_player_detailed_from_json()
        self.write_players_detailed_to_csv()
        


    def get_teams_data(self,teams_base_api):
        '''fetches the list of teams from the specified domain of game using the team base api'''
        response = requests.get(teams_base_api)
        data = json.loads(response.content)
        groups = data.get('content').get('featuredTeamsGroups').get('groups')
        teams =[]
        for group in groups:
            group_title = str(group.get('title'))
            if group_title == Constants.MENS_INTERNATIONAL_TEAMS:
                teams = group.get('teams')
        return teams


    def get_players_by_team_id(team_id:int) -> PlayersShortDatabase:
        '''fetch the list of players using the team id and return list of player short database'''
        players_db = PlayersShortDatabase()
        players_db.insert_records()
        return players_db


    def add_teams_data(self):
        '''inserts teams data from the json data to teams_db'''
        teams_json = self.get_teams_data(Urls.teams_base_api)
        for team_json in teams_json:
            self.teams_db.insert_team_from_json(team_json)


    def add_players_short_data(self):
        '''Add players short data to the repository data can be accessed using players_short_db'''
        if len(self.teams_db.teams) == 0:
            return 
        for team in self.teams_db.teams:
            time.sleep(2)
            players_db = PlayersShortDatabase(team_id=team.id)
            players_db.insert_records()   
            self.players_short_db.append(players_db)
            print(f'Added players to team {team.name}')



    
    def get_player_detailed_from_url(self,url):
        '''get the detailed player data in json format from the url'''
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.content)
        
         
    
    def add_player_detailed_from_json(self):
        if len(self.players_json) == 0:
            print("No players json found :(")
            return
        for player_json in self.players_json:
            player_detailed = PlayerDetailed.from_json(player_json=player_json)
            self.players_detailed_db.players.append(player_detailed)

    def get_player_detailed_json(self):
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            urls = self.get_player_urls()
            players_json = list(executor.map(self.get_player_detailed_from_url,urls))
            self.players_json = players_json

    def write_player_short_data(self,file_name = Constants.PLAYER_SHORT_FILE_NAME):
        '''write the player short data into csv file '''
        for team_players in self.players_short_db:
            team_players.write_csv(file_name = file_name)

    # def add_players_detailed_data(self):
    #     '''adds player data into the players_detailed.players variable '''
    #     for player_url in Repository.get_player_urls(self):
    #         player_json = Repository.get_player_detailed_from_url(player_url)
    #         if player_json is None:
    #             continue
    #         player_detailed = PlayerDetailed.from_json(player_json)
    #         print(f"fetched player data for {player_detailed.player_profile.long_name}")
    #         self.players_detailed_db.players.append(player_detailed)

    def get_player_urls(self,file_name = Constants.PLAYER_SHORT_FILE_NAME ):
        df = pd.read_csv(file_name,names=['id','slug','url'])
        return df['url']

    def write_players_detailed_to_csv(self):
        PlayerDetailed.write_profile_header()
        PlayerDetailed.write_batting_stats_header()
        PlayerDetailed.write_bowling_stats_header()
        players = self.players_detailed_db.players
        
        for player in self.players_detailed_db.players:
            player.write_profile_to_csv()
            player.write_batting_stats_to_csv()
            player.write_bowling_stats_to_csv()


