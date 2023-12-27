origin_unit = input("Origin unit (km, miles, feet): ")
to_unit = input("To what unit (km, miles, feet): ")
amount = float(input("How much: "))

if origin_unit == "km" and to_unit == "miles":
    print(f"Output: {amount * 0.621371:.2f} miles")
elif origin_unit == "miles" and to_unit == "km":
    print(f"Output: {amount / 0.621371:.2f} km")
elif origin_unit == "km" and to_unit == "feet":
    print(f"Output: {amount * 3280.84:.2f} feet")
elif origin_unit == "feet" and to_unit == "km":
    print(f"Output: {amount / 3280.84:.2f} km")
elif origin_unit == "miles" and to_unit == "feet":
    print(f"Output: {amount * 5280:.2f} feet")
elif origin_unit == "feet" and to_unit == "miles":
    print(f"Output: {amount / 5280:.2f} miles")


