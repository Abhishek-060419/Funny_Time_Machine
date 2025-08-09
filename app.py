from flask import Flask, render_template, request
from logic.engine import generate_history

app=Flask(__name__)

@app.route("/",methods=['GET'])
def index():
    return render_template("initial.html")

@app.route("/generate", methods=['POST'])
def generate():
    year = request.form.get('year')
    topic = request.form.get('topic')

    if year and topic:
        # If user chooses random, pick one of the available topics randomly
        if topic == "random":
            import random
            topic = random.choice(["history", "science", "technology"])
        
        sentence = generate_history(year, topic)
        return render_template('result.html', sentence=sentence, year=year, topic=topic)

    return "Please enter a valid year and topic!", 400


if __name__ == "__main__":
    app.run(debug=True)

