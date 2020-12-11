def map_grade_gpa(score):
# The function accepts the candidate score as an input and returns the grade and GPA
    if score >= 90:
        return ('A',4.0)
    elif score >=80:
        return ('B',3.0)
    elif score >=70:
        return ('C',2.0)
    elif score >=60:
        return ('D',1.0)
    else:
        return ('F',0.0)

def main():

# Parsing the file
    with open("score.csv") as f:
        score_list = f.readlines()
    score_list = [x.strip() for x in score_list]

# Handling each entry
    name_list = []
    grade_list = []
    total_gpa = 0
    for entry in score_list:
        name = " ".join(entry.split(" ")[:-1])
        score = int(entry.split(" ")[-1].strip())
        name_list.append(name)

#  Calculate the Grade and GPA for each score
        grade, gpa = map_grade_gpa(score)
        grade_list.append(grade)
        total_gpa += gpa
    average_gpa = total_gpa/len(name_list)    

 # Saving the output
    with open("grade.txt", "w") as f:
        for name,grade in zip(name_list, grade_list):
            individual_grade_string = name +" "+ grade + "\n"
            f.write(individual_grade_string)
        class_gpa_string = "The class GPA is " + str(round(average_gpa,2))
        f.write(class_gpa_string)
main()
