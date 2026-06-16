from file_manager import (
    create_file,
    read_file,
    write_file,
    rename_file,
    move_file,
    delete_file
)

from csv_handler import read_csv

while True:
    print("\n=============================")
    print(" SMART FILE AUTOMAITON SYSTEM ")
    print("=============================")

    print("1. Create File")
    print("2. Read File")
    print("3. Write File")
    print("4. Rename File")
    print("5. Move File")
    print("6. Delete File")
    print("7. Read CSV File")
    print("8. Exit")

    choice = input("\nEnter your choice : ")

    if choice == "1":

        filename = input("Enter the filename to create : ")
        create_file(filename)

    elif choice == "2":

        filename = input("Enter the filename to read : ")
        read_file(filename)    

    elif choice == "3":

        filename = input("Enter the filename to write : ")
        content = input("Enter the content to write : ")
        
        write_file(filename, content)   

    elif choice == "4":

        old_name = input("Enter the current filename : ")
        new_name = input("Enter the new filename : ")
        
        rename_file(old_name, new_name)

    elif choice == "5":

        filename = input("Enter the filename to move : ")
        destination = input("Enter the destination path : ")
        
        move_file(filename, destination)  

    elif choice == "6":

        filename = input("Enter the filename to delete : ")
        delete_file(filename)

    elif choice == "7":

        filename = input("Enter the CSV filename to read : ")
        read_csv(filename)

    elif choice == "8":
        print("\n Thank you for using File Automation System. \nGoodbye!")
        break  

    else:
        print("Invalid choice. Please try again.")                 