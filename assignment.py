# No.1
total = 10
list1 = [11, 5, 17, 18, 23]
for ele in range(0, len(list1)):
    total = total + list1[ele]
 
# printing total value
print("Sum of all elements in given list: ", total)


#No. 2

def match_words(words):
  ctr = 0

  for word in words:
    if len(word) > 1 and word[0] == word[-1]:
      ctr += 1
  return ctr

print(match_words(['abc', 'xyz', 'aba', '1221']))


# No.3 

fruits = ["Apple", "Banana", "Melon", "Banana", "Cherry", "Banana"]
print(fruits)
fruits.remove("Banana")
print(fruits)
fruits.remove("Banana")
print(fruits)
fruits.remove("Banana")
print(fruits)




# No.4
my_list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow','orange','Marble']
print(my_list)
del my_list [0]
print(my_list)
del my_list[4]
print(my_list)
del my_list[5]
print(my_list)

# No.5
def printValues():
	l = list()
	for i in range(1,31):
		l.append(i**2)
	print(l[5:])
printValues()

