import csv

grades_subjects = {}
with open('grades.csv', newline='') as file:
    file = csv.DictReader(file)
    for row in file:
        grade = int(row['Grade'])
        subject = row['Subject']

        if subject not in grades_subjects:
            grades_subjects[subject] = []
        
        grades_subjects[subject].append(grade)

avg_subjects = []
for row in grades_subjects:
    avg = sum(grades_subjects[row]) / len(grades_subjects[row])
    avg_subjects.append({'Subject': row, 'AVG': round(avg, 1)})

with open('average_grades.csv', 'w', newline='') as file:
    fieldsname = ['Subject', 'AVG']
    writer = csv.DictWriter(file,fieldnames=fieldsname)

    writer.writeheader()
    for row in avg_subjects:
        writer.writerow(row)