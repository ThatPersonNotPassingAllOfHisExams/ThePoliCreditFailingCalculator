# Define the credit values for each module
credit_values = {
    "AnalizaMatematica": 100,
    "DEO": 75,
    "SS": 50,
    "MET": 60,
    "AGLAD": 80
}

# Initialize the total payment and a list of failed modules
total_payment = 0
failed_modules = []

# Iterate through each module and calculate the payment
for module, credit in credit_values.items():
    # Prompt the user to input whether the module was passed or failed
    result = input(f"Did you pass {module}? (y/n) ")
    if result.lower() == "y":
        total_payment += credit
    else:
        # If the module was failed, add its credit value to the list of failed modules
        failed_modules.append(module)
        required_credits = input(f"How many credits are required to pass {module}? ")
        total_payment += int(required_credits)

# Print the list of passed modules and their credits
print("Passed modules:")
for module, credit in credit_values.items():
    if module not in failed_modules:
        print(f"{module}: {credit}")

# Print the list of failed modules and their required credits
print("Failed modules:")
for module in failed_modules:
    required_credits = int(input(f"How many credits are required to pass {module}? "))
    print(f"{module}: {required_credits}")

# Print the final payment
print(f"Total payment: ${total_payment}")
