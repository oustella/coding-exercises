# https://app.codesignal.com/challenge/ns25kwheaFf9WLZ45


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


# Use solution by itsoes
s = [start]
while k:
  k -= 1
  q={*s}  # getting unique set of numbers
  for y in wmap:
    if q&{*y}:  # finding intersection between the burnt numbers and the map
      s += y
return sorted({*s})