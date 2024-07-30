import os
from collections import Counter

def menu():
    print("\nText File Organizer")
    print("-------------------")
    print("1. Create a new file")
    print("2. View a file")
    print("3. Append text to a file")
    print("4. Search for a word in a file")
    print("5. Count words in a file")
    print("6. Sort lines in a file")
    print("7. Edit a line in a file")
    print("8. Word frequency analysis")
    print("9. Encrypt a file")
    print("10. Decrypt a file")
    print("11. Backup a file")
    print("12. Restore a file")
    print("13. Merge files")
    print("14. Split file")
    print("15. Find and replace in a file")
    print("16. Display file statistics")
    print("17. Delete a file")
    print("18. List all files")
    print("19. Exit")

def create_file():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        print("File already exists.")
    else:
        with open(filename, 'w') as file:
            print("New file created successfully.")
            content = input("Enter text to write to the file:\n")
            file.write(content + "\n")

def view_file():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            print(f"\nContents of {filename}:\n")
            print(content)
    else:
        print("File not found.")

def append_to_file():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        with open(filename, 'a') as file:
            content = input("Enter text to append to the file:\n")
            file.write(content + "\n")
            print("Text appended successfully.")
    else:
        print("File not found.")

def search_in_file():
    filename = input("Enter the filename: ")
    word = input("Enter the word to search for: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            count = content.lower().count(word.lower())
            print(f"The word '{word}' was found {count} time(s) in {filename}.")
    else:
        print("File not found.")

def count_words_in_file():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            word_count = len(content.split())
            print(f"The file {filename} contains {word_count} word(s).")
    else:
        print("File not found.")

def sort_lines_in_file():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        lines.sort()
        with open(filename, 'w') as file:
            file.writelines(lines)
        print(f"Lines in {filename} have been sorted alphabetically.")
    else:
        print("File not found.")

def edit_line_in_file():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        for index, line in enumerate(lines):
            print(f"{index + 1}: {line.strip()}")
        try:
            line_num = int(input("Enter the line number to edit: "))
            if 1 <= line_num <= len(lines):
                new_line = input("Enter the new content: ")
                lines[line_num - 1] = new_line + "\n"
                with open(filename, 'w') as file:
                    file.writelines(lines)
                print("Line updated successfully.")
            else:
                print("Invalid line number.")
        except ValueError:
            print("Please enter a valid line number.")
    else:
        print("File not found.")

def word_frequency_analysis():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read().lower()
            words = content.split()
            word_freq = Counter(words)
        print("\nWord Frequency Analysis:")
        for word, freq in word_freq.most_common():
            print(f"{word}: {freq}")
    else:
        print("File not found.")

def encrypt_decrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = key if char.islower() else -key
            new_char = chr((ord(char) + shift - 97) % 26 + 97)
            result += new_char
        else:
            result += char
    return result

def encrypt_file():
    filename = input("Enter the filename: ")
    key = int(input("Enter the key (number of positions to shift): "))
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        encrypted_content = encrypt_decrypt(content, key)
        with open(filename, 'w') as file:
            file.write(encrypted_content)
        print(f"The file {filename} has been encrypted.")
    else:
        print("File not found.")

def decrypt_file():
    filename = input("Enter the filename: ")
    key = int(input("Enter the key (number of positions to shift): "))
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
        decrypted_content = encrypt_decrypt(content, -key)
        with open(filename, 'w') as file:
            file.write(decrypted_content)
        print(f"The file {filename} has been decrypted.")
    else:
        print("File not found.")

