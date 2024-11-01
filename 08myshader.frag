#version 150

uniform sampler2D p3d_Texture0;
uniform sampler2D p3d_Texture1;
uniform float osg_FrameTime;
uniform sampler2D bunnytex;
vec4 color;

// Input from vertex shader
in float totaltime;
in vec2 texcoord;
in vec4 p3d_Color;
in vec4 world_pos;
in vec4 myany;
uniform float myfloat;

// Output to the screen
out vec4 p3d_FragColor;

void main() {
  
  color = texture(bunnytex, texcoord);
  //color.a = 1-color.r;
  //color.r = sin(world_pos.x);
  //color.r = sin(texcoord.x*15+(totaltime+1));
  color.r = sin(texcoord.x*15+(osg_FrameTime+1));
  //color.r = sin(texcoord.x*15+( myfloat+1));
  //color.r = sin(texcoord.x*10+(myany.x*50+1));
  //color.a = min(color.a,p3d_Color.y) ;
  
  p3d_FragColor = color;
}
