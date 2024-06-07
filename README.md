# unit_conversions
A dummy unit conversions package

## Overview
This is an sample python package that performs basic temperature and length conversions.

## Installation:
#### clone the repository
First, clone the repository to your local machine.
```bash
git clone https://github.com/Riyaaa1/conversions-package.git
```
Go to the project directory:
```bash
cd conversions-package
```

#### Usage example

from unit_conversions import temperature,length

le = length.Length(100)

print(temperature.celsius_to_fahrenheit(37))
print(le.cm_to_m())

