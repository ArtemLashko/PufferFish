from flask import Flask, render_template
from flask import request, jsonify
import chessengine

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

# A route to return a next move 1
@app.route('/api/v1/suggest_move', methods=['GET'])
def api_all():
    print(request.args)
    if 'fen' in request.args:
        fen = str(request.args['fen'])
    else:
        return -1
    engine_ins = chessengine.Engine(fen)
    engine_ins.debug()
    next_move = engine_ins.alphabeta_move()
    print("My next move is " + str(next_move))
    engine_ins.debug()
    print(engine_ins.leafs)
    return "{'move': '%s'}" % str(next_move)


if __name__ == '__main__':
    app.run(host="localhost",port=3000)
