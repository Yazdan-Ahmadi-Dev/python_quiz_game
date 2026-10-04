
# Python Quiz GAME.
![Static Badge](https://img.shields.io/badge/python%203.15-blue)

A simole quiz game built with python
## Table of contents


- [Features](#features)
- [Project structure](#project-structure)
- [Requirments](#requirments)
- [Installation](#installation)
- [envoirment setup](#envoirment-setup)
- [Usage](#usage)
- [Example output](#example-output)
- [Screanshot](#screanshot)
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
│   question.py
│   README.md
│
├───gif
│       animation.gif.gif
│       quiz_demo.gif
├───pic
│       1.png
│       2.png

```
### file description
| file | description | 
|--- | --- |
| `main.py` | mai file usedd to run quiz game|
| `question.py` | stores question and answer |
| `requirment.txt` | list python pyckages inthe |project|
| `.env.example` | show the envoirment variebels| needed by the project|
| `.gitignor` | tells git which files not trackted|
| `.gitignor` |contains the project|
| `readme.md` | 
| `pic` | stores project screnshot  |
| `pic1` | start code |
| `pic2` | finally code |
| `gifs` | stores demo gif fils |
| `demo.gif` | shows the project demo |

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

## Example output
do u to open admin mode yes/no
no
what your name? yourname

what language are we using?your language using
wrong

what command starts a git?git
wrong

what command show git status?git status
correct

your score is: 1 out of  3

keep practicing yourname
## Screanshot

### start game

![start game](/pic/1.png)

### quiz and final
![start game](/pic/2.png)

## Demo
![quiz game demo](gif\quiz_demo.gif)


## Roadmap
- [x] add multiple quiz question 
- [x] calculate thefinal score
- [x] save result 
- [x] add admin mode
- [ ] add more question 
- [ ] add difficltly leavels
- [ ] add timer


## Contributing

## Licence

## Author

create by [Yazdan Ahmadi]((https://github.com/Yazdan-Ahmadi-Dev))