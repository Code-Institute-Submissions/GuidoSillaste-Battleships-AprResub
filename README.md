# BAD BATTLESHIP GAME Left the name since im not happy

[Live link](https://very-bad-battleship.herokuapp.com/)

Bad Battleship Game is python terminal game which i ran in code institute mock terminal in heroku.

User have to first set all battleships on the board.Each battleship is diffrent size and direction for your board and computers.

## how to play

Game start of with you placing the ships.

Once placed you are shown your board and you can start shooting the enemy by writing a number from 00 to 99.

Missed shots are X and hit ships are O.

Once all ships sank for either you or computer the game is over.

## UX

## Strategy

### Vision

The Bad Battleship game is a old classic game brought to life whit limited python skills inside a terminal.

![Flow Chart]()

### External users goal

- The application user wants to play a logic game

### My Goal

- The Battleships game is played on grids on which each player's fleet of battleships are marked. The locations of the fleets are concealed from the other player. Players call shots at the other player's ships, and the objective of the game is to destroy the opposing player's fleet.
- The application provides a working battleships game for a single user to play against the computer .e.g.
- To Test my skills

### User Stories

As a new and returning user, I want to...

    - Know the theme of the game as soon as I navigate to the landing page.
    - I want to be able to interact with the game. 
    - I want it to feel more personal with choices only I can make.
    - I want to be able to distinguish between the choices I must make in the game.
    - Have an interesting and in-depth storyline.

## Features

### Home Page

The home page is the only page on the application. The terminal design was created and given to me by Code Institue.
Few exsisting features:

- You can choose your board
- Computer board is generated randomly
- ships are hidden
- can only play against computer
- Accepts user input
- input validation error
  - if number 2 big or not a number
  - can not enter same number on either ship placing or shooting

### Future features

- turn to class based
- add secound player
- show scores
- show if ship is sunk and if you hit it
- Create better UI

## Technology Used in design

Throughout the planning, design, testing, and deployment of the website, I have used several technologies.

- [Python](https://www.python.org/):
  - Python is the core programming language used to write all of the code in this application to make it fully functional.
- [GitHub](https://github.com/dashboard):
  - Used to store code for the project after being pushed.
- [Git](https://git-scm.com/):
  - Used for version control by utilizing the GitPod terminal to commit to Git and push to GitHub.
- [GitPod](https://gitpod.io/workspaces):
  - Used as the development environment.
- [Heroku](https://heroku.com/):
  - Used to deploy my application.
- [Lucid Chart](https://lucid.app/users/login#/login):
  - Used to create my flow chart of the story.
- [Pep8](http://pep8online.com/):
  - Used to check my code against Pep8 requirements.

## Data Model

Basic def, while, if, for, try and variable combo.

## Testing

Most of the testing was done manualy by playing the game.

Left 3 diffrent pep8 suggestions inside the code since i had no idea how to change those long lines of codes.

- Left [variable missed1] inside code since function check_shot() returns a missed shot value. Is mainly used for AI to calculate a better shot next turn.
- Left [ms-toolsai.jupyter extension is not synced, but not added in .gitpod.yml] inside it is not part of my code.
- Left [Consider using enumerate instead of iterating with range and len] since i could not reduce the code to enumerate form.

## Panic Time

Had to waste 3 days to get python to work on computer

17 days of nightmarish bugs and relearning and then repeating while being all alone whit no help.

2 many errors every last function was like hell other then the if,elif and else

None of the bugs i tried to fix were fixed

No code breaking bugs remain

### Validator testing

- PEP8
- contained lots of trailing whitespace that did not show up on visualstudio
- do not use bare 'except' added typeerror
- missing whitespace after ',' fixed by deleting lines
- Variable name "ch" doesn't conform to snake_case naming style fixed by changing name
- Consider using enumerate instead of iterating with range and len
- Unused variable 'missed1' if i deleted it code did not work.
- No exception type(s) specified
- ms-toolsai.jupyter extension is not synced, but not added in .gitpod.yml <-- no idea why this is here.

## Deployment

This project static was stored on github and deployed on heroku whit code institute javascript and nodej.

1. Login or Sign Up to [GitHub](https://github.com/login "Link to GitHub login page")
2. Create a new repository.

- Give the repository a name.
- Under Repository template pick the [Code Institute Python Essentials Template](https://github.com/Code-Institute-Org/python-essentials-template).
- Click create repository
- Use GIT ADD.
- GIT COMMIT -m "Comments"
- GIT PUSH
- To commit the code and push to Github

Heroku section.

- Create a new heroku app
- set the var PORT value 8000
- set the buildbacks to python and nodejs
- link heroku app to the repository
- click on deploy

## Credits

- Youtube for training videos on how to make projects
- My own childhood where i played the game a lot
- lots of slackoverflow(was not very usefull) reading
- gitpod projects to see how python classes work(could not find a basic class one)
- especially a single youtube videos
