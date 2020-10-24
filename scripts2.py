#Birthday Cake Candles

#!/bin/python

import math
import os
import random
import re
import sys

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    
    return(candles.count(max(candles)))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(raw_input().strip())

    candles = map(int, raw_input().rstrip().split())

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()

#Number Line Jumps

#!/bin/python

import math
import os
import random
import re
import sys

# Complete the kangaroo function below.
def kangaroo(x1, v1, x2, v2):
    if (v2==v1) and(x1!=x2):
        return 'NO'
    if(v2==v1) and(x1==x2):
        return 'YES'

    if ((x1-x2)%(v1-v2) ==0) and ((-x1+x2)/(v1-v2)>0):
        return 'YES'
    else:
        return 'NO'
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1V1X2V2 = raw_input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()


#Viral Advertising

#!/bin/python3

import math
import os
import random
import re
import sys

# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())

c = 0 
s = 5
l = 0 

#Recursive Digit Sum

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
l=input().split()
n,k = map(int,l)

def superDigit(n, k):
    ns=list(str(n))
    if (len(ns)==1) and (k== 0):
        print(ns[0])
    elif (len(ns)==1) and (k!=0):
        superDigit(str(ns[0])*k,0)
    else:
        n = sum(map(int,ns))
        superDigit(n,k)


superDigit(n,k)

#Insertion Sort - Part 1

#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())
l = list(map(int,input().split()))

for i in reversed(range(1,n)):
    elem = l[i]
    j = i 
    if elem<l[j-1]:
        while elem<l[j-1]:
            l[j]=l[j-1]
            j = j-1
            print(' '.join(list(map(str,l))))
            if j ==0:
                break
        l[j] = elem 
        print(' '.join(list(map(str,l))))

#Insertion Sort - Part 2

# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
l = list(map(int,input().split()))

for i in range(1,n):
    elem = l[i]
    j = i 
    if elem<l[j-1]:
        while elem<l[j-1]:
            l[j]=l[j-1]
            j = j-1
            if j ==0:
                break
        l[j] = elem 
    print(' '.join(list(map(str,l))))
