import easygui
import csv
from datetime import datetime
import time

def taskchecker():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    doin = easygui.enterbox("What have you been doing?")
    print(f"Added your task '{doin}' Next task check in 15mins")
    csvData = [['Date', 'Task'], [dt_string, doin]]
    with open('tasks.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(csvData)
    csvFile.close()


if __name__ == '__main__':
    while True:
        taskchecker()
        time.sleep(900.0)

