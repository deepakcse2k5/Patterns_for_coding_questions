from interval import *

def merge_interval(intervals):
    result = []
    # edge case
    if len(intervals)<=2:
        return intervals
    
    intervals = intervals.sort(key= lambda x:x.start)
    start = intervals[0].start
    end = intervals[0].end

    for i in range(1, len(intervals)):
        interval = intervals[i]
        if interval.start <= end:
            end = max(end, interval.end)
        else:
            result.append(Interval(start,end))
            start = interval.start
            end = interval.end
    result.append(Interval(start, end))
    return result


def merge_interval_v1(intervals):
    result = []
    if not intervals:
        return None
    
    # add first interval into result
    result.append([intervals[0][0], intervals[0][1]])

    
