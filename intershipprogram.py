def calculate_emi(principal, interest_rate, tenure):
    interest_rate = interest_rate / 100 / 12  # Convert annual interest rate to monthly
    tenure = tenure * 12  # Convert tenure from years to months

    emi = (principal * interest_rate * (1 + interest_rate) ** tenure) / ((1 + interest_rate) ** tenure - 1)
    return emi

def print_emis():
    principal = float(input("Enter the principal amount: "))
    interest_rate = float(input("Enter the annual interest rate (in percentage): "))
    tenure = int(input("Enter the loan tenure (in years): "))

    emi = calculate_emi(principal, interest_rate, tenure)

    print("\nEMI Details")
    print("Principal Amount: $", principal)
    print("Interest Rate: ", interest_rate, "%")
    print("Tenure: ", tenure, "years")
    print("EMI: $", round(emi, 2))

print_emis()
