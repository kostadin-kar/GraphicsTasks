from math import cos, sin
from OpenGL.GL import *
from OpenGL.GLUT import *


def draw_triangle():
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
    glColor3f(0.0, 0.7, 0.0)

    glBegin(GL_TRIANGLE_FAN)

    glVertex3f(-0.5, -0.5, 0.0)
    glVertex3f(0.5, -0.5, 0.0)
    glVertex3f(0.5, 0.5, 0.0)
    glVertex3f(-0.5, 0.5, 0.0)

    glEnd()


def draw_square():
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
    glColor3f(0.0, 0.7, 0.0)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 0.5, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.5, 0.5, 0.0)
    glEnd()

    glTranslatef(0.0001, 0.0001, 0)
    glRotatef(0.02, 0, 0, 1)


counter = 0
def draw_something():
    glClear(GL_COLOR_BUFFER_BIT)

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

    glColor3f(0.0, 1.0, 0.0)
    glBegin(GL_TRIANGLES)

    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(0.8, 0.4, 0.0)
    glVertex3f(0.6, 0.8, 0.0)

    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT)

    draw_triangle()
    # draw_square_fan()
    # draw_square()
    # draw_circle()
    # draw_squares()
    # draw_something()

    glutSwapBuffers()


def reshape(width, height):
    glViewport(0, 0, width, height)


def on_init():
    glClearColor(0.0, 0.0, 0.0, 1.0)


def on_key_press(key, x, y):
    decoded = key.decode('utf-8')
    if key == b'\x1b':  # escape
        glutLeaveMainLoop()
    # move
    elif decoded == 'a':
        glTranslatef(-0.2, 0, 0)
    elif decoded == 's':
        glTranslatef(0, -0.2, 0)
    elif decoded == 'd':
        glTranslatef(0.2, 0, 0)
    elif decoded == 'w':
        glTranslatef(0, 0.2, 0)
    # rotate
    elif decoded == 'q':
        glRotatef(10, 0, 0, 1)
    elif decoded == 'e':
        glRotatef(10, 0, 0, -1)
    # scale
    elif decoded == 'r':
        glScalef(1.5, 1.5, 1.5)
    elif decoded == 'f':
        glScalef(0.5, 0.5, 0.5)


glutInit()
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(640, 640)
glutInitWindowPosition(10, 10)
glutCreateWindow("Pesho")

on_init()
glutReshapeFunc(reshape)
glutDisplayFunc(display)
glutIdleFunc(display)
glutKeyboardFunc(on_key_press)

glutMainLoop()