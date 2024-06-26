#version 150

uniform sampler2D p3d_Texture0;
uniform sampler2D p3d_Texture1;

uniform sampler2D mytexture1;
uniform sampler2D mytexture2;

// Input from vertex shader
in vec2 texcoord;
in vec2 texcoord2;
in vec4 p3d_Color;

// Output to the screen
out vec4 p3d_FragColor;

void main() {
    
  vec4 color;
  vec4 v1 = texture(mytexture2, texcoord2);
  vec4 v2 = texture(mytexture1, texcoord);
  color = mix(v1,v2,texcoord.x*1);
  
  //color = textureGrad(mytexture1, texcoord, uv, uv);
  //vec4 color = textureGrad(mytexture2, texcoord, uv2, uv2);
  
  p3d_FragColor = color; //color.bgra;
}
