import json

class Leaderboard():
    def __init__(self):
        global path_to_leaderboard
        path_to_leaderboard = "leaderboard\leaderboard.JSON"
        global player_names
        global player_scores
        player_names = []
        player_scores = []

    def openAndReadJSON(self):
        leaderboard_file = open(path_to_leaderboard)
        leaderboard_data = json.load(leaderboard_file)
        # Initialize arrays to store player names and scores
        global player_scores
        global player_names       

        # Iterate over players and store names and scores
        for player in leaderboard_data['players']:
            player_names.append(player['playerName'])
            player_scores.append(player['playerScore'])

        # Print the arrays
        print("Player Names:", player_names)
        print("Player Scores:", player_scores)
                
        leaderboard_file.close
        return player_names, player_scores

    def safeAndCloseJSON(self, player_names, player_scores):
        # Modify the player names and scores (for example, add a prefix)
        player_names = [f"OK{name}" for name in player_names]
        player_scores = [score * 2 for score in player_scores]

        # Create a new JSON structure with modified data
        modified_data = {
            "players": [
                {"playerName": name, "playerScore": score} for name, score in zip(player_names, player_scores)
            ]
        }

        # Convert the modified data back to JSON
        modified_json = json.dumps(modified_data, indent=2)

        # Print the modified JSON
        print(modified_json)

        # Optionally, you can write the modified JSON to a file
        with open(path_to_leaderboard, 'w') as file:
            file.write(modified_json)