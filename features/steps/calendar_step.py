import dateutil.parser
from behave import *
from grappa import should

from features.environment import Context
from features.steps.fixture import tag
from taiwan_holidays.taiwan_calendar import TaiwanCalendar


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


@then('I should be told that today is not a holiday')
def step_impl(ctx: Context):
    ctx.result | should.be.false


@then('I should get a value error')
def step_impl(ctx: Context):
    ctx.result | should.be.type.of(ValueError)


@tag('taiwan-calendar')
def taiwan_calendar(ctx: Context, scn):
    ctx.calendar = TaiwanCalendar()
