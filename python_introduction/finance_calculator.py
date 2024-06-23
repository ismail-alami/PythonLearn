monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
interest_rate = 0.05
#Projected savings after one year
projected_savings = monthly_savings * interest_rate * 12 + monthly_savings * 12
print("Your monthly savings are $", monthly_savings)
print("Projected savings after one year, with interest, is: $", projected_savings)
