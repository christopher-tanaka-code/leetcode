from typing import List

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        ans = [""] * len(score)

        for rank, idx in enumerate(sorted(range(len(score)), key=lambda i: -score[i]), 1):
            ans[idx] = medals[rank - 1] if rank <= 3 else str(rank)

        return ans