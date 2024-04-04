
light_levels = {
    0: "Off (0%)",
    1: "Low (25%)",
    2: "Medium (50%)",
    3: "High (75%)",
    4: "Maximum (100%)"
}

light_level = 0

while True:
    # Print the current light level
    print(f"The light is currently {light_levels[light_level]}")

    light_level = int(input("Enter a light level (0-4), or 0 to exit: "))

    if light_level == 0:
        break

print("The light is off.")