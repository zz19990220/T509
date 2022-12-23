from flask import Flask, render_template, request
from Human import Human
from Bot import Bot
from Game import Game
app = Flask(__name__)

global game, moves
moves = 0

@app.route('/')
def start():
    return render_template('index.html')

@app.route('/play',methods=['POST'])
def play():
    global game
    player_x = request.form.get('player_type')
    if player_x == "human":
        game = Game(Human(), Human("X"))
    else:
        game = Game(Human(), Bot())
    return render_template('play.html')


@app.route('/move',methods=['POST'])
def move():
    global game, moves
    x, y =int(request.form.get('row')), int(request.form.get('column'))
    player = game.swith_player()
    #print(game.board)
    game.make_move(player, x, y)
    moves += 1
    winner = game.get_winner()
    if winner == None:
        return show_board(game)
    else:
        game.add_result_to_CSV(winner.name, moves)
        return show_board(game,"Game Over! Winner is "+winner.name)

def show_board(game,result=""):
    pos1 = "" if game.board.rows[0][0] == None else game.board.rows[0][0].label
    pos2 = "" if game.board.rows[0][1] == None else game.board.rows[0][1].label
    pos3 = "" if game.board.rows[0][2] == None else game.board.rows[0][2].label
    pos4 = "" if game.board.rows[1][0] == None else game.board.rows[1][0].label
    pos5 = "" if game.board.rows[1][1] == None else game.board.rows[1][1].label
    pos6 = "" if game.board.rows[1][2] == None else game.board.rows[1][2].label
    pos7 = "" if game.board.rows[2][0] == None else game.board.rows[2][0].label
    pos8 = "" if game.board.rows[2][1] == None else game.board.rows[2][1].label
    pos9 = "" if game.board.rows[2][2] == None else game.board.rows[2][2].label
    return render_template('play.html',
                           pos1=pos1,pos2=pos2,pos3=pos3,
                           pos4=pos4,pos5=pos5,pos6=pos6,
                           pos7=pos7,pos8=pos8,pos9=pos9,result=result)

@app.route('/stats',methods=['POST'])
def stats():
    return render_template('stats.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)