# Data and Study Resource Sources

This repository keeps course notes, handouts, diagrams, exported lessons, and example data for the owner's study and revision, and for other learners. Their presence is intentional.

Source and license details were not recorded for every item at the time of review. Add the original author or publisher, source URL, and license/permission when known. Do not present third-party materials as original work.

| Path | Use | Provenance status |
|---|---|---|
| 01_Python/**/*.pdf | Python course notes, trainer notes, and cheat sheets | Original source and redistribution terms are not documented. |
| 02_Advanced_Python/**/*.pdf | Python pattern and loop reference | Original source and redistribution terms are not documented. |
| 03_Data_Analysis/**/*.pdf | NumPy, Matplotlib, and Pandas notes, interview materials, answer key, and documentation | Original source and redistribution terms are not documented. |
| Study diagrams under 01_Python/, 02_Advanced_Python/, and 03_Data_Analysis/ | Concept illustrations and plotting references | Attribution is not recorded file by file. |
| 03_Data_Analysis/02_Matplotlib/Complete_Notes/Matplotlib_HTML_Notes_(Download_and_Use).html | Exported Matplotlib lesson | Original source and redistribution terms are not documented. |
| 03_Data_Analysis/02_Matplotlib/POC_01/Dataset.txt | Earlier data-driven plotting exercise | Data source and redistribution terms are not documented. The current notebook uses clearly labeled synthetic examples and does not load this file. |
| 03_Data_Analysis/03_Pandas/data_used.xlsx | Pandas exercise workbook | Source and redistribution terms are not documented. |
| 03_Data_Analysis/02_Matplotlib/Phot_Used.jpg | Matplotlib image-loading example | Creator and license are not documented. |

The seasonal plotting notebook uses explicitly labeled synthetic values. It does not claim to represent real players, matches, salaries, or currency.

## Natural language processing

| Path or resource | Use | Source and redistribution terms |
|---|---|---|
| 08_Natural_Language_Processing/data/restaurant_reviews.tsv | 1,000 labeled sentiment examples | Synthetic teaching data already in this repository; no external dataset was copied into it. |
| 08_Natural_Language_Processing/data/sample_texts.txt | Shared examples for NLP lessons | Existing shared examples; original attribution was not recorded. |
| UCI SMS Spam Collection | Dataset for the spam classifier; place the downloaded file at 08_Natural_Language_Processing/data/sms_spam.tsv | [UCI dataset page](https://archive.ics.uci.edu/dataset/228/sms+spam+collection). UCI lists CC BY 4.0; attribution is required when redistributing. The data file is not included in this repository. Citation: Almeida and Hidalgo, SMS Spam Collection, UCI Machine Learning Repository, DOI 10.24432/C5CC84. |
| 20 Newsgroups via scikit-learn | Dataset downloaded and cached by the news-topic example when run | [scikit-learn dataset documentation](https://scikit-learn.org/stable/datasets/real_world.html) says the data is fetched from the original 20 Newsgroups source. The documentation does not state a redistribution license. The data is not included here; review the original source terms before redistributing it. |
| [NLTK](https://www.nltk.org/), [spaCy](https://spacy.io/), [scikit-learn](https://scikit-learn.org/stable/), [PyTorch](https://pytorch.org/docs/stable/), [Transformers](https://huggingface.co/docs/transformers/), and [Streamlit](https://docs.streamlit.io/) documentation | API references for original examples and explanations in the NLP lessons | Official documentation sources. No third-party lesson text or code was copied verbatim. Package licenses apply to the packages themselves. |
| prajjwal1/bert-tiny | BERT tokenization, masked-language-model demonstration, and fine-tuning examples | [Hugging Face model card](https://huggingface.co/prajjwal1/bert-tiny) lists the MIT license. Model weights are downloaded at runtime and are not included. |
| sshleifer/distilbart-cnn-12-6 | Summarization examples | [Hugging Face model card](https://huggingface.co/sshleifer/distilbart-cnn-12-6) lists Apache-2.0. Model weights are downloaded at runtime and are not included. |
| distilbert/distilgpt2 | Text generation example | [Hugging Face model card](https://huggingface.co/distilbert/distilgpt2) lists Apache-2.0. Model weights are downloaded at runtime and are not included. |
| distilbert/distilbert-base-uncased-finetuned-sst-2-english | BERT-family sentiment inference example | [Hugging Face model card](https://huggingface.co/distilbert/distilbert-base-uncased-finetuned-sst-2-english) lists Apache-2.0. Model weights are downloaded at runtime and are not included. |
