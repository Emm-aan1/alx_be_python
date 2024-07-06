FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.
    """
    global FAHRENHEIT_TO_CELSIUS_FACTOR

    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.
    """
    global CELSIUS_TO_FAHRENHEIT_FACTOR

    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

def user_input():
    """
    Prompt user to enter a temperature and its unit.
    """
    temp = float(input("Enter the temperature to convert: "))
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().lower()

    if unit == 'c':
        convert = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {convert}°F")
    elif unit == 'f':
        convert = convert_to_celsius(temp)
        print(f"{temp}°F is {convert}°C")
    else:
        print("Invalid unit. Please enter 'C' or 'F'")

user_input()