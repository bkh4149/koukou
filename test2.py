import pygame
from pygame.locals import *
import sys
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面

    msgothic = r'c:\windows\fonts\msgothic.ttc'
    font1 = pygame.font.Font(msgothic, 72)
    font2 = pygame.font.Font(msgothic, 24)

    gNO  = pygame.image.load("img/green.png").convert_alpha()     #野　50x50 0
    gBUSH= pygame.image.load("img/green2.png").convert_alpha()    #森　50x50 1
    gUMI = pygame.image.load("img/sea.png").convert_alpha()       #海　50x50 2
    gYAMA = pygame.image.load("img/mount.png").convert_alpha()    #山　50x50 3
    ar=[[1,1,0,0,3,3],
        [2,2,2,2,1,1],
        [1,1,3,3,1,1]]

    while True:
        screen.fill((255,255,255))                                    # 背景を白
        screen.blit(gNO ,(50,50)) 
        py=100        
        print("===============")
        for a2 in ar:
          px=120
          for a1 in a2:
            print(a1,px,py)
            if a1==0:
              screen.blit(gNO ,(px,py)) 
            elif a1==1:
              screen.blit(gBUSH ,(px,py)) 
            elif a1==2:
              screen.blit(gUMI ,(px,py)) 
            elif a1==3:
              screen.blit(gYAMA ,(px,py)) 
            px +=50
          py +=50
        pygame.display.update()                                       # 画面更新

        # イベント処理
        isBreak = False
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら終了
                pygame.quit()             # Pygameの終了(ないと終われない)
                sys.exit()                # 終了（ないとエラーで終了することになる）
            elif event.type == KEYDOWN :
                if event.key == K_a :
                    isBreak = True
                elif event.key == K_z :
                    isBreak = True
        if isBreak:
          break
    print("end")      

if __name__ == "__main__":
    main()