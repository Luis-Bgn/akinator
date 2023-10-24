import json
from collections import deque
import os

def load_db(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
    return data

def add_newData(file_path: str, data: dict):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent= 2)

def get_Answer(question: str,answer: str, database: dict) -> str | None:
    for q in database["actual"]:
        if q[question] != answer.lower():
            database["actual"].remove(q)
            add_newData('Database.json',database)
    return q["name"]

def get_Question(database: dict, questions: deque):
    if len(list(database['actual'])) <= 1: return
    found: bool = False
    i,k = 0,0
    while found == False:
        q:str = database['actual'][i]
        x: str = q.keys()
        j = 1
        while True:
            aQuestion = list(x)[j]
            if aQuestion in questions:
                print(f'ya existe la pregunta : {aQuestion}')
            else:
                questions.append(aQuestion)
                found = True
                break
            if j < len(x)-1: j = j+1
            else:
                break
        if i < len(list(database['actual']))-1: i = i+1
        else: found = True
    while True:
        y = list(database['preguntas'][0].keys())[k]
        if y == aQuestion:
            print(list(database['preguntas'][0].values())[k])
            break
        if k < len(list(database['preguntas'][0].values())[k])-1: k = k+1
        else: break
    return aQuestion

def start(database: dict):
    database['actual'].clear()
    add_newData('Database.json',database)
    for q in database["types"]:
        database["actual"].append(q)
        add_newData('Database.json',database)
    return

def main():
    database: dict = load_db('Database.json')
    start(database)
    print(" \t| Akinator | \nResponde con 'si' o 'no' o 'exit")
    qList = deque([])
    while True:
        if len(list(database['actual'])) == 0:
            print("Error")
            break
        question = get_Question(database, qList)
        while True:
            us_input: str = input('Tu: ')
            if us_input.lower() == 'si' or us_input.lower() == 'no' or us_input.lower() == 'exit':
                break 
        answer: str = get_Answer(question, us_input, database)
        os.system('cls')
        if us_input.lower() == 'exit' or len(list(database['actual'])) <= 1:
            print("Eres el estudiante", list(database['actual'][0].values())[0])
            break

if __name__ == '__main__':
    main()