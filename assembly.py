import assemblyai as aai

aai.settings.api_key = "ed7acb234a744a5cb9b0f0ae9c3a2130"
transcriber = aai.Transcriber()

transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# transcript = transcriber.transcribe("./my-local-audio-file.wav")

print(transcript.text)