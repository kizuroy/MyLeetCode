from collections import *

def restoreArray(adjacentPairs) -> list[int]:
    graph  = defaultdict(list)

    for j , i in adjacentPairs:
        graph[j].append(i)
        graph[i].append(j)

    for j, i in graph.items():
        if len(i) == 1:
            start = j
            break
    
    res = [start]

    while len(res) < len(adjacentPairs) + 1:
        i = res[-1]
        j = graph[i].pop()
        graph[j].remove(i)
        res.append(j)

    return res
