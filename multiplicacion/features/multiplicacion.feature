Feature: Multiplicacion

Scenario Outline: Get product total values
  Given a <values> to multiply
  When the calculator multiply the values
  Then the <total> of multiply is correct

  Examples: values
  | values         | total |
  | 2,2            | 4     |
  | 4,1            | 4     |
  | 123,0          | 0     |
  | 10,10          | 100   |
  | 5,120          | 600   |