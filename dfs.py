
graph = {1: [2, 3, 4, 5, 6, 7, 8, 9, 11,12,13,14,18,20,22,32],

2: [1,3,4,8,14,18,20,22,31],

3: [1,2,4,8,9,10,14,28,29,33],

4: [1,2,3,8,13,14],

5: [1,7,11],

6: [1,7,11,17],

7: [1,5,6,17],

8: [1,2,3,4],

9: [1,3,31,33,34],

10: [3],

11: [1,5,6],

12: [1],

13: [1,4],

14: [1,2,3,4,34],

15:[33,34],

16:[33,34],

17:[6,7],

18:[1,2],

19:[33,34],

20:[1,2,34],

21:[33,34],

22:[1,2],

23:[33,34],

24:[26,28,30,33,34],

25:[26,28],

26:[24,25,32],

27:[30,34],

28: [3,24,25,34],

29: [3,32,34],

30: [24,27,33,34],

31: [2,9,33,34],

32: [1,25,26,29,33,34],

33: [3,9,15,16,19,21,23,24,30,31,32,34],

34: [9,14,15,16,19,20,21,23,24,27,28,29,30,31,32,33]

}


visited = set() # SET OF VISITED NODES
len_order = len(graph)
counter = 0
order = [0 * i for i in range(len_order)]
vis=[]



def dfs(visited, graph, node):
    global counter, vis
  
# PRINT THE NODE, ADD THE NODE TO VISITED SET, SET ITS ORDER TO 1, INCREMENT THE COUNTER, AND CALL FUNCTION RECURSIVELY FOR ITS NEIGHBOURING NODES IF IT IS NOT ALREADY VISITED
    if node not in visited:
        visited.add(node)
        order[counter] = 1

        print(order)
        counter = counter + 1
        vis.append(node)
        for neighbour in graph[node]:
            if neighbour is None:
                neighbour=
            dfs(visited, graph, neighbour)

v=input("what is the input number")
v=int(v)
print("start number is %d" %v)
dfs(visited, graph,v)
print("The visitation order is: %s" % vis)
print("======================================")