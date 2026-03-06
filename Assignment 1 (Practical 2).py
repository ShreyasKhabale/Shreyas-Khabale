numbers = []
n = int(input("Enter number of elements: "))

for i in range(n):
    numbers.append(int(input(f"Enter element {i+1}: ")))

search = int(input("Enter number to search: "))

found = False
for i in range(n):
    if numbers[i] == search:
        print("Number found at position:", i + 1)
        found = True
        break

if not found:
    print("Number not found in the list")
