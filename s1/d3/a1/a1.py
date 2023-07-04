# Q1
print("hellow world")

# Q2

# Integer
myInt = 24
print("Integer Value : ", myInt," And Integer Type :", type(myInt));

# Float
myFlot = 23.6
print("flot Value : ", myFlot," And flot Type :", type(myFlot));

# String
myStr = "23.6"
print("String Value : ", myStr," And String Type :", type(myStr));

# Boolean
myBool = (5 == 5);
print("myBool Value : ", myBool," And myBool Type :", type(myBool));

# List
myList = [1,2,3,4,"5",6,7];
print("myList Value : ", myList," And myList Type :", type(myList));

# Tuple
myTuple = (1,2,3,4);
print("myTuple Value : ", myTuple," And myTuple Type :", type(myTuple));


# Dictionary
my_dictionary = {"name": "John", "age": 25, "city": "New York"}
print("my_dictionary Value : ", my_dictionary," And my_dictionary Type :", type(my_dictionary));

# Set
my_set = {1, 2, 3, 4, 5}
my_set.add(6)
print("my_dictionary Value : ", my_set," And my_dictionary Type :", type(my_set));

# Q3
newList = [2,4,2,7,4,5,7,2,1,6];
newList.append(20);
newList.remove(5);
# newList[2]="namr";
newList.insert(2,23)
newList = [12] + newList
newList.pop(0)
del newList[0]
newList.sort()
newList.sort(reverse=True)
print(newList);

# Q4
sumList = [3,2,4,6,2];
def sumFun(val):
  return sum(val)

print(sumFun(sumList))

def aver(val):
    if len(val) > 0:
        return sum(val)/len(val)  # Return 0 for an empty list
print(aver(sumList))

# Q5
revStr = "Python"
def revString(str):
  return str[::-1]

print(revString(revStr))  

# Q6 
vowelStr = "yeouafgAPDOS";
vowCount = 0
def countVow(str):
  vowels = "aeiouAEIOU"
  vowCount = 0
  for name in str:
    if name in vowels :
      vowCount += 1
  return vowCount
print(countVow(vowelStr))

# Q7 
givenPrime = 7
def checkPrime(num):
  primeCount = 0
  for i in range(1, int(num) + 1):
    if num % i == 0 :
      primeCount += 1
     
  if primeCount == 2 :
    return True
  else :
    return False
     
print(checkPrime(givenPrime))
    
    
# Q8   
factNum = 4
def findFact(num):
  factProd = 1
  for i in range(1,num+1):
    factProd = factProd*i
  return factProd
  
print(findFact(factNum))

# Q9
def fibonacci_sequence(n):
    sequence = [0, 1]  
    for i in range(2, n):
        next_number = sequence[i-1] + sequence[i-2]
        sequence.append(next_number)
    return sequence[:n]
n = 5
fibonacci_numbers = fibonacci_sequence(n)
print(fibonacci_numbers)

# Q10
def listComph(a,b):
  newList = [];
  for i in range(a,b+1):
    newList.append(i*i);
  return newList;
print(listComph(1,10))