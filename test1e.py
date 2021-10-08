import pygame
from pygame.locals import *
import sys
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    gBUSH= pygame.image.load("img/green2.png").convert_alpha()    #森　50x50 1
    gUMI = pygame.image.load("img/sea.png").convert_alpha()       #海　50x50 2
    gYAMA = pygame.image.load("img/mount.png").convert_alpha()    #山　50x50 3

    map=[1,2,2,3,1,1]

    while True:
        screen.fill((255,255,255))                                    # 背景を白
        for i in range(6):
            if map[i]==1:
                screen.blit(gBUSH ,(i*50+200,300))
            elif map[i]==2:
                screen.blit(gUMI ,(i*50+200,300))
            elif map[i]==3:
                screen.blit(gYAMA ,(i*50+200,300))
        pygame.display.update()                                       # 画面更新

        # イベント処理
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら終了
                pygame.quit()             # Pygameの終了(ないと終われない)
                sys.exit()                # 終了（ないとエラーで終了することになる）
if __name__ == "__main__":
    main()