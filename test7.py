import pygame
from pygame.locals import *
import sys
import random

class Player():
  def __init__(self, x, y, hp, map):
    self.gMAN  = pygame.image.load("img/man1.png").convert_alpha()     
    self.mx = x
    self.my = y
    self.hp = hp
    self.ct = 0
    self.map = map

  def update(self):
    for event in pygame.event.get():  # イベントを取得
        if event.type == QUIT:        # 閉じるボタンが押されたら終了
            pygame.quit()             # Pygameの終了(ないと終われない)
            sys.exit()                # 終了（ないとエラーで終了することになる）
        elif event.type == KEYDOWN :
            oldx = self.mx#一時退避
            oldy = self.my
            if event.key == K_UP :
                self.my -= 1
            elif event.key == K_DOWN:
                self.my += 1
            elif event.key == K_RIGHT:
                self.mx += 1
            elif event.key == K_LEFT:
                self.mx -= 1
            #行けない場所がある場合（はみ出し、海、山） 戻す 
            if (self.mx >= len(self.map[0]) or self.mx <0 or self.my <0 or self.my >= len(self.map)) or \
            self.map[self.my][self.mx]==2 or self.map[self.my][self.mx]==3:#戻す
                self.mx = oldx
                self.my = oldy 
  def draw(self, screen):
    #キャラ表示
    x = self.mx * 50 + 100
    y = self.my * 50 + 100
    if self.map[self.my][self.mx] == 5:
        self.mx, self.my = sub(self.mx, self.my)
    screen.blit(self.gMAN ,(x, y)) 

class Monster():
  def __init__(self, x, y, hp, map):
    self.gALIEN  = pygame.image.load("img/alien2.png").convert_alpha()     
    self.mx = x
    self.my = y
    self.hp = hp
    self.ct = 0
    self.map = map
  def update(self):
    self.ct += 1
    if self.ct % 100 !=0:
      return
    r = random.randint(1, 4)
    if r == 1:
      if self.mx < len(self.map[0])-1 and(self.map[self.my][self.mx+1] == 0 or self.map[self.my][self.mx+1] == 1):
        self.mx += 1
    elif r == 2:
      if self.mx >= 1    and(self.map[self.my][self.mx-1] == 0 or self.map[self.my][self.mx-1] == 1):
        self.mx -= 1
    elif r == 3:
      if self.my < len(self.map)-1 and(self.map[self.my+1][self.mx] == 0 or self.map[self.my+1][self.mx] == 1):
        self.my += 1
    elif r == 4:
      if self.my >= 1    and(self.map[self.my-1][self.mx] == 0 or self.map[self.my-1][self.mx] == 1):
        self.my -= 1
  def draw(self, screen):
    x=self.mx*50+100
    y=self.my*50+100
    screen.blit(self.gALIEN ,(x,y)) 

def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    gNO  = pygame.image.load("img/green.png").convert_alpha()     #野　50x50 0
    gBUSH= pygame.image.load("img/green2.png").convert_alpha()    #森　50x50 1
    gUMI = pygame.image.load("img/sea.png").convert_alpha()       #海　50x50 2
    gYAMA = pygame.image.load("img/mount.png").convert_alpha()    #山　50x50 3
    gSHIRO = pygame.image.load("img/siro.png").convert_alpha()    
    gMURA = pygame.image.load("img/village.png").convert_alpha()  

    map=[[1,1,0,0,3,3,1,1,0,0,3,3],
         [2,2,2,1,1,1,1,1,0,3,0,0],
         [1,3,5,1,1,2,1,1,3,3,0,3],
         [1,1,0,0,3,3,1,1,0,0,4,3],
         [1,1,0,0,3,3,1,5,0,0,2,2],
        ]
    P1 = Player(0,0,100,map)
    M1 = Monster(3,4,100,map)

    while True:
        screen.fill((255,255,255))                                    # 背景を白
        py=100        
        #マップ表示
        for mgyo in map:#１行分描画
            px=100
            for a1 in mgyo:#１マス分描画
                if a1==0:
                  screen.blit(gNO ,(px,py)) 
                elif a1==1:
                  screen.blit(gBUSH ,(px,py)) 
                elif a1==2:
                  screen.blit(gUMI ,(px,py)) 
                elif a1==3:
                  screen.blit(gYAMA ,(px,py)) 
                elif a1==4:
                  screen.blit(gSHIRO ,(px,py)) 
                elif a1==5:
                  screen.blit(gMURA ,(px,py)) 
                px += 50
            py += 50
        #プレイヤー
        P1.update()
        P1.draw(screen)
        #モンスター
        M1.update()
        M1.draw(screen)

        pygame.display.update()                                       # 画面更新



