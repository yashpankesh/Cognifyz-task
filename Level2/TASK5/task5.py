'''Task: File Manipulation

Write a Python program that reads a text file and counts the occurrences of each word in the file. Display the 
results in alphabetical order along with their respective counts.'''

def count_word_occurrences(file_path):
    try:
        # Open the file and read its contents
        with open(file_path, 'r') as file:
            text = file.read()

        # Normalize the text: remove punctuation and convert to lowercase
        words = text.lower().split()
        words = [word.strip(",.?!\"'()[]") for word in words]

        # Count occurrences of each word
        word_count = {}
        for word in words:
            word_count[word] = word_count.get(word, 0) + 1

        # Sort the words alphabetically
        sorted_word_count = dict(sorted(word_count.items()))

        # Display the results
        print("Word occurrences (alphabetical order):")
        for word, count in sorted_word_count.items():
            print(f"{word}: {count}")

    except FileNotFoundError:
        print("Error: The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Prompt the user for the file path
file_path = input("Enter the path of the text file: ")
count_word_occurrences(file_path)
