import pandas as pd
scores=pd.read_csv('scores.csv', header=0, index_col=0)
def map_grade_gpa(score):
# The function accepts the candidate score as an input and returns the grade and GPA
    if score >= 90:
        grade= ('A',4.0)
    elif score >=80:
        grade= ('B',3.0)
    elif score >=70:
        grade= ('C',2.0)
    elif score >=60:
        grade= ('D',1.0)
    else:
        grade= ('F',0.0)
        return grade

#  Calculate the Grade and GPA for each score
total_gpa=0.0
total_rows=len(scores.index)
total_columns=len(scores.columns)
s_gpa=0.0
for i in scores.columns:
    print(i, end='')
    total=0.0
    for j in scores[i]:
        grade=map_grade_gpa(j)
        total += grade
        s_gpa = total/total_rows
        print(f'{(s_gpa):.2}')
        total_gpa=s_gpa
        print(f'The class GPA is:{(total_gpa/total_columns):.2}')





