import time
import requests
from models.player_short_db import PlayersShortDatabase
from models.teams_db import TeamsDatabase
from utils.constants import Urls
import json

class Repository:
    def __init__(self) -> None:
        self.db = TeamsDatabase()
        self.add_teams_data()
        self.add_players_short_data()


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
            self.db.insert_team_from_json(team_json)


    def add_players_short_data(self):
        if len(self.db.teams) == 0:
            return 
        for team in self.db.teams:
            time.sleep(2)
            player_db = PlayersShortDatabase(team_id=team.id)  
            player_db.insert_records()          
            team.players_db = player_db
            print(f'Added players to team {team.name}')
            
