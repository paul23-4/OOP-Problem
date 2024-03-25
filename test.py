import pytest
from scoreboard import create_scoreboard

def test_create_scoreboard():
    participants = [
        {'name': "Habanero Hillary", 'chickenwings': 5 , 'hamburgers': 17, 'hotdogs': 11},
        {'name': "Big Bob" , 'chickenwings': 20, 'hamburgers': 4, 'hotdogs': 11}
    ]
    expected_scoreboard = [
        {'name': "Big Bob", 'score': 134},
        {'name': "Habanero Hillary", 'score': 98}
    ]
    assert create_scoreboard(participants) == expected_scoreboard