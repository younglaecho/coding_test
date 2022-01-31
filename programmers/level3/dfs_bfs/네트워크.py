# def bfs(graph, start_node):
#     visited
    
def solution(n, computers):
    List = [[]] * len(computers)
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j] == 1 and i != j :
                if not List[i]:
                    List[i] = [j]
                else:
                    List[i].append(j)
    cnt = 0
    while List:
        visited = []
        need_visit = []
        
        need_visit.append(List[0])
        
        while need_visit:
            node = need_visit.pop(0)
            List.pop(0)
            if node not in visited:
                visited.append(node)
                need_visit.extend(node) 
    return 



solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])