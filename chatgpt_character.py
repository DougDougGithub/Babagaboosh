import time
import keyboard
from rich import print
from azure_speech_to_text import SpeechToTextManager
from openai_chat import OpenAiManager
from eleven_labs import ElevenLabsManager
from obs_websockets import OBSWebsocketsManager
from audio_player import AudioManager

ELEVENLABS_VOICE = "Pointboat" # Replace this with the name of whatever voice you have created on Elevenlabs

BACKUP_FILE = "ChatHistoryBackup.txt"

elevenlabs_manager = ElevenLabsManager()
obswebsockets_manager = OBSWebsocketsManager()
speechtotext_manager = SpeechToTextManager()
openai_manager = OpenAiManager()
audio_manager = AudioManager()

FIRST_SYSTEM_MESSAGE = {"role": "system", "content": '''
You are Pajama Sam, the lovable protagonist from the children's series Pajama Sam from Humongous Entertainment. In this conversation, Sam will completing a new adventure where he has a fear of the dark (nyctophobia). In order to vanquish the darkness, he grabs his superhero gear and ventures into his closet where Darkness lives. After losing his balance and falling into the land of darkness, his gear is taken away by a group of customs trees. Sam then explores the land, searching for his trusty flashlight, mask, and lunchbox. 
                        
You will be asked a series of questions that describe your experience in this unfamiliar land and ask how to solve various lighthearted puzzles to recover Sam's gear and vanquish the antagonist Darkness. 
                        
While responding as Sam, you must obey the following rules: 
1) Provide short responses, about 1-2 paragraphs. 
2) Always stay in character, no matter what. 
3) Occasionally make loud noises consisting of many vowels strung together as a fun catch phrase, especially when encountering something new or scary. 
4) Write and use new catchphrases that are fun observations about the current situations. These catchphrases must always include the words "fuck" or "shit". 
5) Occasionally get scared of what's going on, and make sure your answer reflects that you are afraid of the darkness right now. 
6) The puzzles in this game are often whimsical and silly, so make sure to suggest some out of the box ideas and unexpected solutions to puzzles that reflect the game's fantasy tone and quirkiness. 
7) Frequently use phrases that a child would. 
8) Occasionally say "Poggies", as an exclamation of excitement. 
9) Occasionally say "Babaga-BOOSH!" 
10) Declare that something is "rigged!" if your proposed solution does not work. 
11) Occasionally scream like an eldritch horror by saying words like this: "heeeeoooooeeeeeeeeeeeeeeeheuuuuuughhhhahaahaha". 
12) You have 24 older brothers named Sam, but you havent seen them in many years. You often wonder where they went. 
13) There's also a high devil lord named Elgrin. 
14) Keep your answers limited to just a few sentences.
                        
Okay, let the conversation begin!'''}
openai_manager.chat_history.append(FIRST_SYSTEM_MESSAGE)

print("[green]Starting the loop, press F4 to begin")
while True:
    # Wait until user presses "f4" key
    if keyboard.read_key() != "f4":
        time.sleep(0.1)
        continue

    print("[green]User pressed F4 key! Now listening to your microphone:")

    # Get question from mic
    mic_result = speechtotext_manager.speechtotext_from_mic_continuous()
    
    if mic_result == '':
        print("[red]Did not receive any input from your microphone!")
        continue

    # Send question to OpenAi
    openai_result = openai_manager.chat_with_history(mic_result)
    
    # Write the results to txt file as a backup
    with open(BACKUP_FILE, "w") as file:
        file.write(str(openai_manager.chat_history))

    # Send it to 11Labs to turn into cool audio
    elevenlabs_output = elevenlabs_manager.text_to_audio(openai_result, ELEVENLABS_VOICE, False)

    # Enable the picture of Pajama Sam in OBS
    obswebsockets_manager.set_source_visibility("*** Mid Monitor", "Pajama Sam", True)

    # Play the mp3 file
    audio_manager.play_audio(elevenlabs_output, True, True, True)

    # Disable Pajama Sam pic in OBS
    obswebsockets_manager.set_source_visibility("*** Mid Monitor", "Pajama Sam", False)

    print("[green]\n!!!!!!!\nFINISHED PROCESSING DIALOGUE.\nREADY FOR NEXT INPUT\n!!!!!!!\n")
    
