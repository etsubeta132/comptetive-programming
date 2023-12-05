class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        ghost_dist = []
        for ghost in  ghosts:
            min_dist = abs(ghost[0]-target[0])+abs(ghost[1]-target[1])
            ghost_dist.append(min_dist)
        
        pacman_dist = abs(target[0])+abs(target[1])
        can_pacman_reach = True
        for i in ghost_dist:
            if i<=pacman_dist:
                can_pacman_reach = False
        return can_pacman_reach
        
