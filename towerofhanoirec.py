def hanoi(n, from_rod, to_rod, spare):
    
    if n == 1:
        # print('move from ' + str(from_rod)+' to_rod ' + str(to_rod))

        return 1

    else:
        # storing the value of how many calls are getting called then adding them to the return
        f = hanoi(n-1, from_rod, spare, to_rod)
        s = hanoi(1, from_rod, to_rod, spare)
        t = hanoi(n-1, spare, to_rod, from_rod)
    return f+s+t


if __name__ == '__main__':
    n, fr, t, sp = input("Enter a the values:  \n").split() #you can use split to input multiple vars 
    n = int(n)
    fr= str(fr)
    t= str(t)
    sp=str(sp)
    print ('the number of plates is %d and the from %s and to %s and the spare is % s' %(n, fr , t, sp) )
    c = hanoi(int(n), str(fr), str(t), str(sp))
    print('the number of moves is %d' % c)
