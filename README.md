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
- The second endpoint "/transactions/load_data" POST receives as body an email, it will create a user with this email if it has not been created before, it will associate all the transactions registered in the file "credit_debit_data.csv" and it will return a message, this same message is sent to the user's email.