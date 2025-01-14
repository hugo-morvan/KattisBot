 def remove_stations(N, M):
    graph = [[] for _ in range(N + 1)]
    
    # build adjacency list from input data structure (list of connected edges)
    edgeList = []
    while len(edgeList) < M:
        line = sys.stdin.readline()
        if not line: break
        a, b, c = [int(x) for x in line.split()]  # each element of list is (a-b pair and distance between them), we will use this to create adjacencyList later on when needed by shortest path algo's...like dijkstra..etc etc !!
        edgeList += [[a, b]]    #[0] = a; [1]=B  #hence A -> B is represented as (A- pair and distance between them) ....and so for all other pairs....!!     ...no need to sort or do anything like that here since we are not building any graph structure based on this data...just using it when required..
        if a != b:  # no self loops allowed in the road network !!      (not sure why its written but whatever)...anyway continue with rest of code as usual !     ..!!   ...if u can tell me anything more about above mentioned line then plz do let me know !!!         .....
            graph[a] += [[b, c]]    # adjacency list representation where a key(station no) has value (connected station and their distance)... !!        ....  for i in range(1, N + 1):          if len([j for j in range(1,N+1)if [i,j]in edgeList or[j,i]in edgeList])==2:
                remove_station = True    #flag to tell us whether a station has exactly two connections with other stations...!!            else:remove_station=False        if not remove_station :  K -=1       for b, c in graph[a]:   print(i,"-",b,"--","\n")
# Generator time: 11.8893 seconds