from collections import deque


def solution(tickets):
    planes = {}
    lines = 0
    for src, des in tickets:
        lines += 1
        if planes.get(src) == None:
            planes[src] = [des]
        else:
            planes[src].append(des)

        if planes.get(des) == None:
            planes[des] = []

    planes = {k: sorted(v) for k, v in planes.items()}
    # is_visited = {(a[0], a[1]): False for a in tickets}
    is_visited = []
    for a in tickets:
        is_visited.append([(a[0], a[1]), False])
    # print(planes)
    #
    # print(is_visited)
    # print("--")
    queue = deque()
    queue.append(['ICN', 'ICN'])

    while queue:
        node, path = queue.pop()
        # print(node, "|", path)
        
        if len(planes[node]) > 0 and is_visited[is_visited.index([(node, planes[node][0]), False])]:
            is_visited[is_visited.index([(node, planes[node][0]), False])] = (node, planes[node][0], True)
            queue.append([planes[node][0], path + " " + planes[node][0]])
            planes[node].remove(planes[node][0])
            # print(planes, node)
        # print(is_visited)

        # print(path)
        # print("---")
    # print(is_visited)
    return path.split(" ")


# print(solution([["ICN", "AAA"], ["ICN", "BBB"], ["ICN", "BBB"], ["BBB", "ICN"], ["BBB", "ICN"], ["AAA", "ICN"]]))
# print(solution([["ICN", "CCC"], ["CCC", "BBB"], ["BBB", "CCC"]]))
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
# print(solution(
#     [["ATL", "ZIX"], ["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"],
#      ["SFO", "ATL"]]))
print(solution([["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]))