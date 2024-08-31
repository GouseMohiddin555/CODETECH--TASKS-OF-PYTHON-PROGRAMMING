def input_grades():
    grades = {}
    print("Enter the grades for each subject/assignment. Type 'done' when finished.")
    
    while True:
        subject = input("Enter subject/assignment name: ")
        if subject.lower() == 'done':
            break
        try:
            grade = float(input(f"Enter grade for {subject}: "))
            if grade < 0 or grade > 100:
                print("Grade must be between 0 and 100. Please try again.")
                continue
            grades[subject] = grade
        except ValueError:
            print("Invalid input. Please enter a numeric value for the grade.")
    
    return grades

def calculate_average(grades):
    if not grades:
        return 0
    return sum(grades.values()) / len(grades)

def display_grades(grades, average):
    print("\n--- Grades Summary ---")
    for subject, grade in grades.items():
        print(f"{subject}: {grade:.2f}")
    print(f"\nAverage Grade: {average:.2f}")
    
    if average >= 90:
        print("Overall Grade: A")
    elif average >= 80:
        print("Overall Grade: B")
    elif average >= 70:
        print("Overall Grade: C")
    elif average >= 60:
        print("Overall Grade: D")
    else:
        print("Overall Grade: F")

def main():
    grades = input_grades()
    average = calculate_average(grades)
    display_grades(grades, average)

if __name__ == "__main__":
    main()
