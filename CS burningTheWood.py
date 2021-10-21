# https://app.codesignal.com/challenge/ns25kwheaFf9WLZ45

# bfs solution
# no sorting needed
from collections import defaultdict
from collections import deque
def burningTheWood(n, wmap, start, k):
    if k == 0 or len(wmap) == 0:
        return [start]
    graph = defaultdict(list)
    for pair in wmap:
        graph[pair[0]].append(pair[1])
        graph[pair[1]].append(pair[0])
    bfs = deque([start])
    visited = [False for _ in range(n)]
    visited[start] = True
    while bfs and k > 0: 
        for _ in range(len(bfs)):
            node = bfs.popleft()
            if node in graph:
                for child in graph[node]:
                    if not visited[child]:
                        bfs.append(child)
                        visited[child] = True  # move visited toggle here to accommodate the k hour requirement
        k -= 1
    res = [i for i,val in enumerate(visited) if val]
    return res


from collections import defaultdict
def burningTheWood(n, wmap, start, k):
    if k == 0:
        return [start]
    else:
        wdict = defaultdict(list)
        for pair in wmap:
            wdict[pair[0]].append(pair[1])
            wdict[pair[1]].append(pair[0])
        if start not in wdict:
            return [start]
        else:
            prev_burnt = [start]
            all_burnt = [start]
            visited = [False] * n
            for i in range(k):
                new_burnt = []
                for m in prev_burnt:
                    if visited[m] == False:
                        new_burnt += [n for n in wdict[m] if n not in all_burnt]
                        visited[m] = True
                all_burnt += new_burnt
                prev_burnt = new_burnt
            return sorted(list(set(all_burnt)))


