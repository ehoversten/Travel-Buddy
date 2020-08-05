Web app that allows signed in users to plan and add. add or, remove their own scheduled trips and join other trips planned by other users.

Implemented changes:
  - Restructured app, modularized into separate components.
  - Cleaned repetitive code; DRY principle
  
Tech – Python, Django, Bootstrap 4, SQLite

# Project: Quiz Game

&nbsp;

## Description

This is a small multiple choice quiz game. The user will be presented with a welcome screen and instructions on how to play the game. User clicks the start button to begin the game, a countdown timer is initialized and displayed on screen. User is presented with a series of questions with 4 multiple choice options. User will select/click an answer choice and the next question and answer set will be presented. When all questions have been answered, or the timer has run out, user score is calculated and user can enter their name and be added to the list of persisted scores.
  
User will be shown leader board modal with the option
at game end or by clicking on the 'Highscores' link in the navbar. Use will have ability to close leader board modal and clearing currently saved users and scores.

- Visit the project page:
  https://ehoversten.github.io/quiz_game/

&nbsp;

## Technologies:

- Python (ver 3.6.5)
- Django (ver 2.2.15)
- HTML 5
- CSS 3
- JavaScript

&nbsp;

## Usage:

![Game Start Image](./assets/img/game_start.png)

![Question Image](./assets/img/question.png)

![User Form Image](./assets/img/user_form.png)

![Game Leaderboard Image](./assets/img/leaderboard.png)

## Instructions

Clone repo to your local machine
```python
$ git clone  ....
```

Open a terminal and change directories into the Travel-Buddy/ directory
```python
$ cd Travel-Buddy/
```

Install your preferred python virtual environment with Python version 3.6.5
```python
$ pip install venv
```

Install django application by running
```python
$ pip install -r requirements.txt
```

Run the application
```python
$ cd src/
$ python manage.py runserver
```

&nbsp;

## Maintainers

- Erik Hoversten
- Jose Gonzalez

## License:

Licensed under the MIT license.
