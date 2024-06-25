def prime_checker(number):
    times = 0
    for n in range(1, number):
        if number % n == 0:
            times += 1
    if times > 2:
        print(f"It's not a prime number.")
    else:
        print(f"It's a prime number.")


n = int(input())
prime_checker(number=n)