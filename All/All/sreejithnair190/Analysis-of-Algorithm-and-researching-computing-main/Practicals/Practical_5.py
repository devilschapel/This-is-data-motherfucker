import sys
INF = sys.maxsize

def Floyd_Warshall(graph,V):
    dist = list(map(lambda i: list(map(lambda j: j,i)),graph))
    for k in range(V):
        for i in range(V):
            for j in range(V):
                dist[i][j] = min((dist[i][j]),((dist[i][k])+(dist[k][j])))
    Print_Graph(dist,V)

def Print_Graph(dist,V):
    for i in range(V):
        for j in range(V):
            if dist[i][j] == INF:
                dist[i][j] = "INF"
            print(dist[i][j], end=" ")
        print()

if __name__ == "__main__":
    V = 4
    graph = [
        [0,5,INF,10],
        [INF,0,3,INF],
        [INF,INF,0,1],
        [INF,INF,INF,0]
    ]
    Floyd_Warshall(graph,V)
