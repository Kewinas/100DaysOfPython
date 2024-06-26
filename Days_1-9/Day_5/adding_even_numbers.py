target = int(input())

result = 0
for number in range(1, target+1):
  if number % 2 == 0:
    result += number

print(result)
