def minTrioDegree(n: int, edges: list[list[int]]) -> int:
    adj = [[False] * (n + 1) for _ in range(n + 1)]  
    grau = [0] * (n + 1)                             
    majors = [[] for _ in range(n + 1)]              

    for u, v in edges:
        adj[u][v] = True
        adj[v][u] = True
        grau[u] += 1
        grau[v] += 1
        if u < v:
            majors[u].append(v)
        else:
            majors[v].append(u)

    millor = -1
    for u in range(1, n + 1):
        for v in majors[u]:
            for w in majors[v]:
                if adj[u][w]:
                    g = grau[u] + grau[v] + grau[w] - 6
                    if millor == -1 or g < millor:
                        millor = g
    return millor


if __name__ == "__main__":
    print(minTrioDegree(6, [[1, 2], [1, 3], [2, 3], [1, 4], [2, 5], [3, 6], [4, 5], [5, 6]]))  
    print(minTrioDegree(7, [[1, 2], [2, 3], [3, 1], [3, 4], [4, 5], [5, 6], [6, 4], [6, 7]]))  
