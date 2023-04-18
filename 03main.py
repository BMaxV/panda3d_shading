from direct.showbase.ShowBase import ShowBase
from panda3d.core import Shader

from panda_interface_glue import panda_interface_glue as pig
class Wrapper:
    
    # I should definitely
    # use the system built in drag main to do this.
    # pretty sure anyway.
    
    def __init__(self):
        self.b = ShowBase()
        self.b.enableParticles()
        self.ob=load_object(self.b)
        
        self.selected_text="ground.jpg"
        
        
        b=pig.create_button("switch me",(0,0,-0.5),0.05,self.set_tex2,tuple())
        
        tex1=loader.loadTexture('testgrid.png')
        tex2=loader.loadTexture('ground.jpg')
        tex3=loader.loadTexture('bunny.png')
        
        tex1 = loader.loadTexture('testgrid.png')
        self.ob.setShaderInput("mytexture1", tex1)
        self.ob.setShaderInput("mytexture2", tex2)
        self.ob.setShaderInput("bunnytex", tex3)
        
        shader = Shader.load(Shader.SL_GLSL,
                     vertex="03myshader.vert",
                     fragment="03myshader.frag")
        self.ob.setShader(shader)
        
        self.t=0
    
    def set_tex2(self,*args):
        
        if self.selected_text=="ground.jpg":
            tex2=loader.loadTexture("sand.png")
            self.ob.setShaderInput("mytexture2", tex2)
            self.selected_text="sand.png"
            
        else:
            tex2=loader.loadTexture('ground.jpg')
            self.ob.setShaderInput("mytexture2", tex2)
            self.selected_text="ground.jpg"
    
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
