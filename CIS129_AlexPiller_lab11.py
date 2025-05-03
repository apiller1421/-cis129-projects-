# 9.1
def write_grades():
    with open("grades.txt", "w") as file:
        while True:
            try:
                grade = int(input("Enter a grade (or -1 to finish): "))
                if grade == -1:
                    break
                file.write(f"{grade}\n")
            except ValueError:
                print("Please enter a valid integer grade.")

write_grades()

# 9.2
def read_and_calculate_average():
    try:
        with open("grades.txt", "r") as file:
            grades = [int(line.strip()) for line in file if line.strip().isdigit()]
        
        if grades:
            total = sum(grades)
            count = len(grades)
            average = total / count

            print("\nGrades:")
            for grade in grades:
                print(grade)

            print(f"\nTotal: {total}")
            print(f"Count: {count}")
            print(f"Average: {average:.2f}")
        else:
            print("No valid grades found in the file.")
    except FileNotFoundError:
        print("grades.txt not found. Run 9.1 first.")

read_and_calculate_average()

# 9.3
def write_student_records():
    with open("grades.csv", "w", newline="") as file:
        writer = csv.writer(file)

        while True:
            first = input("Enter student's first name (or 'done' to finish): ")
            if first.lower() == 'done':
                break
            last = input("Enter student's last name: ")

            try:
                exam1 = int(input("Enter exam 1 grade: "))
                exam2 = int(input("Enter exam 2 grade: "))
                exam3 = int(input("Enter exam 3 grade: "))
                writer.writerow([first, last, exam1, exam2, exam3])
            except ValueError:
                print("Invalid input. Please enter integer grades.")

write_student_records()
