# ical_toronto_waste

Converts Toronto Open Data Solid Waste data into useable iCal and CSV calendars.

![Example](AllCals.jpg)

| Zone | Google Calendar/iCal | Outlook/Yahoo! Calendars/CSV |
|------|:--------------------:|:----------------------------:|
| Tuesday 1 | [iCal](https://raw.githubusercontent.com/mihir8786/ical_toronto_waste/refs/heads/main/output/ics/Tuesday1.ics) | [CSV](https://github.com/mihir8786/ical_toronto_waste/blob/main/output/csv/Tuesday1.csv) |
| Tuesday 2 | [iCal](https://raw.githubusercontent.com/mihir8786/ical_toronto_waste/refs/heads/main/output/ics/Tuesday2.ics) | [CSV](https://github.com/mihir8786/ical_toronto_waste/blob/main/output/csv/Tuesday2.csv) |
| Wednesday 1 | [iCal](https://raw.githubusercontent.com/mihir8786/ical_toronto_waste/refs/heads/main/output/ics/Wednesday1.ics) | [CSV](https://github.com/mihir8786/ical_toronto_waste/blob/main/output/csv/Wednesday1.csv) |
| Wednesday 2 | [iCal](https://raw.githubusercontent.com/mihir8786/ical_toronto_waste/refs/heads/main/output/ics/Wednesday2.ics) | [CSV](https://github.com/mihir8786/ical_toronto_waste/blob/main/output/csv/Wednesday2.csv) |
| Thursday 1 | [iCal](https://raw.githubusercontent.com/mihir8786/ical_toronto_waste/refs/heads/main/output/ics/Thursday1.ics) | [CSV](https://github.com/mihir8786/ical_toronto_waste/blob/main/output/csv/Thursday1.csv) |
| Thursday 2 | [iCal](https://raw.githubusercontent.com/mihir8786/ical_toronto_waste/refs/heads/main/output/ics/Tuesday2.ics) | [CSV](https://github.com/mihir8786/ical_toronto_waste/blob/main/output/csv/Thursday2.csv) |
| Friday 1 | [iCal](https://raw.githubusercontent.com/mihir8786/ical_toronto_waste/refs/heads/main/output/ics/Friday1.ics) | [CSV](https://github.com/mihir8786/ical_toronto_waste/blob/main/output/csv/Friday1.csv) |
| Friday 2 | [iCal](https://raw.githubusercontent.com/mihir8786/ical_toronto_waste/refs/heads/main/output/ics/Friday2.ics) | [CSV](https://github.com/mihir8786/ical_toronto_waste/blob/main/output/csv/Friday2.csv) |

Find out when your waste gets collected [here](https://www.toronto.ca/services-payments/recycling-organics-garbage/houses/collection-schedule/)


## Updating
1. Grab the latest CSV file from [here](https://open.toronto.ca/dataset/solid-waste-pickup-schedule/)
1. Save the file to the schedules directory (should be named `pickup-schedule-YYYY.csv`)
1. Run `python ical_toronto_waste.py`


## Contributing
1. Fork it
1. Create your feature branch: git checkout -b my-new-feature
1. Commit your changes: git commit -am 'Add some feature'
1. Push to the branch: git push origin my-new-feature
1. Submit a pull request

## License

> This script is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 2 of the License, or (at your option) any later version.
> This script is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. Please refer to the GNU General Public License http://www.gnu.org/licenses/
