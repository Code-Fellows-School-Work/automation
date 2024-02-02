from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
import os
# shell utility
import shutil
import re

console = Console()

def create_folder(directory):
    os.mkdir(directory)

def remove_user(user_name):
    """
    Deletes a user and moves it to the recycle bin located in automation/assets/recycle
    """
    try:
        # location of users
        base_directory = "automation/assets"
        
        recycle_folder_name = "recycle"
        target_path = os.path.join(base_directory, recycle_folder_name, user_name)  # Correct path to
        
        # used ChatGPT to figure out how to create directory if it doesn't exist
        # create recycle directory if it doesn't exist
        if not os.path.exists(os.path.join(base_directory, recycle_folder_name)):
            os.makedirs(os.path.join(base_directory, recycle_folder_name))
        
        source_path = os.path.join(base_directory, user_name)
        
        # move the directory to the recycle bin
        shutil.move(source_path, target_path)
        
    except FileNotFoundError:
        console.print("[bold red] Directory or file not found [/bold red]")

def list_files(directory):
    """
    Display all the files in the directory
    """
    try:
        files = os.listdir(directory)
        table = Table(title=f"Files in {directory}")
        table.add_column("File Name", style="dim")
        for file in files:
            table.add_row(file)
        console.print(table)
    except FileNotFoundError:
        console.print("[bold red] File not found [/bold red]")

def move_file(directory, file, target_directory):
    """
    Move the given file from the current directory to the target directory
    """
    try:
        source_path = os.path.join(directory, file) # platform specific full file path
        target_path = os.path.join(target_directory, file)
        shutil.move(source_path, target_path)
        console.print(f"{file} moved from {directory} to {target_directory}")
    except FileNotFoundError:
        console.print("[bold red] Directory or file not found [/bold red]")

def search_files(directory, pattern):
    """
    Searches for a file in a directory
    """
    try:
        # files refers to all the file names in the directory
        files = os.listdir(directory)
        matches = [file for file in files if re.search(pattern, file)]
        table = Table(title=f"Files in {directory}")
        table.add_column("Matching File Name", style="dim")
        for match in matches:
            table.add_row(match)
        console.print(table)
    except FileNotFoundError:
        console.print("[bold red] Directory not found [/bold red]")

def test(args):
    print(args)


if __name__ == "__main__":

    while True:
    # console.print adds the formatting to the numbers
        console.print("\n1. Create new directory\n2. Delete user\n3. Search Files\n4. Exit")
        choice = Prompt.ask("Choose a task (Enter the number)")

        if choice == "1":
            directory = Prompt.ask("Enter the directory name")
            create_folder(directory)
        elif choice == "2":
            user_name = Prompt.ask("Enter the user name")
            remove_user(user_name)
        # elif choice == "3":
        #     directory = Prompt.ask("Enter the directory to search files")
        #     pattern = Prompt.ask("Enter the regex pattern to search for:")
        # else:
            break
