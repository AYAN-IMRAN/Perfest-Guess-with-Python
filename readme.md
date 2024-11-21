# Number Guessing Game with Flask 🎮

Welcome to the **Number Guessing Game** project! This simple web-based game is built using **Python** and **Flask** where users try to guess a randomly generated number between 1 and 50. 🚀

## Table of Contents
- [Introduction](#introduction)
- [How to Run the Project](#how-to-run-the-project)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)

---

## Introduction

This is a fun and simple web application that allows you to play a **Number Guessing Game**. Every time you reload the page, a new number is randomly generated, and you get the chance to guess it.

- Guess the number between **1** and **50**.
- Receive feedback on whether your guess is too high or too low.
- The game ends when you guess the correct number! 🎉

---

## How to Run the Project

To get started, follow the steps below:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/number-guessing-game.git
    ```

2. **Install Dependencies**:
    Make sure you have Python installed. Then, create a virtual environment and install the dependencies.
    ```bash
    cd number-guessing-game
    python3 -m venv venv
    source venv/bin/activate  # For Linux/macOS
    venv\Scripts\activate     # For Windows
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    python app.py
    ```

4. Open your browser and visit `http://127.0.0.1:5000` to play the game!

---

## Project Structure

### `app.py`

This file contains the Python code for the Flask application, handling the backend logic of the game.

```python
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
```

### `templates/index.html`

This file contains the front-end code for the game, using **HTML**, **CSS**, and **JavaScript**. It uses **Bootstrap** for styling and **jQuery** for AJAX requests.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Guessing Game</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css">
    <style>
        body {
            background-color: #121212;
            color: #e0e0e0;
            font-family: Arial, sans-serif;
        }
        .container {
            margin-top: 50px;
        }
        .result-message {
            font-size: 1.5em;
            margin-top: 20px;
        }
        .btn-primary {
            background-color: #6200ea;
            border-color: #6200ea;
        }
        .btn-primary:hover {
            background-color: #3700b3;
            border-color: #3700b3;
        }
        .input-group-text {
            background-color: #6200ea;
            color: #fff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center text-white">Guess the Number Game 🎮</h1>
        <div class="row justify-content-center">
            <div class="col-md-6">
                <div class="input-group">
                    <input type="number" id="userGuess" class="form-control" placeholder="Enter your guess (1-50)" min="1" max="50">
                    <button class="btn btn-primary" id="submitGuess">Guess</button>
                </div>
                <div id="result" class="result-message text-center"></div>
                <div id="attempts" class="text-center mt-3"></div>
            </div>
        </div>
    </div>

    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <script>
        $(document).ready(function() {
            let gameOver = false;  // Track if the game is over

            $("#submitGuess").click(function() {
                if (gameOver) {
                    alert("The game is over! Reload the page to play again.");
                    return;  // Stop any further guesses if the game is over
                }

                const userGuess = $("#userGuess").val();
                if (userGuess === "") {
                    alert("Please enter a number!");
                    return;
                }

                $.ajax({
                    type: "POST",
                    url: "/guess",
                    data: { guess: userGuess },
                    success: function(response) {
                        $("#result").text(response.message);  // Show the message (congratulations or error)
                        
                        if (response.status === "success") {
                            $("#attempts").text(``);
                            gameOver = true;  // Mark game as over
                            $("#submitGuess").prop('disabled', true);  // Disable the guess button
                        } else {
                            $("#attempts").text(`Attempts: ${response.guesses}`);  // Show the number of attempts
                        }

                        // Clear the input field after the guess
                        $("#userGuess").val('');
                    }
                });
            });
        });
    </script>
</body>
</html>
```

---

## Technologies Used

- **Python**: Backend programming language.
- **Flask**: Web framework for Python.
- **HTML/CSS**: Front-end for the game interface.
- **JavaScript (jQuery)**: For handling AJAX requests and updating the UI dynamically.
- **Bootstrap**: For responsive design and styling.

---

## Contribute

Feel free to fork the repository and submit a pull request for any enhancements or bug fixes! 😊

---

**Enjoy the game and happy coding!** 🎉🚀
