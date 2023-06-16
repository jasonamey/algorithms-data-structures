from collections import defaultdict

def tournamentWinner(competitions, results):
    dd = defaultdict(int)
    for i in range(0, len(results)):
        winnerIdx = results[i]
        i = 0 if i == 1 else 1
        winner = competitions[i][winnerIdx]
        dd[winner] = dd[winner] + 1
        print(dd)
    maxWins = 0
    currWinner = ""
    for team in dd:
        if dd[team] > maxWins:
            maxWins = dd[team]
            currWinner = team
    return currWinner

# c = [
#     ["HTML", "C#"],
#     ["C#", "Python"],
#     ["Python", "HTML"]
#   ]
# r = [0, 0, 1]
#
# tournamentWinner(c, r)
