import pygame, sys,os
from pygame.locals import *
import random
W=[255,255,255]
B=[0,200,255]
w=80
n=input()
s=w*n
FPS=60
a=[]
for i in range(1,n*n):
  a.append(i)
a.append(0)
DISPLAYSURF = pygame.display.set_mode((s, s), 0, 32)
def main():
  global DISPLAYSURF, fpsClock
  pygame.init()
  fpsClock=pygame.time.Clock()
  DISPLAYSURF = pygame.display.set_mode((s, s), 0, 32)
  pygame.display.set_caption('Slide')
  DISPLAYSURF.fill((200,200,200))
  pygame.display.update()
  shuffle()
  while True:
    display()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type==KEYDOWN:
              if event.key==K_UP:
                 game(0)
              elif event.key==K_DOWN:
                 game(1)
              elif event.key==K_RIGHT:
                 game(2)
              elif event.key==K_LEFT:
                 game(3)
                 
              
    
    fpsClock.tick(FPS)
        
   
    

def display():
  global DISPLAYSURF, fpsClock
  font = pygame.font.SysFont("calibri",40)
  DISPLAYSURF.fill((200,200,200))
  for j in range(n+1):
      for k in range(n):
          pygame.draw.rect(DISPLAYSURF, B, (j*w,k*w, 0,w))
          pygame.draw.rect(DISPLAYSURF, B, (j*w, k*w, w,0))
  for j in range(n):
     for k in range(n):
         if a[k*n+j]!=0:
             pygame.draw.rect(DISPLAYSURF, W, (j*w+10,k*w+10, w-20,w-20))
             score1 = font.render(str(a[k*n+j]), True,(0,255,255))
             DISPLAYSURF.blit(score1,(j*w+30,k*w+30))
         if a[k*n+j]==0:
             pygame.draw.rect(DISPLAYSURF, B, (j*w,k*w, w,w))

  
  pygame.display.update()
  
def game(s):
  z=[0,0]
  for i in range(n):
    for j in range(n):
      if a[i*n+j]==0:
        z=[i,j]
  i=z[0]
  j=z[1]
  if s==0 and z[0]+1<n:
     a[i*n+j]=a[(i+1)*n+j]
     a[(i+1)*n+j]=0
  elif s==1 and z[0]-1>=0:
     a[i*n+j]=a[(i-1)*n+j]
     a[(i-1)*n+j]=0
  elif s==3 and z[1]+1<n:
     a[i*n+j]=a[i*n+j+1]
     a[i*n+j+1]=0
  elif s==2 and z[1]-1>=0:
     a[i*n+j]=a[i*n+j-1]
     a[i*n+j-1]=0
    
  
def shuffle():
  for i in range(n*100):
    r=random.randint(0,1000)
    game(r%4)
  
if __name__ == '__main__':
    main()
