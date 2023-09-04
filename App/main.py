from repository import Repository



def run():
    teams = Repository()
    for team in teams.teams_db.teams:
        players_count = len(team.players_db.players_shor_db)
        print(team.name, " has ", players_count, ' records')

if __name__ == "__main__":
    run()