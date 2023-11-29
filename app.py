import streamlit as st
import websocket
import json

url = 'wss://api.assemblyai.com/v2/transcript'

def on_message(ws, message):
    response = json.loads(message)
    if 'text' in response:
        st.write(response['text'])

def on_error(ws, error):
    st.error("Something went wrong. Please try again.")

def on_close(ws):
    st.info("Connection closed.")

def on_open(ws):
    def run(*args):
        audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
        if audio_file:
            st.audio(audio_file)
            st.write("Transcription in progress...")
            headers = {
                'authorization': 'ed7acb234a744a5cb9b0f0ae9c3a2130',
                'content-type': 'audio/wav'
            }
            ws.send(json.dumps({"audio": audio_file.read()}))
        else:
            st.warning("Please upload an audio file.")

    run()

def main():
    st.title("Song Transcription App")
    st.write("Upload an audio file and watch the magic happen!")

    ws = websocket.WebSocketApp(url=url, on_open=on_open, on_message=on_message, on_error=on_error, on_close=on_close)

if __name__ == '__main__':
    main()
