from helper import audio_to_text

audio_file = open("example-audio.m4a", "rb")

response = audio_to_text(audio_file)

print(response)