import bge


def move_from_player_position(cont):
    player = bge.logic.getCurrentScene().objects["Player_Controller"]
    cont.owner.worldPosition = player.worldPosition