import os
import sys
from datetime import datetime
from time import sleep

GREEN = "\033[1;32m"
CYAN = "\033[1;36m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

print(f"{GREEN}██╗    ██╗ █████╗ ███████╗██╗     █████╗ ██╗     ")
print(f"██║    ██║██╔══██╗██╔════╝██║    ██╔══██╗██║     ")
print(f"{CYAN}██║ █╗ ██║███████║███████╗██║    ███████║██║     ")
print(f"██║███╗██║██╔══██║╚════██║██║    ██╔══██║██║     ")
print(f"{GREEN}╚███╔███╔╝██║  ██║███████║███████╗██║  ██║███████╗")
print(f" ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚══════╝{RESET}")
print(f"\n{YELLOW}==================================================={RESET}")
print(f"{CYAN}          WASI AL OS v1.6 | Developer: Wasi Al      {RESET}")
print(f"{YELLOW}==================================================={RESET}\n")


print("\nStarting Wasi-Al-OS...")
for i in range(3):
    print("Loading" + "." * (i + 1))
    sleep(0.5)

password = "1234"

user_pass = input("Enter Password: ")

if user_pass != password:
    print("Wrong Password!")
    sys.exit()

print("Access Granted!")

name = input("\nEnter your name: ")
print(f"\nWelcome {name}!")

while True:
    print("\n========== MENU ==========")
    print("1. About System")
    print("2. Developer Info")
    print("3. Date & Time")
    print("4. Calculator")
    print("5. Notes")
    print("6. Exit")

    choice = input("\nChoose option: ")

    if choice == "1":
        print("\nWASI AL OS v1.6")
        print("A Python-based mini operating system.")

    elif choice == "2":
        print("\nDeveloper: Wasi Al")  
        print("GitHub: https://github.com/WasiaL007")

    elif choice == "3":
        print("\nCurrent Date & Time:")
        print(datetime.now())

    elif choice == "4":
        try:
            a = float(input("First number: "))
            op = input("Operator (+ - * /): ")
            b = float(input("Second number: "))

            if op == "+":
                print("Result =", a + b)
            elif op == "-":
                print("Result =", a - b)
            elif op == "*":
                print("Result =", a * b)
            elif op == "/":
                if b == 0:
                    print("Cannot divide by zero!")
                else:
                    print("Result =", a / b)
            else:
                print("Invalid operator!")

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    elif choice == "5":
        print("\n===== NOTES =====")
        print("1. Write Note")
        print("2. View Notes")

        note_choice = input("Choose option: ")

        if note_choice == "1":
            note = input("Write a note: ")
            with open("notes.txt", "a") as f:
                f.write(note + "\n")
            print("Note saved successfully!")

        elif note_choice == "2":
            print("\n===== SAVED NOTES =====")
            try:
                with open("notes.txt", "r") as f:
                    print(f.read())
            except:
                print("No notes found!")

        else:
            print("Invalid option!")

    elif choice == "6":
        print("\nShutting down Wasi-Al-OS...")
        break

    else:
        print("Invalid option!")
