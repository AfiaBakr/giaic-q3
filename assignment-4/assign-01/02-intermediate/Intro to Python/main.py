# Constants for planetary gravity
MARS_MULTIPLE = 0.378
MERCURY_GRAVITY = 0.376
VENUS_GRAVITY = 0.889
MARS_GRAVITY = 0.378
JUPITER_GRAVITY = 2.36
SATURN_GRAVITY = 1.081
URANUS_GRAVITY = 0.815
NEPTUNE_GRAVITY = 1.14

def mars_weight_calculator():
    """Calculates and prints the weight on Mars."""
    try:
        earth_weight_str = input("Enter a weight on Earth: ")
        earth_weight = float(earth_weight_str)
        mars_weight = earth_weight * MARS_MULTIPLE
        rounded_mars_weight = round(mars_weight, 2)
        print("The equivalent weight on Mars: " + str(rounded_mars_weight))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

def planetary_weight_calculator():
    """Calculates and prints the weight on the selected planet."""
    try:
        earth_weight = float(input("Enter a weight on Earth: "))
        planet = input("Enter a planet (e.g., Mars, Jupiter): ").capitalize()

        if planet == "Mercury":
            gravity_constant = MERCURY_GRAVITY
        elif planet == "Venus":
            gravity_constant = VENUS_GRAVITY
        elif planet == "Mars":
            gravity_constant = MARS_GRAVITY
        elif planet == "Jupiter":
            gravity_constant = JUPITER_GRAVITY
        elif planet == "Saturn":
            gravity_constant = SATURN_GRAVITY
        elif planet == "Uranus":
            gravity_constant = URANUS_GRAVITY
        elif planet == "Neptune":
            gravity_constant = NEPTUNE_GRAVITY
        else:
            print("Invalid planet name.")
            return

        planetary_weight = earth_weight * gravity_constant
        rounded_weight = round(planetary_weight, 2)
        print("The equivalent weight on " + planet + ": " + str(rounded_weight))

    except ValueError:
        print("Invalid input! Please enter a numeric value.")

def main():
    print("Weight Conversion Program")
    print("1. Convert Earth weight to Mars weight")
    print("2. Convert Earth weight to another planet")
    choice = input("Enter your choice (1 or 2): ")

    if choice == "1":
        mars_weight_calculator()
    elif choice == "2":
        planetary_weight_calculator()
    else:
        print("Invalid choice. Please select 1 or 2.")

if __name__ == "__main__":
    main()
