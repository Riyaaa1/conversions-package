def celsius_to_fahrenheit(celsius):
    return round((9/5*celsius)+ 32,2)

def celsius_to_kelvin(celsius):
    return round(celsius+273.15,2)

def fahrenheit_to_celsius(fahrenheit):
    return round(((fahrenheit - 32) * 5/9), 2)

def kelvin_to_celsius(kelvin):
    return round(kelvin - 273.15, 2)

if __name__ =="__main__":
    import sys
    print(kelvin_to_celsius(float(sys.argv[1])))