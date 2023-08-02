from classes.result import Result


class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if isinstance(value, str) and not hasattr(self, "title") and 0 < len(value):
            self._title = value
        else:
            raise Exception


    def results(self, new_result=None):
        return [result for result in Result.all if result.game == self]


    def players(self, new_player=None):
        return list([result for result in Result.all if result.players == self])


    def average_score(self, player):
        return sum(self.results/len(self.results()))