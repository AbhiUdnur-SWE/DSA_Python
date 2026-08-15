INF = 999


def print_solution(nv, distance):
    for i in range(nv):
        for j in range(nv):
            if distance[i][j] == INF:
                print("INF", end=" ")
            else:
                print(distance[i][j], end=" ")
        print(" ")


def floyd_warshall(nv, graph):

    distnace = graph
    for k in range(nv):
        for i in range(nv):
            for j in range(nv):
                distnace[i][j] = min(distnace[i][j], distnace[i][k] + distnace[k][j])

    print_solution(nv, distnace)
