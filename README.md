[![Build Status](https://travis-ci.org/TheSteelGuy/Ride-My-WayApiV1.svg?branch=ft-Getmethods-%23158520402)](https://travis-ci.org/TheSteelGuy/Ride-My-WayApiV1)
[![Coverage Status](https://coveralls.io/repos/github/TheSteelGuy/Ride-My-WayApiV1/badge.svg?branch=ft-Getmethods-%23158520402)](https://coveralls.io/github/TheSteelGuy/Ride-My-WayApiV1?branch=ft-Getmethods-%23158520402)
[![Maintainability](https://api.codeclimate.com/v1/badges/e2de538dbd66b0ebc848/maintainability)](https://codeclimate.com/github/TheSteelGuy/Ride-My-WayApiV1/maintainability)

# Ride-my-wayAPIv1

## Introduction
* An API for the Ride-my-way front end app.
* Ride-my-way App is a carpooling application that provides drivers with the ability to    
  create ride offers and passengers to join available ride offers.
## NB
The app purely uses python data structures hence no persistance

## Technologies used & needed.
* **[Python2](https://www.python.org/downloads/)**).
* **[Flask](flask.pocoo.org/)**  

## Link to heroku:
https://infinite-dusk-68356.herokuapp.com/
## Current endpoints(More to follow)
*  #### User signup. 

    `POST /api/v1/auth/signup`: 
    ```
    headers = {content_type:application/json}

    {
        "name": "collo",
        "email: "070-333-2222",
        "password: "12345",
        "confirm_pwd":"1234"
    }
    ```

* #### User sigin.
    `POST /api/v1/auth/login`: 
    ```
    headers = {content_type:application/json}

    {
        "username":"collo",
        "password": "1234"
    }
    ```

* #### User Logout. 
    `POST /api/v1/auth/logout`
    ```
    headers = {content_type:application/json}
    ```

* #### Create a ride offer.
    `POST /api/v1/users/rides`: 
    ```
    headers = {content_type:application/json}

    {
        "destination": "Mombasa",
        "date": "11-8-2018",
        "time": "26-06-2018 21:00",
        "meetpoint": "some description",
        "charges": 1200,
    }
    ```
* #### Get available rides.
    `GET /api/v1/rides`
    ```
    headers = {content_type:application/json}
    ```


* #### Get a specific ride.   
    `GET /api/v1/rides/<rideId>` 
    ```
    headers = {content_type:application/json} 
    ```
    

* #### Make requests to join a ride.
    `POST /api/v1/rides/<rideId>/requests`:
    ```
    headers = {content_type:application/json}

    {
        "destination": "mombasa"
    }
    ```
* #### Cancel a ride already offered 
    `DELETE /api/v1/rides/<rideId>/cancel`
    ```
    headers = {content_type:application/json}
    ```

## Installation guide and usage

 #### **Clone the repo.**
    ```
    $ git clone https://github.com/TheSteelGuy/Ride-My-WayApiV1.git
    ```
 #### **Create virtual environment & Activate.**
    ```
    $ virtualenv -p python myenv 
    $ source myenv/bin/activate
    ```
 #### **Install Dependancies.**
    ```
    (myenv)$ pip install -r requirements.txt
    ```
 #### **Enviroment variables.**



 #### **Run the app**
   ```
    (myenv)$ python run.py
   ```
 #### **Run Tests**
  ```
  (myenv)$ pytest --cov=tests
  ```
### Summary of the endpoints

| Endpoints                                       |       Functionality                  |
| ------------------------------------------------|:------------------------------------:|
| `POST /api/v1/auth/signup`                      |  creates a user
| `POST /api/v1/auth/signin `                     |  login a user                        |   
| `GET  /api/v1/rides/<rideId>`                   |  Get a ride                          |
| `GET  /api/v1/users/rides`                            |  gets all rides                      |
| `DELETE /api/v1/rides/<rideId>`                 |  deletes/cancels                     |
| `POST  /api/v1/users/rideId/requests`           |  Request to join aride               |
|` POST /api/v1/auth/logout`                      |  logs out a user                     |
