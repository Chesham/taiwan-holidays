import os
from datetime import datetime
from glob import glob
from typing import Union

import dateutil.parser
import dateutil.tz
import pandas as pd
from dateutil.relativedelta import relativedelta


class TaiwanCalendar:
    def __init__(self):
        self.timezone = dateutil.tz.gettz('Asia/Taipei')
        self.load()

    def is_holiday(self, date: Union[datetime, str]) -> bool:
        if isinstance(date, str):
            date = dateutil.parser.parse(date)
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

    def iter_workdays(self, start: Union[datetime, str], end: Union[datetime, str]):
        start = self.parse_date(start)
        end = self.parse_date(end)
        cur = start
        for cur in self.iter_dates(start, end):
            if self.is_holiday(cur):
                continue
            yield cur

    def iter_dates(self, start: Union[datetime, str], end: Union[datetime, str]):
        start = self.parse_date(start)
        end = self.parse_date(end)
        cur = start
        step = relativedelta(days=1)
        cond = lambda x: x <= end
        if start > end:
            step = -step
            cond = lambda x: x >= end
        while cond(cur):
            yield cur
            cur += step

    def parse_date(self, date: Union[datetime, str]) -> datetime:
        if isinstance(date, str):
            date = dateutil.parser.parse(date)
        return date.replace(tzinfo=self.timezone)
