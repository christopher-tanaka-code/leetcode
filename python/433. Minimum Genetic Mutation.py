from collections import deque
from typing import List

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)  # Quick lookup for valid genes
        if endGene not in bank_set:
            return -1  # If endGene is not in the bank, impossible to reach
        
        # BFS queue: stores (current_gene, mutations_count)
        queue = deque([(startGene, 0)])
        visited = set([startGene])
        genes = ['A', 'C', 'G', 'T']
        
        while queue:
            current, steps = queue.popleft()
            
            if current == endGene:
                return steps
            
            # Try mutating each position
            for i in range(8):
                for g in genes:
                    if g != current[i]:
                        mutated = current[:i] + g + current[i+1:]
                        if mutated in bank_set and mutated not in visited:
                            visited.add(mutated)
                            queue.append((mutated, steps + 1))
        
        return -1  # No path found
