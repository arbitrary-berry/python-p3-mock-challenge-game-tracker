from classes.result import Result


class Player:
    all = []

    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, value):
        if type(value) is str and 2 <= len(value) <= 16:
            self._username = value
        else:
            raise Exception

    def results(self, new_result=None):
        pass

    def games_played(self, new_game=None):
        pass

    def played_game(self, game):
        pass

    def num_times_played(self, game):
        pass

    @classmethod
    def highest_scored(cls, game):
        pass
