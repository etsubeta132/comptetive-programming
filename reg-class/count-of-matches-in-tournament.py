class Solution:
    def numberOfMatches(self, n: int) -> int:
        # even each team gets paired with another team total n/2 matches n/2 next round
        #  odd one team randomly advances rest gets paired n-1/2 matches n-1/2+1 next round
        teams = n
        team_adv = 0
        tot_match = 0
        while teams >= 2:
            if teams%2:
                teams = teams-1
                matches = teams/2
                teams = (teams/2)+1
            else:
                matches = teams/2
                teams = teams/2
            teams = teams
            tot_match+=matches
        return int(tot_match)



        