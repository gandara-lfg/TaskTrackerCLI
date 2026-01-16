import sys 
import os
import json
from datetime import datetime

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    else:
        return []
    
def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=2)


def addTask(task):
    tasks = load_tasks()
    if tasks:
        highest_id = 0
        for t in tasks:
            if t["id"] > highest_id:
                highest_id = t["id"]
        id = highest_id + 1
    else:
        id = 1

    new_task = {"id": id, 
                "description": task, 
                "status": "To do",
                "createdAt": datetime.now().isoformat(),
                "updatedAt": datetime.now().isoformat()}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {id})")

def removeTask(id):
    tasks = load_tasks()
    id = int(id)
    
    found = False
    new_tasks = []
    
    for task in tasks:
        if task["id"] == id:
            found = True  # Don't add this one
        else:
            new_tasks.append(task)
    
    if found:
        save_tasks(new_tasks)
        print(f"Task removed successfully (ID: {id})")
    else:
        print(f"Task with ID {id} not found")  

def changeStatus(id, status):
    tasks = load_tasks()
    currTask = tasks[int(id)-1]
    status = int(status)
    match status:
        case 1:
            currTask["status"] = "To do"
        case 2:
            currTask["status"] = "In Progress"
        case 3:
            currTask["status"] = "Completed"
    currTask["updatedAt"] = datetime.now().isoformat()
    save_tasks(tasks)
    print(f"Task status successfully changed")


def printTasks():
    tasks = load_tasks()
    print("---------------------------")
    print("|        All tasks:       |")
    print("---------------------------")
    print("----------------------------------------")
    for task in tasks:
        print("ID: " + str(task["id"]))
        print("Task: " + task["description"])
        print("Status: " + task["status"])
        print("Time Created: " + task["createdAt"])
        print("Time Updated: " + task["updatedAt"])
        print("----------------------------------------")


def printMain():
    print("---------------------------")
    print("|    WELCOME TO TASKER    |")
    print("---------------------------")

def printCommands():
    print("----------------------------------------------------------------------------")
    print("ALL COMMANDS:")
    print("help - gives you all possible commands")
    print("print - prints the entire current todo list")
    print("add (task) - adds the task given after the command to the todo list")
    print("remove (task) - removes the task given after the command to the todo list")
    print("status (id) (#)- changes the status of the id inputed to inputed status"
          "\nTypes of # for status:")
    print("1 - todo | 2 - in progress | 3 - completed")
    print("----------------------------------------------------------------------------")


def main():

    if len(sys.argv) < 2:
        print("Please type a command")
    else:
        command = sys.argv[1]

        match command:
            case "start":
                printMain()
                printCommands()
            case "help":
                printCommands()
            case "add":
                if len(sys.argv) < 3:
                    print("Please provide what task you would like to add")
                else:
                    addTask(sys.argv[2])
            case "remove":
                if len(sys.argv) < 3:
                    print("Please provide what task you would like to remove")
                else:
                    removeTask(sys.argv[2])
            case "print":
                printTasks()
            case "status":
                if len(sys.argv) < 3:
                    print("Please provide the id type of status of the task you would like to modify")
                elif (len(sys.argv) < 4) or (not sys.argv[3].isdigit()):
                    print("Please provide the type of status as an int (type help to see all options)")
                else:
                    changeStatus(sys.argv[2], sys.argv[3])
    

if __name__ == "__main__":
    main()
