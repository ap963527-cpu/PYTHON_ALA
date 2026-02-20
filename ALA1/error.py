print("Countdown Program")
num = int(input("Enter starting number: "))
sum_total = 0

while num >= 0:
print("Number:", num)   # Error: No indentation inside while
sum_total = sum_total + num   # Error: No indentation

if num % 2 == 0:   # Error: This if should be inside while
print("Even")   # Error: No indentation
else:
print("Odd")   # Error: No indentation

num = num - 1   # Error: Should be inside while loop
print("Total sum:", sum_total)

if sum_total > 100   # Error: Missing colon :
print("Big total")   # Error: No indentation
else:
print("Small total")   # Error: No indentation
