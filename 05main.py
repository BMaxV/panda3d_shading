from direct.showbase.ShowBase import ShowBase
from panda3d.core import Shader
from panda3d.core import TransparencyAttrib

from panda3d.core import TextureStage

class Wrapper:
    
    # I should definitely
    # use the system built in drag main to do this.
    # pretty sure anyway.
    
    def __init__(self):
        self.b = ShowBase()
        self.b.enableParticles()
        self.ob=load_object(self.b)
        self.ob.setTransparency(TransparencyAttrib.MAlpha)
        self.selected_text="ground.jpg"
        
        #tex1=loader.loadTexture('testgrid.png')
        #tex2=loader.loadTexture('ground.jpg')
        tex=loader.loadTexture("loading10001-0060.avi")
        tex.setPlayRate(2)
        tex.play()
        ts = TextureStage('ts')
        #pattern = loader.loadTexture('color_pattern.png')
        self.ob.setTexture(ts, tex)
        self.ob.setTexScale(ts, 0.1, 0.1)
        #ts = TextureStage('ts')
        #self.ob.setTexture(ts,tex)
        #for x in self.ob.children:
        #self.ob.setUvRange(tex)
        #tex3=loader.loadTexture("bunny.png")
        self.ob.setShaderInput("animatedtex", tex)
        
        shader = Shader.load(Shader.SL_GLSL,
                     vertex="05myshader.vert",
                     fragment="05myshader.frag")
                     
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
    #ob.setTwoSided(True)
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
