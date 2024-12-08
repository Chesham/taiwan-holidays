import os
from datetime import datetime
from glob import glob

import dateutil.parser
import dateutil.tz
import pandas as pd


class TaiwanCalendar:
    def __init__(self):
        self.timezone = dateutil.tz.gettz('Asia/Taipei')
        self.load()

    def is_holiday(self, date: datetime):
        s = self.lookup.loc[self.lookup['西元日期'] == f'{date:%Y-%m-%d}']
        if s.empty:
            raise ValueError(f'No data for {date:%Y-%m-%d}')
        return s.iloc[0]['是否放假'] == 2

    def load(self):
        lookup = []
        for i in glob(os.path.join(os.path.split(__file__)[0], 'data', '*.csv')):
            df = pd.read_csv(
                i,
                converters={
                    '西元日期': dateutil.parser.parse,
                    '備註': lambda x: str(x) if x else None,
                },
            )
            df['西元日期'] = df['西元日期'].dt.tz_localize(self.timezone)
            lookup.append(df)
        self.lookup = pd.concat(lookup)
