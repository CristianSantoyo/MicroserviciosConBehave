Feature: Division

Scenario Outline: Get division total values
    Given a <values> to divide
    When the calculator divide the values
    Then the <total> of divide is correct

  Examples: values
  | values         | total |
  | 4,2            | 2     |
  | 9,-3           | -3    |
  | 20,10          | 2     |
  | 99,11          | 9     |
  | 23,23          | 1     |