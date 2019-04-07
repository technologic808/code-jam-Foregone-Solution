t = int(input()) # read a line with a single integer
for i in range(1, t + 1):
    n = int(input()) # read an integer
    length = len(str(n)) # length of number
    strN = list(str(n)) # create number list from given number to manipulate
    strM = ['0'] * length # create identical length number list M with just zeroes
    for idx, k in enumerate(str(n)): # iterate through the number as a string
        if k == '4': # check if the digit 4 is present
            # split 4 into 3 and 1 (arbitrarity choosen)
            strN[idx] = '3'
            strM[idx] = '1'
    # join back the lists into numbers
    int1 = int(''.join(strN))
    int2 = int(''.join(strM))
    print("Case #{}: {} {}".format(i, int1, int2))
    # check out .format's specification for more formatting options
