age = int(input("What is your age? ----->  "))
revenue = float(input("What is your monthly revenue? ---->  "))
credit = int(input("What is your monthly credit score? ----->  "))
years = float(input("how many years are you in the business? ----->  "))
defaults = bool(input("Do you have any defaults? ---->  "))
cl = str(input("What is your collaterals name? ---->  "))
cv = float(input("What is your collaterals value? ---->  "))

loan_limit = 0
base_rate = 0

if age >= 21 and years >= 2.0 and defaults == False:
    print("Requirement Pass!")
    if credit >= 720: # tier 1
        loan_limit = 3 * revenue
        print("Your loan limit is", loan_limit)
        if revenue >= 50000:
                base_rate = 0.015 * revenue
                print("Your Base Rate is", base_rate)
        else:
                base_rate = 0.025 * revenue
                print("Your Base Rate is", base_rate)

        if cv >= loan_limit:
                print("Collateral", cv, "with value of", credit, "is ACCEPTED!")
        else:
                print("Rejected: Insufficient collateral value")

        if loan_limit % 5000 != 0:
            base_rate += 250
            print("Updated Fee is", base_rate)
    elif 620 <= credit < 720: # Tier 2
        loan_limit = 1.5 * revenue
        print("Your Loan Limit is", loan_limit)
        if years >= 5.0:
            base_rate = revenue * 0.02
            print("Your Base Rate is", base_rate)
        else:
            base_rate = revenue * 0.035
            print("Your Base Rate is", base_rate)
    elif credit < 620:
        print("Rejected: Credit score below requirement")
    else:
        print("Rejected!")
else:
    print("Rejected: High Risk Application or Ineligible Owner")


