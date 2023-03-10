from Object import *
from Camera import *
from Project import *
import sys
import pygame as pg


class SoftwareRenderer:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 1600, 900
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [-5, 1, -55])
        self.projection = Projection(self)
        self.object = self.get_object_from_file('resources/radar_obj.obj')
        self.object.rotate_y(-math.pi / 4)

    def get_object_from_file(self, filename):
        vertex, faces = [], []
        with open(filename) as f:
            for line in f:
                if line.startswith('v '):
                    vertex.append([float(i) for i in line.split()[1:]] + [1])
                elif line.startswith('f'):
                    faces_ = line.split()[1:]
                    faces.append([int(face_.split('/')[0]) - 1 for face_ in faces_])
        return Object3D(self, vertex, faces)

    def draw(self):
        self.screen.fill(pg.Color('pink'))
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            for event in pg.event.get():
                # if event.type == pg.QUIT:
                #     running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                       sys.exit()  # Set running to False to end the while loop.
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)



app = SoftwareRenderer()
app.run()