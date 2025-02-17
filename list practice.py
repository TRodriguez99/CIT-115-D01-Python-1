#Spacing
MAX_STRINGS="35s"
#Number values, how many decimal places and float
NUMBER_FORMAT="15,.2f"
#1st person's name and money
sName1=input("Person A:")
fMoney1=float(input("money spent:"))
#2nd person's name and money
sName2=input("Person B:")
fMoney2=float(input("money spent:"))
#3rd person's name and money
sName3=input("Person C:")
fMoney3=float(input("money spent:"))
#4th person's name and money
sName4=input("Person D:")
fMoney4=float(input("money spent:"))
#Total(Be sure to use float not string)
fTotal=fMoney1 + fMoney2 + fMoney3 + fMoney4
#Always use double-quotes when using fStrings followed by curly brackets
print(f"{sName1:{MAX_STRINGS}}  {fMoney1:{NUMBER_FORMAT}}")
print(f"{sName2:{MAX_STRINGS}}  {fMoney2:{NUMBER_FORMAT}}")
print(f"{sName3:{MAX_STRINGS}}  {fMoney3:{NUMBER_FORMAT}}")
print(f"{sName4:{MAX_STRINGS}}  {fMoney4:{NUMBER_FORMAT}}")
print(f"{'Total:':{MAX_STRINGS}} {fTotal:16,.2f}")

