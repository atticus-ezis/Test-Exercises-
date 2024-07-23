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

file_path = '/Users/atticusezis/coding/sandbox/Python Excersizes/data.txt'

def calculate_average_score(file_path):
    new_dict=[]
    with open(file_path, 'r') as file:
        for line in file:
            parts = line.strip().split(', ')
            name = parts[0]
            scores = list(map(int, parts[1:]))
            average_score = sum(scores) / len(scores)
            new_dict.append({'name':name, 'average score': round(average_score,2)})
    return new_dict
print(calculate_average_score(file_path))


