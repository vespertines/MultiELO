import math

class MultiELO:
    def __init__(self, num_players, k_factor):
        self.num_players = num_players
        self.k_factor = k_factor
        self.players = {}
        for i in range(num_players):
            self.players[i] = {'rating': 1500, 'games_played': 0}
    
    def expected_score(self, player, opponent_ratings):
        exponent = sum([(opponent_ratings[i] - player['rating'])/400.0 for i in opponent_ratings.keys()])
        return 1.0 / (1.0 + math.pow(10, exponent/self.num_players))

    def update_ratings(self, results):
        for i in range(self.num_players):
            player = self.players[i]
            opponent_ratings = {}
            for j in range(self.num_players):
                if i != j:
                    opponent_ratings[j] = self.players[j]['rating']
            
            expected = self.expected_score(player, opponent_ratings)
            actual = results[i]
            player['rating'] += self.k_factor * (actual - expected)
            player['games_played'] += 1
            player['rating'] = int(player['rating'] + 0.5)
    
    def get_ratings(self):
        ratings = {}
        for i in range(self.num_players):
            player = self.players[i]
            ratings[i] = player['rating']
        return ratings

if __name__ == '__main__':
    num_players = int(input("Enter the number of players: "))
    k_factor = float(input("Enter the k-factor value: "))
    num_rounds = int(input("Enter the number of rounds: "))
    multielo = MultiELO(num_players, k_factor)

    for i in range(num_rounds):
        results = []
        for j in range(num_players):
            result = int(input(f"Enter the placement for player {j+1} in round {i+1}: "))
            results.append(result)
        multielo.update_ratings(results)
    
    ratings = multielo.get_ratings()
    print("Current MultiELO Ratings:")
    for player, rating in ratings.items():
        print(f"Player {player+1}: {rating}")