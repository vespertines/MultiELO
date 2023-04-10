# MultiELO

MultiELO is a Python package that calculates ELO ratings for multiple players in a game tournament. It can be used for any game with a placement-based scoring system.

## usage

To use MultiELO, simply run the MultiELO.py file and enter the number of players, k-factor value, and number of rounds when prompted. Then enter the placement of each player for each round. The current ratings of all players will be output at the end.

## Installation

You can install MultiELO using pip:

```bash
pip install multielo

```

## Example

Here's an example usage of MultiELO:

```basg
Enter the number of players: 4
Enter the k-factor value: 32
Enter the number of rounds: 3
Enter the placement for player 1 in round 1: 2
Enter the placement for player 2 in round 1: 1
Enter the placement for player 3 in round 1: 3
Enter the placement for player 4 in round 1: 4
Enter the placement for player 1 in round 2: 1
Enter the placement for player 2 in round 2: 2
Enter the placement for player 3 in round 2: 3
Enter the placement for player 4 in round 2: 4
Enter the placement for player 1 in round 3: 1
Enter the placement for player 2 in round 3: 2
Enter the placement for player 3 in round 3: 4
Enter the placement for player 4 in round 3: 3
Current MultiELO Ratings:
Player 1: 1536
Player 2: 1586
Player 3: 1396
Player 4: 1476
```

## License
MultiELO is licensed under the MIT License.
