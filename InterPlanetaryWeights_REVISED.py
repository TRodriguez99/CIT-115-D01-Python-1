#Toni Rodriguez
#Professor Candido
#CIT-115-D01
#2/16/2025

                            #Chapter 2 Assignment: Interplanetary Weights

#Planet Surface Gravity Factors (named constants)
MERCURY_FACTOR = 0.38
VENUS_FACTOR = 0.91
MOON_FACTOR = 0.165
MARS_FACTOR = 0.38
JUPITER_FACTOR = 2.34
SATURN_FACTOR = 0.93
URANUS_FACTOR = 0.92
NEPTUNE_FACTOR = 1.12
PLUTO_FACTOR = 0.066

#Line-formatted constants
MAX_STRINGS = "20s"
NUMBER_FORMAT = "10,.2f"

#Type in your name
sName = input("What is your name:")

#nEarth_WEIGHT is a "Named Constant," entered as "float" data type
nEarthWeight = float(input("What is your weight:"))

#Conversion Formula: Weight = Earth Weight x Surface Gravity Factor
fMercury = nEarthWeight * MERCURY_FACTOR
fVenus = nEarthWeight * VENUS_FACTOR
fMoon = nEarthWeight * MOON_FACTOR
fMars = nEarthWeight * MARS_FACTOR
fJupiter = nEarthWeight * JUPITER_FACTOR
fSaturn = nEarthWeight * SATURN_FACTOR
fUranus = nEarthWeight * URANUS_FACTOR
fNeptune = nEarthWeight * NEPTUNE_FACTOR
fPluto = nEarthWeight * PLUTO_FACTOR

#Finished and ready to run
print(sName,"Here are your weights on our solar system's planets:")
print(f"{'Weight on Mercury:':{MAX_STRINGS}} {fMercury:{NUMBER_FORMAT}}")
print(f"{'Weight on Venus:':{MAX_STRINGS}} {fVenus:{NUMBER_FORMAT}}")
print(f"{'Weight on our moon:':{MAX_STRINGS}} {fMoon:{NUMBER_FORMAT}}")
print(f"{'Weight on Mars:':{MAX_STRINGS}} {fMars:{NUMBER_FORMAT}}")
print(f"{'Weight on Jupiter:':{MAX_STRINGS}} {fJupiter:{NUMBER_FORMAT}}")
print(f"{'Weight on Saturn:':{MAX_STRINGS}} {fSaturn:{NUMBER_FORMAT}}")
print(f"{'Weight on Uranus:':{MAX_STRINGS}} {fUranus:{NUMBER_FORMAT}}")
print(f"{'Weight on Neptune:':{MAX_STRINGS}} {fNeptune:{NUMBER_FORMAT}}")
print(f"{'Weight on Pluto:':{MAX_STRINGS}} {fPluto:{NUMBER_FORMAT}}")