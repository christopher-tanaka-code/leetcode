class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slots = 1

        for node in preorder.split(","):
            # Every node uses one available slot
            slots -= 1

            # If no slot is available, serialization is invalid
            if slots < 0:
                return False

            # Non-null nodes create two child slots
            if node != "#":
                slots += 2

        # Valid serialization uses all slots exactly
        return slots == 0