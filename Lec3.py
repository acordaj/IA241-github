'''
lec 3 
'''

my_list = [1, 2, 3, 4, 5,]

print(my_list)

my_nested_list = [1, 2, 3, my_list]

print(my_nested_list)

my_list[0] = 6
print(my_list)

print(my_list[0])
print(my_list[1])
print(my_list[-1])

print(my_list)
print(my_list[1:3])
print(my_list[:])

x,y = ['a','b']

print(x)

print(my_list)
my_list.append(7)
print(my_list)

my_list.remove(7)
print(my_list)

my_list.sort()
print(my_list)

my_list.reverse()
print()


print(my_list + [8,9])

x,y = ['a','b']

my_list.extend(  ['a','b']    )
print(my_list)


print('c' in my_list)

print(len(my_list))