def sub(mmsx,mmsy):
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面

    gMAN  = pygame.image.load("img/man1.png").convert_alpha()     
    gALIEN  = pygame.image.load("img/alien.png").convert_alpha()     

    gNO  = pygame.image.load("img/green.png").convert_alpha()     #野　50x50 0
    gBUSH= pygame.image.load("img/green2.png").convert_alpha()    #森　50x50 1
    gUMI = pygame.image.load("img/sea.png").convert_alpha()       #海　50x50 2
    gYAMA = pygame.image.load("img/mount.png").convert_alpha()    #山　50x50 3
    gSHIRO = pygame.image.load("img/siro.png").convert_alpha()    
    gMURA = pygame.image.load("img/village.png").convert_alpha()  

    map=[[0,0,0,0,0,0,1,1,0,0,0,0],
         [0,0,0,0,0,1,1,1,0,0,0,0],
         [1,0,0,1,1,0,1,1,0,0,0,0],
         [1,1,0,0,0,0,1,1,0,0,0,0],
         [1,1,0,0,0,0,0,0,0,0,0,5],
        ]
    mxgyou=len(map)
    mxretsu=len(map[0])

    msx=0
    msy=0

    while True:
        screen.fill((255,255,255))                                    # 背景を白
        py=100        

        #マップ表示
        for mgyo in map:#１行分描画
            px=100
            for a1 in mgyo:#１マス分描画
                if a1==0:
                  screen.blit(gNO ,(px,py)) 
                elif a1==1:
                  screen.blit(gBUSH ,(px,py)) 
                elif a1==2:
                  screen.blit(gUMI ,(px,py)) 
                elif a1==3:
                  screen.blit(gYAMA ,(px,py)) 
                elif a1==4:
                  screen.blit(gSHIRO ,(px,py)) 
                elif a1==5:
                  screen.blit(gMURA ,(px,py)) 
                px +=50
            py +=50

        #キャラ表示
        mx=msx*50+100
        my=msy*50+100
        if map[msy][msx] == 5:
          return mmsx+1,mmsy
        screen.blit(gMAN ,(mx,my)) 

        pygame.display.update()                                       # 画面更新

        # イベント処理
        isBreak = False
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら終了
                pygame.quit()             # Pygameの終了(ないと終われない)
                sys.exit()                # 終了（ないとエラーで終了することになる）
            elif event.type == KEYDOWN :
                oldx = msx
                oldy = msy
                if event.key == K_a :#終了
                    isBreak = True
                elif event.key == K_z :
                    isBreak = True
                elif event.key == K_UP :
                    msy -= 1
                elif event.key == K_DOWN:
                    msy += 1
                elif event.key == K_RIGHT:
                    msx += 1
                elif event.key == K_LEFT:
                    msx -= 1

                #行けない場所がある場合（はみ出し、海、山） 戻す 
                if (msx >= mxretsu or msx <0 or msy <0 or msy >=mxgyou) or map[msy][msx]==2 or map[msy][msx]==3:#戻す
                    msx = oldx
                    msy = oldy 
        if isBreak:
            break
    print("end")      

if __name__ == "__main__":
    main()