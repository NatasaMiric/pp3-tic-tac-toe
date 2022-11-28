# TIC-TAC-TOE

Tic Tac Toe is a Python terminal game, which runs in the Code Institute mock terminal on Heroku.

Users are playing against the computer by selecting one of the nine squares on the grid in each round. The player who gets his three marks on vertical, horizontal or diagonal row is the winner. 

[Live version of my project]()

# How to play

Tic Tac Toe is based on the classic pen and paper game that requires logical thinking. You can read more about it on [Wikipedia](https://en.wikipedia.org/wiki/Tic-tac-toe). 

In this version, the player is represented with the 'X' sign and the computer with 'O'.

Players take turns by entering a number from 1 to 9, corresponding to the square in the 3*3 grid.   

After each round, the user can see his and the computer's choice on the board. 

The winner is the first player who gets his three marks ('X' or 'O') on a vertical, horizontal, or diagonal row.    

## Table of Content

* [Flowchart](#Flowchart)

* [User Stories](#User-Stories)

* [Features](#Features)
  * [Existing features](#existing-features)
  * [Future Features](#future-features)
  
* [Technologies Used](#Technologies-Used)
  * [Languages & Libraries](#Languages-&-Libraries)
  * [Programs](#Programs) 

* [Testing](#Testing)
  * [Validator Testing](#validator-testing) 
  * [Testing User Stories](#testing-user-stories)
      
 * [Deployment](#Deployment)

* [Credits](#Credits)
  * [Code Used](#Code-Used)
  * [Content](#Content)
  
------
## Flowchart

## User Stories

 * As a visiting user, I would like to be able to play the game against an opponent.
 * As a visiting user, I would like to be able to see my and the computers choice on the board.
 * As a visiting user, I would like to be able to restart the game. 

## Features
### Existing features

**Displays the welcome message and asks the user to input the name**

**Displays the rules of the game**

**Displays the game board**

**Accepts user input**

**Play against the computer**

**Generates random computer input**

**Input validation and error-checking**
  * You must enter the numbers
  * You cannot enter numbers less than 1 and greater than 9
  * You cannot choose an already occupied square 

### Future Features

* Allow the player to choose his symbol for playing.
* Randomly choose which player is going first.
* Keep track of the score on the scoreboard.
* Implement different levels of game difficulty: easy, medium and hard.

## Technologies Used

### Languages & Libraries

Python - for building the game. 
JavaScript - generated from the python essential template built by Code Institute.
HTML - generated from the python essential template built by Code Institute.

The following Python libraries were used:
  * random -  to randomize the choices for the computer,
  * os -  to eliminate previous code on the terminal window making it clutter free and improves UX.

  ### Programs

GitHub- was used to store the project.

Git - was used for version control.

Visual Studio - was used as a local IDE.

Heroku - was used to deploy the app.

[Lucid Chart](https://www.lucidchart.com/pages/landing?utm_source=google&utm_medium=cpc&utm_campaign=branded_sitelink_en_lucidchart&km_CPC_CampaignId=1490375427&km_CPC_AdGroupID=55688909257&km_CPC_Keyword=lucid%20chart&km_CPC_MatchType=e&km_CPC_ExtensionID=21193716975&km_CPC_Network=g&km_CPC_AdPosition=&km_CPC_Creative=442433236001&km_CPC_TargetID=kwd-55720648523&km_CPC_Country=1012212&km_CPC_Device=c&km_CPC_placement=&km_CPC_target=&gclid=Cj0KCQiAsoycBhC6ARIsAPPbeLsu4EhgeL7oc8f5b4Q0lNfOeEAW1uvF-pLQ2OGzaXgm9ZB7HkvQCDUaAoXdEALw_wcB) - was used for creating and designing the flowchart of the project.

## Testing
### Validator Testing
### Testing User Stories

## Deployment

The game was deployed on Heroku. The following steps were used to deploy the game to Heroku:

  * Sign into Heroku.
  * On the main dashboard choose to Create new app.
  * Choose a unique name for your project and the region, based on where you are located (as   I'm in Europe, I chose Europe), and then click on Create app.
  * Then go to the Settings tab.
  * In Settings click on Reveal Config Vars and enter the following key: PORT and     
    value: 8000.    
  * Next scroll down to Buildpacks and click Add buildpack, choose Python and then click Save 
    changes.
  * Repeat the above step and select nodejs and click Save changes.
  * Next go to the Deploy tab.
  * Under the Deployment method choose Github and then click Connect to GitHub you will probably be prompted to sign into your GitHub.
  * Then you can search for your GitHub repository, in my case this was pp3-tic-tac-toe and click connect.
  * To deploy automatically you will need to select Enable Automatic Deploys which will rebuild the app every time you push a change to GitHub.
  * To deploy manually go to the Manual deploy section below and click Deploy Branch. Just remember you will need to do this every time you make a change to your code on Github.
  * Below you will see your app was successfully deployed with a view button below this that will take you to the URL of your deployed app.


## Credits

* Code Institute for the deployment terminal.
* Wikipedia for the details of the Tic-Tac-Toe game. 
* [Stack Overflow](https://stackoverflow.com/questions/33203038/nested-loops-in-nested-lists) for finding the solution on how to check the winning condition in the game.
* [YouTube video](https://www.youtube.com/watch?v=dK6gJw4-NCo&t=1245s) for inspiration and ideas on how to implement the game. 