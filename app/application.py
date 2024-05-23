#   Importing the necessary libraries/modules.

from flask import Flask, render_template
import json

application=Flask(__name__, template_folder="templates", static_folder="static")

#   Rendering the home page.

@application.route("/")
def index():
    return render_template("home.html")

#   Rendering the loading page.

@application.route("/loading")
def loading():
    return render_template("loading.html")

#   Rendering the topic modelling visualisation page.

@application.route("/topic_modelling")
def topic_modelling():
    data=None

    #   Loading the relevant data from the JSON file.

    with open(r"data/topic_modelling.json", "r") as f:
        data=json.load(f)

    data=data[:1000]    #   Limiting the number of documents to 1000.
    return render_template("topic_modelling.html", data=data)

#   Rendering the conversation network visualisation page.

@application.route(r"/conversation_network")
def conversation_network():
    data=None

    #   Loading the relevant data from the JSON file.

    with open(r"data/conversation_network.json", "r") as f:
        data=json.load(f)

    data=data[:1000]    #   Limiting the number of documents to 1000.
    return render_template("conversation_network.html", data=data)

#   Driver function.

if __name__=="__main__":
    application.run(debug=True)