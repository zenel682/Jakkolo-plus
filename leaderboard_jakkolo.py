import json

class Leaderboard():
    def __init__(self):
        global path_to_leaderboard
        path_to_leaderboard = "/home/jakkolo/jakkolo/jakkolo-plus/leaderboard/leaderboard.JSON"
        global player_names_scores

    def openAndReadJSON(self):
        leaderboard_file = open(path_to_leaderboard)
        leaderboard_data = json.load(leaderboard_file)
        # Initialize arrays to store player names and scores
        global player_names_scores    

        # Iterate over players and store names and scores
        player_names_scores = [(player['playerName'], player['playerScore']) for player in leaderboard_data['players']]

        # Print the arrays
        #print("Player Names:", player_names_scores)

        leaderboard_file.close
        return player_names_scores

    def safeAndCloseJSON(self, player_names_scores):
        # Create a new JSON structure with modified data
        players = [{'playerName': name, 'playerScore': score} for name, score in player_names_scores]
        # Create a dictionary with the 'players' key
        data_to_write = {'players': players}

        # Convert the modified data back to JSON
        modified_json = json.dumps(data_to_write, indent=2)

        # Print the modified JSON
        #print(modified_json)

        # Optionally, you can write the modified JSON to a file
        with open(path_to_leaderboard, 'w') as file:
            file.write(modified_json)

    def compareCurrentplayerWithLeaderboard(self, players):
        test = [("afect", 123), ("tre", 55), ("zua", 234223)]
        players.insert([0][0], "noob")
        if players[0][1] > test[0][1]:
            print("hudere")
        #players.sort(key = lambda i:i[1], reverse = True)
        print(players)
        
"""        
players = [("name", 442), ("test", 25), ("kobi", 232)]
lb = Leaderboard()
lb.compareCurrentplayerWithLeaderboard(players)"""
