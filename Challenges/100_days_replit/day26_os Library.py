from replit import audio
import os, time


def play():
  source = audio.play_file('audio.wav')
  source.paused = False  # unpause the playback
  while True:
    _ = input('Stop? (y/N) : ').lower()
    if _ == 'y':
      break
    else:
      continue


while True:
  os.system('clear')
  print('🎵 MyPOD Music Player')
  time.sleep(1)
  print()
  user = int(
    input('''
Press 1 to Play
Press 2 to Exit

Press anything else to see the menu again
'''))

  # check whether you should call the play() subroutine depending on user's input
  if user == 1:
    print('Playing some proper tunes for you!')
    play()
  elif user == 2:
    print('Exiting the music player. Goodbye!')
    break
