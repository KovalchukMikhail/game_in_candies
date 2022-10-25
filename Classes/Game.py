
class Game():
    player_one_name = ''
    count_candies = 150
    player_id = ''
    status_game = False

    def __init__(self, player_one_name, player_id,  type_game = 0, player_two_name = 'Computer'):
        self.type_game = type_game
        self.player_one_name = player_one_name
        self.player_two_name = player_two_name
        self.player_id = player_id

    def step_game(self):
        pass

    

        
        