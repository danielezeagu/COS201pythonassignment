# Program to compute personal income tax (2009 rates)

print("Filing Status Options:")
print("0 - Single filer")
print("1 - Married filing jointly or qualifying widow(er)")
print("2 - Married filing separately")
print("3 - Head of household")

#Ask the user for filing status
status = int(input("Enter your filing status (0, 1, 2, or 3): "))

#Ask for taxable income
income = float(input("Enter your taxable income: "))

# Variable to store the calculated tax
tax = 0

#Compute tax based on filing status
#SINGLE FILER
if status == 0:
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 82250:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
    elif income <= 171550:
        tax = (8350 * 0.10 +
               (33950 - 8350) * 0.15 +
               (82250 - 33950) * 0.25 +
               (income - 82250) * 0.28)
    elif income <= 372950:
        tax = (8350 * 0.10 +
               (33950 - 8350) * 0.15 +
               (82250 - 33950) * 0.25 +
               (171550 - 82250) * 0.28 +
               (income - 171550) * 0.33)
    else:
        tax = (8350 * 0.10 +
               (33950 - 8350) * 0.15 +
               (82250 - 33950) * 0.25 +
               (171550 - 82250) * 0.28 +
               (372950 - 171550) * 0.33 +
               (income - 372950) * 0.35)

#MARRIED FILING JOINTLY
elif status == 1:
    if income <= 16700:
        tax = income * 0.10
    elif income <= 67900:
        tax = 16700 * 0.10 + (income - 16700) * 0.15
    elif income <= 137050:
        tax = 16700 * 0.10 + (67900 - 16700) * 0.15 + (income - 67900) * 0.25
    elif income <= 208850:
        tax = (16700 * 0.10 +
               (67900 - 16700) * 0.15 +
               (137050 - 67900) * 0.25 +
               (income - 137050) * 0.28)
    elif income <= 372950:
        tax = (16700 * 0.10 +
               (67900 - 16700) * 0.15 +
               (137050 - 67900) * 0.25 +
               (208850 - 137050) * 0.28 +
               (income - 208850) * 0.33)
    else:
        tax = (16700 * 0.10 +
               (67900 - 16700) * 0.15 +
               (137050 - 67900) * 0.25 +
               (208850 - 137050) * 0.28 +
               (372950 - 208850) * 0.33 +
               (income - 372950) * 0.35)

#MARRIED FILING SEPARATELY
elif status == 2:
    if income <= 8350:
        tax = income * 0.10
    elif income <= 33950:
        tax = 8350 * 0.10 + (income - 8350) * 0.15
    elif income <= 68525:
        tax = 8350 * 0.10 + (33950 - 8350) * 0.15 + (income - 33950) * 0.25
    elif income <= 104425:
        tax = (8350 * 0.10 +
               (33950 - 8350) * 0.15 +
               (68525 - 33950) * 0.25 +
               (income - 68525) * 0.28)
    elif income <= 186475:
        tax = (8350 * 0.10 +
               (33950 - 8350) * 0.15 +
               (68525 - 33950) * 0.25 +
               (104425 - 68525) * 0.28 +
               (income - 104425) * 0.33)
    else:
        tax = (8350 * 0.10 +
               (33950 - 8350) * 0.15 +
               (68525 - 33950) * 0.25 +
               (104425 - 68525) * 0.28 +
               (186475 - 104425) * 0.33 +
               (income - 186475) * 0.35)

#HEAD OF HOUSEHOLD
elif status == 3:
    if income <= 11950:
        tax = income * 0.10
    elif income <= 45500:
        tax = 11950 * 0.10 + (income - 11950) * 0.15
    elif income <= 117450:
        tax = 11950 * 0.10 + (45500 - 11950) * 0.15 + (income - 45500) * 0.25
    elif income <= 190200:
        tax = (11950 * 0.10 +
               (45500 - 11950) * 0.15 +
               (117450 - 45500) * 0.25 +
               (income - 117450) * 0.28)
    elif income <= 372950:
        tax = (11950 * 0.10 +
               (45500 - 11950) * 0.15 +
               (117450 - 45500) * 0.25 +
               (190200 - 117450) * 0.28 +
               (income - 190200) * 0.33)
    else:
        tax = (11950 * 0.10 +
               (45500 - 11950) * 0.15 +
               (117450 - 45500) * 0.25 +
               (190200 - 117450) * 0.28 +
               (372950 - 190200) * 0.33 +
               (income - 372950) * 0.35)

#INVALID STATUS
else:
    print("Invalid filing status.")
    exit()

#Display the result
print(f"Your calculated tax is: ${tax:.2f}")
