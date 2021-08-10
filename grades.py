def grades(number1, number2, number3):
    homework = (number1 / 25) * 100
    assessment = (number2 / 50) * 100
    exam = (number3 / 100) * 100
    return homework, assessment, exam

scores = grades(20, 30, 70)
name = input("What is your name?")
print(name, "ICT Grades", scores)