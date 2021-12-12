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
    self.isRet = False

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
  def draw(self, screen,font):
    #キャラ表示
    x = self.mx * 50 + 100
    y = self.my * 50 + 100
    if self.map[self.my][self.mx] == 5:
        self.mx, self.my = sub(self.mx, self.my)
    elif self.map[self.my][self.mx] == 4:
        self.mx, self.my = missionClear()
    screen.blit(self.gMAN ,(x, y)) 
    text1 = font.render("HP:"+str(self.hp), True, (0,0,255)) 
    screen.blit(text1, (140,400))

  def drawFromSub(self, screen, font):
    #キャラ表示
    x = self.mx * 50 + 100
    y = self.my * 50 + 100
    if self.map[self.my][self.mx] == 5:
        self.isRet = True
    screen.blit(self.gMAN ,(x, y)) 
    text1 = font.render("HP:"+str(self.hp), True, (0,0,255)) 
    screen.blit(text1, (140,400))


class Monster():
  def __init__(self, x, y, hp, map):
    self.gALIEN  = pygame.image.load("img/alien2.png").convert_alpha()     
    self.mx = x
    self.my = y
    self.hp = hp
    self.ct = 0
    self.map = map
    if random.randint(1,3)==1:
      self.isCovid = True
    else:
      self.isCovid = False

  # def update2(self,P,Ms):#行ける所にだけいくやりかた
  #   self.ct += 1
  #   if self.ct % 100 !=0:
  #     return
  #   r = random.randint(1, 4)
  #   if r == 1:
  #     if self.mx < len(self.map[0])-1 and(self.map[self.my][self.mx+1] == 0 or self.map[self.my][self.mx+1] == 1):
  #       self.mx += 1
  #   elif r == 2:
  #     if self.mx >= 1    and(self.map[self.my][self.mx-1] == 0 or self.map[self.my][self.mx-1] == 1):
  #       self.mx -= 1
  #   elif r == 3:
  #     if self.my < len(self.map)-1 and(self.map[self.my+1][self.mx] == 0 or self.map[self.my+1][self.mx] == 1):
  #       self.my += 1
  #   elif r == 4:
  #     if self.my >= 1    and(self.map[self.my-1][self.mx] == 0 or self.map[self.my-1][self.mx] == 1):
  #       self.my -= 1
  #   #covidの処理
  #   if self.isCovid:
  #     if P.mx==self.mx and P.my==self.my :
  #       P.hp -= 30
  #     for M in Ms:
  #       if M.mx==self.mx and M.my==self.my:
  #         M.isCovid=True

  def update(self,P,Ms):#行けない場所がある場合（はみ出し、海、山） 戻す 
    oldx, oldy = self.mx, self.my
    self.ct += 1
    if self.ct % 100 !=0:
      return
    r = random.randint(1, 4)
    if r == 1:
        self.mx += 1
    elif r == 2:
        self.mx -= 1
    elif r == 3:
        self.my += 1
    elif r == 4:
        self.my -= 1
    #行けない場所がある場合（はみ出し、海、山） 戻す 
    if (self.mx >= len(self.map[0]) or self.mx <0 or self.my <0 or self.my >= len(self.map)) or \
    self.map[self.my][self.mx]==2 or self.map[self.my][self.mx]==3:#戻す
        self.mx, self.my = oldx, oldy 
    #covidの処理
    if self.isCovid:
      if P.mx==self.mx and P.my==self.my :
        P.hp -= 50
        if P.hp<0:
          youLoose()
      for M in Ms:
        if M.mx==self.mx and M.my==self.my:
          M.isCovid=True

  def draw(self, screen):
    x = self.mx*50+100
    y = self.my*50+100
    screen.blit(self.gALIEN ,(x,y)) 
    if self.isCovid:
      pygame.draw.circle(screen,(210,0,0),(x+20,y+20),5) 

