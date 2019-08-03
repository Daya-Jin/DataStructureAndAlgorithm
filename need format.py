def networkDelayTime(times, N: int, K: int) -> int:
    adj_table = {idx: list() for idx in range(1, N+1)}
    for f, t, time in times:
        adj_table[f].append((t, time))

    res = [0x7FFFFFFF]*(N+1)
    res[K] = 0
    q = [(K, 0)]    # (node_idx,cur_time)
    visited = [False]*(N+1)

    while q:
        vis_node, cur_time = q.pop(0)

        for t, time in adj_table[vis_node]:
            res[t] = min(res[t], cur_time+time)
            if not visited[t]:
                q.append((t, cur_time+time))

        visited[vis_node] = True

    return max(res) if max(res) < 0x7FFFFFFF else -1


networkDelayTime(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], N=4, K=2)