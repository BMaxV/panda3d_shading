from direct.showbase.ShowBase import ShowBase
from panda3d.core import Shader

class Wrapper:
    
    # I should definitely
    # use the system built in drag main to do this.
    # pretty sure anyway.
    
    def __init__(self):
        self.b = ShowBase()
        self.b.enableParticles()
        self.ob=load_object(self.b)
        
        tex1=loader.loadTexture('testgrid.png')
        tex2=loader.loadTexture('ground.jpg')
        #self.ob.setTexture(tex)
        tex1 = loader.loadTexture('testgrid.png')
        self.ob.setShaderInput("mytexture1", tex1)
        self.ob.setShaderInput("mytexture2", tex2)
        
        shader = Shader.load(Shader.SL_GLSL,
                     vertex="02myshader.vert",
                     fragment="02myshader.frag")
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
    #ob.setColor(0,1,0,1)
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
