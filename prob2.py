import argparse

import jdatetime


# print(jdatetime.datetime.today())


class TimestampOpen:

    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.a = open(self.filename, 'a')
        self.first = jdatetime.datetime.today()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.last = jdatetime.datetime.today()
        self.a.append(self.first)
        self.a.append(self.last)
        self.a.close()
        return self.a


# ____________________________________________________________________________________________________
# bande tamrin seri 8 ro hanooz kamel nkrdm vali argparse be in shekl hast

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='average of marks')

    parser.add_argument('-s', '--start_date', metavar='StartDate', action='store', type=float, help='starting time')
    parser.add_argument('-e', '--end_date', metavar='EndDate', action='store', default=2, help='ending time')
    parser.add_argument('-w', '--week_date', metavar='WeekDate', action='store', default=2, help='day of the week')

    args = parser.parse_args()
    print()
