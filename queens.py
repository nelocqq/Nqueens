from constraint import *
import pygame
import sys
import time

pygame.init()
tamanio=600
Blue=(0,100,255)
White = (255, 255, 255)



def searchSolutions(True):
    problem = Problem()
    print("cuantas reinas desea ubicar")
    size = input()
    cols = range(size)
    rows = range(size)
    vect = range(size)
    print vect
    start = time.time()
    problem.addVariables(cols, rows)
    for col1 in cols:
        for col2 in cols:
            if col1 < col2:
                problem.addConstraint(lambda row1, row2, col1=col1, col2=col2:
                                      abs(row1-row2) != abs(col1-col2) and
                                      row1 != row2, (col1, col2))
    solutions = problem.getSolution()
    end = time.time()
    time_elapsed = end - start
    time_in_miliseconds = time_elapsed * 1000
    pantalla=pygame.display.set_mode((tamanio,tamanio))
    Drawqueen(pantalla,size,vect)
    time.sleep(2)
    print ("LA SOLUCION ES:\n")
    for solution in solutions:
        vect[solution]=solutions[solution]
    print vect
    Drawqueen(pantalla,size,vect)
    pygame.display.flip()
    

    print 'tiempo de ejecucion:\t{} ms'.format(time_in_miliseconds)

def Drawqueen(pantalla,size,vect):
    escala = abs(tamanio/size)
    pantalla.fill(White)
    for Draw in range(size):
        pygame.draw.line(pantalla, Blue ,(0,escala*Draw),(tamanio,escala*Draw),2)
        pygame.draw.line(pantalla, Blue ,(escala*Draw,0),(escala*Draw,tamanio),2)
    for i,j in enumerate(vect):
        pygame.draw.circle(pantalla, Blue, (((i*escala)+(escala/2)), ((escala*j)+(escala/2))), escala/3, 0)
    pygame.display.flip()
    


searchSolutions(True)

    

