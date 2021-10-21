# Add a new time window into an array of presorted time window
# sorted by the start time
# Time complexity O(n), space complexity O(n)
# The key is to have `interval_to_merge` to keep merging until the rest
# of the interval arrays is larger

def add_interval(intervals, new_interval):
    result = []
    interval_to_merge = new_interval  # key step
    for i, cur_interval in enumerate(intervals):
        if cur_interval[1] < interval_to_merge[0]:
            result.append(cur_interval)
        elif cur_interval[0] > interval_to_merge[1]:
            result.append(interval_to_merge)
            return result + intervals[i:]  # key step
        else:
            interval_to_merge = [min(cur_interval[0], interval_to_merge[0]), max(cur_interval[1], interval_to_merge[1])]
    result.append(interval_to_merge)
    return result

intervals = [[1,5], [6,12], [14, 15]]
new_interval = [3,6]
print(add_interval(intervals, new_interval)) # [[1, 12], [14, 15]]