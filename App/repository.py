import time
import requests
from models.player_detailed_db import PlayerDetailedDb
from models.player_short_db import PlayersShortDatabase
from models.teams_db import TeamsDatabase
from utils.constants import Urls
from models.player_detailed import PlayerDetailed
import json

class Repository:
    def __init__(self) -> None:
        self.teams_db = TeamsDatabase()
        self.players_detailed_db = PlayerDetailedDb()
        self.add_teams_data()
        self.add_players_short_data()
        self.add_players_detailed_data()
        


    def get_teams_data(self,teams_base_api):
        response = requests.get(teams_base_api)
        data = json.loads(response.content)
        groups = data.get('content').get('featuredTeamsGroups').get('groups')
        teams =[]
        for group in groups:
            group_title = str(group.get('title'))
            if group_title == "POPULAR MEN'S INTERNATIONAL TEAMS":
                teams = group.get('teams')
        return teams


    def get_players_by_team_id(team_id:int) -> PlayersShortDatabase:
        players_db = PlayersShortDatabase()
        players_db.insert_records()
        return players_db


    def add_teams_data(self):
        teams_json = self.get_teams_data(Urls.teams_base_api)
        for team_json in teams_json:
            self.teams_db.insert_team_from_json(team_json)


    def add_players_short_data(self):
        if len(self.teams_db.teams) == 0:
            return 
        for team in self.teams_db.teams:
            time.sleep(2)
            player_db = PlayersShortDatabase(team_id=team.id)  
            player_db.insert_records()          
            team.players_db = player_db
            print(f'Added players to team {team.name}')



    @staticmethod
    def get_player_detailed_from_url(url):
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.content)
        



    def add_players_detailed_data(self):

        if len(self.teams_db.teams) == 0:
            return
        
        for team in self.teams_db.teams[1:2]: # change the number of teams in the list during deployment
            if len(team.players_db.players_short_db) == 0:
                continue
            for player_short in team.players_db.players_short_db[:10]:
                player_json = Repository.get_player_detailed_from_url(player_short.get_url())
                if player_json is None:
                    continue
                player_detailed = PlayerDetailed.from_json(player_json)
                print(f"fetched player data for {player_detailed.player_profile.long_name}")
                self.players_detailed_db.players.append(player_detailed)
