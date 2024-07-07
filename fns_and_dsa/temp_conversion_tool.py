# Define global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

# Conversion functions
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

def main():
    try:
        # Prompt user for temperature input
        temp = float(input("Enter the temperature to convert: "))
        
        # Prompt user for the temperature unit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Perform the conversion based on the unit
        if unit == 'C':
            converted_temp = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {converted_temp}°F")
        elif unit == 'F':
            converted_temp = convert_to_celsius(temp)
            print(f"{temp}°F is {converted_temp}°C")
        else:
            raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    except ValueError as ve:
        print(f"Invalid input: {ve}. Please enter a numeric value.")

if __name__ == "__main__":
    main()

