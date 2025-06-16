import json
import csv

with open('tasks.json', 'r') as file:
    data = json.load(file)

def total_tasks(data):
    return len(data)

def completed_tasks(data):
    num = 0
    for value in data:
        if value['completed'] == True:
            num += 1 
    return num

def pending_tasks(data):
    return len(data)-completed_tasks(data)

def average_lvl(data):
    avg = sum([priority['priority'] for priority in data]) / total_tasks(data)
    return round(avg, 1)

for row in data:
    print(f"ID: {row['id']} Task: {row['task']} completed: {row['completed']} priority: {row['priority']}")

print(f"Total tasks: {total_tasks(data)} \nCompleted tasks: {completed_tasks(data)} \nPending tasks: {pending_tasks(data)} \nAverage priority: {average_lvl(data)}")

with open('tasks.csv', 'w', newline='') as file:
    fildnames = ['id', 'task', 'completed', 'priority']
    writer = csv.DictWriter(file, fildnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)