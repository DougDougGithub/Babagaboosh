# Babagaboosh
App that lets you have a verbal conversation with OpenAi's GPT 4

## Instructions
- Install Python 3.9.2
- Run `pip install -r requirements.txt`
- Set up accounts with Azure TTS, Elevenlabs, and OpenAi. Then add your account's API keys as env variables.
- If you are using OBS, enable the OBS Websocket Server in OBS and make sure the Port and Password match the variables listed in the websockets_auth.py file
- In chatgpt_character.py, replace "Pointboat" with the name of the Ai voice that you've created on Elevenlabs.com
- Run `chatgpt_character.py'. Once it's running, press F4 to start the conversation, press P to finish talking and send your voice to the Ai.
