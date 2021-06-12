# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
group_number = int(input())
number_of_kids = []
for _ in range(group_number):
    number_of_kids.append(int(input()))
for _ in range(group_number, 9):
    number_of_kids.append(None)

dictionary = {}

for i in range(9):
    dictionary[groups[i]] = number_of_kids[i]

print(dictionary)
