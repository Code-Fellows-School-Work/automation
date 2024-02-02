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

def delete_user(directory, file, target_directory):
    """
    Transfers a user file to the recycle folder. If recycle folder doesn't exist, also creates recycle folder
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
        console.print("\n1. Create new directory\n2. Move file\n3. Search Files\n4. Exit")
        choice = Prompt.ask("Choose a task (Enter the number)")

        if choice == "1":
            directory = Prompt.ask("Enter the directory name")
            create_folder(directory)
        # elif choice == "2":
        #     directory = Prompt.ask("Enter the current directory of the file")
        #     file = Prompt.ask("Enter the file to move")
        #     target_directory = Prompt.ask("Enter the target directory to move file to")
        #     move_file(directory, file, target_directory)
        # elif choice == "3":
        #     directory = Prompt.ask("Enter the directory to search files")
        #     pattern = Prompt.ask("Enter the regex pattern to search for:")
        # else:
            break
