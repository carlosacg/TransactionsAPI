# TransactionsAPI

### About

This project is an API developed in Python with Flask, SQLAlchemy.


### Installation

1. Clone this repository.

2. If you do not have Docker in your computer, install it. https://www.docker.com/products/docker-desktop/

3. Once the repository is cloned, access the environment variables file located in "conf/environments/.env-development" and add your database credentials and google account data for sending emails.

4. Once you have configured your environment variables you can proceed to run the program by executing "docker-compose build" and then "docker-compose up".


### How to use it

The API has two endpoints and runs on port 8084.
- The first endpoint "/" GET simply returns a welcome message, implying that the program is running.
<img width="613" alt="Screen Shot 2022-07-19 at 4 30 44 PM" src="https://user-images.githubusercontent.com/24283414/179851987-eb0abf6a-f9fa-4488-bc63-0afee5bafa88.png">

- The second endpoint "/transactions/load_data" POST receives as body an email, it will create a user with this email if it has not been created before, it will associate all the transactions registered in the file "credit_debit_data.csv" and it will return a message, this same message is sent to the user's email.
<img width="791" alt="Screen Shot 2022-07-19 at 4 32 22 PM" src="https://user-images.githubusercontent.com/24283414/179852181-6c4e537d-f3f2-4ca9-838a-c00df0a92ce4.png">

<img width="732" alt="Screen Shot 2022-07-19 at 4 32 58 PM" src="https://user-images.githubusercontent.com/24283414/179852264-4797bd95-298a-4fb0-b5bd-0d5f1abac7fb.png">

### More info

The architecture used in this project is MVC(Model, View, Controller).

The models involved are the following:

<img width="697" alt="Screen Shot 2022-07-19 at 4 39 34 PM" src="https://user-images.githubusercontent.com/24283414/179853283-fbf53f26-13a7-4fd5-a2d2-3838522d951b.png">

