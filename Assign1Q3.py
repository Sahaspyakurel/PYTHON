def grade_exam(student_path,answers_path):
    with open(answers_path,"r") as file:
        correct_answers= file.read().splitlines()

    with open(student_path, "r") as file:
        student_answers=file.read().splitlines()

    num_correct_answers=0
    incorrect_answers=[]
    for i in range(len(correct_answers)):
        if student_answers[i]==correct_answers[i]:
            num_correct_answers += 1
        else:
            incorrect_answers.append(i+1)

    print(f"Total correct answers : {num_correct_answers}")
    print(f"Total incorrect answers : {len(incorrect_answers)}")
    print(f"Incorrect answers : {incorrect_answers}")

    if num_correct_answers>=15:
        print("The student passed the exam")

    else:
        print("The student has failed the exam")
    
answers_path="answers.txt"
student_path="student_answers.txt"

grade_exam(answers_path, student_path)
