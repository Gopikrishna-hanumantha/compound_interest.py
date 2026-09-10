p=float(input("Enter principal amount"))
r=float(input("Enter interest rate (%)"))
n=int(input("Enter number of times compounded per year"))
t=float(input("Enter time in years"))
r=r/100
amount=p * (1 + r/n) ** (n*t)
interest = amount - p
print("amount is",amount)
print("The compound interest is",interest)

