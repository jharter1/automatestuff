def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result

n = input("Give me a number:")
while n != 1:
    try:
        n = collatz(int(n))
    except ValueError:
        print ("Try using an integer instead, kiddo")
