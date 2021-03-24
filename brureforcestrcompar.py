def brute(f_string, min_string):
    # there is no need to add +1 because it will always be on starting position of 0 so +1 and -1 will cancel
    patt_len = len(min_string)
    full_len = len(f_string)
    comp = full_len-patt_len
    positions = []
    isvalid = False
    count = 0
    for i in range(comp):
        j = 0
        while j < (patt_len-1) and min_string[j] == f_string[i+j]:
            j = j+1
            if (min_string[j] == f_string[i+j]):
                isvalid = True
            else:
                isvalid = False

        if j == patt_len-1 and isvalid == True:
            positions.append(i)

            count = i+j

    # return -1
    # this is how to print all with a comma and you need to use the , to add it as a string
    print("The postions are: ", *positions)
    print("the count of comparison is: %d" % count)


if __name__ == '__main__':
    # how to grab this line to an array maybe check the lab 2?\
    print("this is from index 0 to n")
    arr = input("what is the full string? \n")
    print(" this is the full char: " + arr)
    arr = arr.replace(" ", "")
    pattern = input("What is the pattern? \n")
    print(" this is the pattern: %s " % pattern)
    pattern = pattern.replace(" ", "")
    v = brute(arr, pattern)
    print("-----------------------------------------")
