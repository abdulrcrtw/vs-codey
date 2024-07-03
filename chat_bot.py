
def ask_name():
    name = input("What is your name ? ").capitalize()
    return name 

def calculate_expenses(expenses):
    sum_total = sum(expenses) 
    return sum_total

def calculate_savings(income, expenses):
    """Subtracts expenses from income to calculate savings."""
    savings = income - expenses 
    return f"Total savings: ${savings: .2f}"

def simple_interest(principal, rate, time):
    """Calculate simple interest on a principal over time at a given rate."""
    interest = principal * (rate / 100) * time 
    return f"Simple interest: ${interest: .2f}"

def compound_interest(principal, rate, times_compounded, years):
    """Calculate compound interest."""
    amount = principal * (1 + (rate / 100) / times_compounded) ** (times_compounded * years)
    interest = amount - principal 
    return f"Compound interest: ${interest: .2f}"
    
command = input("Which command would you like to run? Options: expenses, ask_name, simple_interest, compound_interest ")

if command == "expenses":
    print(calculate_expenses(exp))
elif command == "ask_name":
    ask_name()
elif command == "compound_interest":
    pricipal = input("What is the principal? ")
    rate = input("What is the rate? ")
    compound_interest()
    
else:
    print("invalid comment ")
