# Initialize variables
n = 1234
sum = 0

# Loop to calculate sum of digits
while n != 0:
    sum = sum + n % 10
    n = n // 10   # Integer division

# Print result
print("Sum of digits =", sum)