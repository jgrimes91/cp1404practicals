COLOURS = {"AliceBlue": "#f0f8ff", "BlueViolet": "#8a2be2", "burlywood3": "#cdaa7d", "CadetBlue": "#5f9ea0",
           "chocolate": "#d2691e", "coral4": "#8b3e2f", "cornsilk": "fff8dc", "cyan1": "#00ffff",
           "DarkGoldenrod": "#b8860b", "grey": "#bebebe"}

colour_picker = input("Please enter a colour: ")
while colour_picker == "":
    print("Invalid colour: ")
    colour_picker = input("Please enter a colour: ")
if colour_picker in COLOURS:
    print(COLOURS[colour_picker])