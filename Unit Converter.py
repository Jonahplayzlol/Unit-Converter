def miles_to_km(miles):
    return miles * 1.60934

def km_to_miles(km):
    return km / 1.60934

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def menu():
    print("\n--- Jonah's Unit Converter ---")
    print("1. Miles → Kilometers")
    print("2. Kilometers → Miles")
    print("3. Celsius → Fahrenheit")
    print("4. Fahrenheit → Celsius")
    print("5. Exit")

def main():
    while True:
        menu()
        choice = input("Choose an option (1-5): ")

        if choice == "1":
            miles = float(input("Enter miles: "))
            print(f"{miles} miles = {miles_to_km(miles):.2f} km")

        elif choice == "2":
            km = float(input("Enter kilometers: "))
            print(f"{km} km = {km_to_miles(km):.2f} miles")

        elif choice == "3":
            celsius = float(input("Enter Celsius: "))
            print(f"{celsius}°C = {celsius_to_fahrenheit(celsius):.2f}°F")

        elif choice == "4":
            fahrenheit = float(input("Enter Fahrenheit: "))
            print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit):.2f}°C")

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()