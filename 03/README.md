# Advent of Code 2022 - Day 03
## (Rucksack Reorganization)

Introduced timing through the decorator `@tim.tim`

### [`main1.py`](main1.py)
Using `ord(char)` to get the ASCII code for the character stored in the rucksack, 
then applying an offset to get the relative value

### [`main2.py`](main2.py)
Same translation logic from char to score, however this time using sets instead of lists.
This means I can use set operations such as `intersection()` which is nice.






