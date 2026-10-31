def celcius_to_fahrenheit(celcius, round_to=1):
    fahrenheit = (celcius * 9 / 5) + 32
    return round(fahrenheit, round_to)

def fahrenheit_to_celcius(fahrenheit, round_to=1):
    celcius = (fahrenheit - 32) * 5 / 9
    return round(celcius, round_to)
print(fahrenheit_to_celcius(32), "Celcius")

print("\n  °C  |   °F")
print("------+-------")
for c in range(0, 101, 20):
    print(f"{c:5} | {celcius_to_fahrenheit(c):6}")

print("98.6 °F =", fahrenheit_to_celcius(98.6), "°C")
print("Round trip 37 °C:", fahrenheit_to_celcius(celcius_to_fahrenheit(37)))
print(fahrenheit_to_celcius(200, round_to= 4 ), "°C")