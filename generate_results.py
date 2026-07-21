from operator import attrgetter


def report_ranking(team_db):
    team_db.sort(key = attrgetter('elo'), reverse = True)
    filename = "test.txt"
    with open(filename, "w") as doc:
        rank = 1
        for team in team_db:
            doc.write(f"Rank {rank}: {team.name} ({team.elo:.2f} pts.)\n")
            rank +=1
    print(f"Ranking generated as {filename} in root!")
