def add_note():
    note = input("Enter your note: ")
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note added.")

def view_notes():
    try:
        with open("notes.txt", "r") as file:
            content = file.read()
            if content.strip():
                print("\nYour Notes:")
                print(content)
            else:
                print("No notes found.")
    except FileNotFoundError:
        print("No notes file yet.")

def search_notes():
    keyword = input("Enter keyword to search: ")
    try:
        with open("notes.txt", "r") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    print(line.strip())
    except FileNotFoundError:
        print("No notes file found.")

def delete_notes():
    confirm = input("Delete all notes? (y/n): ")
    if confirm.lower() == "y":
        open("notes.txt", "w").close()
        print("All notes deleted.")

def main():
    while True:
        print("\nNotes Manager")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Search Notes")
        print("4. Delete All Notes")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            delete_notes()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
