# Babagaboosh
Simple app that lets you have a verbal conversation with OpenAi's GPT 4.
Written by DougDoug. Feel free to use this for whatever you want! Credit is appreciated but not required.

## SETUP:
1) This was written in Python 3.9.2. Install page here: https://www.python.org/downloads/release/python-392/

3) Run `pip install -r requirements.txt` to install all modules.

4) This uses the Microsoft Azure TTS, Elevenlabs, and OpenAi services. You'll need to set up an account with these services and generate an API key from them. Then add these keys as windows environment variables named AZURE_TTS_KEY, AZURE_TTS_REGION, ELEVENLABS_API_KEY, and OPENAI_API_KEY respectively.

5) Optionally, you can use OBS Websockets and an OBS plugin to make images move while talking.
First open up OBS. Make sure you're running version 28.X or later.
Click Tools, then WebSocket Server Settings.
Make sure "Enable WebSocket server" is checked. Make sure Server Port is '4455', and set the Server Password to 'TwitchChat9'. If you use a different Server Port or Server Password in your OBS, just make sure you update the websockets_auth.py file accordingly.
Next install the Move OBS plugin: https://obsproject.com/forum/resources/move.913/
Now you can use this plugin to add a filter to an audio source that will change an image's transform based on the audio waveform. For example, I have this filter on a specific audio track that will move Pajama Sam's image whenever text-to-speech audio is playing in that audio track.
Note that OBS must be open when you're running this code, otherwise OBS WebSockets won't be able to connect.
If you don't need the images to move while talking, you can just delete the OBS portions of the code.

6) Elevenlabs is the service I use for Ai voices. Once you've made an Ai voice on the Elevenlabs website, open up chatgpt_character.py and replace the ELEVENLABS_VOICE variable with the name of your Ai voice.

## Using the App

1) Run `chatgpt_character.py'

2) Once it's running, press F4 to start the conversation, and Azure Speech-to-text will listen to your microphone and transcribe it into text.

3) Once you're done talking, press P. Then the code will send all of the recorded text to the Ai. Note that you should wait a second or two after you're done talking before pressing P so that Azure has enough time to process all of the audio.

4) Wait a few seconds for OpenAi to generate a response and for Elevenlabs to turn that response into audio. Once it's done playing the response, you can press F4 to start the loop again and continue the conversation.
