import pygame

def create_button(image="/Users/dheemankumar/Desktop/FILE/audio ai/asd.png",button_width=50,button_height=50,position=(0,0)):
    button_image = pygame.image.load(image)  # Replace with your button image path
    button_image = pygame.transform.scale(button_image, (button_width, button_height))
    button_rect = button_image.get_rect(midtop=(position))
    return button_image,button_rect