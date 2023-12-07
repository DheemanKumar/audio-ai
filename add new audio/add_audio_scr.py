import pygame
import os
import AddNewAudio

audio_index=0

data=[]

path = os.path.dirname(os.path.abspath(__file__))
os.chdir(path)



audio_files=[]

parent_folder = path
child_folder = 'audio'

# Create the full path to the child folder
child_folder_path = os.path.join(parent_folder, child_folder)
noise_sound=os.path.join(child_folder_path,"noise.mp3")
language_file_path=[
    os.path.join(child_folder_path,"female english.mp3"),
    os.path.join(child_folder_path,"male english.mp3"),
    os.path.join(child_folder_path,"female hindi.mp3"),
    os.path.join(child_folder_path,"male hindi.mp3"),
    os.path.join(child_folder_path,"female punjabi.mp3"),
    os.path.join(child_folder_path,"male punjabi.mp3"),
    os.path.join(child_folder_path,"female bengali.mp3"),
    os.path.join(child_folder_path,"male bengali.mp3")
]



# Check if the child folder exists
if os.path.exists(child_folder_path) and os.path.isdir(child_folder_path):
    for i in language_file_path:
        if os.path.exists(i):
            pass
        else:
            print(f"The child folder '{i}' does not exist.")
            exit()
else:
    print(f"The child folder '{child_folder}' does not exist.")
    exit()

os.chdir(path)


# Initialize pygame
pygame.init()

# Set up display
screen_width, screen_height = 600, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Add new Audio")

# Font for buttons and title
font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 36)

