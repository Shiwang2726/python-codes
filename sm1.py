1# Use for, .split(), and if to create a Statement that will print out words that start with 's':
# st = 'Print only the words that start with s in this sentence'

st = 'shiwangi sad ku h'
for word in st.split():
    if word[0] == 's':
        print(word)
    else:
        print('sorry word do not start with "s"' )
        
# use range() to print all the even numbers from 0 to 10
mylist = [x for x in range(0,10) if x%2==0]
print(mylist)
       #or
y = list(range(0,10,2))
print(y)

# Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.
z = [a for a in range(1,50) if a%3==0 ]
print(z)

#Go through the string below and if the length of a word is even print "even!"
# st = 'Print every word in this sentence that has an even number of letters'
mystring = 'sillua'
s = len(mystring)
if s%2==0:
    print("even!")
    
    #or
num = 'aman'
for num in num.split():
 if len(num)%2 == 0:
    print(num+" <-- has an even length!")
    
# Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for d in range(1,101):
    if d%3==0 and d%5==0:
        print('fizzbuzz')
    elif d%3==0:
        print('fizz')
    elif d%5==0:
        print("buzz")
    else:
        print(d)
        
        #Use a List Comprehension to create a list of the first letters of every word in the string below:
asdy= 'amna sad hogya ku'
q = [asdy [0] for asdy in asdy.split()]
print(q)
