def solution(tickets):
    visited = [False] * len(tickets)
    answer = []

    def dfs(src, path):
        if len(path) == len(tickets) + 1:
            answer.append(path)
            return

        for idx, ticket in enumerate(tickets):
            if not visited[idx] and src == ticket[0]:
                visited[idx] = True
                dfs(ticket[1], path + [ticket[1]])
                visited[idx] = False

    dfs("ICN", ["ICN"])

    answer.sort()
    return answer[0]


# print(solution([["ICN", "AAA"], ["ICN", "BBB"], ["ICN", "BBB"], ["BBB", "ICN"], ["BBB", "ICN"], ["AAA", "ICN"]]))
# print(solution([["ICN", "CCC"], ["CCC", "BBB"], ["BBB", "CCC"]]))
# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
print(solution(
    [["ATL", "ZIX"], ["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"],
     ["SFO", "ATL"]]))
# print(solution([["ICN", "JFK"], ["ICN", "AAD"], ["JFK", "ICN"]]))
