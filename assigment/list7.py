odd = [1, 9]

odd.insert(-1, 3) # list.insert(indexNumber, element)

# Output: [1, 3, 9] 
print(odd)

odd.insert(1, 30)
print(odd)

odd.insert(6, 30); #element will added at the rear

odd[2:2] = [5, 7]
# This doesn't replace any value (bcoz empty list), but adds the new list elements into the list Odd
print(odd) # [1, 30, 5, 7, 3, 9, 30]

list2 = [50, 70, 90]

odd[4:3] = list2 # Note: You cannot move backwards
print(odd) # [1, 30, 5, 7, 50, 70, 90, 3, 9, 30]


list3 = [100, 400, 500]

odd[2:5] = list3[1:1]

# Output: [1, 3, 5, 7, 9]
print(list2)
