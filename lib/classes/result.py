class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

    @property
    def score(self):
        return self.score
    
    @score.setter
    def score(self, value):
        if type(value) is int and 1 <= value <= 5000:
            self._score = score
        else:
            raise Exception