import statistics

universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats():
    total_students = 0
    total_tuition = 0
    for i in range(0, len(universities)):
        total_students+=universities[i][1]
        total_tuition+=universities[i][2]
    return total_students, total_tuition

def median():
    median_student = []
    median_tuition = []
    for i in range(0, len(universities)):
        median_student.append(universities[i][1])
        median_tuition.append(universities[i][2])
    return statistics.median(median_student), statistics.median(median_tuition)

def mean():
    mean_students = sum(list(x[1] for x in universities))/len(universities)
    mean_tuition = sum(list(x[2] for x in universities))/len(universities)
    return mean_students, mean_tuition

total_students, total_tuition = enrollment_stats()
median_students, median_tuition = median()
mean_students, mean_tuition = mean()

print('******************************')
print(f'Total students: {total_students:,}')
print(f'Total tuition: $ {total_tuition:,}\n')
print(f'Student mean: {mean_students:,.2f}')
print(f'Student median: {median_students:,}\n')
print(f'Tuition mean: $ {mean_tuition:,.2f}')
print(f'Tuition median: $ {median_tuition:,}')
print('******************************')