#Say "Hello, World!" With Python

if __name__ == '__main__':
    print("Hello, World!")

#Pyhton if-Else

#!/bin/python3

import math
import os
import random
import re
import sys

n = int(input())
if n%2 !=0:
    print('Weird')
else:
    if 2<=n<=5 :
        print('Not Weird')
    if 6<=n<=20:
        print('Weird')
    if n>20:
        print('Not Weird')

#Arithmetic Operators

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
print(a+b)
print(a-b)
print(a*b)

#Python: Division

from __future__ import division

if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())

print(a//b)
print(a/b)

#Loops
if __name__ == '__main__':
    n = int(raw_input())
i=0
while i < n:
    print(i**2)
    i=i+1

#Write a function
def is_leap(year):
    leap = False
    if year%4 ==0:
        leap = True 
        if year%400==0:
            leap = True
        if year%100 ==0 and year%400!= 0:
            leap = False
    return leap

#Print Function
from __future__ import print_function

if __name__ == '__main__':
    n = int(raw_input())

out = str()
i=1
while i <=n:
    out+= str(i)
    i+=1
print(out)

#List Comprehensions
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

c = [x,y,z]

I,J,K = [i for i in range(x+1)],[j for j in range(y+1)],[k for k in range(z+1)]
print([[i,j,k] for i in I for j in J for k in K  if i+j+k!=n])

#Find the Runner-Up Score!
if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
sarr=set(arr)
sarr.remove(max(sarr))
print(max(sarr))

#Nested Lists
if __name__ == '__main__':
    students =[]
    scores =[] 
    for _ in range(int(raw_input())):
        name = raw_input()
        score = float(raw_input())
        students+=[[name,score]]
        scores += [score]

m = 10000
for elem in students:
    if elem[1]<m and elem[1]!= min(scores):
        m= elem[1]
out=[]
for elem in students:
    if elem[1]==m:
        out += [elem[0]]

out.sort()

for elem in out:
    print(elem)

#Finding the percentage
    

if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
l = list(student_marks.get(query_name))
avg="{:.2f}".format(sum(l)/3)
print(avg)

#Lists
if __name__ == '__main__':
    N = int(raw_input())

l= []
for i in range(N):
    line= raw_input().split()
    command=line[0]
    index = map(int,(line[1:]))
    if command != "print":
        eval("l."+str(command)+str(tuple(index)))
    else: 
        print(l)

#Tuples
if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())

print(hash(tuple(integer_list)))

#sWAP cASE

def swap_case(s):

    return s.swapcase()

#String Split and Join
def split_and_join(line):
    return line.replace(" ","-")





#What's Your Name?
def print_full_name(a, b):
    print "Hello " +str(a)+" "+str(b) +"! You just delved into python."





#Mutations

def mutate_string(string, position, character):
    return string[:position]+ str(character)+string[position+1:]

#Find a string

def count_substring(string, sub_string):
    l= []
    for i in range(len(string)+1):
        for j in range(i):
            l+= [string[j:i]]
    n=0
    for elem in l:
        if elem == sub_string:
            n=n+1
    return n



#String Validators
if __name__ == '__main__':
    s = raw_input()

alphanumeric = False
alphabetical = False
digit = False
lowercase = False
uppercase = False

for i in range(len(s)):
    if s[i].isalnum()== True:
        alphanumeric = True
    if s[i].isalpha()==True:
        alphabetical = True
    if s[i].isdigit() == True:
        digit = True
    if s[i].islower()== True:
        lowercase = True
    if s[i].isupper()== True:
        uppercase = True

print(alphanumeric)
print(alphabetical)
print(digit)
print(lowercase)
print(uppercase)



#Text Alignment
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))




#Text Wrap
def wrap(string, max_width):
    n=1
    i=0
    new_string=""
    while n<= len(string)/max_width:
        i+=1
        if i== max_width:
            new_string+=string[(n-1)*i:n*i]+"\n"
            n+=1
            i=0
    new_string+=string[len(new_string)-n+1:]
        
    return new_string

    





#Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int,input().split())
j=1
for i in range(int((n-1)/2)):
    print("-"*int((m-(j*3))/2)+str(".|.")*j+"-"*int((m-(j*3))/2))
    j+=2
