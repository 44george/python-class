#comparing heights of 3 students
def find_tallest(john_height, alice_height, bob_height):
    if john_height > alice_height and john_height > bob_height:
        tallest = "John"
        tallest_height = john_height
    elif alice_height > john_height and alice_height > bob_height:
        tallest = "Alice"
        tallest_height = alice_height
    else:
        tallest = "Bob"
        tallest_height = bob_height
    
    return tallest, tallest_height

# Input heights
john_height = float(input("Enter John's height in cm: "))
alice_height = float(input("Enter Alice's height in cm: "))
bob_height = float(input("Enter Bob's height in cm: "))

# Find and print the tallest student
tallest_student, height = find_tallest(john_height, alice_height, bob_height)
print(f"The tallest student is {tallest_student} with a height of {height} cm.")