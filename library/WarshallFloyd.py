def WarshallFloyd(dist,n):
    '''
    全点対最短路を求める/O(n**3)
    '''
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j],dist[i][k] + dist[k][j])
    return dist