print("WELCOME".center(m,"-"))

j= 2*(int((n-1)/2))-1
for i in range(int((n-1)/2)):
    print("-"*int((m-(j*3))/2)+str(".|.")*j+"-"*int((m-(j*3))/2))
    j=j-2



#String Formatting


def print_formatted(number):
    for i in range (number):
        i=i+1
        space = len("{0:b}".format(number))
        print(("{0:{space}d} {0:{space}o} {0:{space}x} {0:{space}b}".format(i,space=space)).upper())



#Alphabet Rangoli
def print_rangoli(size):
    s=""
    for i in reversed(range(1,size+1)):
        s+=str(chr(ord('`')+i))
        l=list(s)
        s1='-'.join(l+l[len(l)::-1][1:len(s)])
        print('-'*(2*i-2)+s1+'-'*(2*i-2))

    for i in reversed(range(size-1)):
        l.pop(len(l)-1)
        s1='-'.join(l+l[len(l)::-1][1:len(s)])
        print('-'*(2*size-(2*(i+1)))+s1+'-'*(2*size-(2*(i+1))))




#Capitalize!


# Complete the solve function below.
def solve(s):
    l = s.split(' ')
    for i in range(len(l)) :
        l[i] = l[i].capitalize()
    return(' '.join(l))



#The Minion Game

def minion_game(string):
    vowels = 'AEIOU'

    kevsc = 0
    stusc = 0
    for i in range(len(string)):
        if s[i] in vowels:
            kevsc += (len(string)-i)

        else:
            stusc += (len(string)-i)

    if kevsc > stusc:
        print "Kevin", kevsc
    elif kevsc < stusc:
        print "Stuart", stusc
    else:
        print "Draw"



#Merge the Tools!
def merge_the_tools(string, k):
    for i in range(k,len(string)+1,k):
        p= ''.join(set(string[i-k:i]))
        print(p)

#collections.Counter()
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

n, s = raw_input(), map(int,raw_input().split())

S = Counter(s)

earns = 0 

for i in range (int(raw_input())):
    l = map(int,raw_input().split())
    size = l[0]
    price = l[1]
    if S[size] >0:
        earns += price
        S[size] += -1

print(earns)



#Introduction to Sets

def average(array):
    l =list(set(array))
    return(sum(l)/len(l))


#No Idea!#################

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
arr = input().split()
A = set(input().split())
B = set(input().split())

r = 0 

for elem in arr:
    if elem in A:
        r+= 1
    elif elem in B:
        r=r-1
print(r)



#Symmetric Difference
# Enter your code here. Read input from STDIN. Print output to STDOUT

cardA = raw_input()
A = set(map(int,raw_input().split()))

cardB= raw_input()
B= set(map(int, raw_input().split()))

l= list(A.symmetric_difference(B))
l.sort()
for elem in l:
    print(elem)

#Incorrect Regex

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = int(input())

for i in range(int(n)):
    regx = input()
    try:
        re.compile(regx)
        r = True
    except re.error:
        r = False
    print(r)

#Set .add()
# Enter your code here. Read input from STDIN. Print output to STDOUT

s=set()
x=True

for i in range(int(raw_input())-1):
    s.add(raw_input())

print(len(s))

#Set .discard(), .remove() & .pop()


n = input()
s = set(map(int, raw_input().split()))

for i in range(input()):
    line= raw_input().split()
    if len(line)==2:
        comand= 's.'+'('.join(line)+')'
    elif len(line)==1:
        comand='s.'+line[0]+'()'
    
    eval(comand)

print(sum(list(s)))




#Set .union() Operation


# Enter your code here. Read input from STDIN. Print output to STDOUT

CardA= raw_input()
A=set(raw_input().split())

CardB= raw_input()
B=set(raw_input().split())

print(len(A.union(B)))



#Set .intersection() Operation
# Enter your code here. Read input from STDIN. Print output to STDOUT
cardA=raw_input()
A = set(raw_input().split())

cardB=raw_input()
B=set(raw_input().split())

print(len(A.intersection(B)))



#Set .difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
cardA=raw_input()
A= set(raw_input().split())

cardB= raw_input()
B= set(raw_input().split())

