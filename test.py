import pygame
from pygame.locals import *
import sys
def main():
    pygame.init()                                 # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面

    px=120
    py=100
    while True:
        screen.fill((255,255,255))                                    # 背景を白
        pygame.draw.circle(screen,(10,10,10),(px,py),50)              # ●
        pygame.draw.rect(screen, (255,0,0), Rect(10,100,50,50), 1)    # ■
        pygame.draw.line(screen, (0,255,0), (0,200), (100,300), 2)    # 線
        pygame.display.update()                                       # 画面更新

        # イベント処理
        for event in pygame.event.get():  # イベントを取得
            if event.type == QUIT:        # 閉じるボタンが押されたら終了
                pygame.quit()             # Pygameの終了(ないと終われない)
                sys.exit()                # 終了（ないとエラーで終了することになる）
if __name__ == "__main__":
    main()