#EMI Calculator

loan = float(input("Loan Amount: "))
rate = float(input("Interest Rate (%): "))
years = int(input("Years: "))

m_rate = rate / 1200
n = years * 12

emi = loan * m_rate * (1 + m_rate) ** n / ((1 + m_rate) ** n - 1)

print("EMI =", round(emi, 2))




