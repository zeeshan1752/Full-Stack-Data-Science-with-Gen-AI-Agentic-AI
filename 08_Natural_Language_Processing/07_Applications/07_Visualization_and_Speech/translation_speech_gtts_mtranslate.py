from pathlib import Path
import time
from io import BytesIO

import pandas as pd
import streamlit as st
from gtts import gTTS
from mtranslate import translate


# Page configuration
st.set_page_config(
    page_title="Language Translation",
    page_icon="🌐",
    layout="wide"
)


# Read language dataset
CSV_PATH = Path(__file__).resolve().parent / "language.csv"

try:
    df = pd.read_csv(CSV_PATH)
    df.dropna(subset=["name", "iso"], inplace=True)

    df["name"] = df["name"].astype(str).str.strip()
    df["iso"] = df["iso"].astype(str).str.strip()

    df = df[
        (df["name"] != "") &
        (df["iso"] != "")
    ].drop_duplicates(subset=["name"])

    lang_array = dict(zip(df["name"], df["iso"]))
    langlist = list(lang_array.keys())

except (FileNotFoundError, KeyError, pd.errors.ParserError) as error:
    st.error(f"Unable to load the language dataset: {error}")
    st.stop()


# Languages supported by gTTS
speech_langs = {
    "af", "ar", "bg", "bn", "bs", "ca", "cs", "cy",
    "da", "de", "el", "en", "eo", "es", "et", "fi",
    "fr", "gu", "hi", "hr", "hu", "hy", "id", "is",
    "it", "ja", "jw", "km", "kn", "ko", "la", "lv",
    "mk", "ml", "mr", "ms", "my", "ne", "nl", "no",
    "pl", "pt", "ro", "ru", "si", "sk", "sq", "sr",
    "su", "sv", "sw", "ta", "te", "th", "tl", "tr",
    "uk", "ur", "vi", "zh-CN", "zh-TW"
}


# Translation function with retry handling
@st.cache_data(ttl=3600, show_spinner=False)
def get_translation(text, target_code):
    last_error = None

    for attempt in range(2):
        try:
            result = translate(text, target_code)

            if not result or not result.strip():
                raise ValueError("The translation service returned an empty result.")

            return result

        except Exception as error:
            last_error = error
            message = str(error).lower()

            if "429" in message or "too many requests" in message:
                # Avoid repeatedly retrying a rate-limited service.
                if attempt == 0:
                    time.sleep(2)
                    continue

            raise RuntimeError(str(error)) from error

    raise RuntimeError(str(last_error))


# Streamlit interface
st.title("Language-Translation")

inputtext = st.text_area(
    "Hi Please Enter text here to Translate",
    height=100,
    placeholder="Enter text here..."
)

choice = st.sidebar.radio(
    "SELECT LANGUAGE",
    langlist
)

c1, c2 = st.columns([4, 3])


# Translate only when the button is clicked
if st.button("Translate", type="primary"):

    text_to_translate = inputtext.strip()

    if not text_to_translate:
        st.warning("Please enter some text to translate.")

    else:
        target_code = lang_array[choice]

        try:
            with st.spinner("Translating..."):
                output = get_translation(
                    text_to_translate,
                    target_code
                )

            with c1:
                st.text_area(
                    "TRANSLATED TEXT",
                    value=output,
                    height=200
                )

            # Generate audio when the language is supported
            if target_code in speech_langs:
                try:
                    with st.spinner("Generating audio..."):
                        audio_buffer = BytesIO()

                        tts = gTTS(
                            text=output,
                            lang=target_code,
                            slow=False
                        )

                        tts.write_to_fp(audio_buffer)
                        audio_bytes = audio_buffer.getvalue()

                    with c2:
                        st.audio(
                            audio_bytes,
                            format="audio/mp3"
                        )

                        st.download_button(
                            label="Download Audio File",
                            data=audio_bytes,
                            file_name="translated_audio.mp3",
                            mime="audio/mpeg"
                        )

                except Exception:
                    st.warning(
                        "Translation succeeded, but audio generation "
                        "failed. Please try again later."
                    )

            else:
                st.info(
                    "Audio generation is not supported for this "
                    "language code in the current configuration."
                )

        except Exception as error:
            message = str(error).lower()

            if "429" in message or "too many requests" in message:
                st.error(
                    "The translation service has temporarily limited "
                    "requests. Please wait before trying again."
                )
            else:
                st.error(f"Translation failed: {error}")

