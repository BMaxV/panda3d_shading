#version 150

// Input from vertex shader
in vec4 p3d_Color;

// Output to the screen
out vec4 p3d_FragColor;

void main() {
  p3d_FragColor = p3d_Color;
}
