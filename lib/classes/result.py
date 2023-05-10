class Result:

    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        Result.all.append(self)
        
        player.results(self)

        player.games_played(game)


        game.results(self)
        game.players(player)