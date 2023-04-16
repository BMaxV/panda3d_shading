#version 150

// Uniform inputs
uniform mat4 p3d_ModelViewProjectionMatrix;
uniform vec4 position;
uniform sampler2D p3d_Texture0;

// Vertex inputs
in vec2 p3d_MultiTexCoord0;
in vec4 p3d_Vertex;
//in vec4 p3d_Color;

// Output to fragment shader
out vec2 texcoord;
out vec4 p3d_Color;

void main() {
  gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
  p3d_Color.r = p3d_Vertex.y;
  //p3d_Texture0.r=1;
  texcoord = p3d_MultiTexCoord0;
}
