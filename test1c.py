import pygame
from pygame.locals import *
import sys
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    gBUSH= pygame.image.load("img/green2.png").convert_alpha()    #森　50x50 1

    px=120
    py=100
    while True:
        screen.fill((255,255,255))                                    # 背景を白
        for i in range(4):
            screen.blit(gBUSH ,(i*50+200,300)) 
        pygame.display.update()                                       # 画面更新

        # イベント処理
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら終了
                pygame.quit()             # Pygameの終了(ないと終われない)
                sys.exit()                # 終了（ないとエラーで終了することになる）
if __name__ == "__main__":
    main()