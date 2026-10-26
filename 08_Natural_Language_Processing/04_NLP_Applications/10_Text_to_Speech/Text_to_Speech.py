# Text-to-Speech with gTTS

from gtts import gTTS

text = input("Enter text to convert to speech: ").strip()

if not text:
    print("Please enter some text.")
else:
    language = input("Language code (press Enter for English): ").strip() or "en"
    try:
        audio = gTTS(text=text, lang=language)
        output_file = "tts_output.mp3"
        audio.save(output_file)
        print(f"Saved audio to {output_file}")
        print("Open the MP3 file in a media player, or play it with IPython.display.Audio in a notebook.")
    except Exception as error:
        print("Could not generate speech. Check your internet connection and language code.")
        print("Details:", error)
