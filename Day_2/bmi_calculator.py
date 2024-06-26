height = input()
weight = input()

height_fixed = float(height)
weight_fixed = int(weight)

bmi = weight_fixed / height_fixed ** 2
print(int(bmi))