class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        Result.all.append(self)

    @property
    def score(self):
        return self.score
    
    @score.setter
    def score(self, value):
        if type(value) is int and 1 <= value <= 5000:
            self._score = value
        else:
            raise Exception
        
    @property
    def player(self):
        return self.player
    
    @player.setter
    def player(self, player):
        from classes.player import Player

        if isinstance(player, Player):
            self._player = player
        else:
            raise Exception

    @property
    def game(self):
        return self.game
    
    @game.setter
    def game(self, game):
        from classes.game import Game

        if isinstance(game, Game):
            self._game = game
        else:
            raise Exception