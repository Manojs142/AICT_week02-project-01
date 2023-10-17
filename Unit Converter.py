def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def meters_to_feet(meters):
    feet = meters * 3.28084
    return feet

def feet_to_meters(feet):
    meters = feet / 3.28084
    return meters

def kilograms_to_pounds(kilograms):
    pounds = kilograms * 2.20462
    return pounds

def pounds_to_kilograms(pounds):
    kilograms = pounds / 2.20462
    return kilograms

while True:
    print("Choose an option:")
    print("1. Temperature Converter (Celsius to Fahrenheit / Fahrenheit to Celsius)")
    print("2. Length Converter (Meters to Feet / Feet to Meters)")
    print("3. Weight Converter (Kilograms to Pounds / Pounds to Kilograms)")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        temp_choice = input("Enter 'C' for Celsius to Fahrenheit conversion, 'F' for Fahrenheit to Celsius conversion: ")
        if temp_choice.upper() == 'C':
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"{celsius}°C is equal to {fahrenheit}°F")
        elif temp_choice.upper() == 'F':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"{fahrenheit}°F is equal to {celsius}°C")
        else:
            print("Invalid input. Please enter 'C' or 'F'.")

    elif choice == '2':
        length_choice = input("Enter 'M' for Meters to Feet conversion, 'F' for Feet to Meters conversion: ")
        if length_choice.upper() == 'M':
            meters = float(input("Enter length in meters: "))
            feet = meters_to_feet(meters)
            print(f"{meters} meters is equal to {feet} feet")
        elif length_choice.upper() == 'F':
            feet = float(input("Enter length in feet: "))
            meters = feet_to_meters(feet)
            print(f"{feet} feet is equal to {meters} meters")
        else:
            print("Invalid input. Please enter 'M' or 'F'.")

    elif choice == '3':
        weight_choice = input("Enter 'K' for Kilograms to Pounds conversion, 'P' for Pounds to Kilograms conversion: ")
        if weight_choice.upper() == 'K':
            kilograms = float(input("Enter weight in kilograms: "))
            pounds = kilograms_to_pounds(kilograms)
            print(f"{kilograms} kilograms is equal to {pounds} pounds")
        elif weight_choice.upper() == 'P':
            pounds = float(input("Enter weight in pounds: "))
            kilograms = pounds_to_kilograms(pounds)
            print(f"{pounds} pounds is equal to {kilograms} kilograms")
        else:
            print("Invalid input. Please enter 'K' or 'P'.")

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid input. Please choose a valid option (1/2/3/4)")
