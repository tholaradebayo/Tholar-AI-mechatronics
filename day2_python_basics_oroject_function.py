def get_student_scores(name):
    ''' ask for 3 scores and return as a list'''
    
    scores=[]
    for i in range(3):
        
        while True:
            try:
                score = float(input(f"Enter score {i+1} for {name} (0–100): "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100.")
                
            except ValueError:
                print('please enter a numeric number')
    
    return scores

def calculate_average(scores):
    '''compute mean'''
    
    
    average_scores= sum(scores)/len(scores)
    
    return average_scores

def get_grade(average):
    """Assign A, B, C, D, F based on average"""
    if 70 <= average <= 100:
        return 'A'
    elif 60 <= average < 70:
        return 'B'
    elif 50 <= average < 60:
        return 'C'
    elif 40 <= average < 50:
        return 'D'
    else:
        
        return 'F'
    
    

    

def analyze_class(data):
    """Compute class statistics (average, best, lowest students)"""
    
    averages = [info['average'] for info in data.values()]

    class_average = sum(averages) / len(averages)
    highest_average = max(averages)
    lowest_average = min(averages)

    highest_students = [name for name, info in data.items() if info['average'] == highest_average]
    lowest_students = [name for name, info in data.items() if info['average'] == lowest_average]
    
    return {
        'class_average': class_average,
        'highest_average': highest_average,
        'highest_students': highest_students,
        'lowest_average': lowest_average,
        'lowest_students': lowest_students
    }


def display_summary(data, stats):
    """Display student results and class summary without tabulate"""
    
    print("\n--- STUDENT RESULTS ---")
    print(f"{'Name':<15} {'Scores':<20} {'Average':<8} {'Grade':<6}")
    print("-"*55)
    
    
    for name, info in data.items():
        scores_str = ', '.join(str(s) for s in info['scores'])
        print(f"{name:<15} {scores_str:<20} {info['average']:<8.2f} {info['grade']:<6}")
    

    print("\n--- CLASS SUMMARY ---")
    print(f"Class average: {stats['class_average']:.2f}")
    print(f"Highest average: {stats['highest_average']:.2f} by {', '.join(stats['highest_students'])}")
    print(f"Lowest average: {stats['lowest_average']:.2f} by {', '.join(stats['lowest_students'])}")



def main():
    print("WELCOME TO STUDENT GRADE ANALYSIS")
    
    while True:
        try:
            n = int(input("How many students? "))
            if n > 0:
                break
            else:
                print(" Please enter a positive number.")
        except ValueError:
            print(" Invalid input! Enter a number.")
    
    student_data = {}
    for i in range(n):
        name = input("\nEnter student's name: ")
        scores = get_student_scores(name)
        average = calculate_average(scores)
        grade = get_grade(average)
        student_data[name] = {
            'scores': scores,
            'average': average,
            'grade': grade
        }
    
    summary = analyze_class(student_data)
    display_summary(student_data, summary)


if __name__ == "__main__":
    main()