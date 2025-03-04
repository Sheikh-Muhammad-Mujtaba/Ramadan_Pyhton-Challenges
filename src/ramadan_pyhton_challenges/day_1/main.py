import click #to create command line interface
import os #to interact with the operating system
import json #to work with json files


TODO_FILE = "todo.json"

# ANSI Escape Codes for Colors
class Colors:
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)
        
@click.group()
def cli():
    """Simple todo app manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)
    click.echo(f"{Colors.GREEN}Task added successfully: {task}{Colors.RESET}")

@click.command()    
def list():
    '''list all the tasks'''
    tasks = load_tasks()
    if not tasks:
        click.echo(f"{Colors.RED}No tasks found")
        return
    for index, task in enumerate(tasks, 1 ):
        status = f"{Colors.GREEN}Done ✅{Colors.RESET}" if task["done"] else f"{Colors.BOLD}{Colors.RED}Not done ❌{Colors.RESET}"
        click.echo(f"{Colors.YELLOW}{index}. {task['task']} -{Colors.RESET} [{status}] {Colors.RESET}")
        

@click.command()
@click.argument("task_number", type=int)
def complete(task_number):
    '''Mark a task as done'''
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['done'] = True
        save_tasks(tasks)
        click.echo(f"{Colors.GREEN}Task {task_number} marked as done{Colors.RESET}")
    else:
        click.echo(f"{Colors.RED}Invalid task number provided {task_number}{Colors.RESET}")


@click.command()
@click.argument("task_number", type=int)
def remove(task_number):
    '''Remove a task from the list'''
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        save_tasks(tasks)
        click.echo(f"{Colors.GREEN}Task {task_number} removed successfully{Colors.RESET}")
    else:
        click.echo(f"{Colors.RED}Invalid task number provided {task_number}{Colors.RESET}")

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(remove)


if __name__ == "__main__":
    cli()  