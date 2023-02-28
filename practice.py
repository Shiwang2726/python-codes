# Q1.Given a list, write a Python program to swap first and last element of the list.
list1 = [1,2,3,4]
t = list1[0]
list1[0] = list1[len(list1)-1]
list1[len(list1)-1] = t

print(list1)

lis = [12, 35, 9, 56, 24]
te = lis[0]
lis[0] = lis[len(lis)-1]
lis[len(lis)-1] = te
print(lis)

# Q2.Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.
# pos2 and pos5
l = [11,22,33,44,55]
num = l[1]
l[1] = l[len(l)-1]
l[len(l)-1] = num
print(l)

# Q3. finding length of a list using the Naive Method
 #Finding length of list
# using loop
# Initializing counter
test = [1,2,3,4,5]
print('list is : ' + str(test))
an = 0
for i in test:
        an = an + 1
print('length of list using naive method is : ' + str(an))

# method 2:
a= [1,2,3]
print('length of a :' , len(a))
        

# Q4. Given two numbers, write a Python code to find the Maximum of these two numbers.
a = 4
b = 5
print(max(a,b))
    
#Q5. Given two numbers, write a Python code to find the Minimum of these two numbers.
c = 55
d = 78
print(min(c,d))


x = int(input('enter the number : '))
if x<0:
        print('number is negative')
else:
        print('number is positive')    
            
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
print(employee_check(work_ho) )


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