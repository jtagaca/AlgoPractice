def insertionSort():
    
    arr = list(map(int, input().split())) # inputting the number in an array on a single line
    for i in range(0, n):
        print("enter number: ")
        ele = int(input())
        
        arr.append(ele)

    count = 0
    print("Original array"+str(arr))
    for i in range(1, len(arr)):

        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            count += 1
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key
        print(arr)
    print("count of the basic operation is:" + str(count))


insertionSort()
