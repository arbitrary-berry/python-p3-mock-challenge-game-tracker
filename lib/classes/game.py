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
        pass

    def players(self, new_player=None):
        pass

    def average_score(self, player):
        pass
