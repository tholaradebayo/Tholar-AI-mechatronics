print('WELCOME TO STUDENT GRADE ANALYSIS')

while True:
    try:
        n = int(input('How many students? '))
        if n <= 0:
            print("Please enter a positive number of students.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a valid number.")
data={}

for i in range(n):
    name=input('what is the name of the student ')
    while True:
        try:
            score = float(input(f"Enter {name}'s score (0–100): "))
            if 0 <= score <= 100:
                break
            else:
                print("Score must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    if score <= 100 and score >= 70:
        grade='A'
    
    
    elif score<70 and score>=60:
        grade='B'
    
    elif score<60 and score>=50:
        grade='C'
        

    else:
        grade='F'
        
    data[name] = {'score': score, 'grade': grade}
    
scores = [info['score'] for info in data.values()] 

average_score = sum(scores) / len(scores)
highest_score = max(scores)
lowest_score = min(scores)

highest_students = [name for name, info in data.items() if info['score'] == highest_score]
lowest_students = [name for name, info in data.items() if info['score'] == lowest_score]

        
for name, info in data.items():
    print(f"{name} scored {info['score']} which is graded as {info['grade']}")
    
    
print(f"Class average: {average_score:.2f}")
print(f"Highest score: {highest_score} by {', '.join(highest_students)}")
print(f"Lowest score: {lowest_score} by {', '.join(lowest_students)}")
    
    