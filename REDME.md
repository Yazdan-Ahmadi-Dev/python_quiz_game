# Python Quiz GAME
A simole quiz game built with python
## Table of contents



- [Features](#features)
- [Project structure](#project-structure)
- [Requirments](#requirments)
- [Installation](#installation)
- [envoirment setup](#envoirment-setup)
- [Usage](#usage)
- [Example output](#example-output)
- [Screenshot](#screenshot)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Licence](#licence)
- [Author](#author)


## Features
- qize system 
  - Aska the player multiple question 
  - check the answer  automatoclly
  - calculates the final score 
- resulte storage 
  - save a quiz result file `result.txt`
- admin mode
  - askes for the admin passwords
  - check id the password is correct 
  - keeps the passwords outside the mine python file
    python files
    - loads the password from `.env`


## Project structure

```text
python_quiz_game/
│   .env.example
│   .gitignore
│   main.py
|   requirment.txt
│   question.py
│   README.md
│   result.txt
```
### file description
- `main.py` - mai file usedd to run quiz game
- `question.py` - stores question and answer 
- `requirment.txt` - list python pyckages inthe project
- `.env.example` - show the envoirment variebels needed by the project
- `.gitignor` - tells git which files not trackted
- `.gitignor` -contains the project
- `readme.md` - 

## Requirments
- `python 3`
- `python-dotenv`

## Installation
1. open terminal in the project folder
2. check that python in installed
```bash
python --version
```
3. install the python package:
```bash
pip install -r requirements.txt
```
## envoirment setup
create a `.env` file from `.env.example `
```bash
cp .env.example .env
```
2. open the new `.env `file
3. replaxe the example value with yore own password
```text
QUUIZ_ADMIN_PASSWORD=your password
```
4. save the file
5. 
> do not commit your `.env` file 
## Usage
1. open a terminal in the project 
2. run the quiz game
```bash
python main.py
```
3. choose `yes` or `no` from admin mode
4. if you choose `yes` you should enter passport
5. enter your name 
6. answer the question 
7. see your final score and massege 
8. you result is saved in `result.txt`


## screenshot
### start game
![srart game](pic\1.png)

### quiz
![quiz game](pic\2.png)

### quiz
![quiz game](pic\3.png)
## Roadmap
- [x] add multiple quiz qestion
- [x] calculate the final score
- [x] save result to a file
- [x] add admin mode
- [ ] add more quiz questions
- [ ] add difficultli
- [ ] add a timer
## Contributing

## Licence

## Author
creat by [yazdan ahmadi](https://github.com/Yazdan-Ahmadi-Dev)