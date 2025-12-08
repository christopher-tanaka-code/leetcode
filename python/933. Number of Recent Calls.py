from collections import deque

class RecentCounter:

    def __init__(self):
        # Initialize a deque to store timestamps of requests
        self.requests = deque()

    def ping(self, t: int) -> int:
        # Add the new request
        self.requests.append(t)
        
        # Remove requests that are older than t - 3000
        while self.requests and self.requests[0] < t - 3000:
            self.requests.popleft()
        
        # Return the number of requests within the last 3000 milliseconds
        return len(self.requests)