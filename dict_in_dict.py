students = {
    1: {'name': 'John', 'school': 'AUBG', 'grades': [2,3,4,6,5]},
    2: {'name': 'Katya', 'school': 'AUBG', "grades": [3,5,6,5,6]},
    3: {'name': 'Tony', 'school': 'AUBG', "grades": [4,4,6,6,6]}
           }


for i in students: 
        grade_average=(float(sum(students[i]["grades"]))/float(len(students[i]["grades"]))) 
        print("Student name: ",students[i]["name"],"\tAverage grades: ",grade_average)