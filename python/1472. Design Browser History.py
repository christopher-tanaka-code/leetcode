class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.i = 0  # current index

    def visit(self, url: str) -> None:
        # clear forward history
        self.history = self.history[:self.i + 1]
        self.history.append(url)
        self.i += 1

    def back(self, steps: int) -> str:
        self.i = max(0, self.i - steps)
        return self.history[self.i]

    def forward(self, steps: int) -> str:
        self.i = min(len(self.history) - 1, self.i + steps)
        return self.history[self.i]
