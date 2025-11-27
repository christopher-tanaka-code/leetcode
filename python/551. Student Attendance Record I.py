class Solution:
    def checkRecord(self, s: str) -> bool:
        absences = 0
        late_streak = 0
        
        for ch in s:
            if ch == 'A':
                absences += 1
                if absences >= 2:
                    return False
                late_streak = 0
            elif ch == 'L':
                late_streak += 1
                if late_streak >= 3:
                    return False
            else:  # 'P'
                late_streak = 0
        
        return True
