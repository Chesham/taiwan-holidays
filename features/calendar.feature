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