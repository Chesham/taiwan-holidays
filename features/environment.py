from datetime import datetime, tzinfo
from typing import Protocol

import behave.runner
import dateutil.tz
from behave.model import Scenario

from features.steps.fixture import get_tag_handler
from taiwan_holidays.taiwan_calendar import TaiwanCalendar


def before_scenario(ctx: behave.runner.Context, scn: Scenario):
    timezone = dateutil.tz.gettz('Asia/Taipei')
    ctx.timezone = timezone
    for h in (h for tag in scn.tags if (h := get_tag_handler(tag)) is not None):
        h(ctx, scn)


class CalendarContext(Protocol):
    calendar: TaiwanCalendar
    today: datetime
    timezone: tzinfo


class Context(CalendarContext, behave.runner.Context): ...
