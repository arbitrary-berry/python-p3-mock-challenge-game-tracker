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
        return list([result for result in Result.all if result.player == self])
        pass

    def games_played(self, new_game=None):
        return list((self.games()))
        pass

    def played_game(self, game):
        if [result for result in Result.all if result.player == self]:
            return True
        else:
            return False

    def num_times_played(self, game):
        return len(self.games_played())

    @classmethod
    def highest_scored(cls, game):
        pass