print(len(A.difference(B)))



#Set .symmetric_difference() Operation

# Enter your code here. Read input from STDIN. Print output to STDOUT
cardA=raw_input()
A= set(raw_input().split())

cardB= raw_input()
B= set(raw_input().split())

print(len(A.symmetric_difference(B)))



#Set Mutations

# Enter your code here. Read input from STDIN. Print output to STDOUT
sCard=raw_input()
s = set(raw_input().split())
n = int(raw_input())

for i in range(n):
    comand = raw_input().split()[0]
    s2 = set(raw_input().split())
    eval('s.'+ comand +'(s2)')


print(sum(list(map(int,s))))



#The Captain's Room


# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(raw_input())

l = map(int,raw_input().split())
s = set(l)

print(((sum(set(s))*n)-(sum(l)))/(n-1))


#Check Subset
# Enter your code here. Read input from STDIN. Print output to STDOUT

for i in range(int(raw_input())):
    subset = True
    cA, A = raw_input(), set(raw_input().split())
    cB,B = raw_input(), set(raw_input().split())
    for elem in A:
        if elem not in B:
            subset = False
    print(subset)
        
#Check Strict Superset        
# Enter your code here. Read input from STDIN. Print output to STDOUT
A= set(raw_input().split())
ss = True

for i in range(int(raw_input())):
    B= set(raw_input().split())
    if len(B)>= len(A):
        ss = False
    for elem in B:
        if elem not in A:
            ss = False

print(ss)




#collections.Counter()

# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter

n, s = raw_input(), map(int,raw_input().split())

S = Counter(s)

earns = 0 

for i in range (int(raw_input())):
    l = map(int,raw_input().split())
    size = l[0]
    price = l[1]
    if S[size] >0:
        earns += price
        S[size] += -1

print(earns)


#DefaultDict Tutorial
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict
from collections import OrderedDict
n, m = map(int,input().split())


A = defaultdict(list)
B= []
for i in range(1,n+1):
    A[input()].append(i)

for i in range(m):
    B+= [input()]


for elem in B:
    if elem in A.keys():
        print(' '.join(map(str,A[elem])))
    else:
        print(-1)


#Collections.namedtuple()
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple
n = int(raw_input())
ST = namedtuple('ST', ','.join(raw_input().split()))

m = 0 

for i in range(n):
    v1,v2,v3,v4 = raw_input().split()
    st = ST(v1,v2,v3,v4)
    m+= float(st.MARKS)
print('{:.2f}'.format(m/n))




#Collections.OrderedDict()

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict

d=OrderedDict()

for elem in range(int(raw_input())):
    p = raw_input().split()
    prod = ''
    for elem in p:
        if elem.isdigit():
            price=int(elem)
        else:
            prod += elem +' '
    if prod not in d.keys():
        d[prod]= int(price)
    else:
        d[prod]+= int(price) 


for elem in d.keys():
    print(elem + str(d[elem]))



#Word Order
# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import Counter
from collections import OrderedDict

Od= OrderedDict()
w=[]
for i in range(int(raw_input())):
    word = raw_input()
    Od[word]=0
    w+= [word] 

c = Counter(w)
for elem in c.keys():
    Od[elem] = str(c.get(elem))

print(len(Od.items()))
print(' '.join(Od.values()))


    




#Collections.deque()
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
for i in range(int(raw_input())):
    l = raw_input().split()
    if len(l)==2:
        comand ='d.'+ l[0]+'('+str(l[1])+')'
    elif len(l)==1:
        comand = 'd.'+l[0]+'()'
    eval(comand)

e = []
for elem in d:
    e +=[str(elem)]  

print(' '.join(e))




#Company Logo
#!/bin/python

import math
import os
import random
import re
import sys

from collections import Counter
from collections import OrderedDict
import operator

l = list(raw_input())
d = Counter(l)
dS0 = OrderedDict(sorted(d.items(),key=operator.itemgetter(0)))
dS1 = OrderedDict(sorted(dS0.items(),key=operator.itemgetter(1),reverse=True))



for i in range(3):
    print(dS1.keys()[i]+' '+str(dS1[dS1.keys()[i]]))
    







#Piling Up!

# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

