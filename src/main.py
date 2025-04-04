def convert_units():
    print("Welcome to the Unit Converter!")
    print("Choose the conversion type:")
    print("1. Temperature (Celsius <-> Fahrenheit)")
    print("2. Distance (Kilometers <-> Miles)")
    print("3. Weight (Kilograms <-> Pounds)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        temp = float(input("Enter the temperature: "))
        unit = input("Convert from (C/F): ").strip().upper()
        if unit == "C":
            result = (temp * 9/5) + 32
            print(f"{temp}°C is {result:.2f}°F")
        elif unit == "F":
            result = (temp - 32) * 5/9
            print(f"{temp}°F is {result:.2f}°C")
        else:
            print("Invalid unit entered.")

    elif choice == "2":
        dist = float(input("Enter the distance: "))
        unit = input("Convert from (KM/MI): ").strip().upper()
        if unit == "KM":
            result = dist * 0.621371
            print(f"{dist} km is {result:.2f} miles")
        elif unit == "MI":
            result = dist / 0.621371
            print(f"{dist} miles is {result:.2f} km")
        else:
            print("Invalid unit entered.")

    elif choice == "3":
        weight = float(input("Enter the weight: "))
        unit = input("Convert from (KG/LB): ").strip().upper()
        if unit == "KG":
            result = weight * 2.20462
            print(f"{weight} kg is {result:.2f} lb")
        elif unit == "LB":
            result = weight / 2.20462
            print(f"{weight} lb is {result:.2f} kg")
        else:
            print("Invalid unit entered.")

    else:
        print("Invalid choice.")

if __name__ == "__main__":
    convert_units()
