from direct.showbase.ShowBase import ShowBase
from panda3d.core import Shader
from panda3d.core import TransparencyAttrib
#from panda_object_create import panda_object_create_load
from direct.task import Task
from panda3d.core import LVector4f


# this is not really complete, I wanted to get a custom float value in here
# the time is nice though, good for animating, e.g. water.

class Wrapper(ShowBase):
        
    def __init__(self):
        ShowBase.__init__(self)
        #self.b = ShowBase()
        #self.b=base
        #self.b.enableParticles()
        
        #self.t = 0.0
        #verts = [(0,0,0),(1,0,0.5),(0,0,1)]
        #faces = [[0,1,2]]
        
        
        #self.ob=load_object(self.b)
        self.ob=load_object(base)
        
        #self.ob = panda_object_create_load.make_object(self.render,verts,faces,twosided=True,texture="this")
        #self.ob.setPos(0,20,0)
        #self.ob.reparentTo(self.aspect2d)
        #self.ob.setHpr(45,45,45)
        #self.ob.setTransparency(TransparencyAttrib.MAlpha)
        #self.selected_text="ground.jpg"
        
        #tex1=loader.loadTexture('testgrid.png')
        #tex2=loader.loadTexture('ground.jpg')
        tex3=loader.loadTexture('bunny.png')
        
        #self.ob.setShaderInput("bunnytex", tex3)
        
        # something with fog and camera distance here.
        self.ob.setShaderInput("bunnytex", tex3)
        #self.ob.setShaderInput("totaltime", self.t)
        self.myvec=LVector4f(1,0,0,0)
        self.ob.setShaderInput("myany", self.myvec)
        self.myfloat = 0.0
        self.ob.setShaderInput("myfloat", self.myvec)
        
        
        shader = Shader.load(Shader.SL_GLSL,
                     vertex="08myshader.vert",
                     fragment="08myshader.frag")
        self.ob.setShader(shader)
        self.myshader = shader
        self.t=0
        
        self.taskMgr.add(self.main)
    
    def main(self,*args):#,delta_t):
        delta_t = globalClock.dt
        #print(delta_t)
        self.myvec[0]+=delta_t
        #print(self.myvec)
        self.t+=delta_t
        self.myfloat += delta_t
        self.ob.setShaderInput("totaltime", self.t)
        self.ob.setShader(self.myshader)
        #print(self.t)
        #self.ob.setHpr((self.t*5,0,0))
        return Task.cont

def load_object(showbase,name="cube",path="./",pos=(0,20,0),scale=(1,1,1)):    
    name=path+name
    try:
        ob = showbase.loader.loadModel(name)
    except OSError as e:
        print("my error",e)
        #wait that probably should be in the create load function
        #can't find the file
        return None
    
    ob.setPos(*pos)
    ob.reparentTo(showbase.render)
    ob.setScale(*scale)
    ob.setTwoSided(True)
    return ob

def main():
    W = Wrapper()
    #W.main = GameMain()
    while True:
        delta_t = globalClock.dt
        W.b.taskMgr.step()
        W.main(delta_t)

if __name__=="__main__":
    #main()
    W=Wrapper()
    W.run()
