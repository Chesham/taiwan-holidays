# taiwan-holidays

`taiwan-holidays` is a Python package designed to check whether a specific date is a workday or a holiday in Taiwan, based on the official work calendar provided by the Taiwan government.

![coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![license](https://img.shields.io/badge/license-MIT-green)

## Features

- Determine if a date is a workday or holiday.
- Support for official Taiwan government work calendar rules, including special adjusted workdays and holidays.
- Easy-to-use API for date checking.

## Installation

You can install `taiwan-holidays` via pip:

```bash
pip install taiwan-holidays
```

## Usage

Here's how you can use taiwan-holidays in your Python project.

### Example

```python
calendar = TaiwanCalendar()
date = dateutil.parser.parse('2024-12-08')
print(calendar.is_holiday(date))
print(calendar.is_holiday('2024-12-08'))
print(calendar.is_holiday('20241208'))
print(calendar.is_holiday('2024/12/08'))
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements

Special thanks to the Taiwan government for providing the official administrative calendar as the basis for this package.

Feel free to report any issues or suggest new features in the Issues section.
