from direct.showbase.ShowBase import ShowBase
from panda3d.core import Shader
from panda3d.core import TransparencyAttrib
from panda_object_create import panda_object_create_load
from direct.task import Task
from panda3d.core import LVector4f
import math

# this is not really complete, I wanted to get a custom float value in here
# the time is nice though, good for animating, e.g. water.

class Wrapper:

    def __init__(self):
        self.b = ShowBase()
        
        verts = [(0, 0, 0), (1, 0, 0.05), (0, 0, 0.1)]
        faces = [[0, 1, 2]]
        
        if False:
            verts = [(0, 0, 0),
                    (0, 0, 0.1), 
                    (0.3,0,0.7),
                    (0.3,0,0.3),
                    (0.4,0,0.5),
                    (0.4,0,0.1),
                    (0.6,0,0.6),
                    (0.6,0,0.4),
                    (0.4,0,0.5),
                    (0.4,0,0.1),
                    (1, 0, 0.05) ]
            faces = [[0, 1, 2, 3],[3,2,4,5]]#,[5,4,6,7],[7,6,8]]#,[8,9,10]]


        
        self.ob = panda_object_create_load.make_object(
            self.b.render, verts, faces, twosided=True, texture="this",transparent =1)
        
        self.ob.reparentTo(self.b.aspect2d)
        
        # this is optional.
        self.ob.setHpr(0,-15,-15)
        self.ob.setPos(-0.9,0,-0.9)
        
        self.myfloat = 0.0
        
        tex1=loader.loadTexture('testgrid.png')
        self.ob.setShaderInput("mytexture1", tex1)
        self.ob.setShaderInput("myfloat", self.myfloat)

        shader = Shader.load(Shader.SL_GLSL,
                             vertex="08myshader.vert",
                             fragment="08myshader.frag")
        self.ob.setShader(shader)
        self.myshader = shader
        self.t = 0

    def main(self, *args):
        delta_t = globalClock.dt
        self.t += delta_t
        self.myfloat = math.sin(self.t)
        
        self.ob.setShaderInput("myfloat", self.myfloat)
        self.ob.setShader(self.myshader)
        
        return Task.cont

def load_object(showbase, name="cube", path="./", pos=(0, 20, 0), scale=(1, 1, 1)):
    name = path+name
    try:
        ob = showbase.loader.loadModel(name)
    except OSError as e:
        print("my error", e)
        # wait that probably should be in the create load function
        # can't find the file
        return None

    ob.setPos(*pos)
    ob.reparentTo(showbase.render)
    ob.setScale(*scale)
    ob.setTwoSided(True)
    return ob

def main():
    W = Wrapper()
    # W.main = GameMain()
    while True:
        delta_t = globalClock.dt
        W.b.taskMgr.step()
        W.main(delta_t)

if __name__ == "__main__":
    main()
