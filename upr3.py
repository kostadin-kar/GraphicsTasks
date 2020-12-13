from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy


def draw_with_vao():
    vertices = [
        -0.5, 0.5, 0,
        -0.5, -0.5, 0,
        0.5, -0.5, 0,

        0.5, -0.5, 0,
        0.5, 0.5, 0,
        -0.5, 0.5, 0
    ]

    vao_id = glGenVertexArrays(1)
    glBindVertexArray(vao_id)

    vbo_id = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_id)

    vertices_array = numpy.array(vertices, numpy.float32)
    glBufferData(GL_ARRAY_BUFFER, vertices_array, GL_STATIC_DRAW)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    glEnableVertexAttribArray(0)
    glDrawArrays(GL_TRIANGLES, 0, int(len(vertices_array) / 3))
    glDisableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)


def draw_with_vao_and_indices():
    vertices = [
        -0.5, 0.5, 0,
        -0.5, -0.5, 0,
        0.5, -0.5, 0,
        0.5, 0.5, 0,
    ]

    indices = [
        0, 1, 3,
        3, 1, 2
    ]

    vao_id = glGenVertexArrays(1)
    glBindVertexArray(vao_id)

    ebo_id = glGenBuffers(1)
    glBindBuffer(GL_ELEMENT_ARRAY_BUFFER, ebo_id)

    indices_array = numpy.array(indices, numpy.int32)
    glBufferData(GL_ELEMENT_ARRAY_BUFFER, indices_array, GL_STATIC_DRAW)

    vbo_id = glGenBuffers(1)
    glBindBuffer(GL_ARRAY_BUFFER, vbo_id)

    vertices_array = numpy.array(vertices, numpy.float32)
    glBufferData(GL_ARRAY_BUFFER, vertices_array, GL_STATIC_DRAW)
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, None)

    glEnableVertexAttribArray(0)
    glDrawElements(GL_TRIANGLES, int(len(indices_array)), GL_UNSIGNED_INT, None)
    glDisableVertexAttribArray(0)

    glBindBuffer(GL_ARRAY_BUFFER, 0)
    glBindVertexArray(0)


def draw_with_shaders():
    vertex_shader_source = """
        #version 400 core

        in vec3 position; //input layout (location = 0)
        out vec3 color; //output
        
        void main(void){
            gl_Position = vec4(position,1.0); //4th coordinate for position
            color = vec3(position.x+0.5,1.0,position.y+0.5); //rgb
        } 
    """

    fragment_shader_source = """
        #version 400 core

        in vec3 color; // input is the output data from vertexShader
        out vec4 outColor; // output is the rgb data
        
        void main(void){
            outColor = vec4(color,1.0);
        }
    """

    vertex_shader = glCreateShader(GL_VERTEX_SHADER)
    glShaderSource(vertex_shader, vertex_shader_source)
    glCompileShader(vertex_shader)
    print(glGetShaderInfoLog(vertex_shader))

    fragment_shader = glCreateShader(GL_FRAGMENT_SHADER)
    glShaderSource(fragment_shader, fragment_shader_source)
    glCompileShader(fragment_shader)

    shader_program = glCreateProgram()
    glAttachShader(shader_program, vertex_shader)
    glAttachShader(shader_program, fragment_shader)
    glBindAttribLocation(shader_program, 0, 'position')
    glLinkProgram(shader_program)
    glValidateProgram(shader_program)

    glUseProgram(shader_program)
    glDeleteShader(vertex_shader)
    glDeleteShader(fragment_shader)

    draw_with_vao_and_indices()

    glDetachShader(shader_program, vertex_shader)
    glDetachShader(shader_program, fragment_shader)
    glDeleteProgram(shader_program)


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    # draw_with_vao()
    # draw_with_vao_and_indices()
    # draw_with_shaders()

    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)


def on_init():
    glClearColor(0.0, 0.0, 0.0, 1.0)


glutInit()
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(640, 640)
glutInitWindowPosition(10, 10)
glutCreateWindow("Pesho")

on_init()
glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutIdleFunc(display)

glutMainLoop()
