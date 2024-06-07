# unit_conversions
A dummy unit conversions package

## Overview
This is an sample python package that performs basic temperature and length conversions.

## Installation:
#### clone the repository
First, clone the repository to your local machine.
git clone https://github.com/Riyaaa1/conversions-package.git

#### pip install the package using local distribution file
pip install /path/to/dist/unit_conversions-1.0.0.tar.gz

#### Usage example

from unit_conversions import temperature,length

le = length.Length(100)

print(temperature.celsius_to_fahrenheit(37))
print(le.cm_to_m())

