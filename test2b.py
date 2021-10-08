import pygame
from pygame.locals import *
import sys
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面

    gNO  = pygame.image.load("img/green.png")     #野　50x50 0
    gBUSH= pygame.image.load("img/green2.png")    #森　50x50 1
    gUMI = pygame.image.load("img/sea.png")       #海　50x50 2
    gYAMA = pygame.image.load("img/mount.png")    #山　50x50 3
    map=[[1,1,0,0,3,3],
        [2,2,2,2,1,1],
        [1,1,3,3,1,1]]

    while True:
        screen.fill((255,255,255))                                    # 背景を白
        #マップ表示
        for gy in range(3):
          for rt in range(6):
            if map[gy][rt]==0:
              screen.blit(gNO ,(rt*50+200,gy*50+100)) 
            elif map[gy][rt]==1:
              screen.blit(gBUSH ,(rt*50+200,gy*50+100)) 
            elif map[gy][rt]==2:
              screen.blit(gUMI ,(rt*50+200,gy*50+100)) 
            elif map[gy][rt]==3:
              screen.blit(gYAMA ,(rt*50+200,gy*50+100)) 
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