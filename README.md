# Interactive Conversational Analysis & Visualisation on Cornell Movie-Dialogs Corpus Using D3.js:

This repository showcases an interactive conversational analysis of the Cornell Movie-Dialogs Corpus, visualised using D3.js, as part of the Data Analysis & Visualisation (DS3001) course final project, encompassing 220,579 exchanges between 10,292 character pairs in 617 movies.

### Dependencies:

* Jupyter Notebook ([install](https://docs.jupyter.org/en/latest/install.html))
* ConvoKit ([install](https://convokit.cornell.edu/))
* pandas ([install](https://pandas.pydata.org/docs/getting_started/install.html))
* NLTK ([install](https://www.nltk.org/install.html))
* scikit-learn ([install](https://scikit-learn.org/stable/install.html))
* Flask ([install](https://flask.palletsprojects.com/en/3.0.x/installation/))

## Introduction:

Conversational analytics is a technology-driven process that involves analysing data from human conversations to extract meaningful insights. These conversations can occur across various channels such as phone calls, chatbots, social media, customer service interactions, and more. The primary goal of conversational analytics is to understand the content, context, and sentiment of conversations to improve customer experiences, streamline operations, and inform strategic decision-making.

## What Is Cornell Movie Dialogs Corpus?

Cornell Movie-Dialogs Corpus is a [dataset](https://convokit.cornell.edu/documentation/movie.html) compiled by the Cornell University for use in natural language processing (NLP) research. It consists of a large collection of movie dialogues from various sources (220,579 conversational exchanges between 10,292 pairs of movie characters in 617 movies), including Hollywood movies. The dataset is structured in such a way that it includes metadata about the movies, such as the titles, genres, release years, and the characters involved in each dialogue exchange. This corpus has been widely used for tasks such as dialogue generation, sentiment analysis, and conversational modeling in the field of natural language processing (NLP).

## What Is Our Approach?

For our analysis of the Cornell Movie-Dialogs Corpus, we employ natural language processing (NLP) techniques, including topic modelling, to uncover hidden thematic structures within the dialogues. Additionally, we create a conversation network to organise and summarise the extensive textual information, allowing us to understand the connections between entities in the dataset.

## Techniques Used:

### Conversation Network:

A conversation network is a graphical representation of interactions between entities within a dataset, particularly focusing on dialogues and conversations. In the context of the Cornell Movie-Dialogs Corpus, a conversation network can help visualise and analyse the relationships and communication patterns between characters.

### Topic Modelling:

Topic modelling is a type of statistical modeling used to identify abstract topics that occur in a collection of documents. It helps in organising and summarising large datasets of textual information. The most common techniques for topic modelling are Latent Dirichlet Allocation (LDA) and Non-Negative Matrix Factorisation (NMF). Topic modelling can be effectively applied to the Cornell Movie-Dialogs Corpus to reveal hidden thematic structures within the dialogues.

## Usage:

* ``Conversation Analytics.ipynb`` — Comprises a thorough conversational analysis performed on the Cornell Movie-Dialogs Corpus.
* ``application.py`` — Source code for the analytical dashboard application (Flask).
* `templates` — Contains the source codes for the web pages (`home.html`, `loading.html`, `conversation_network.html`, and `topic_modelling.html`) rendered by the web application (Flask).
* `data` — Comprises the visualisation data structured in JavaScript Object Notation (JSON) format.
* `static` — Contains all the icons and visual elements utilised by the web application (Flask).

## Contributors:

This project owes its existence to the exceptional individual who contributed to it.
* **[Areeba Riaz](https://github.com/areeba9593) (i211736@nu.edu.pk)**
