

def simple_interest(principal, rate, time):
    """Calculates simple interest on a principal over time at a given rate.""" 
    interest = principal*(rate/100)*time 
    return f"Simple interest: ${interest:.2f}"
principal = 70
rate = 25
time = 6
simple_interest = principal*(rate/100)*time 

str = f"Simple interest: ${simple_interest}"

print(simple_interest)

