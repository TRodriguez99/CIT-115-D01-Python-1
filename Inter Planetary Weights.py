#Toni Rodriguez
#Professor Candido
#CIT-115-D01
#2/16/2025

                            #Chapter 2 Assignment: Interplanetary Weights

#Planet Surface Gravity Factors
nMercury = 0.38
nVenus = 0.91
nMoon = 0.165
nMars = 0.38
nJupiter = 2.34
nSaturn = 0.93
nUranus = 0.92
nNeptune = 1.12
nPluto = 0.066

#Line-formatted constants
MAX_STRINGS = "20s"
NUMBER_FORMAT = "10,.2f"

#Type in your name
sName = input("What is your name:")

#nEarth_WEIGHT is a "Named Constant," entered as "float" data type
nEARTH_WEIGHT = float(input("What is your weight:"))

#Conversion Formula: Weight = Earth Weight x Surface Gravity Factor
nMer = nEARTH_WEIGHT * nMercury
nVen = nEARTH_WEIGHT * nVenus
nMoo = nEARTH_WEIGHT * nMoon
nMar = nEARTH_WEIGHT * nMars
nJup = nEARTH_WEIGHT * nJupiter
nSat = nEARTH_WEIGHT * nSaturn
nUra = nEARTH_WEIGHT * nUranus
nNep = nEARTH_WEIGHT * nNeptune
nPlu = nEARTH_WEIGHT * nPluto

#Finished and ready to run
print(sName,"Here are your weights on our solar system's planets:")
print(f"{'Weight on Mercury:':{MAX_STRINGS}} {nMer:{NUMBER_FORMAT}}")
print(f"{'Weight on Venus:':{MAX_STRINGS}} {nVen:{NUMBER_FORMAT}}")
print(f"{'Weight on our moon:':{MAX_STRINGS}} {nMoo:{NUMBER_FORMAT}}")
print(f"{'Weight on Mars:':{MAX_STRINGS}} {nMar:{NUMBER_FORMAT}}")
print(f"{'Weight on Jupiter:':{MAX_STRINGS}} {nJup:{NUMBER_FORMAT}}")
print(f"{'Weight on Saturn:':{MAX_STRINGS}} {nSat:{NUMBER_FORMAT}}")
print(f"{'Weight on Uranus:':{MAX_STRINGS}} {nUra:{NUMBER_FORMAT}}")
print(f"{'Weight on Neptune:':{MAX_STRINGS}} {nNep:{NUMBER_FORMAT}}")
print(f"{'Weight on Pluto:':{MAX_STRINGS}} {nPlu:{NUMBER_FORMAT}}")