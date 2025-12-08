from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()
        
        # Fill the initial queues with indices
        for i, s in enumerate(senate):
            if s == 'R':
                radiant.append(i)
            else:
                dire.append(i)
        
        # Simulate the rounds
        while radiant and dire:
            r_index = radiant.popleft()
            d_index = dire.popleft()
            
            # The senator with the smaller index bans the other
            if r_index < d_index:
                radiant.append(r_index + n)  # Goes to the end for the next round
            else:
                dire.append(d_index + n)
        
        return "Radiant" if radiant else "Dire"
