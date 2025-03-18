import pygame

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((800,800))
is_pause = False
running = True


is_playing = False
is_paused = False


songs = ["blo.mp3","car.mp3","girl.mp3"]
current_song_index = 0
def song_mixer(index):
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()
    print(f"Playing: {songs[index]}")



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not is_playing:
                    song_mixer(current_song_index)
                    is_playing = True
                    is_paused = False
                else:
                    if is_paused:
                        pygame.mixer.music.unpause()
                        print("Resumed")
                        is_paused = False
                    else:
                        pygame.mixer.music.pause()
                        print("paused")
                        is_paused = True
            elif event.key == pygame.K_RIGHT:
                current_song_index = (current_song_index +1) % len(songs)
                song_mixer(current_song_index)
                is_paused = False
                is_playing = True
            elif event.key == pygame.K_LEFT:
                current_song_index = (current_song_index - 1) % len(songs)
                song_mixer(current_song_index)
                is_playing = True
                is_paused = False
    screen.fill((255,255,255))
    pygame.display.flip()
pygame.quit()