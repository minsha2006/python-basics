file_name = input("Enter the file name: ")

try:
    with open(file_name, "r") as file:
        content = file.read()
        words = content.split()
        word_count = len(words)

    print("Total number of words in the file:", word_count)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

