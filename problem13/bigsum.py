# Open the file in read mode
with open('numbers.txt', 'r') as file:
    # Read the contents of the file
    content = file.read()

    # Convert the contents to a list of numbers
    # Use split() to handle spaces or newlines
    numbers = [int(num) for num in content.replace(',', ' ').split()]
full_sum=sum(numbers)
print(int(str(full_sum)[:10]))
