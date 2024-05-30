
t = int(input())

for _ in range(t):

    num = int(input())

    for i in range(32):

        shift = 1 << i
        if (num & shift) != 0:
            if num == 2 ** i:
                if num == 1:
                    print(num + 2)
                else:
                    print( num + 1)
            else:
                print( 2 ** i)
            
            break 
    
    
