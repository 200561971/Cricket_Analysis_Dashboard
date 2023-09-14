from models.team import Team
from models.csv_writer import CsvWriter
class TeamsDatabase:
    def __init__(self) -> None:
        self.teams : [Team] = []

    def insert_team(self, team:Team):
        self.teams.append(team)
    
    def remove_team(self, team_id:int):
        if len(self.teams) == 0:
            print(f"No teams in Database!")
        for team in self.teams:
            if team.id == team_id and isinstance(team, Team):
                self.teams.remove(team)
                print(f"Removed team '{team.name} with id: {team.id}'")

    def insert_team_from_json(self,team_json):
        team = Team.from_json(team_json)
        self.teams.append(team)
        print(f"Added new team {team.name} with id: {team.id} to Database")
    
    def write_csv(self):
        csv_writer = CsvWriter(file_path="teams.csv")
        header = ['id','name','slug','abbr','flag_url']
        team_rows = [ [team.id, team.name, team.slug, team.abbr,team.flag_url] for team in self.teams]
        csv_writer.write_header(header)
        csv_writer.write_rows(team_rows)
