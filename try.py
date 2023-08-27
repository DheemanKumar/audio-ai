import pygame
import os

# Initialize pygame
pygame.init()

# Set up display
screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Audio Player")

# Load audio file
audio_file = "/Users/dheemankumar/Desktop/songs/128-Tera Fitoor - Genius 128 Kbps.mp3"  # Replace with your audio file path
pygame.mixer.music.load(audio_file)

# Load button images
play_button_image = pygame.image.load("/Users/dheemankumar/Desktop/FILE/audio ai/asd.png")  # Replace with your button image path
pause_button_image = pygame.image.load("/Users/dheemankumar/Desktop/FILE/audio ai/asd.png")  # Replace with your button image path
stop_button_image = pygame.image.load("/Users/dheemankumar/Desktop/FILE/audio ai/asd.png")  # Replace with your button image path

# Resize button images
button_width, button_height = 50, 50  # Set the button size
play_button_image = pygame.transform.scale(play_button_image, (button_width, button_height))
pause_button_image = pygame.transform.scale(pause_button_image, (button_width, button_height))
stop_button_image = pygame.transform.scale(stop_button_image, (button_width, button_height))

# Create button rectangles
play_button_rect = play_button_image.get_rect(midtop=(screen_width // 2 - button_width, screen_height - 60))
pause_button_rect = pause_button_image.get_rect(midtop=(screen_width // 2, screen_height - 60))
stop_button_rect = stop_button_image.get_rect(midtop=(screen_width // 2 + button_width, screen_height - 60))

# Font for title
font = pygame.font.Font(None, 36)

# Main loop
running = True
playing = False
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if play_button_rect.collidepoint(event.pos):
                if not playing:
                    if paused:
                        pygame.mixer.music.unpause()
                        paused = False
                    else:
                        pygame.mixer.music.play()
                    playing = True
            elif pause_button_rect.collidepoint(event.pos):
                if playing:
                    pygame.mixer.music.pause()
                    playing = False
                    paused = True
            elif stop_button_rect.collidepoint(event.pos):
                pygame.mixer.music.stop()
                playing = False
                paused = False

    screen.fill((255, 255, 255))
    
    # Draw title
    title_text = font.render("Audio Player", True, (0, 0, 0))
    title_rect = title_text.get_rect(midtop=(screen_width // 2, 20))
    screen.blit(title_text, title_rect)
    
    # Draw buttons
    screen.blit(play_button_image, play_button_rect)
    screen.blit(pause_button_image, pause_button_rect)
    screen.blit(stop_button_image, stop_button_rect)
    
    pygame.display.flip()

pygame.quit()
