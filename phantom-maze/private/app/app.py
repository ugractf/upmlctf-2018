from flask import Flask, render_template, request


app = Flask(__name__)

with open("array.txt") as f:
    ARRAY = f.read().split()


@app.route('/')
def index():
    return render_template('index.html', start=ARRAY[0])


@app.route('/maze/<id>')
def maze(id):
    if id in ARRAY:
        pos = ARRAY.index(id)
        if pos == 1509:
            return render_template('maze.html', flag='uctf_h1dd3n_1n_th3_m4z3')
        if pos == len(ARRAY) - 1:
            return render_template('final.html')
    return render_template('maze.html')


@app.route('/next', methods=['POST'])
def next():
    id = request.form['id']
    pos = ARRAY.index(id)
    return ARRAY[pos + 1]


if __name__ == "__main__":
    app.run()

