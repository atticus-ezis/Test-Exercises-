# Problem 1 
# You are given a list of dictionaries, where each dictionary contains information about a person  
# Your task is to write a function that sorts this list of dictionaries by score in descending order 
# and then by age in ascending order if scores are equal. 

people = [
    {'name': 'John', 'age': 25, 'score': 90},
    {'name': 'Jane', 'age': 22, 'score': 90},
    {'name': 'Dave', 'age': 27, 'score': 85},
    {'name': 'Lucy', 'age': 24, 'score': 95},
    {'name': 'Mark', 'age': 23, 'score': 85}
]

people_decending = sorted(people, key=lambda student: (-student['score'], student['age']))
#print(people_decending)

# Problem 2
# You are given a text file named data.txt containing several lines of text. 
# Each line represents a record of a student's name and their scores in three subjects 
# Your task is to write a function that reads this file, calculates the average score for each student, 
# and returns a list of dictionaries where each dictionary contains the student's name and their average score.

file_path = '/Users/atticusezis/coding/sandbox/Python Exercises/data.txt'

def calculate_average_score(file_path):
   score_dict = []
   with open(file_path, 'r') as file:
      for line in file:
         cleaned_list = line.strip().split(', ')
         name = cleaned_list[0]
         scores = list(map(int, cleaned_list[1:]))
         average_score = sum(scores)/ len(scores)
         score_dict.append({'name':name, 'average_score':round(average_score,2)})
      return score_dict
#print(calculate_average_score(file_path))

# You are given a list of dictionaries representing a collection of books in a library. 
# Each dictionary contains the following keys: title, author, year, and genre. 
# Write a Python function called filter_books that filters the books based on the given criteria. 
# The function should accept four optional parameters: author, year, genre, and title_contains. 
# The function should return a list of books that match all the provided criteria.

books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "Fiction"},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction"},
    {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian"},
    {"title": "Moby Dick", "author": "Herman Melville", "year": 1851, "genre": "Adventure"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "year": 1951, "genre": "Fiction"}
]

def filter_books(books, author=None, year=None, genre=None, title_contains=None):
   filtered_books = books

   if author:
      filtered_books = [book for book in filtered_books if book['author'] == author]
   if year:
      filtered_books = [book for book in filtered_books if book['year'] == year]
   if genre: 
      filtered_books = [book for book in filtered_books if book['genre'] == genre]
   if title_contains:
      filtered_books = [book for book in filtered_books if title_contains.lower() in book['title'].lower()]
   return filtered_books
test = filter_books(books, title_contains='M')
#print(test)

# Write a Python function called separate_words_and_numbers that takes this string as input 
# and returns a tuple containing two lists: one list of words and another list of numbers. 
# The numbers should be returned as integers.

input_string = "apple 12 banana 34 cherry 56"

def separate_words_and_numbers(input_string):
  string_list = input_string.strip().split()
  numbers = []
  words = []
  for x in string_list:
     if x.isdigit():
        numbers.append(int(x))
     else:
        words.append(x)
  return words, numbers 


words, numbers = separate_words_and_numbers(input_string)
#print(words)

# You are given a list of tuples, where each tuple represents a point in a 2D plane with x and y coordinates. 
# Write a Python function called closest_point that takes this list of points 
# and a single point as arguments and returns the point from the list that is closest to the given point. 
# Use the Euclidean distance to determine the closeness.

import math

points = [(1, 2), (3, 4), (5, 6), (7, 8)]
reference_point = (4, 4)

def closest_point(points, reference_point):
    x2 = reference_point[0]
    y2 = reference_point[1]

    distance_list = []

    for point in points:
       x1 = point[0]
       y1 = point[1]
       distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
       distance_list.append({"point":point, "distance":round(distance,2)})
       sorted_list = sorted(distance_list, key=lambda dis: dis['distance'])
    return sorted_list


test = closest_point(points, reference_point)
#print(test)

# You are given a list of transactions where each transaction is represented as a dictionary 
# with the following keys: id, amount, and type
# The type can be either "credit" or "debit". 
# Write a Python function called calculate_balance that calculates and returns the final balance 
# after processing all transactions. The balance starts at 0. A "credit" transaction adds 
# the amount to the balance, while a "debit" transaction subtracts the amount from the balance.

transactions = [
    {"id": 1, "amount": 100, "type": "credit"},
    {"id": 2, "amount": 50, "type": "debit"},
    {"id": 3, "amount": 200, "type": "credit"},
    {"id": 4, "amount": 30, "type": "debit"}
]

def calculate_balance(transactions):
   
   balance = 0

   for item in transactions:
      if item['type'] == "credit":
         balance += item["amount"]
      else:
         balance -= item["amount"]
   return balance

test = calculate_balance(transactions)
# print(test)
    
# You are given a list of strings representing names. 
# Write a Python function called group_anagrams that groups the anagrams together. 
# The function should return a list of lists, where each sublist contains strings that are anagrams of each other.

from collections import defaultdict

names = ["listen", "silent", "enlist", "hello", "ohlle", "world"]

def group_anagrams(names):
   
   anagram = defaultdict(list)

   for name in names:
      name_list = ''.join(sorted(name.lower()))
      anagram[name_list].append(name)
   return (anagram.values())

#print(group_anagrams(names))
   
# Write a Python function called find_top_k_frequent that takes this list and an integer k as arguments 
# and returns a list of the k most frequent elements in descending order of their frequency. 
# If two elements have the same frequency, they should be returned in descending order of their value.

from collections import Counter

nums = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5]
k = 3

def find_top_k_frequent(nums, k):
   
   freq = Counter(nums)

   sorted_list = sorted(freq.items(), key=lambda x: (-x[0], -x[1]) )

   top_k = (element for element in sorted_list[:k])
      
#print(find_top_k_frequent(nums, k))


# swap variables

x = 1
y = 2

x, y = y, x

# check if number is prime 

def is_prime():
   x = int(input("enter number"))
   if x < 2:
      print("1 isn't prime")
   for i in range(2, int((x**.5)+1)):
      if x % i == 0:
         print("Not prime")
         return
   print("prime")

# check factorial of a number 

def factorial_finder():
   x = int(input('number: '))
   factorial = x
   for i in range(2,x):
      factorial = factorial * i 
   print(factorial)

#factorial_finder()

dict_memo = {}
def factorial_memo(n):
   if n == 0:
      return 1
   if n in dict_memo:
      return dict_memo[n]

   dict_memo[n] = n * factorial_memo(n-1)
   return dict_memo[n]

#print(factorial_memo(3))














memo = {}
def integral_memo(x):
   if x == 0:
      return 1
   if x in memo:
      return memo[x]
   memo[x] = x * integral_memo(x-1)
   return memo[x]


print(integral_memo(3))
      