for i in range(int(raw_input())):
    n = int(raw_input())
    l = deque(map(int,raw_input().split()))
    ok = True
    for i in range(1, n-1):
        if l[0]>l[len(l)-1]:
            c = l.popleft()
        else:
            c= l.pop()
        if c< max(l[0],l[len(l)-1]):
            ok = False
    if ok == False:
        print('No')
    else:
        print('Yes')

        
                        




#Calendar Module

# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar

day = map(int,raw_input().split())
days = ['MONDAY','THUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
print(days[int(calendar.weekday(day[2],day[0],day[1]))])



#Time Delta
#!/bin/python3

import math
import os
import random
import re
import sys
import datetime

from datetime import timedelta
# Complete the time_delta function below.

def time_delta(t1, t2):
    d1 = datetime.datetime.strptime(t1[4:],"%d %b %Y %H:%M:%S %z")
    d2 = datetime.datetime.strptime(t2[4:],"%d %b %Y %H:%M:%S %z")
    t = d1-d2
    return str(int(abs(t.total_seconds())))

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()



#Exceptions
for i in range (int(raw_input())):
    l = raw_input().split()
    if l[1].isdigit()== False:
        print ('Error Code: invalid literal for int() with base 10: ' +'\''+ str(l[1])+ '\'' )
    if l[0].isdigit()== False:
        print ('Error Code: invalid literal for int() with base 10: ' +'\''+ str(l[0])+ '\'' )
    elif l[1]== '0':
        print('Error Code: integer division or modulo by zero')
    elif (l[1].isdigit()== True) and(l[1]!='0'):
        
        print(str(int(l[0])/int(l[1])))



#Zipped!
# Enter your code here. Read input from STDIN. Print output to STDOUT

i = raw_input().split()
ns = int(i[0])
n = int(i[1])
l=[]
for i in range(n):
    l += [map(float,raw_input().split())]
    z = zip(*l)

for elem in z:
    print('{:0.2f}'.format(sum(elem)/int(n)))



#Athlete Sort

#!/bin/python

import math
import os
import random
import re
import sys


n, m = map(int,raw_input().split())
l= []
for i in range(n):
    l+= [map(int, raw_input().split())+[i]]

k = int(raw_input())
l.sort(key = lambda i: (i[k], i[m]))


for elem in l:
    e = map(str, elem[:len(elem)-1])
    print (' '.join(e))



#ginortS

# Enter your code here. Read input from STDIN. Print output to STDOUT

s = raw_input()
l = list(s)
lcl = []
lcU =[]
lco = []
lce = []
for elem in l:
    if elem.isdigit():
        if int(elem)%2 == 0:
            lce += elem
        else:
            lco += elem
    else:
        if elem.isupper():
            lcU += elem
        else:
            lcl += elem
lcl.sort()
lcU.sort()
lco.sort()
lce.sort()

print( ''.join(lcl+lcU+lco+lce))



#Map and Lambda Function

cube = lambda x:x**3


def fibonacci(n):
    l=[0,1]
    if n<2:
        return l[:n]
    else:
        for i in range(n-2):
            a,b = l[len(l)-1], l[len(l)-2]
            l+=[a+b]
        return l


    




#Detect Floating Point Number


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
import sys
n = int(input())
patt = r'^[+-]?\d*\.\d+$'



for i in range (n):
    print(bool(re.match(patt, input())))



#Re.split()
regex_pattern = r"[.,]"	# Do not delete 'r'.

#Group(), Groups() & Groupdict()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = raw_input()

pattern = r'([a-zA-Z0-9])\1'
m = re.search(pattern, s)
if m == None:
    print (-1)
else:
    print(m.group(1))
        
    



#Re.findall() & Re.finditer()

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = raw_input()
pattern= r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]'
m=re.findall(pattern, s)
if m == []:
    print(-1)
else:
    for elem in m:
        print(elem)




#Re.start() & Re.end()
# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

s = raw_input()
k = raw_input()

m = re.compile(k).search(s)
 
if m == None:
    print "(-1, -1)"

while m:
    print (tuple([m.start(),m.end()-1]))
    m = re.compile(k).search(s,m.start() + 1)




#Regex Substitution


# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())

