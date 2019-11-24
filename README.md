# HackaTUM2019: BMW Challenge
## Inspiration

* Encouraging people to have an efficient drive via a leaderboard 
* inspired from the social fitness network Strava

## What it does

* Encouraging people to have an efficient drive via a leaderboard 
* Companies sponsor the challenge for a particular route
* Cars/drivers undertake it
* Every month all users on a particular route is evaluated in the form of a leaderboard based on the average fuel consumption on that route
* The user with least fuel consumption (present at the top of the chart) receives a token.

## How we built it

* Frontend:
   * Python Flask
* Backend:
   * Solidity:
      * deploy the smart contract
      * add User: adding a new user to the app
      * add route: new challenge route is added to the system
      * subscribe to the route: user subscribing to the challenge
      * add drive to route: user drives along the subscribed challenge
      * get the average fuel consumption score for the subscribed route
      * transfer rewards (tokens) at the end of the month
* Integration:
   * Web3js

## Challenges we ran into

* New topic -- new concept & technologies (Solidity, Blockchains etc.)
* Integrating backend and frontend
* Sleep deprivation, not enough pizza ;)

## Accomplishments that we're proud of

* Our awesome team! B-)
* Successfully deploying a smart contract using ethereum 
* Surviving the Hackathon ;) 

## What we learned

* Concepts of Blockchain, Ethereum, Smart contracts
* Flask

## What's next for IncentiDRIVE

* This can be extended as tokens for sustainable charging of electric cars
