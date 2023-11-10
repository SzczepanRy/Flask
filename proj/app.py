
from flask import Flask, render_template, request
import json

app = Flask(__name__)
def load_data():
    with open('salary.json', 'r') as file:
        data = json.load(file)
    return data



def averageSalary(data):
    total_salary = sum(float(record['salary']) for record in data)

    return round(total_salary / len(data),2)

def findLast(data, last_name):
    last={}
    for i in data :
        if(i['last_name'].lower() == last_name.lower()):
            last = i
    print(last)

    return last

def calculateMax(data):
    arr = []
    for i in data :arr.append(float(i['salary']))

    return round(max(arr),2)

def calculateMin(data):
    arr = []
    for i in data: arr.append(float(i['salary']))

    return round(min(arr), 2)


@app.route('/', methods=['GET'])
def display_data():
    data = load_data()
    parsed_data = []
    for key, value in data.items():
        record = value.split(';')
        parsed_data.append({
            'id':record[0],
            'last_name': record[1],
            'first_name': record[2],
            'salary': record[3]
        })

    max = calculateMax(parsed_data)
    print(max)
    min = calculateMin(parsed_data)
    average = round(averageSalary(parsed_data),2)

    return render_template('tablica.html', data=parsed_data, max=max, min=min,average=average)

@app.route('/find', methods=['POST'])
def find():
    data = load_data()
    parsed_data = []
    for key, value in data.items():
        record = value.split(';')
        parsed_data.append({
            'id': record[0],
            'last_name': record[1],
            'first_name': record[2],
            'salary': record[3]
        })

    max = calculateMax(parsed_data)
    print(max)
    min = calculateMin(parsed_data)
    average = round(averageSalary(parsed_data), 2)

    last_name = request.form['last_name']
    if last_name:
        matching_records = findLast(parsed_data, last_name)
        return render_template('tablica.html', data=matching_records, max=max, min=min,average=average)


if __name__ == '__main__':
    app.run(debug=True)