from typing import List

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Taller people first.
        # For same height, smaller k first.
        people.sort(key=lambda person: (-person[0], person[1]))

        queue = []

        for person in people:
            queue.insert(person[1], person)

        return queue