for i in range (n):
    s = input()
    s1= re.sub(r'(?<= )(&{2})(?= )', "and", s)
    s2 = re.sub(r'(?<= )(\|{2})(?= )', "or",s1)
    print(s2)


#Validating Roman Numerals

regex_pattern = r'(M{0,3})(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(?=$)' 






#Validating phone numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
regex_pattern = r'(7|8|9){1}\d{9}$' 

n = int(input())

for i in range (n):
    if bool(re.match(regex_pattern, input()))==True:
        print('YES')
    else:
        print('NO')



#Validating and Parsing Email Addresses

# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
regex_pattern = r'<[a-zA-Z0-9]+[a-zA-Z0-9\.\_\-]+@[A-Za-z]+\.([a-z]{1,3})>' 
n = int(input())

for i in range (n):
    s = input().split()
    if bool(re.match(regex_pattern, s[1]))==True:
        print(' '.join(s))
    



#Hex Color Code

# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

s = sys.stdin.read()

import re
regex_pattern = r'(\#([0-9a-fA-F]{3}){1,2})(?!(\n|\s)+\{)'

m  = re.findall(regex_pattern,s)
for elem in m:
    print(elem[0])



#HTML Parser - Part 1


# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser
import sys

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):        
        print ('Start :',tag)
        for elem in attrs:
            print ('->',elem[0],'>',elem[1])
    def handle_endtag(self, tag):
        print ('End   :',tag)
    def handle_startendtag(self, tag, attrs):
        print ('Empty :',tag)
        for elem in attrs:
            print ('->',elem[0],'>',elem[1])

MyHTMLParser().feed(sys.stdin.read())
            


#HTML Parser - Part 2


from HTMLParser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        if data != '\n':
            if data.count('\n')== 0:
                print(">>> Single-line Comment \n" + str(data))
            else:
                print(">>> Multi-line Comment \n" + str(data))
    def handle_data(self, data):
        if data != '\n':
            print (">>> Data     \n" + str(data))
  
  
  
  
  

  
  
  
html = ""       
for i in range(int(raw_input())):
    html += raw_input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()


#Detect HTML Tags, Attributes and Attribute Values

# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser
import sys
    

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs): 
        print (tag)
        for elem in attrs:
            print ('->',elem[0],'>',elem[1])
    
    def handle_startendtag(self, tag, attrs):
        print (tag)
        for elem in attrs:
            print ('->',elem[0],'>',elem[1])
    
MyHTMLParser().feed(sys.stdin.read())



#Validating UID
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pU = r'([A-Z].*){2}'
pD = r'([0-9].*){3}'
pL = r'^[A-Za-z0-9]{10}$'
pR=  r'.*(.).*\1'

n = int(input())

for i in range(n):
    s = input()
    if (
        (bool(re.search(pU,s))== True) and 
        (bool(re.search(pD,s))== True )and 
        (bool(re.search(pL,s))== True )and 
        (bool(re.search(pR,s))== False)):
        print('Valid')
    else:
        print('Invalid')




#Validating Credit Card Numbers

# Enter your code here. Read input from STDIN. Print output to STDOUT

import sys
import re
s = sys.stdin.read()
l = s.split('\n')
regex_pattern = r'[4-6]\d{3}(?:-?\d{4}){3}'
pattnot= r'(\d)\1{3,}'


for elem in l[1:]:
    if elem in re.findall(regex_pattern,s):
        if not re.search(pattnot,elem.replace('-','')):
            print('Valid')
        else:
            print('Invalid')
    else:
        print('Invalid')






#Validating Postal Codes

regex_integer_in_range = r"^[1-9]\d{5}$" # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(?=(\d)\d\1)"	# Do not delete 'r'.




#Matrix Script



#!/bin/python3

import math
import os
import random
import re
import sys


n,m = map(int, input().split())

l=[]
s = ''
for i in range(n):
    l+= [list(input())]


for i in range (m):
    for elem in l:
        s+= elem[i]


print(re.sub(r'(?<=\w)([\|\!\@\#\$\%\&\s]+)(?=\w)',' ', s))







#XML 1 - Find the Score

def get_attr_number(node):
    if node.getchildren == None:
        return 0
    return( len(node.attrib) + sum(get_attr_number(child) for child in node.getchildren()))




