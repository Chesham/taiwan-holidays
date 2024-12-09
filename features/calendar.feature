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