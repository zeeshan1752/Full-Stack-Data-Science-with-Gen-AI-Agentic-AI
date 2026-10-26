# Text-to-Speech (TTS)

Text-to-Speech (TTS) converts written text into audio that sounds like spoken language. In the trainer's Streamlit demo, TTS is used to read a paragraph aloud and to play translated text in the selected language.

## 1. How It Works

1. Collect the text to be spoken.
2. Choose a supported language code, such as `en` for English.
3. Send the text to a TTS engine.
4. Save or stream the generated audio, then play it for the user.

This lesson uses `gTTS`, a Python interface to Google's online text-to-speech service. It requires an internet connection. It is not an offline TTS engine.

## 2. Install

```bash
python -m pip install gTTS
```

## 3. Generate an MP3 file

The script in [Text_to_Speech.py](Text_to_Speech.py) demonstrates the basic workflow. The example saves an MP3 file in the current working directory.

```python
from gtts import gTTS

text = "Natural Language Processing helps computers work with human language."
audio = gTTS(text=text, lang="en")
audio.save("tts_output.mp3")
print("Saved audio to tts_output.mp3")
```

Expected message:

```text
Saved audio to tts_output.mp3
```

The audio file is created when the code runs successfully. The spoken result depends on the text, language code, service availability, and network connection.

## 4. Play audio in a notebook or Streamlit app

In Jupyter, use:

```python
from IPython.display import Audio, display

display(Audio("tts_output.mp3"))
```

In Streamlit, use:

```python
import streamlit as st

st.audio("tts_output.mp3", format="audio/mp3")
```

Using `st.audio` avoids relying on Windows-only commands such as `os.system("start temp.mp3")`, which do not work consistently across operating systems or hosted environments.

## 5. Important points

- TTS converts text to audio; speech recognition converts audio to text.
- The language code must be supported by the selected TTS service.
- Avoid saving every request to the same filename in multi-user apps; use unique or temporary files where needed.
- Do not put private or sensitive text into an online service unless its data handling is appropriate for the use case.
- Handle empty input and network errors in a complete application.

## 6. Practice exercises

1. Convert a short English sentence to speech.
2. Try another supported language code and compare pronunciation.
3. Add a text input and a button to a Streamlit app, then display the generated audio with `st.audio`.
4. Add an empty-input check and a helpful error message.

## References

- [gTTS documentation](https://gtts.readthedocs.io/en/latest/)
- [Streamlit audio element](https://docs.streamlit.io/develop/api-reference/media/st.audio)
