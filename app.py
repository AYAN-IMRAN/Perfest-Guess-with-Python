from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Global variables to hold the number and guesses
n = random.randint(1, 50)
guesses = 0
game_over = False  # Track if the game is over

@app.route('/')
def index():
    global n, guesses, game_over
    n = random.randint(1, 50)  # Reset the game every time the page is reloaded
    guesses = 0
    game_over = False  # Reset the game over flag when the page reloads
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    global n, guesses, game_over

    # If the game is over, don't process the guess
    if game_over:
        return jsonify({"message": "The game is over! Reload to play again.", "status": "error", "guesses": guesses})

    user_guess = int(request.form['guess'])
    guesses += 1
    
    if user_guess < n:
        message = "Too High! 🔼"
        status = "error"
    elif user_guess > n:
        message = "Too Low! 🔽"
        status = "error"
    else:
        message = f"Congrats! You've guessed the number {n} in {guesses} attempts! 🎉"
        status = "success"
        game_over = True  # End the game after a correct guess

    return jsonify({"message": message, "status": status, "guesses": guesses})

if __name__ == '__main__':
    app.run(debug=True)
