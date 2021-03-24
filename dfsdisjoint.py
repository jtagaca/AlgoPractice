graph = {1: [9],

2: [3],

3: [4],

4: [6],

5: [6],

6: [8],

7: [2,8,9],

8: [11],

9: [],

10: [],

11: [10],



}
# n=input("How many keys?")
# n=int(n)

# for i in range(1,n+1):
#     n = int(input("Enter number of elements : "))
#     #this line will read input from user using map function
#     arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n]
#     graph[i]=arr
g=str(graph)

print("this is the graph " + g)


visited = set()  # SET OF VISITED NODES

len_order = len(graph)

counter = 0

order = [0 * i for i in range(len_order)]

vis = []


def dfs(visited, graph, node):
    global counter, vis

    # PRINT THE NODE, ADD THE NODE TO VISITED SET, SET ITS ORDER TO 1, INCREMENT THE COUNTER, AND CALL FUNCTION RECURSIVELY FOR ITS NEIGHBOURING NODES IF IT IS NOT ALREADY VISITED

    visited.add(node)
    vis.append(node)
    counter+=1
    order[node-1] = counter

    for neighbour in graph[node]:
        if neighbour not in visited:
            dfs(visited, graph, neighbour)


v = input("what is the input number ")

v = int(v)

print("start number is %d" % v)
dfs(visited, graph, v)
for node in graph:
    if node not in visited:
        dfs(visited, graph, node)

print("The visitation order is: %s" % vis)

print("======================================")