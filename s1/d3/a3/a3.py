# Q1 **Tuple Unpacking**: Create a list of tuples, each containing a name and an age. Then, use tuple unpacking to iterate through the list and print each name and age.
#     - *Input*: [("John", 25), ("Jane", 30)]
#     - *Output*: "John is 25 years old. Jane is 30 years old."
list1 = [("John", 25), ("Jane", 30)]
for i in list1:
  print(f"{i[0]} is {i[1]} years old")

# Q2 **Dictionary Manipulation**: Create a dictionary with keys as names and values as ages. Write functions to add a new name-age pair, update the age of a name, and delete a name from the dictionary.
#     - *Input*: Add "John": 25, Update "John": 26, Delete "John"
#     - *Output*: "{}, {'John': 26}, {}"

decton = {}


def addnaag(obj, name, age):
  obj[name] = age


def update_age(obj, name, age):
  if name in obj:
    obj[name] = age


def remove_det(obj, name):
  if name in obj:
    del obj[name]


addnaag(decton, "John", 35)
print(decton)

update_age(decton, "John", 24)
print(decton)

remove_det(decton, "John")
print(decton)

# Q3. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"

list = [2, 7, 11, 15]
target = 9
listSize = len(list)


def findInt(list, target):
  answ = []
  for i in range(0, listSize):
    for j in range(0, listSize):
      if list[i] != list[j] and (list[i] + list[j]) == target:
        answ.append(i)
        answ.append(j)
        return answ


print(findInt(list, target))

# Q4. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

palinCh = "naman"
str = ""
for i in reversed(palinCh):
  str += i
if str == palinCh:
  print("it is palindrome")
else:
  print("it is not paliindrome")


# Q4. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"
def selection_sort(arr):
  for i in range(len(arr)):
    min_idx = i
    for j in range(i + 1, len(arr)):
      if arr[j] < arr[min_idx]:
        min_idx = j
    arr[i], arr[min_idx] = arr[min_idx], arr[i]
  return arr


arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)
