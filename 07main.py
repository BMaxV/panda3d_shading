from direct.showbase.ShowBase import ShowBase
from panda3d.core import Shader
from panda3d.core import TransparencyAttrib

# fog?
# this is distance based transparency, which is sort of kind of the same.
# https://docs.panda3d.org/1.10/python/programming/shaders/coordinate-spaces
# use p3d_ModelMatrix to get 3d world position for the shader vertex

class Wrapper:
        
    def __init__(self):
        self.b = ShowBase()
        self.b.enableParticles()
        self.ob=load_object(self.b)
        self.ob.setTransparency(TransparencyAttrib.MAlpha)
        self.selected_text="ground.jpg"
        
        #tex1=loader.loadTexture('testgrid.png')
        #tex2=loader.loadTexture('ground.jpg')
        tex3=loader.loadTexture('bunny.png')
        
        self.ob.setShaderInput("bunnytex", tex3)
        
        # something with fog and camera distance here.
        #self.ob.setShaderInput("bunnytex", tex3)
        
        
        shader = Shader.load(Shader.SL_GLSL,
                     vertex="07myshader.vert",
                     fragment="07myshader.frag")
        self.ob.setShader(shader)
        
        self.t=0
    
    def main(self,delta_t):
        self.t+=delta_t
        self.ob.setHpr((self.t*5,0,0))

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
    main()
