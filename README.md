[![Build Status](https://travis-ci.org/TheSteelGuy/Ride-My-WayApiV1.svg?branch=ft-Getmethods-%23158520402)](https://travis-ci.org/TheSteelGuy/Ride-My-WayApiV1)
[![Coverage Status](https://coveralls.io/repos/github/TheSteelGuy/Ride-My-WayApiV1/badge.svg?branch=ft-Getmethods-%23158520402)](https://coveralls.io/github/TheSteelGuy/Ride-My-WayApiV1?branch=ft-Getmethods-%23158520402)
[![Maintainability](https://api.codeclimate.com/v1/badges/e2de538dbd66b0ebc848/maintainability)](https://codeclimate.com/github/TheSteelGuy/Ride-My-WayApiV1/maintainability)

# Ride-my-wayAPIv1


### Introduction
Ride-my App is a carpooling application that provides drivers with the ability to create ride offers
and passengers to join available ride offers.
Required Features
1. Users can create an account and log in.
2. Drivers can add ride offers..
3. Passengers can view all available ride offers.
4. Passengers can see the details of a ride offer and request to join the ride. E.g What time
the ride leaves, and where it is headed 
5. Drivers can view the requests to the ride offer they created.
6. Drivers can either accept or reject a ride request.

#### Getting Started




#### Setting
* First install the virtual environment globally `sudo pip instal virtualenv`
* create the virtual enviroment `virtualenv --python=python2 myenv`
* change directory to myenv
* activate virtual environment `source myenv/bin/activate`
* clone the repo by running on terminal `git clone https://github.com/TheSteelGuy/Ride-My-WayApiV1.git `
* run pip install -r requirements.txt
* change directory to the repo `cd the cloned repo`

#### How to run flask
* Run  `python run.py`

### test endpoints using postman
send `GET, POST, DELETE` to there equivalent endpoints each time passing required parameters. 

Interact with the Api live at https://infinite-dusk-68356.herokuapp.com/


#### Testing:
run ```pytest --cov=api```


*`
#### Ride my way API endpoints

| Endpoints                                       |       Functionality                  |
| ------------------------------------------------|:------------------------------------:|
| `POST /aut/api/v1/signup`                       |  creates a user
| `POST /api/v1/auth/signin                       |  login a user                        |   
| `GET  /api/v1/rides/<rideId>`                   |  Get a ride                          |
| `GET  /api/v1/rides`                            |  gets all rides                      |
| `DELETE /api/v1/rides/<rideId>`                 |  deletes/cancels                     |
| `POST  /api/v1/users/rideId/requests`           |  Request to join aride               |
|` POST auth/api/v1/logout`                       |  logs out a user                     |
