def get_color_name(red, green, blue):
    if red >= 200 and green <= 50 and blue <= 50:
        return "Red"
    elif red <= 50 and green >= 200 and blue <= 50:
        return "Green"
    elif red <= 50 and green <= 50 and blue >= 200:
        return "Blue"
    elif red >= 150 and green >= 150 and blue <= 50:
        return "Yellow"
    elif red <= 50 and green >= 150 and blue >= 150:
        return "Cyan"
    elif red >= 150 and green <= 50 and blue >= 150:
        return "Magenta"
    elif red >= 50 and red <= 150 and green <= 50 and blue <= 50:
        return "Dark Red"
    elif red <= 50 and green >= 50 and green <= 150 and blue <= 50:
        return "Dark Green"
    elif red <= 50 and green <= 50 and blue >= 50 and blue <= 150:
        return "Dark Blue"
    elif red >= 150 and red <= 250 and green >= 150 and green <= 250 and blue <= 50:
        return "Light Yellow"
    elif red <= 50 and green >= 150 and green <= 250 and blue >= 150 and blue <= 250:
        return "Light Cyan"
    elif red >= 150 and red <= 250 and green <= 50 and blue >= 150 and blue <= 250:
        return "Light Magenta"
    else:
        return "Unknown"