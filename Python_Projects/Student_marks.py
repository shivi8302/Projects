studetn_marks = { }

def add_student(name, mark):
    studetn_marks[name] = mark

    print(f"Added '{name}' with a {mark}")

def update_student(name, mark):
    if name in studetn_marks:
        studetn_marks[name] = mark
        print(f"'{name}' with a marks are updated {mark}")

    else:
        print(f"{name} is not found")

def delete_student(name):
    if name in studetn_marks:
        del studetn_marks[name]
        print(f"{name} is successfully deleted")

    else:
        print(f"{name} is not found")

def display_all_student(name,mark):
    if name in studetn_marks:
        for name, mark in studetn_marks.items():
            print(f"{name}:{mark}")

    else:
        print("student",name,"not found")

def main():
    while True:
        print("\nStudent Marks Management System ")     
        print("1. Add student")     
        print("2. Update student")     
        print("3. Delete student")     
        print("4. Display student")     
        print("5. Exit")     
        choice = int(input("Enter your choice:"))
        if choice == 1:
             name =  input("Enter student name:")
             mark = int(input("Enter student marks:"))
             add_student(name, mark)

        elif choice == 2:
            name =  input("Enter student name:")
            mark = int(input("Enter student marks:"))
            update_student(name, mark)

        elif choice == 3:
            name =  input("Enter student name:")
            delete_student(name)

        elif choice == 4:
            print("\nThe list of all students>>")
            display_all_student(name, mark)
            
        elif choice == 5:
            print("Closing the program...")
            break

        else:
            print("Invalid choice")            
       
main()