def index_of_node(node_id,k): 
    for i in range(0,len(k)):  
        if k[i][0]==node_id:
            return i


        
def max_height(Node):
    if Node[0]==0:     
        return 0
    if Node[1]==0 and Node[2]==0: 
        return 1
    else:
        left_index=index_of_node(Node[1],k)
        right_index=index_of_node(Node[2],k) 
        L_height=0
        R_height=0
        if left_index!=None:  
            L_height=max_height(k[left_index])
        if right_index!=None: 
            R_height=max_height(k[right_index])
        return max(L_height,R_height) + 1
    
     


k = [ 
[1, 0 ,2],
[2, 3, 4],
[3, 5 ,6],
[5 ,7, 8],
[7 ,9, 0],
[9, 0 ,10],
[10 ,0 ,11],
[11, 0 ,12],
[12 ,13 ,0],
[13 ,14, 15],
[14, 0 ,0],
[15 ,16, 0],
[16, 0 ,0],
[8 ,17, 18],
[17 ,0 ,19],
[19 ,0 ,20],
[20 ,21 ,0],
[21 ,0, 0],
[18 ,0, 22],
[22 ,0, 23],
[23, 0 ,24],
[24 ,0, 0],
[6 ,25, 26],
[25 ,27, 0],
[27 ,28, 0],
[28, 0, 29],
[29 ,0, 0],
[26 ,30, 0],
[30 ,0, 0],
[4, 31 ,32],
[31 ,0, 33],
[33 ,34 ,0],
[34 ,0, 0],
[32, 0, 0]
 ]

v=max_height(k[0])
print('array is ' +str(k))
print('height of the tree %d' %v)
print("===========================")