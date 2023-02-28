   
   #suffle a list
num = [1,2,3,4,5]
from random import shuffle
shuffle(num)
print(num)

#shuffle a list using function:
mylist = [1,2,3,4]
def shuffle_po(mylist):
    shuffle(mylist)
    return mylist
result=shuffle_po(mylist)
print(result)

  
            
# unpacking tuple python function
work_ho = [('ban',100),('han',200),('tan',300)]
def employee_check(work_ho):
    curent_max =0
    employee_of_the_month =''
    for employee,hours in work_ho:
        if hours>curent_max:
            curent_max=hours
            employee_of_the_month=employee
        else:
            pass
    return (employee_of_the_month,curent_max)
print(employee_check(work_ho))


# practice on functions:
from pkg_resources import working_set


def even_num(num_list):
    even_number=[]
    for number in num_list:
        if number%2==0:
           even_number.append(number)
        else:
            pass   
    return even_number
print(even_num([1,2,3,4,5]))

#Define a function called myfunc that takes in an arbitrary number of arguments, and returns a list containing only 
# those arguments that are even
def myfunc(*args):
    even_list = []
    for temp in args:
        if temp%2==0:
            even_list.append(temp)
    return even_list
print(myfunc(12,1,4,5,6))


#Define a function called myfunc that takes in a string, and returns a matching string where every even letter is uppercase, and every odd
# letter is lowercase. Assume that the incoming string only contains letters, and don't worry about numbers, spaces or punctuation. 
# The output string can start with either an uppercase or lowercase letter, so long as letters alternate throughout the string.
def myfunc(x):
    out = []
    for i in range(len(x)):
        if i%2==0:
            out.append(x[i].lower())
        else:
            out.append(x[i].upper())
    return ''.join(out)
print(myfunc('Anthropomorphism'))



#WARMUP SECTION:
#Q1.LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if 
# one or both numbers are odd
def m_func(s,m):
    if s%2==0 and m%2==0:
        if s>m:
            return m
        elif m>s:
            return s
    elif s%2!=0 or m%2!=0:
        if s>m:
            return s
        else:
            return m
print(m_func(2,4))

                              #or
def m_func(s,m):
    if s%2==0 and m%2==0:
        return min(s,m)
    else:
        return max(s,m)
    print(m_func(2,4))                             

#Q2.Write a function takes a two-word string and returns True if both words begin with same letter
#animal_crackers('Levelheaded Llama') --> True
#animal_crackers('Crazy Kangaroo') --> False
def a_func(text):
    word = text.split()
    
    first = word[0]
    second = word[1]
    return first[0]==second[0]
print(a_func('aman anil'))
    
                         #or
def a_func(text):
    word = text.split()
    return word[0][0]==word[1][0]
print(a_func('aman anil'))

#Q3. Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
def n_func(z,w):
    if z+w==20:
        return True
    elif z==20 or w==20:
        return True
    else:
        return False
print(n_func(1,0))  

                                    #or
def l_func(t,j):
  return t+j==20 or t==20 or j==20
print(l_func(2,2))



# LEVEL 1 PROBLEMS:

#Q4.Write a function that capitalizes the first and fourth letters of a name
def old_func(name):
   first_letter =name[0]
   inbtween =name[1:3]
   fourth_letter =name[3]
   rest =name[4:]
   return first_letter.upper()+inbtween+fourth_letter.upper()+rest
print(old_func('shiwang'))