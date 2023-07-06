# Möglichkeit 1

numbers = [3, 7, 12, 20]
result = numbers[0] + numbers[1] + numbers[2] + numbers[3]
print(result)


# Möglichkeit 2 (kommt erst später)
numbers = [3, 7, 12, 20]
result = 0
for number in numbers:
    result += number

print(result)
