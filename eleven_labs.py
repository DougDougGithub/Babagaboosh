from elevenlabs import generate, stream, set_api_key, voices, play, save
import time
import os

set_api_key(os.getenv('ELEVENLABS_API_KEY'))

class ElevenLabsManager:

    def __init__(self):
        # CALLING voices() IS NECESSARY TO INSTANTIATE 11LABS FOR SOME FUCKING REASON
        all_voices = voices()
        print(f"\nAll ElevenLabs voices: \n{all_voices}\n")

    # Convert text to speech, then save it to file. Returns the file path
    def text_to_audio(self, input_text, voice="Doug VO Only", save_as_wave=True, subdirectory=""):
        audio_saved = generate(
          text=input_text,
          voice=voice,
          model="eleven_monolingual_v1"
        )
        if save_as_wave:
          file_name = f"___Msg{str(hash(input_text))}.wav"
        else:
          file_name = f"___Msg{str(hash(input_text))}.mp3"
        tts_file = os.path.join(os.path.abspath(os.curdir), subdirectory, file_name)
        save(audio_saved,tts_file)
        return tts_file

    # Convert text to speech, then play it out loud
    def text_to_audio_played(self, input_text, voice="Doug VO Only"):
        audio = generate(
          text=input_text,
          voice=voice,
          model="eleven_monolingual_v1"
        )
        play(audio)

    # Convert text to speech, then stream it out loud (don't need to wait for full speech to finish)
    def text_to_audio_streamed(self, input_text, voice="Doug VO Only"):
        audio_stream = generate(
          text=input_text,
          voice=voice,
          model="eleven_monolingual_v1",
          stream=True
        )
        stream(audio_stream)


if __name__ == '__main__':
    elevenlabs_manager = ElevenLabsManager()

    elevenlabs_manager.text_to_audio_streamed("This is my streamed test audio, I'm so much cooler than played", "Doug Melina")
    time.sleep(2)
    elevenlabs_manager.text_to_audio_played("This is my played test audio, helo hello", "Doug Melina")
    time.sleep(2)
    file_path = elevenlabs_manager.text_to_audio("This is my saved test audio, please make me beautiful", "Doug Melina")
    print("Finished with all tests")

    time.sleep(30)
