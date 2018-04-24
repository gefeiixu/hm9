from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def inspiration():
    with open('inspiration.txt') as ins:
        sources = ins.read().split('\n')
    return random.choice(sources)


if __name__=='__main__':
    app.run()


