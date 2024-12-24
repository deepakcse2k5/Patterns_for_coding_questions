class Interval:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.closed = True
    def set_closed(self, closed):
        self.closed = closed
    
    def __str__(self) -> str:
        return "[" + str(self.start) + ", " + str(self.end) + "]" if self.closed else \
        "(" + str(self.start) + ", " + str(self.end) + ")"
    

    