import pygame
from pygame.locals import *
import sys
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面

    gMAN  = pygame.image.load("img/man1.png").convert_alpha()     #野　50x50 0
    gNO  = pygame.image.load("img/green.png").convert_alpha()     #野　50x50 0
    gBUSH= pygame.image.load("img/green2.png").convert_alpha()    #森　50x50 1
    gUMI = pygame.image.load("img/sea.png").convert_alpha()       #海　50x50 2
    gYAMA = pygame.image.load("img/mount.png").convert_alpha()    #山　50x50 3

    map=[[1,1,0,0,3,3],
        [2,2,2,1,1,1],
        [1,3,3,1,1,2]]

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
                px +=50
            py +=50

        #キャラ表示
        mx=msx*50+100
        my=msy*50+100
        screen.blit(gMAN ,(mx,my)) 

        pygame.display.update()                                       # 画面更新

        # イベント処理
        isBreak = False
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら終了
                pygame.quit()             # Pygameの終了(ないと終われない)
                sys.exit()                # 終了（ないとエラーで終了することになる）
            elif event.type == KEYDOWN :
                ox = msx
                oy = msy
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
                if (msx > 5 or msx <0 or msy <0 or msy >2) or map[msy][msx]==2 or map[msy][msx]==3:#戻す
                    msx = ox
                    msy = oy 
        if isBreak:
            break
    print("end")      

if __name__ == "__main__":
    main()