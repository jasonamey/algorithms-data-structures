from collections import defaultdict



def tournamentWinner(competitions, results):
      dd = defaultdict(int)
      max = 0
      winningTeam = ''
      for i in range(len(results)): 
          winningTeamIdx = results[i]
          winningTeamIdx = 1 if winningTeamIdx == 0 else 0
          teamName = competitions[i][winningTeamIdx]
          dd[teamName] += 1
      for winner in dd: 
          if dd[winner] > max: 
              max = dd[winner]
              winningTeam = winner
      return winningTeam

# c = [
#     ["HTML", "C#"],
#     ["C#", "Python"],
#     ["Python", "HTML"]
#   ]
# r = [0, 0, 1]
#
# tournamentWinner(c, r)
