from pgx.core import EnvId, State

__all__ = ["State", "EnvId"]


def make(env_id: EnvId):
    if env_id == "tic_tac_toe/v0":
        from pgx.tic_tac_toe import TicTacToe

        return TicTacToe()
    elif env_id == "shogi/v0":
        from pgx.shogi import Shogi

        return Shogi()
    elif env_id == "go-19x19/v0":
        from pgx.go import Go

        return Go(size=19)
    elif env_id == "backgammon/v0":
        from pgx.backgammon import Backgammon

        return Backgammon()
    elif env_id == "minatar/asterix/v0":
        from pgx.minatar.asterix import MinAtarAsterix

        return MinAtarAsterix()
    else:
        raise NotImplementedError()
