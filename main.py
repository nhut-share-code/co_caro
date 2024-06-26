import subprocess
import pygame
import sys

# Khởi tạo Pygame
pygame.init()

# Màu sắc
BG_COLOR = (255, 255, 255)
BUTTON_COLOR = (0, 128, 0)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Font chữ
font = pygame.font.Font('font/arial.ttf', 24)

# Màn hình
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Cờ caro")

# Hàm để vẽ nút "Chơi với bạn"
def draw_play_with_friend_button():
    button_rect = pygame.Rect(200, 150, 200, 80)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    text_surface = font.render("Chơi với bạn", True, BUTTON_TEXT_COLOR)
    screen.blit(text_surface, (button_rect.centerx - text_surface.get_width() // 2, button_rect.centery - text_surface.get_height() // 2))
    return button_rect

# Hàm để vẽ nút "Chơi với bot"
def draw_play_with_bot_button():
    button_rect = pygame.Rect(200, 250, 200, 80)
    pygame.draw.rect(screen, BUTTON_COLOR, button_rect)
    text_surface = font.render("Chơi với bot", True, BUTTON_TEXT_COLOR)
    screen.blit(text_surface, (button_rect.centerx - text_surface.get_width() // 2, button_rect.centery - text_surface.get_height() // 2))
    return button_rect

# Hàm để kiểm tra xem chuột có được nhấn vào nút không
def check_button_click(pos, button_rect):
    return button_rect.collidepoint(pos)

# Vòng lặp trò chơi
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            play_with_friend_button_rect = draw_play_with_friend_button()
            play_with_bot_button_rect = draw_play_with_bot_button()
            
            if check_button_click(event.pos, play_with_friend_button_rect):
                running = False
                subprocess.run(["python", "1vs1/game.py"])  # Chạy trò chơi với người bạn
                
            elif check_button_click(event.pos, play_with_bot_button_rect):
                running = False
                subprocess.run(["python", "1vsmay/bot.py"])   # Chạy trò chơi với bot

    screen.fill(BG_COLOR)
    draw_play_with_friend_button()
    draw_play_with_bot_button()
    pygame.display.flip()

pygame.quit()
sys.exit()
