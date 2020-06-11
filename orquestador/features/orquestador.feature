Feature: Orquestador

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