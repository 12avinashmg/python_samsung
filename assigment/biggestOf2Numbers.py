# Find sum of list elements with out using sum()
# Count the elements in a List without using count()
# Find minimum and maximum elements in a list without using min() and max()

# Program to search an element in a list:
list1 = []
print("Enter elements to the list, -1 to stop")
while True:
    element = int(input())
    if element == -1:
        break
    list1.append(element)
    
print("The list elements are: ", list1)

serach_key = int(input("Enter search number: "))
flag = False # Assume the element is not present in the list
for element in list1: # For Each loop
    if element == serach_key:
        print("Key found")
        flag = True
        break

if not flag:
    print("Key not found")

"""
Python List
* List is a DS
* Python List grows and shrinks dynamically
* Pyhton List is an Object
* List can hold same type of Values or different Types
* List is mutable 
* List can have list as its elements (Multi dimentional)
* List index starts from Zero
* The append() inserts an element to the list at the end
* Insert() takes 2 args, 1st is the index at which new element to be inserted, 2nd arg is the element

Program to find Factorial of a number
Program to check if a number is a Perfect Square
Program to Print Fibonacci series of n terms
Program to count digits in a number
Program to find sum of digits in a number
Program to accept avgScore and print result of the student as follow:
0-39 Fail, 40-59 Second Sclass 60-84 First class, 85-100 Distinction

Find sum of the series of m terms
1. n + n2 + n3 + n4 +......
2. 1 - n + n2 - n3 + .....
3. n - n2/3 +n4/5 - n8/7 +......

Print the following Patterns after reading the No. of lines (n)
1. ***************

2. m spaces after every m *s
if m = 3, ***   ***   ***   

3.
*
**
***
****
*****

     *
    **
   ***
  ****
 *****
******

    *  1
   * *  3
  *   *  5
 *     *  7
*********  9

4. Rhombus (Odd)
5. Hollow Equilataral Triangle
6. Hollow Rhombus
7. X of Stars (Odd)
8. Hollow Square
9. X inside a hallow Square (Odd)
*************
**         **
* *       * *
*  *     *  *
*   *   *   *
*     *     *
*    * *    *
*   *   *   *
*  *     *  * 
**        * *
*          **
*************
"""
