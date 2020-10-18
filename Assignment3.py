#%%
# ques 1 WAP to check number is prime or not 
num=int(input('enter number to check prime or not'))
if num > 1:  
   for i in range(2,num):  
       if (num % i) == 0:  
           print(num,"is not a prime number")          
           break  
   else:  
       print(num,"is a prime number")  
         
else:  
   print(num,"is not a prime number") 

#%%
# Ques 2 WAP to print Fibonacci Series

nterms=int(input('enter the size of fiboncii series'))
#first two count
n1,n2=0,1
count=0
if(nterms<=0):
    print('enter the correct size')
elif nterms==1:
    print('fiboncii series is ',n1)
    print(n1)
else:
    print('fiboncii series is:')
    while(count<nterms):
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        count=count+1 
   #%%
       #ques3 perform Python basic String Operation like 
       # a.use of escape sequences 
txt = "We are the \"Rajasthani\" from the west ."
print(txt)
       #%%
       # b.retrieving specific index value 
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
index = vowels.index('e')
print('The index of e:', index)
index = vowels.index('i')
print('The index of i:', index)
#%%
    #c. String concatenation
a="sourabh "
b="rathore"
c=a+b
print(c)
#%%
# d.string slicing as well as use of strides
b = "Hello, World"
print(b[2:5])

#%%
    #e. Use of Negative Index
name="sourabh"
print(name[-1])
#%%
#ques  perform all the string functions 
#1capitalize(): Upper case the first letter in this sentence:
name="sourabh"
cap=name.capitalize()
print(cap)
#%%
#Upper case the string:

txt = "Hello my friends"

x = txt.upper()

print(x)

#%%
# lower() coverts the string into lower
txt="Hello Sourabh "
x=txt.lower()
print(x)

#%%
# title() :Converts the first character of each word to upper case
txt = "Welcome to careerpoint"

x = txt.title()

print(x)
#%%
#find()
txt = "Hello, welcome sourabh."

x = txt.find("welcome")

print(x)
#%%
#count():Return the number of times the value "apple" appears in the string:
txt = "I love apple iphone"

x = txt.count("apple")

print(x)
#%%
#isaplha()
txt = "SourabhR"

x = txt.isalpha()

print(x)
#%%
#isdigit():Check if all the characters in the text are digits:
txt = "50800"

x = txt.isdigit()

print(x)
#%%
#islower():Returns True if all characters in the string are lower case
txt = "hello world!"

x = txt.islower()

print(x)

#%%

#%%
#isupper(): Returns True if all characters in the string are upper case
x="SOURABH"
y=x.isupper()
print(y)
#%%
a=" Writing programs or programming is a very creative  \n and rewarding activity  You can write programs for \n many reasons ranging from making your living to solving \n a difficult data analysis problem to having fun to helping \n someone else solve a problem  This book assumes that \n {\em everyone} needs to know how to program and that once \n you know how to program, you will figure out what\n you want to do with your newfound skills \n \n We are surrounded in our daily lives with computers ranging \n from laptops to cell phones  We can think of these computers \n as our personal assistants who can take care of many things \n on our behalf  The hardware in our current-day computers \n is essentially built to continuously ask us the question \n What would you like me to do next \n \n Our computers are fast and have vasts amounts of memory \n and  could be very helpful to us if we only knew the language to \n speak to explain to the computer what we would like it to \n do next If we knew this language we could tell the \n computer to do tasks on our behalf that were reptitive \n Interestingly, the kinds of things computers can do best \n are often the kinds of things that we humans find boring \n and mind-numbing "
print(a.upper())


#%%
X="X-DSPAM-Confidence:    0.8475";
k=X.find('0')
b=X[k:]
n=float(b)
print(b)

#%%
def num_changer(string_int):
    list_of_numbers = []
    for element in range(0, len(string_int)):
        list_of_numbers.append(string_int[element])
    map_object = map(int, list_of_numbers)
    new_list_of_numbers = list(map_object)
    odd_list = []
    even_list = []
    for num in new_list_of_numbers:  
        if num % 2 != 0:
            odd_list.append(num)
        else:
            even_list.append(num)
    o = [str(i) for i in odd_list] 
    odds = int("".join(o))
    e = [str(i) for i in even_list] 
    evens = int("".join(e))
    result = odds+evens
    print(string_int+"-->"+ str(result))           
num_changer("123456")        
#%%