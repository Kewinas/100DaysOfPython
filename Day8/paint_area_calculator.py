def paint_calc(height, width, cover):
  cans = round((height * width) / coverage)
  if ((height * width) % coverage) == 0:
    print(f"You'll need {cans} cans of paint.")
  else:
    print(f"You'll need {cans + 1} cans of paint.")


test_h = int(input())
test_w = int(input())
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
