import pygame
import os
import functions as fn

audio_index=0

data=[]

# Initialize pygame
pygame.init()

# Set up display
screen_width, screen_height = 400, 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Audio Player")




# Font for buttons and title
font = pygame.font.Font(None, 24)
title_font = pygame.font.Font(None, 36)

# Create button rectangles and labels
play_button_rect = pygame.Rect(screen_width // 2 - 125, screen_height - 220, 50, 30)
pause_button_rect = pygame.Rect(screen_width // 2 -25, screen_height - 220, 50, 30)
stop_button_rect = pygame.Rect(screen_width // 2 +75, screen_height - 220, 50, 30)



male_button_rect = pygame.Rect(screen_width // 2 , screen_height - 100, 80, 30)
female_button_rect = pygame.Rect(screen_width // 2 , screen_height - 50, 80, 30)


english_button_rect = pygame.Rect(screen_width // 2 -180, screen_height - 100, 80, 30)
hindi_button_rect = pygame.Rect(screen_width // 2 -180, screen_height - 50, 80, 30)
punjabi_button_rect = pygame.Rect(screen_width // 2 -90, screen_height - 100, 80, 30)
bangoli_button_rect = pygame.Rect(screen_width // 2 -90, screen_height - 50, 80, 30)

# happy_button_rect = pygame.Rect(screen_width // 2 +60, screen_height - 100, 80, 30)
# sad_button_rect = pygame.Rect(screen_width // 2 +60, screen_height - 50, 80, 30)


noise_button_rect = pygame.Rect(screen_width // 2 +90, screen_height - 75, 80, 30)

previous_button_rect = pygame.Rect(20, 120, 30, 30)
next_button_rect = pygame.Rect(screen_width -40, 120, 30, 30)
empty_button_rect = pygame.Rect(screen_width // 2 +75, screen_height - 180, 100, 30)



def move_audio(index):
    new_data=fn.getdata(index)
    audio_file =os.path.join(os.getcwd(),"3sec_audio", new_data["name"]  )# Replace with your audio file path
    pygame.mixer.music.load(audio_file)
    return new_data

data=move_audio(audio_index)


# Load audio file



# Main loop
running = True
playing = False
paused = False

#print(data)

#data={"name":"","male":0,"female":0,"happy":0,"sad":0,"noise":0}


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
            elif male_button_rect.collidepoint(event.pos) and data["noise"]==0 :
                data["male"]=1
                if (data["female"]==1):
                    data["female"]=0
            elif female_button_rect.collidepoint(event.pos) and data["noise"]==0:
                data["female"]=1
                if (data["male"]==1):
                    data["male"]=0
            elif english_button_rect.collidepoint(event.pos) and data["noise"]==0 :
                data["english"]=1
                if (data["hindi"]==1):
                    data["hindi"]=0
                if (data["punjabi"]==1):
                    data["punjabi"]=0
                if (data["bangoli"]==1):
                    data["bangoli"]=0
            elif hindi_button_rect.collidepoint(event.pos) and data["noise"]==0 :
                data["hindi"]=1
                if (data["punjabi"]==1):
                    data["punjabi"]=0
                if (data["bangoli"]==1):
                    data["bangoli"]=0
                if (data["english"]==1):
                    data["english"]=0
            elif punjabi_button_rect.collidepoint(event.pos) and data["noise"]==0 :
                data["punjabi"]=1
                if (data["hindi"]==1):
                    data["hindi"]=0
                if (data["bangoli"]==1):
                    data["bangoli"]=0
                if (data["english"]==1):
                    data["english"]=0
            elif bangoli_button_rect.collidepoint(event.pos) and data["noise"]==0 :
                data["bangoli"]=1
                if (data["hindi"]==1):
                    data["hindi"]=0
                if (data["punjabi"]==1):
                    data["punjabi"]=0
                if (data["english"]==1):
                    data["english"]=0

            elif noise_button_rect.collidepoint(event.pos):
                if (data["noise"]==0):
                    data["noise"]=1
                    data["english"]=0
                    data['female']=0
                    data["male"]=0
                    data["hindi"]=0
                    data["punjabi"]=0
                    data["bangoli"]=0
                else:
                    data["noise"]=0 
            
            elif next_button_rect.collidepoint(event.pos):
                fn.updatedata(audio_index,data)
                audio_index=audio_index+1
                try:
                    data=move_audio(audio_index)
                except:
                    audio_index=audio_index-1
                    break

            elif previous_button_rect.collidepoint(event.pos):
                fn.updatedata(audio_index,data)
                audio_index=audio_index-1
                if(audio_index>=0):
                    data=move_audio(audio_index)
                else:
                    audio_index=audio_index+1
            
            elif empty_button_rect.collidepoint(event.pos):
                fn.updatedata(audio_index,data)
                while True:
                    audio_index=audio_index+1
                    try:
                        data=move_audio(audio_index)
                    except:
                        audio_index=audio_index-1
                        break
                    if (data["noise"]==0):
                        if((data["female"]==0 and data["male"]==0) or (data["english"]==0 and data["hindi"]==0) and (data["punjabi"]==0 and data["bangoli"]==0)):
                            break
                    
                


            

    screen.fill((255, 255, 255))
    
    # Draw title
    title_text = title_font.render("Audio Player", True, (0, 0, 0))
    title_rect = title_text.get_rect(midtop=(screen_width // 2, 20))
    screen.blit(title_text, title_rect)

    # Draw title
    name_text = title_font.render(data["name"], True, (0, 0, 0))
    name_rect = name_text.get_rect(midtop=(screen_width // 2, 100))
    screen.blit(name_text, name_rect)
    
    # Draw buttons with labels
    if pygame.mixer.music.get_busy():
        pygame.draw.rect(screen, (0, 255, 0), play_button_rect)
    else:
        pygame.draw.rect(screen, (200, 200, 200), play_button_rect)

    pygame.draw.rect(screen, (200, 200, 200), pause_button_rect)
    pygame.draw.rect(screen, (200, 200, 200), stop_button_rect)

    #print(type(data))

    if(data["male"]) :
        pygame.draw.rect(screen, (0, 255, 0), male_button_rect)
    else :
        pygame.draw.rect(screen, (200, 200, 200), male_button_rect)

    if(data["female"]) :
        pygame.draw.rect(screen, (0, 255, 0), female_button_rect)
    else :    
        pygame.draw.rect(screen, (200, 200, 200), female_button_rect)

    if(data["english"]) :
        pygame.draw.rect(screen, (0, 255, 0), english_button_rect)
    else :
        pygame.draw.rect(screen, (200, 200, 200), english_button_rect)

    if(data["hindi"]) :
        pygame.draw.rect(screen, (0, 255, 0), hindi_button_rect)
    else :    
        pygame.draw.rect(screen, (200, 200, 200), hindi_button_rect)

    if(data["punjabi"]) :
        pygame.draw.rect(screen, (0, 255, 0), punjabi_button_rect)
    else :
        pygame.draw.rect(screen, (200, 200, 200), punjabi_button_rect)

    if(data["bangoli"]) :
        pygame.draw.rect(screen, (0, 255, 0), bangoli_button_rect)
    else :    
        pygame.draw.rect(screen, (200, 200, 200), bangoli_button_rect)

    if(data["noise"]):
        pygame.draw.rect(screen, (0,255, 0), noise_button_rect)
    else :
        pygame.draw.rect(screen, (255, 0,0), noise_button_rect)

    pygame.draw.rect(screen, (200, 200, 200), previous_button_rect)
    pygame.draw.rect(screen, (200, 200, 200), next_button_rect)
    pygame.draw.rect(screen, (200, 200, 200), empty_button_rect)


    play_text = font.render("Play", True, (0, 0, 0))
    pause_text = font.render("Pause", True, (0, 0, 0))
    stop_text = font.render("Stop", True, (0, 0, 0))
    male_text = font.render("Male", True, (0, 0, 0))
    female_text = font.render("Female", True, (0, 0, 0))
    english_text = font.render("English", True, (0, 0, 0))
    hindi_text = font.render("Hindi", True, (0, 0, 0))
    punjabi_text = font.render("Punjabi", True, (0, 0, 0))
    bangoli_text = font.render("Bangoli", True, (0, 0, 0))
    noise_text = font.render("Noise", True, (0, 0, 0))
    previous_text = font.render("P", True, (0, 0, 0))
    next_text = font.render("N", True, (0, 0, 0))
    empty_text = font.render("Find empty", True, (0, 0, 0))
    



    
    screen.blit(play_text, play_button_rect.topleft)
    screen.blit(pause_text, pause_button_rect.topleft)
    screen.blit(stop_text, stop_button_rect.topleft)
    screen.blit(male_text, male_button_rect.topleft)
    screen.blit(female_text, female_button_rect.topleft)
    screen.blit(english_text, english_button_rect.topleft)
    screen.blit(hindi_text, hindi_button_rect.topleft)
    screen.blit(punjabi_text, punjabi_button_rect.topleft)
    screen.blit(bangoli_text, bangoli_button_rect.topleft)
    screen.blit(noise_text, noise_button_rect.topleft)
    screen.blit(previous_text, previous_button_rect.topleft)
    screen.blit(next_text, next_button_rect.topleft)
    screen.blit(empty_text, empty_button_rect.topleft)

    
    pygame.display.flip()

    if not pygame.mixer.music.get_busy():
        playing = False

fn.updatedata(audio_index,data)
fn.savedata()
pygame.quit()


