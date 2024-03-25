# Competitive Eating Competition Scoreboard

## Description

In a competitive eating competition, you are tasked with choosing a winner based on the points earned from consuming three types of food: chicken wings, hamburgers, and hot dogs. Each type of food is worth a different amount of points:

- Chicken wings: 5 points
- Hamburgers: 3 points
- Hot dogs: 2 points

This project provides a function to generate a scoreboard for the competition. The function takes a list of participants, where each participant is represented by an object with their name and the number of chicken wings, hamburgers, and hot dogs they consumed. The function calculates the total score for each participant and returns a sorted list of participants with their names and scores. If two participants have the same score, they are sorted alphabetically by name.

## Usage

To use the scoreboard generator function, import it into your Python code:

```python
from scoreboard import generate_scoreboard

participants = [
    {"name": "Habanero Hillary", "chickenwings": 5, "hamburgers": 17, "hotdogs": 11},
    {"name": "Big Bob", "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}
]

scoreboard = generate_scoreboard(participants)
print(scoreboard)