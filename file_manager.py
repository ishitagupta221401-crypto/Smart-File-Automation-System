import os
import shutil

from logger import log_activity

def create_file(filename):
    try:
        with open(filename,"w")as file:
            file.write("")

        log_activity(f"Created file :{filename}")
        print("File created successfully.")

    except Exception as e:
        print("Error :", e)


def read_file(filename):
    try:
        with open(filename, "r")as file:
            print("\nFile Content:\n")
            print(file.read())

        log_activity(f"Read file :{filename}")

    except FileNotFoundError:
        print("File not found. ")


def write_file(filename, text):
    try:
        with open(filename, "a")as file:
            file.write(text + "\n")

        log_activity(f"Update file: {filename}")
        print("Data written successfully.")

    except Exception  as e:
        print("Error:",e)

def rename_file(old_name, new_name):
    try:
        os.rename(old_name,new_name)

        log_activity(
            f"Renamed {old_name}to{new_name}"
        )

        print("File renamed successfully.")

    except Exception as e:
        print("Error:",e)


def move_file(source, destination):
    try:
        shutil.move(source, destination)

        log_activity(
            f"Moved {source} to {destination}"
        )            

        print("File moved successfully.")

    except Exception as e:
        print("Error:",e)   

def delete_file(filename):
    try:
        os.remove(filename)

        log_activity(
            f"Deleted file: {filename}"
        )

        print("File deleted successfully.")

    except Exception as e:
        print("Error:", e)       