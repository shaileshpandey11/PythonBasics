def convert(c):
    if c < -273.15:
        return "Temp doesn't make sense"
    else:
        f = c * 9 // 5 + 32
        return float(f)


print(convert(-280))