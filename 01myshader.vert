#version 150

// Uniform inputs
uniform mat4 p3d_ModelViewProjectionMatrix;

// Vertex inputs
in vec4 p3d_Vertex;

// Output to fragment shader
out vec4 p3d_Color;

void main() {
  gl_Position = p3d_ModelViewProjectionMatrix * p3d_Vertex;
  p3d_Color.r = p3d_Vertex.y;
}
