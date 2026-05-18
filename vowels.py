text = "Hello World"

count = 0

for char in text:
    if char in "aeiouAEIOU":
        count += 1

print("Number of vowels:", count)

