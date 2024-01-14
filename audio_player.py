import pygame
import time
import os
import asyncio
import soundfile as sf
from mutagen.mp3 import MP3

class AudioManager:

    def __init__(self):
        # Use higher frequency to prevent audio glitching noises
        # Use higher buffer because why not (default is 512)
        pygame.mixer.init(frequency=48000, buffer=1024) 

    def play_audio(self, file_path, sleep_during_playback=True, delete_file=False, play_using_music=True):
        """
        Parameters:
        file_path (str): path to the audio file
        sleep_during_playback (bool): means program will wait for length of audio file before returning
        delete_file (bool): means file is deleted after playback (note that this shouldn't be used for multithreaded function calls)
        play_using_music (bool): means it will use Pygame Music, if false then uses pygame Sound instead
        """
        print(f"Playing file with pygame: {file_path}")
        if not pygame.mixer.get_init(): # Reinitialize mixer if needed
            pygame.mixer.init(frequency=48000, buffer=1024) 
        if play_using_music:
            # Pygame Music can only play one file at a time
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
        else:
            # Pygame Sound lets you play multiple sounds simultaneously
            pygame_sound = pygame.mixer.Sound(file_path) 
            pygame_sound.play()

        if sleep_during_playback:
            # Calculate length of the file, based on the file format
            _, ext = os.path.splitext(file_path) # Get the extension of this file
            if ext.lower() == '.wav':
                wav_file = sf.SoundFile(file_path)
                file_length = wav_file.frames / wav_file.samplerate
                wav_file.close()
            elif ext.lower() == '.mp3':
                mp3_file = MP3(file_path)
                file_length = mp3_file.info.length
            else:
                print("Cannot play audio, unknown file type")
                return

            # Sleep until file is done playing
            time.sleep(file_length)

            # Delete the file
            if delete_file:
                # Stop Pygame so file can be deleted
                # Note: this will stop the audio on other threads as well, so it's not good if you're playing multiple sounds at once
                pygame.mixer.music.stop()
                pygame.mixer.quit()
                try:  
                    os.remove(file_path)
                    print(f"Deleted the audio file.")
                except PermissionError:
                    print(f"Couldn't remove {file_path} because it is being used by another process.")

    async def play_audio_async(self, file_path):
        """
        Parameters:
        file_path (str): path to the audio file
        """
        print(f"Playing file with asynchronously with pygame: {file_path}")
        if not pygame.mixer.get_init(): # Reinitialize mixer if needed
            pygame.mixer.init(frequency=48000, buffer=1024) 
        pygame_sound = pygame.mixer.Sound(file_path) 
        pygame_sound.play()

        # Calculate length of the file, based on the file format
        _, ext = os.path.splitext(file_path) # Get the extension of this file
        if ext.lower() == '.wav':
            wav_file = sf.SoundFile(file_path)
            file_length = wav_file.frames / wav_file.samplerate
            wav_file.close()
        elif ext.lower() == '.mp3':
            mp3_file = MP3(file_path)
            file_length = mp3_file.info.length
        else:
            print("Cannot play audio, unknown file type")
            return

        # We must use asyncio.sleep() here because the normal time.sleep() will block the thread, even if it's in an async function
        await asyncio.sleep(file_length)


# TESTS
if __name__ == '__main__':
    audio_manager = AudioManager()
    MP3_FILEPATH = "TestAudio_MP3.mp3"
    WAV_FILEPATH = "TestAudio_WAV.wav"

    if not os.path.exists(MP3_FILEPATH) or not os.path.exists(WAV_FILEPATH):
        exit("Missing test audio")
    
    # MP3 Test
    audio_manager.play_audio(MP3_FILEPATH)
    print("Sleeping until next file")
    time.sleep(3)

    # Lots of MP3s at once test
    x = 10
    while x > 0:
        audio_manager.play_audio(MP3_FILEPATH,False,False,False)
        time.sleep(0.1)
        x -= 1
    print("Sleeping until next file")
    time.sleep(3)

    # Wav file tests
    audio_manager.play_audio(WAV_FILEPATH)
    print("Sleeping until next file")
    time.sleep(3)

    # Lots of WAVs at once test
    x = 10
    while x > 0:
        audio_manager.play_audio(WAV_FILEPATH,False,False,False)
        time.sleep(0.1)
        x -= 1
    print("Sleeping until next file")
    time.sleep(3)

    # Async tests
    async def async_audio_test():
        await audio_manager.play_audio_async(MP3_FILEPATH)
        time.sleep(1)
        await audio_manager.play_audio_async(WAV_FILEPATH)
        time.sleep(1)
    print("Playing async audio")
    asyncio.run(async_audio_test())

    # Deleting file tests
    # audio_manager.play_audio(MP3_FILEPATH, True, True)
    # print("Sleeping until next file")
    # time.sleep(3)
    # audio_manager.play_audio(WAV_FILEPATH, True, True)
    # print("Sleeping until next file")
    # time.sleep(3)
    