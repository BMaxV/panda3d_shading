#version 150

uniform sampler2D p3d_Texture0;
uniform sampler2D p3d_Texture1;

uniform sampler2D bunnytex;
vec4 color;

// Input from vertex shader
in vec2 texcoord;
in vec4 p3d_Color;
in vec4 world_pos;

// Output to the screen
out vec4 p3d_FragColor;

void main() {
  
  color = texture(bunnytex, texcoord);
  //color.a = 1-color.r;
  color.a = (world_pos.y - 20.5);
  //color.a = min(color.a,p3d_Color.y) ;
  
  p3d_FragColor = color; 
}
