# Text Summarization Application

Status: The code has not been run locally.

## Install

    python -m pip install streamlit torch transformers

The first run downloads pretrained model weights from Hugging Face. They stay in the local cache and are not included in the repository.

## Run

    streamlit run 08_Natural_Language_Processing/08_Projects/04_Text_Summarization_Application/text_summarization_app_streamlit.py

## What you will learn

The local Streamlit app accepts a passage and displays a shorter generated summary. After the model is downloaded, the text is processed by the model on your computer; this example does not call a hosted inference API.

## Common mistakes

- Very long passages may be truncated to fit the model's input limit.
- Check generated summaries for missing or incorrect details before sharing them.
