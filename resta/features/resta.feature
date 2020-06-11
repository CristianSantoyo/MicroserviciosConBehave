Feature: Resta

Scenario Outline: Get subtraction total values
  Given a <values> to subtract
  When the calculator subtracts the values
  Then the <total> of substraction  is correct

  Examples: values
  | values         | total |
  | 5,2            | 3     |
  | 2,1            | 1     |
  | 21,10          | 11    |
  | 12,15          | -3    |
  | 12,20          | -8    |