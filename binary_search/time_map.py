class TimeMap:
    def __init__(self):
        self.store = {}

    def set(self, key, value, timestamp):
        if key not in self.store:
            self.store[key]= {}
        self.store[key][timestamp] = value
    
    def get(self, key, timestamp):
        if key not in self.store:
            return ""
        time_dict = self.store[key]

        closed_timestamp = -1

        for t in time_dict:
            if t<=timestamp and (closed_timestamp == -1 and t>closed_timestamp):
                closed_timestamp = t
        if closed_timestamp==-1:
            return ""
        else:
            return time_dict[closed_timestamp]
        

time_map = TimeMap()
time_map.set("alice", "happy", 1)
print(time_map.get("alice", 1))    # Outputs: happy
print(time_map.get("alice", 2))    # Outputs: happy
time_map.set("alice", "sad", 3)
print(time_map.get("alice", 3))    # Outputs: sad