#XML2 - Find the Maximum Depth

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if maxdepth <= level :
        maxdepth+=1
    level = level +1
    for child in elem:
        depth(child, level)
        





#Arrays


def arrays(arr):
    return(numpy.array(arr[::-1],float))

#Shape and Reshape
import numpy


my_array = numpy.array(list(map(int,input().split())))
print (numpy.reshape(my_array,(3,3)))





#Transpose and Flatten
import numpy
n,m= map(int,input().split())
l =[]
for i in range(n):
    l+= [list(map(int,input().split()))]

my_array = numpy.array(l)
my_array2=  numpy.array(l)
print(numpy.transpose(my_array))
print(my_array2.flatten())










#Concatenate

import numpy

n,m,p = map(int, input().split())

l = list(map(int,input().split()))
a = numpy.array(l)

for i in range(n+m-1):
    l = list(map(int,input().split()))
    a= numpy.concatenate((a,numpy.array(l)),axis=0)

print(numpy.reshape(a,((n+m),p)))



#Zeros and Ones

import numpy

n = tuple(map(int,input().split()))

a = numpy.zeros(n, dtype = numpy.int)

b = numpy.ones(n , dtype = numpy.int)



print(a)
print(b)



#Eye and Identity

import numpy

n,m  = map(int,input().split())

print (str(numpy.eye(n,m, k = 0)).replace('0.',' 0.').replace('1.',' 1.'))




#Array Mathematics

import numpy


n, m = map(int, input().split())
la=[]
lb=[]
for i in range(n):
    la+=[list(map(int,input().split()))]
a = numpy.array(la)

for i in range(n):
    lb+=[list(map(int,input().split()))]
b = numpy.array(lb)





print(a+b,a-b,a*b,a//b,a%b,a**b,sep='\n')



#Floor, Ceil and Rint


import numpy as ny
ny.set_printoptions(sign=' ')

a = ny.array(list(map(float,input().split())))


print(ny.floor(a))
print(ny.ceil(a))
print(ny.rint(a))


#Sum and Prod


import numpy
n,m = map(int, input().split())
l = []
for i in range (n):
    l += [list(map(int, input().split()))]
a = numpy.array(l)

s = numpy.sum(a,axis=0)
p = numpy.prod(s)


print(p)


#Min and Max
import numpy

n,m = map(int, input().split())
l = []

for i in range (n):
    l += [list(map(int, input().split()))]
a = numpy.array(l)
A= numpy.min(a,axis=1)
print(numpy.max(A))



#Mean, Var, and Std
import numpy
numpy.set_printoptions(legacy='1.13')


n,m = map(int, input().split())
l = []

for i in range (n):
    l += [list(map(int, input().split()))]
a = numpy.array(l)

print(numpy.mean(a,axis=1))
print(numpy.var(a,axis=0))
print(numpy.std(a,axis= None))




#Dot and Cross

import numpy

n=int(input())
l = []

for i in range (n):
    l += [list(map(int, input().split()))]
a = numpy.array(l)

l = []

for i in range (n):
    l += [list(map(int, input().split()))]
b = numpy.array(l)

print(numpy.dot(a,b))



#Inner and Outer


import numpy as ny

A = ny.array(list(map(int,input().split())))
B = ny.array(list(map(int,input().split())))


print (ny.inner(A, B))
print (ny.outer(A, B))

#Polynomials


import numpy
coeff = list(map(float,input().split()))
x = float(input())
print(numpy.polyval(coeff,x))


#Standardize Mobile Number Using Decorators

def wrapper(f):
    def fun(l):
        for i in range(len(l)):
            l[i] = l[i][len(l[i])-10:]
        l.sort()
        for elem in l:
            print('+91 {} {}'.format(elem[:5],elem[5:]))
    return fun



#Decorators 2 - Name Directory


def person_lister(f):
    def inner(people):
        people.sort(key=lambda x: int(x[2]))
        return(map(f, people))
    return inner

#Linear ALgebra

import numpy

n=int(input())
l = []

for i in range (n):
    l += [list(map(float, input().split()))]
a = numpy.array(l)

print ('{:.2}'.format(numpy.linalg.det(a)))







