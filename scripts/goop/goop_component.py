import bge
import math
from random import randint, random, choice
from scripts.utils.animate import animate
from mathutils import Vector
from collections import OrderedDict

TIME_WAIT_FOR_PATROL = 240
TIME_WAIT_FOR_ATTACK = 160

class GoopComponent(bge.types.KX_PythonComponent):

    args = OrderedDict([
        ("speed", 0.6),
        ("Player", ""),
        ("Enemy State", {"Idle", "Patrol", "Attack", "Follow", "Death"})
    ])

    def start(self, args):
        scene = bge.logic.getCurrentScene()
        self.enemy_state = {
            "Idle": self.__idle,
            "Patrol": self.__patrol,
            "Attack": self.__atack,
            "Follow": self.__follow,
            "Death": self.__death
        }
        self.speed = args["speed"]
        self.current_enemy_state = args["Enemy State"]

        self.is_add_sound_death = False
        self.is_added_collisor = False

        self.time_wait_attack = TIME_WAIT_FOR_ATTACK
        self.timer_wait_patrol = 0

        self.player = scene.objects[args["Player"]]
        self.armature = self.object.childrenRecursive["arm_goop"]
        self.mesh_goop_death = self.object.childrenRecursive["mesh_goop_death"]
        self.mesh_goop = self.object.childrenRecursive["mesh_goop"]
        self.fisic_character = bge.constraints.getCharacter(self.object)

    def update(self):
        if self.object["vida"] >= 0:
            self.enemy_state[self.current_enemy_state]()
        else:
            self.__death()

    def __death(self):
        self.fisic_character.reset()
        self.mesh_goop.visible = False
        self.mesh_goop_death.visible = True
        animate(armature=self.mesh_goop_death,
                name="goop_death", start_frame=0, end_frame=25)
        if not self.is_add_sound_death:
            self.is_add_sound_death = True
            self.object.scene.addObject("sound_gooo_death", None, 60.0)
        if self.mesh_goop_death.isPlayingAction and self.mesh_goop_death.getActionFrame() > 23:
            self.object.endObject()

    def __follow(self):
        player = self.object.scene.objects[self.player.name]
        if self.object.getDistanceTo(player) <= 2.5:
            self.current_enemy_state = "Attack"

        direction = player.worldPosition - self.object.worldPosition
        self.fisic_character.walkDirection = direction * self.speed
        self.follow_direction(self.fisic_character.walkDirection)
        animate(armature=self.armature, name="idle_goop",
                start_frame=1, end_frame=20)

    def __patrol(self):
        if self.is_near_player():
            self.fisic_character.reset()
            self.current_enemy_state = "Follow"
        angle = self.object["timer"] * 0.5
        x = math.sin(angle)
        y = math.sin(angle)

        self.fisic_character.walkDirection = Vector([x, y, 0]) * self.speed
        animate(armature=self.armature, name="idle_goop",
                start_frame=1, end_frame=20)
        self.follow_direction(self.fisic_character.walkDirection)

    def __idle(self):
        if self.is_near_player():
            self.current_enemy_state = "Follow"
        self.timer_wait_patrol += 1
        animate(armature=self.armature, name="idle_goop",
                start_frame=1, end_frame=20)
        if self.timer_wait_patrol == TIME_WAIT_FOR_PATROL:
            if choice([True, False]):
                self.current_enemy_state = "Patrol"
            self.timer_wait_patrol = 0

    def __atack(self):
        player = self.object.scene.objects[self.player.name]
        self.__add_collide_attack()
        animate(armature=self.armature, name="idle_goop",
                start_frame=1, end_frame=20)

        if self.object.getDistanceTo(player) <= 2.5:
            self.fisic_character.reset()

        if self.object.getDistanceTo(player) > 3.5:
            self.current_enemy_state = "Follow"

        if self.time_wait_attack == TIME_WAIT_FOR_ATTACK:
            animate(armature=self.armature, name="attack_goop",
                    start_frame=0, end_frame=45, layer=1, blend=8)
            self.is_added_collisor = False
            self.time_wait_attack = 0
        self.time_wait_attack += 1

    def follow_direction(self, direction):
        if direction.length != 0:
            self.object.alignAxisToVect(direction, 1, 1.0)
            self.object.alignAxisToVect([0, 0, 1], 2, 1)

    def is_near_player(self) -> bool:
        if not self.player.name in self.object.scene.objects:
            return False
        player = self.object.scene.objects[self.player.name]
        return self.object.getDistanceTo(player) < 5

    def __add_collide_attack(self):
        if (self.armature.isPlayingAction(1) and self.armature.getActionName(1) == "attack_goop" and not self.is_added_collisor
                and self.armature.getActionFrame(1) > 33 and self.armature.getActionFrame(1) > 36):
            self.object.scene.addObject("Goop_collide", self.object.childrenRecursive["Local_collide"], 1.0)
            self.is_added_collisor = True
