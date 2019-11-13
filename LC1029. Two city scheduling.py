# https://leetcode.com/problems/two-city-scheduling/
# Solution by LC user Hai_dee


def twoCitySchedCost(costs):
    # sort the costs by their price difference
    # trips with highest price for city B are put in front
    sorted_costs = sorted(costs, key=lambda x: x[0] - x[1])  # using costs.sorted() can save memory
    N = len(costs)  # don't need to initialize N but saves time typing and for better readability

    # adding up prices for city A for the first half and prices for city B for the second half
    # the second half essentially have trips whose city B price is cheaper or no more expensive than city A
    total_costs = sum([x[0] for x in sorted_costs[:N//2]] + [x[1] for x in sorted_costs[N//2:]])  # use `//` because `/` produces a float in Python 3
    return total_costs


test = [[10,20],[30,200],[400,50],[30,20]]
twoCitySchedCost(test)