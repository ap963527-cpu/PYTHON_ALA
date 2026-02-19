print("Countdown Program")
num = int(input("Enter starting number: "))
sum_total = 0

while num >= 0:
    print("Number:", num)
    sum_total = sum_total + num

    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

    num = num - 1

print("Total sum:", sum_total)

if sum_total > 100:
    print("Big total")
else:
    print("Small total")

