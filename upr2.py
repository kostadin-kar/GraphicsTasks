from math import cos, sin
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def draw_triangle():
    glLoadIdentity()

    glColor3f(0.0, 0.7, 0.0)
    glBegin(GL_TRIANGLES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.5, -0.5, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.5, -0.5, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 0.5, 0.0)

    glEnd()


def draw_square_fan():
    glLoadIdentity()

    glColor3f(0.0, 0.7, 0.0)
    glBegin(GL_TRIANGLE_FAN)

    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)

    glEnd()


def draw_square():
    glLoadIdentity()

    glColor3f(0.0, 0.7, 0.0)
    glBegin(GL_TRIANGLES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.5, 0.5, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.5, -0.5, 0.0)

    glEnd()

    glBegin(GL_TRIANGLES)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.5, 0.5, 0.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.5, -0.5, 0.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-0.5, -0.5, 0.0)

    glEnd()


def draw_circle():
    glLoadIdentity()

    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_TRIANGLE_FAN)

    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)

    glEnd()

    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_LINE_LOOP)

    for i in range(0, 65):
        angle = 6.2832 * i / 64
        x = 0.5 * cos(angle)
        y = 0.5 * sin(angle)
        glVertex2f(x, y)
        
    glEnd()


def draw_squares():
    glLoadIdentity()

    glColor3f(0.0, 0.7, 0.0)

    global counter
    glRotatef(counter, 0.0, 0.0, 1.0)
    counter += 0.06

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.5, 0.5, 0.0)
    glEnd()


counter = 0
def draw_something():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glLoadIdentity()  # rotate triangle
    glBegin(GL_TRIANGLE_FAN)

    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)

    glEnd()

    # glLoadIdentity()  # rotate all
    global counter
    glRotatef(counter, 0.0, 1.0, 0.0)
    counter += 0.01

    glColor3f(0.0,1.0,0.0)
    glBegin(GL_TRIANGLES)

    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(0.8, 0.4, 0.0)
    glVertex3f(0.6, 0.8, 0.0)

    glEnd()


def draw_pyramid():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.3, 0.0, -7.0)
    
    global counter

    glRotatef(counter, 1.0, 0.0, 0.0)
    counter += 0.1

    # Begin drawing the pyramid with 4 triangles
    glBegin(GL_TRIANGLES)
    # Front
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Right
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    # Back
    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)

    # Left
    glColor3f(0.0,1.0,0.0)
    glVertex3f( 0.0, 1.0, 0.0)
    glVertex3f(-1.0,-1.0,-1.0)
    glVertex3f(-1.0,-1.0, 1.0)

    # Bottom
    glColor3f(0.0,0.0,1.0)
    glVertex3f( -1.0, -1.0, 1.0)
    glVertex3f( 1.0, -1.0, 1.0)
    glVertex3f( 1.0, -1.0, -1.0)

    glVertex3f( -1.0, -1.0, 1.0)
    glVertex3f( -1.0, -1.0, -1.0)
    glVertex3f( 1.0, -1.0, -1.0)

    glEnd()  # Done drawing the pyramid


def draw_tetrahedron():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glTranslatef(0.3, 0.0, -7.0)

    global counter
    glRotatef(counter, 0.0, 1.0, 0.0)
    counter += 0.06

    # glutWireTetrahedron()
    glutSolidTeapot(1.0)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    draw_triangle()
    # draw_square_fan()
    # draw_square()
    # draw_circle()
    # draw_squares()
    # draw_something()
    # draw_pyramid()
    # draw_tetrahedron()

    glutSwapBuffers()


def reshape(width, height):
    if height == 0:
        height = 1
    aspect = width / height
    glViewport(0,0, width, height)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, aspect, 0.1, 100.0)


def on_init():
    glClearColor(0.0, 0.0, 0.0, 1.0)

    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LEQUAL)
    glShadeModel(GL_SMOOTH)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)


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
