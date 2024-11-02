#version 150

vec4 color1;
vec4 color2;
bvec3 temp;

uniform sampler2D p3d_Texture0;
uniform sampler2D mytexture1;

// Input from vertex shader
in vec2 texcoord;
in vec4 p3d_Color;
in vec4 world_pos;
uniform float myfloat;

// Output to the screen
out vec4 p3d_FragColor;

void main() {
  
  // solid color
  color1.r = 1;
  color1.g = 0;
  color1.b = 0;
  color1.a = 1;
  
  // or the texture color
  color1 = texture(mytexture1, texcoord);
  
  // you can also set green to 0 and alpha to 0, and you
  // get a bar that gets empty. plus, all the other usual mixing and
  // texturing will also work.
  
  color2.r = 0;
  color2.g = 1;
  color2.b = 0;
  color2.a = 0;
  
  if (texcoord.x < myfloat) {
  p3d_FragColor =color1;
}
  else {
  p3d_FragColor=color2;
}

}
