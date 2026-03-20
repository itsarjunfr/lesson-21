num_list = [4,5,1,6,9,5,5,41,5,23]
print('Original list:', num_list)
sum = 0
for i in num_list:
    sum += i
print('Sum of all integers in the list:', sum)
print('Number of integers in list:', len(num_list))
num_list.sort()
print('Smallest integer in list:', min(num_list))
print('Largest integer in list:', max(num_list))