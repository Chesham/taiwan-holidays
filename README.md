# taiwan-holidays

`taiwan-holidays` is a Python package designed to check whether a specific date is a workday or a holiday in Taiwan, based on the official work calendar provided by the Taiwan government.

![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![license](https://img.shields.io/badge/license-MIT-green)
![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)
![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)
![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)
![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)
![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)

## Features

- Determine if a date is a workday or holiday.
- Support for official Taiwan government work calendar rules, including special adjusted workdays and holidays.
- Easy-to-use API for date checking.
- Currently, only the official Taiwanese government calendar of public working days starting from the year 2019 (Republic of China year 108) **onwards** is supported.

## Installation

You can install `taiwan-holidays` via pip:

```bash
pip install taiwan-holidays
```

## Usage

Here's how you can use taiwan-holidays in your Python project.

### Example

```python
from taiwan_holidays.taiwan_calendar import TaiwanCalendar


calendar = TaiwanCalendar()
date = dateutil.parser.parse('2024-12-08')
print(calendar.is_holiday(date))
print(calendar.is_holiday('2024-12-08'))
print(calendar.is_holiday('20241208'))
print(calendar.is_holiday('2024/12/08'))

# Iterate workdays through a range of dates, including the start and end dates
calendar.iter_workdays('2024-12-01', '2024-12-31')

# Also you can iterate with reversed dates
calendar.iter_workdays('2024-12-31', '2024-12-01')
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

Special thanks to the Taiwan government for providing the official administrative calendar as the basis for this package.

Feel free to report any issues or suggest new features in the Issues section.
