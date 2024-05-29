# Loan eligibility check
name = input("Enter your Name: ")
age = int(input("Enter your Age: "))
annual_income = int(input("Enter your Annual income: "))

# Print  age and annual income to verify correct input types
print("Type of Age:", type(age))
print("Type of Annual income:", type(annual_income))

# Check loan eligibility
if age >= 21 and annual_income >= 21000:
    loan_status = "Loan granted"
else:
    loan_status = "Loan not granted"

# Print the loan status
print(loan_status)
