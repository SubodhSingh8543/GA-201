# Q1 Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
val = ""
for i in range(1, 6):
  val += f"{i}" + " "
  print(val)

# Q2
numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
  if i % 5 == 0:
    if i > 500:
      break
    elif i > 150:
      continue
    print(i)

# Q3
s1 = "Aulte"
s2 = "Kelly"
midInd = len(s1) // 2
s3 = s1[:midInd] + s2 + s1[midInd:]
print(s3)

# Q4
str1 = "PyNaTive"
strL = ""
strU = ""
for i in str1:
  if i.islower():
    strL += i
  else:
    strU += i
print(strL + strU)

# Q5
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []

minLen = min(len(list1), len(list2))

for i in range(minLen):
  newStr = ""
  newStr += list1[i] + list2[i]
  list3.append(newStr)

list3.extend(list1[minLen:])
list3.extend(list2[minLen:])

print(list3)

# Q6
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]

for list1, list2 in zip(list1, reversed(list2)):
  print(list1, list2)

# Q7
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []

for i in list1:
  for j in list2:
    newStr = i + " " + j
    list3.append(newStr)
print(list3)

# Q9
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
obj = {}

for i in employees:
  obj[i] = defaults
print(obj)

# Q10
tuple1 = (11, [22, 33], 44, 55)
list1 = list(tuple1)
list1[1][0] = 222
tuple1 = tuple(list1)
print(tuple1)
