class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie

        # Each pig has rounds + 1 possible states:
        # dies in round 1, dies in round 2, ..., dies in last round, or survives
        states = rounds + 1

        pigs = 0
        detectable_buckets = 1

        while detectable_buckets < buckets:
            pigs += 1
            detectable_buckets *= states

        return pigs