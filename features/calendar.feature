Feature: Calendar

    @taiwan-calendar
    Scenario: Test holiday
        Given today is 2024-02-13
        When I check if today is a holiday
        Then I should be told that today is a holiday

    @taiwan-calendar
    Scenario: Test days not in the calendar
        Given today is 2018-12-03
        When I check if today is a holiday
        Then I should get a value error

    @taiwan-calendar
    Scenario Outline: Test holiday using string
        Given today is <today>
        When I check if today is a holiday
        Then I should be told that today is a holiday
        Examples:
            | today        |
            | "2024-02-13" |
            | "20240213"   |
            | "2024/02/13" |
            | "2024.02.13" |
            | "2024 02 13" |

    @taiwan-calendar
    Scenario: Test days not in the calendar using string
        Given today is "2018-12-03"
        When I check if today is a holiday
        Then I should get a value error

    @taiwan-calendar
    Scenario: Iterate workdays
        When I iterate workdays from 2024-02-01 to 2024-02-29
        Then I should get 16 workdays
        And The date 2024-02-01 should in the workdays
        And The date 2024-02-02 should in the workdays
        And The date 2024-02-05 should in the workdays
        And The date 2024-02-06 should in the workdays
        And The date 2024-02-07 should in the workdays
        And The date 2024-02-15 should in the workdays
        And The date 2024-02-16 should in the workdays
        And The date 2024-02-17 should in the workdays
        And The date 2024-02-19 should in the workdays
        And The date 2024-02-20 should in the workdays
        And The date 2024-02-21 should in the workdays
        And The date 2024-02-22 should in the workdays
        And The date 2024-02-23 should in the workdays
        And The date 2024-02-26 should in the workdays
        And The date 2024-02-27 should in the workdays
        And The date 2024-02-29 should in the workdays

    @taiwan-calendar
    Scenario: Iterate workdays with reversed dates
        When I iterate workdays from 2024-02-29 to 2024-02-01
        Then I should get 16 workdays
        And The date 2024-02-01 should in the workdays
        And The date 2024-02-02 should in the workdays
        And The date 2024-02-05 should in the workdays
        And The date 2024-02-06 should in the workdays
        And The date 2024-02-07 should in the workdays
        And The date 2024-02-15 should in the workdays
        And The date 2024-02-16 should in the workdays
        And The date 2024-02-17 should in the workdays
        And The date 2024-02-19 should in the workdays
        And The date 2024-02-20 should in the workdays
        And The date 2024-02-21 should in the workdays
        And The date 2024-02-22 should in the workdays
        And The date 2024-02-23 should in the workdays
        And The date 2024-02-26 should in the workdays
        And The date 2024-02-27 should in the workdays
        And The date 2024-02-29 should in the workdays

    @taiwan-calendar
    Scenario: Iterate workdays with the same date
        When I iterate workdays from 2024-02-01 to 2024-02-01
        Then I should get 1 workdays
        And The date 2024-02-01 should in the workdays

    @taiwan-calendar
    Scenario: Iterate workdays with the same date and it is a holiday
        When I iterate workdays from 2024-02-03 to 2024-02-03
        Then I should get 0 workdays

    @taiwan-calendar
    Scenario: Iterate with a holiday
        When I iterate workdays from 2024-02-02 to 2024-02-03
        Then I should get 1 workdays
        And The date 2024-02-02 should in the workdays