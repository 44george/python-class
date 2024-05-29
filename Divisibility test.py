#TEST FOR DIVISIBILITY TEST OF 5 AND 11
def is_divisible_by_7(n):
    return n % 7 == 0

def is_divisible_by_11(n):
    return n % 11 == 0

#TESTING
def test_divisibility(n):
    divisible_by_7 = is_divisible_by_7(n)
    divisible_by_11 = is_divisible_by_11(n)

    print(f"Testing divisibility for {n}:")
    if divisible_by_7:
        print(f"{n} is divisible by 7.")
    else:
        print(f"{n} is not divisible by 7.")
    
    if divisible_by_11:
        print(f"{n} is divisible by 11.")
    else:
        print(f"{n} is not divisible by 11.")

# Example usage
number = int(input("Enter a number to test: "))
test_divisibility(number)