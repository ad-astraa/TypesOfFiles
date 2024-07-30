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
def backup_file():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        backup_filename = filename + ".backup"
        with open(filename, 'r') as file:
            content = file.read()
        with open(backup_filename, 'w') as backup_file:
            backup_file.write(content)
        print(f"Backup of {filename} created as {backup_filename}.")
    else:
        print("File not found.")

def restore_file():
    filename = input("Enter the filename to restore: ")
    backup_filename = filename + ".backup"
    if os.path.exists(backup_filename):
        with open(backup_filename, 'r') as backup_file:
            content = backup_file.read()
        with open(filename, 'w') as file:
            file.write(content)
        print(f"{filename} has been restored from {backup_filename}.")
    else:
        print("Backup file not found.")

def merge_files():
    files = input("Enter the filenames to merge, separated by commas: ").split(',')
    output_file = input("Enter the output filename: ")
    with open(output_file, 'w') as outfile:
        for filename in files:
            filename = filename.strip()
            if os.path.exists(filename):
                with open(filename, 'r') as infile:
                    outfile.write(infile.read() + "\n")
            else:
                print(f"File {filename} not found.")
    print(f"Files merged into {output_file}.")

def split_file():
    filename = input("Enter the filename to split: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        lines_per_file = int(input("Enter the number of lines per split file: "))
        for i in range(0, len(lines), lines_per_file):
            split_filename = f"{filename}_part_{i//lines_per_file + 1}.txt"
            with open(split_filename, 'w') as split_file:
                split_file.writelines(lines[i:i + lines_per_file])
            print(f"Created split file: {split_filename}")
    else:
        print("File not found.")

def find_and_replace_in_file():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        find_word = input("Enter the word to find: ")
        replace_word = input("Enter the word to replace with: ")
        with open(filename, 'r') as file:
            content = file.read()
        new_content = content.replace(find_word, replace_word)
        with open(filename, 'w') as file:
            file.write(new_content)
        print(f"All occurrences of '{find_word}' replaced with '{replace_word}'.")
    else:
        print("File not found.")

def display_file_statistics():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            lines = content.splitlines()
            words = content.split()
            characters = len(content)
            most_common_word = Counter(words).most_common(1)[0]
        print(f"\nStatistics for {filename}:")
        print(f"Lines: {len(lines)}")
        print(f"Words: {len(words)}")
        print(f"Characters: {characters}")
        print(f"Most common word: '{most_common_word[0]}' (appears {most_common_word[1]} time(s))")
    else:
        print("File not found.")

def delete_file():
    filename = input("Enter the filename: ")
    if os.path.exists(filename):
        os.remove(filename)
        print(f"The file {filename} has been deleted.")
    else:
        print("File not found.")

def list_files():
    files = [f for f in os.listdir() if os.path.isfile(f)]
    if files:
        print("\nList of files:")
        for file in files:
            print(file)
    else:
        print("No files found.")

def main():
    while True:
        menu()
        choice = input("Enter your choice (1-19): ")
        if choice == '1':
            create_file()
        elif choice == '2':
            view_file()
        elif choice == '3':
            append_to_file()
        elif choice == '4':
            search_in_file()
        elif choice == '5':
            count_words_in_file()
        elif choice == '6':
            sort_lines_in_file()
        elif choice == '7':
            edit_line_in_file()
        elif choice == '8':
            word_frequency_analysis()
        elif choice == '9':
            encrypt_file()
        elif choice == '10':
            decrypt_file()
        elif choice == '11':
            backup_file()
        elif choice == '12':
            restore_file()
        elif choice == '13':
            merge_files()
        elif choice == '14':
            split_file()
        elif choice == '15':
            find_and_replace_in_file()
        elif choice == '16':
            display_file_statistics()
        elif choice == '17':
            delete_file()
        elif choice == '18':
            list_files()
        elif choice == '19':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

