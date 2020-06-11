Feature: Suma

Scenario Outline: Get sum total values
  Given a <values> to sum
  When the calculator sums the values
  Then the <total> of sum is correct

  Examples: values
  | values         | total |
  | 4,7            | 11    |
  | 5,3            | 8     |
  | 11,33          | 44    |
  | 82,15          | 97    |
  | 12,10          | 22    |