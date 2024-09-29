#temperatur conversion tool
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
eELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celcius
def convert_to_fahrenheit(celsius):
    fahrenheit = (celcius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def main():
    temperature = float(input("Enter the temperature to convert: "))
    unit == input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
    if unit == "F":
        celcius = convert_to_celsius(temperature)
        print(f"{temperature}°F is {celsius}°C"}
