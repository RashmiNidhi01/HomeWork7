import pandas as pd
point = 0.0
grade_gpa = ''

def get_student_grades(score):

    if score >= 90:
        grade_gpa= 'A'
        point = 4.0
    elif score >= 80:
        grade_gpa = 'B'
        point = 3.0
    elif score >= 70:
        grade_gpa = 'C'
        point = 2.0
    elif score >= 60:
        grade_gpa = 'D'
        point = 1.0
    elif score < 60:
        grade_gpa = 'F'
        point = 0.0
    return point

def main():
    
    READ_FILENAME = 'scores.csv'
    scores = pd.read_csv('scores.csv', delimiter=',', index_col=0, header=0)

    student_grades = scores.applymap(get_student_grades)
    pd.set_option('precision', 2)

    mean = student_grades.mean(axis = 0)
    print(mean)
    gpa = student_grades.stack().mean()
    print(f'The class GPA is {gpa:.2f}')

main()