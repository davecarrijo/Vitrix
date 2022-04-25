import os
import ursina

from lib.crate import Crate


class Wall(ursina.Entity):
    base_dir = os.path.join("assets","textures")
    def __init__(self, position):
        super().__init__(
            position=position,
            scale=2,
            model="cube",
            texture=os.path.join(Wall.base_dir, "wall.png"),
            origin_y=-0.5
        )
        
        self.texture.filtering = None
        self.collider = ursina.BoxCollider(self, size=ursina.Vec3(1, 2, 1))


class Map:
    def __init__(self):
        for y in range(1, 4, 2):
            Wall(ursina.Vec3(6, y, 0))
            Wall(ursina.Vec3(6, y, 2))
            Wall(ursina.Vec3(6, y, 4))
            Wall(ursina.Vec3(6, y, 6))
            Wall(ursina.Vec3(6, y, 8))

            Wall(ursina.Vec3(4, y, 8))
            Wall(ursina.Vec3(2, y, 8))
            Wall(ursina.Vec3(0, y, 8))
            Wall(ursina.Vec3(-2, y, 8))
        Crate(ursina.Vec3(8, 1, 8))