class Back():
  def __init__(self, map):
    self.gNO  = pygame.image.load("img/green.png").convert_alpha()     #野　50x50 0
    self.gBUSH = pygame.image.load("img/green2.png").convert_alpha()    #森　50x50 1
    self.gUMI = pygame.image.load("img/sea.png").convert_alpha()       #海　50x50 2
    self.gYAMA = pygame.image.load("img/mount.png").convert_alpha()    #山　50x50 3
    self.gSHIRO = pygame.image.load("img/siro.png").convert_alpha()    
    self.gMURA = pygame.image.load("img/village.png").convert_alpha()  
    self.map = map

  def update(self):
    pass
  def draw(self, screen):
    #マップ表示
    py = 100        
    for mgyo in self.map:#１行分描画
        px = 100
        for a1 in mgyo:#１マス分描画
            if a1 == 0:
              screen.blit(self.gNO ,(px,py)) 
            elif a1 == 1:
              screen.blit(self.gBUSH ,(px,py)) 
            elif a1 == 2:
              screen.blit(self.gUMI ,(px,py)) 
            elif a1 == 3:
              screen.blit(self.gYAMA ,(px,py)) 
            elif a1 == 4:
              screen.blit(self.gSHIRO ,(px,py)) 
            elif a1 == 5:
              screen.blit(self.gMURA ,(px,py)) 
            px += 50
        py += 50


def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    font1 = pygame.font.SysFont("hg明朝bhgp明朝bhgs明朝b", 35)#◆  
    map = [
      [1,1,0,0,3,3,1,1,0,0,3,3],
      [2,2,2,1,1,1,1,1,0,3,0,0],
      [1,3,5,1,1,2,1,1,3,3,0,3],
      [1,1,0,0,3,3,1,1,0,0,4,3],
      [1,1,0,0,3,3,1,5,0,0,2,2],
    ]
    numAliens=5
    B1 = Back(map)
    P1 = Player(0, 0, 100, B1.map)
    Ms=[]
    for i in range(numAliens):
      Ms.append(Monster(random.randint(0,11), random.randint(0,4), random.randint(30,120), B1.map))

    while True:
        screen.fill((255,255,255))                                    # 背景を白
        B1.draw(screen)
        #プレイヤー
        P1.update()
        P1.draw(screen,font1)
        #モンスター
        for i in range(numAliens):
          Ms[i].update(P1,Ms)
          Ms[i].draw(screen)
        pygame.display.update()                                       # 画面更新
        print("P1.hp=",P1.hp)
#--------------パラレルワールド
def sub(mmsx,mmsy):
    #pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    font1 = pygame.font.SysFont("hg明朝bhgp明朝bhgs明朝b", 35)#◆  
    map2=[
      [0,0,0,0,0,0,1,1,0,0,0,0],
      [0,0,0,0,0,1,1,1,0,0,0,0],
      [1,0,0,1,1,0,1,1,0,0,0,0],
      [1,1,0,0,0,0,1,1,0,0,0,0],
      [1,1,0,0,0,0,0,0,0,0,0,5],
    ]
    B2 = Back(map2)    
    P2 = Player(0, 0, 100, B2.map)
    while True:
        screen.fill((255,255,255))                                    # 背景を白
        B2.draw(screen)
        P2.update()
        P2.drawFromSub(screen,font1)
        if P2.isRet:
          return mmsx+1,mmsy  # ◆戻る
        pygame.display.update()                                       # 画面更新


#--------------パラレルワールド
def missionClear():
    font1 = pygame.font.SysFont("hg明朝bhgp明朝bhgs明朝b", 35)#◆  
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    while True:
        screen.fill((255,255,255))                                    # 背景を白
        text1 = font1.render("ミンションコンプリート！！ ", True, (0,0,255)) 
        screen.blit(text1, (140,230))
        pygame.display.update()                                       # 画面更新
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら終了
                pygame.quit()             # Pygameの終了(ないと終われない)
                sys.exit()  


#--------------パラレルワールド
def youLoose():
    font1 = pygame.font.SysFont("hg明朝bhgp明朝bhgs明朝b", 35)#◆  
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    while True:
        screen.fill((255,255,255))                                    # 背景を白
        text1 = font1.render("あなたの負けです！ ", True, (0,0,255)) 
        screen.blit(text1, (140,230))
        pygame.display.update()                                       # 画面更新
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら終了
                pygame.quit()             # Pygameの終了(ないと終われない)
                sys.exit()  

#=========================================
if __name__ == "__main__":
    main()