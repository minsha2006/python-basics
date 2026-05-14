file_name = input("Enter the file name: ")

try:
    with open(file_name, "r") as file:
        content = file.read()
        print("\nFile Contents:\n")
        print(content)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)