import dateutil.parser
from behave import *
from grappa import should

from features.environment import Context
from features.steps.fixture import tag
from taiwan_holidays.taiwan_calendar import TaiwanCalendar


@given('today is "{date_str}"')
def step_impl(ctx: Context, date_str):
    ctx.today = date_str


@given('today is {date_str}')
def step_impl(ctx: Context, date_str):
    ctx.today = dateutil.parser.parse(date_str).replace(tzinfo=ctx.timezone)


@when('I check if today is a holiday')
def step_impl(ctx: Context):
    try:
        ctx.result = ctx.calendar.is_holiday(ctx.today)
    except Exception as e:
        ctx.result = e


@then('I should be told that today is a holiday')
def step_impl(ctx: Context):
    ctx.result | should.be.true


@then('I should get a value error')
def step_impl(ctx: Context):
    ctx.result | should.be.type.of(ValueError)


@tag('taiwan-calendar')
def taiwan_calendar(ctx: Context, scn):
    ctx.calendar = TaiwanCalendar()


@when(u'I iterate workdays from {start} to {end}')
def step_impl(ctx: Context, start, end):
    it = ctx.calendar.iter_workdays(start, end)
    ctx.workdays = list(it)


@then(u'I should get {days:d} workdays')
def step_impl(ctx: Context, days):
    workdays = ctx.workdays
    workdays | should.have.length(days)


@then(u'The date {date} should in the workdays')
def step_impl(ctx: Context, date):
    date = dateutil.parser.parse(date).replace(tzinfo=ctx.timezone)
    workdays = ctx.workdays
    workdays | should.contains(date)
