import sys

n, m, k = list(map(int, sys.stdin.readline().strip().split()))

adj_table = {key: list() for key in range(n + m)}
for _ in range(k):
    i, j = list(map(int, sys.stdin.readline().strip().split()))
    i -= 1
    j += n - 1

    adj_table[i].append(j)
    adj_table[j].append(i)

n_comp = 0
visited = [False] * (n + m)
q = list()

for idx in range(n + m):
    if not visited[idx]:
        q.append(idx)
        n_comp += 1

        while q:
            vis_node = q.pop(0)
            visited[vis_node] = True
            for neighbor in adj_table[vis_node]:
                if not visited[neighbor]:
                    q.append(neighbor)

for idx in range(n, n + m):
    if len(adj_table[idx]) == 0:
        n_comp -= 1

print(n_comp - 1)