# Create button rectangles and labels
save_button_rect = pygame.Rect(screen_width // 2 - 225, screen_height - 175, 50, 30)
play_button_rect = pygame.Rect(screen_width // 2 -125, screen_height - 175, 50, 30)
confirm_button_rect = pygame.Rect(screen_width // 2 -25, screen_height - 175, 50, 30)

male_button_rect = pygame.Rect(screen_width // 2 , screen_height - 100, 80, 30)
female_button_rect = pygame.Rect(screen_width // 2 , screen_height - 50, 80, 30)

english_button_rect = pygame.Rect(screen_width // 2 -250, screen_height - 100, 80, 30)
hindi_button_rect = pygame.Rect(screen_width // 2 -250, screen_height - 50, 80, 30)
punjabi_button_rect = pygame.Rect(screen_width // 2 -150, screen_height - 100, 80, 30)
bangoli_button_rect = pygame.Rect(screen_width // 2 -150, screen_height - 50, 80, 30)

noise_button_rect = pygame.Rect(screen_width // 2 +150, screen_height - 75, 80, 30)








# Main loop
running = True
playing = False
change=True
check=False

noise=2
gender=0
language=0


def audio_select():
    audio_file=noise_sound
    if gender==1:
        if language==1:
            audio_file=language_file_path[1]
        elif language==2:
            audio_file=language_file_path[3]
        elif language==3:
            audio_file=language_file_path[5]
        elif language==4:
            audio_file=language_file_path[7]
    elif gender==2:
        if language==1:
            audio_file=language_file_path[0]
        elif language==2:
            audio_file=language_file_path[2]
        elif language==3:
            audio_file=language_file_path[4]
        elif language==4:
            audio_file=language_file_path[6]

    pygame.mixer.music.load(audio_file)

def is_audio_playing():
    return pygame.mixer.music.get_busy()


def play_playsample():
    sample_audio=AddNewAudio.get_sample()
    pygame.mixer.music.load(sample_audio)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if (is_audio_playing()):
                playing=True
            else:
                playing=False

            if save_button_rect.collidepoint(event.pos):
                change=True
                check=True
                if not playing:
                    audio_select()
                    pygame.mixer.music.play()

            elif play_button_rect.collidepoint(event.pos):
                if(check):
                    change=True
                    play_playsample()
                    pygame.mixer.music.play()

                    
            
            elif confirm_button_rect.collidepoint(event.pos):
                if(check):
                    change=True
                    AddNewAudio.execute(noise,gender,language)
                    exit()
            
            elif male_button_rect.collidepoint(event.pos) and noise==1 :
                change=True
                check=False
                gender=1
                pygame.mixer.music.stop()
            elif female_button_rect.collidepoint(event.pos) and noise==1 :
                change=True
                check=False
                gender=2
                pygame.mixer.music.stop()
            elif english_button_rect.collidepoint(event.pos) and noise==1:
                change=True
                check=False
                language=1
                pygame.mixer.music.stop()
            elif hindi_button_rect.collidepoint(event.pos) and noise==1 :
                change=True
                check=False
                language=2
                pygame.mixer.music.stop()
            elif punjabi_button_rect.collidepoint(event.pos) and noise==1 :
                change=True
                check=False
                language=3
                pygame.mixer.music.stop()
            elif bangoli_button_rect.collidepoint(event.pos) and noise==1 :
                change=True
                check=False
                language=4
                pygame.mixer.music.stop()

            elif noise_button_rect.collidepoint(event.pos):
                change=True
                pygame.mixer.music.stop()
                if (noise==1):
                    noise=2
                    language=0
                    gender=0
                else:
                    noise=1
            

            
                


            
    if(change):
        
        screen.fill((255, 255, 255))
        # Draw title
        title_text = title_font.render("Add new Audio", True, (0, 0, 0))
        title_rect = title_text.get_rect(midtop=(screen_width // 2, 20))
        screen.blit(title_text, title_rect)

    
        
        pygame.draw.rect(screen, (200, 200, 200), save_button_rect)

        if(check):
            pygame.draw.rect(screen, (200, 200, 200), play_button_rect)
        else:
            pygame.draw.rect(screen, (100, 100, 100), play_button_rect)

        if(check):
            pygame.draw.rect(screen, (200, 200, 200), confirm_button_rect)
        else:
            pygame.draw.rect(screen, (100, 100, 100), confirm_button_rect)


        #print(type(data))

        if(gender==1) :
            pygame.draw.rect(screen, (0, 255, 0), male_button_rect)
        else :
            pygame.draw.rect(screen, (200, 200, 200), male_button_rect)

        if(gender==2) :
            pygame.draw.rect(screen, (0, 255, 0), female_button_rect)
        else :    
            pygame.draw.rect(screen, (200, 200, 200), female_button_rect)

        if(language==1) :
            pygame.draw.rect(screen, (0, 255, 0), english_button_rect)
        else :
            pygame.draw.rect(screen, (200, 200, 200), english_button_rect)

        if(language==2) :
            pygame.draw.rect(screen, (0, 255, 0), hindi_button_rect)
        else :    
            pygame.draw.rect(screen, (200, 200, 200), hindi_button_rect)

        if(language==3) :
            pygame.draw.rect(screen, (0, 255, 0), punjabi_button_rect)
        else :
            pygame.draw.rect(screen, (200, 200, 200), punjabi_button_rect)

        if(language==4) :
            pygame.draw.rect(screen, (0, 255, 0), bangoli_button_rect)
        else :    
            pygame.draw.rect(screen, (200, 200, 200), bangoli_button_rect)

        if(noise==2):
            pygame.draw.rect(screen, (0,255, 0), noise_button_rect)
        else :
            pygame.draw.rect(screen, (255, 0,0), noise_button_rect)

        



        save_text = font.render("Save", True, (0, 0, 0))
        play_text = font.render("Play", True, (0, 0, 0))
        confirm_text = font.render("Confirm", True, (0, 0, 0))
        male_text = font.render("Male", True, (0, 0, 0))
        female_text = font.render("Female", True, (0, 0, 0))
        english_text = font.render("English", True, (0, 0, 0))
        hindi_text = font.render("Hindi", True, (0, 0, 0))
        punjabi_text = font.render("Punjabi", True, (0, 0, 0))
        bangoli_text = font.render("Bangoli", True, (0, 0, 0))
        noise_text = font.render("Noise", True, (0, 0, 0))
    



        screen.blit(save_text, save_button_rect.topleft)
        screen.blit(play_text, play_button_rect.topleft)
        screen.blit(confirm_text, confirm_button_rect.topleft)
        screen.blit(male_text, male_button_rect.topleft)
        screen.blit(female_text, female_button_rect.topleft)
        screen.blit(english_text, english_button_rect.topleft)
        screen.blit(hindi_text, hindi_button_rect.topleft)
        screen.blit(punjabi_text, punjabi_button_rect.topleft)
        screen.blit(bangoli_text, bangoli_button_rect.topleft)
        screen.blit(noise_text, noise_button_rect.topleft)

    
        pygame.display.flip()

        change=False

pygame.quit()

#print(noise,gender,language)
#You have selected female english voice. Do you want to save it. A sample of provided audio is listed below.