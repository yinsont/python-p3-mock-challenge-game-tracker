class Player:

    all = []

    def __init__(self, username):
        self.username = username
        self._results = []
        self._games_played = []

    @property
    def username (self):
        return self._username
    
    @username.setter
    def username(self, username):
        if type(username) == str and 2 <= len(username) <= 16 :
            self._username = username
        else: raise Exception
        
    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def games_played(self, new_game=None):
        from classes.game import Game
        if new_game and isinstance(new_game, Game) and new_game not in self._games_played :
            self._games_played.append(new_game)
        return self._games_played
    
    def played_game(self, game):
        return game in self._games_played
    
    def num_times_played(self, game):
        count = 0
        for result in self._results:
            if game == result.game:
                count += 1
        return count
    
    @classmethod
    def highest_scored(cls, game):
        # return max()
        pass
        
