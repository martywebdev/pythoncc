from pathlib import Path

path = Path('guest.txt')

print("Enter 'quit' to exit the program.")

while True:
    name = input("What's your name? ")

    if name.lower() == 'quit':
        break

    # Append the name to the file
    if path.exists():
        current_content = path.read_text()
        path.write_text(current_content + f"{name}\n")
    else:
        path.write_text(f"{name}\n")

    print(f"Added {name} to the guest list!")
