import csv
import glob
import logging
import sys
from collections import defaultdict
from datetime import datetime


logging.basicConfig(stream=sys.stdout,
                    level=logging.INFO,
                    format='[%(levelname)s] %(message)s')

CALENDAR_OUTPUT_DIR = 'output/'
CSV_OUTPUT_DIR = 'csv/'
ICS_OUTPUT_DIR = 'ics/'

CSV_OUT_PATH = CALENDAR_OUTPUT_DIR + CSV_OUTPUT_DIR
ICS_OUT_PATH = CALENDAR_OUTPUT_DIR + ICS_OUTPUT_DIR

SCHEDULES_FILE_REGEX = 'schedules/pickup-schedule-*.csv'

INPUT_DATE_FORMATS = ['%d-%m-%Y', '%Y-%m-%d']  # Multiple possible date formats
CSV_DATE_FORMAT = '%m-%d-%y'
ICS_DATE_FORMAT = '%Y%m%d'
ICS_DATETIME_FORMAT = '%Y%m%dT%H%M%S'


def main():
    data = process_data()
    write_csv(data)
    write_ics(data)


def process_data():
    logging.info('Parsing City of Toronto Open Data')

    data = defaultdict(list)

    for file in sorted(glob.glob(SCHEDULES_FILE_REGEX)):
        logging.info(f'Parsing {file}')
        with open(file) as calendar_file:
            lines = csv.reader(calendar_file)

            # Skip header
            lines.__next__()

            for row in lines:
                pickup = Pickup(row)
                data[pickup.calendar].append(pickup)

    return data


def write_csv(data):
    logging.info('Writing CSV calendars')

    for calendar in data:
        pickups = data[calendar]
        logging.info('Writing %s CSV', calendar)

        with open(f'{CSV_OUT_PATH}{calendar}.csv', 'w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(
                ["Subject", "Start Date", "All Day Event", "Description"])

            for pickup in pickups:
                start_date = datetime.strftime(pickup.day, CSV_DATE_FORMAT)
                csv_writer.writerow(
                    [pickup.subject, start_date, 'TRUE',
                     f'{pickup.description} - See {pickup.url}'])

    logging.info('Finished writing CSV calendars')


def write_ics(data):
    logging.info('Writing ICS calendars')

    ics_generation_time = datetime.strftime(
        datetime.now(), ICS_DATETIME_FORMAT)

    for calendar in data:
        pickups = data[calendar]

        logging.info('Writing %s ICS', calendar)

        with open(f'{ICS_OUT_PATH}{calendar}.ics', 'w', encoding='utf-8') as ics_file:
            ics_file.write('BEGIN:VCALENDAR\r\n')
            ics_file.write('VERSION:2.0\r\n')
            ics_file.write('CALSCALE:GREGORIAN\r\n')
            ics_file.write('METHOD:PUBLISH\r\n')
            ics_file.write(
                'PRODID:https://github.com/mtpettyp/ical_toronto_waste\r\n')
            ics_file.write(f'X-WR-CALNAME:{calendar} Waste Pickup\r\n')
            ics_file.write('X-WR-TIMEZONE:America/Toronto\r\n')

            for pickup in pickups:
                start_date = datetime.strftime(pickup.day, ICS_DATE_FORMAT)
                ics_file.write('BEGIN:VEVENT\r\n')
                ics_file.write(f'URL;VALUE=URI:{pickup.url}\r\n')
                ics_file.write(f'SUMMARY:{pickup.subject}\r\n')
                ics_file.write(f'DTSTART;VALUE=DATE:{start_date}\r\n')
                ics_file.write(
                    f'DTSTAMP;VALUE=DATETIME:{ics_generation_time}\r\n')
                ics_file.write(f'UID:{start_date}{calendar}\r\n')
                ics_file.write(f'DESCRIPTION:{pickup.description}\r\n')
                ics_file.write('TRANSP:TRANSPARENT\r\n')
                ics_file.write('END:VEVENT\r\n')

            ics_file.write('END:VCALENDAR\r\n')

    logging.info('Finished writing ICS calendars')


SUBJECT_GARBAGE = 'Garbage Day'
EMOJI_GARBAGE = '🗑'
SUBJECT_RECYCLING = 'Recycling Day'
EMOJI_RECYCLING = '♻️'
SUBJECT_YARD_WASTE = 'Yard Waste'
EMOJI_YARD_WASTE = '🍂'
SUBJECT_CHRISTMAS_TREE = 'Christmas Tree'
EMOJI_CHRISTMAS_TREE = '🎄'

URL_GARBAGE = ('https://www.toronto.ca/services-payments/recycling-organics-garbage/'
               'houses/what-goes-in-my-green-bin/')
URL_RECYCLING = 'https://www.toronto.ca/services-payments/recycling-organics-garbage/waste-wizard/'


def parse_date(date_str):
    """
    Attempts to parse a date string in multiple formats.
    Returns a datetime object if successful, raises ValueError if not.
    """
    for date_format in INPUT_DATE_FORMATS:
        try:
            return datetime.strptime(date_str, date_format)
        except ValueError:
            continue
    raise ValueError(f"Date {date_str} does not match any known format.")


class Pickup:
    def __init__(self, row):
        [_, self.calendar, day, green_bin, garbage,
            recycling, yard_waste, christmas_tree] = row
        self.day = parse_date(day)  # Use the flexible date parser
        self.green_bin = green_bin != '0'
        self.garbage = garbage != '0'
        self.recycling = recycling != '0'
        self.yard_waste = yard_waste != '0'
        self.christmas_tree = christmas_tree != '0'

    @property
    def subject(self):
        emoji = []
        types = []
        if self.christmas_tree:
            emoji.append(EMOJI_CHRISTMAS_TREE)
            types.append(SUBJECT_CHRISTMAS_TREE)
        if self.yard_waste:
            emoji.append(EMOJI_YARD_WASTE)
            types.append(SUBJECT_YARD_WASTE)
        if self.recycling:
            emoji.append(EMOJI_RECYCLING)
            types.append(SUBJECT_RECYCLING)
        if self.garbage:
            emoji.append(EMOJI_GARBAGE)
            types.append(SUBJECT_GARBAGE)
        return '{} {}'.format(('').join(emoji), ('/').join(types))

    @property
    def description(self):
        types = []
        if self.christmas_tree:
            types.append('Christmas Tree')
        if self.garbage:
            types.append('Garbage')
        if self.recycling:
            types.append('Recycling')
        if self.green_bin:
            types.append('Green Bin')
        if self.yard_waste:
            types.append('Yard Waste')
        return ('/').join(types)

    @property
    def url(self):
        if self.recycling:
            return URL_RECYCLING
        return URL_GARBAGE


if __name__ == "__main__":
    main()