# Service Template
This project aims to be a boilerplate for an asyncrhonous service with a REST API in front-end. It is based on Flask.

## Features
- Front-End API using Flask
- API versionning (using Flask's blueprint)
- Runs without any extra configuration
- Flask best practice
- Developpment/Production environement
- Scalable
- Ready to deploy


## Requirements
> Checkout requirements.txt for more details

- Flask
- Python (3 or 2.7)


## Installation
1. Clone the repo
2. (optional) search "service_name" and replace by the name of your service (Folders, Filename, in code).
3. Install a virtual environement to install dependencies
```bash
 python -m venv venv
```
4. Start the virtual environement
```bash
source venv/bin/activate
```
5. Install required dependencies if the requirements file exists
```bash
pip install -r requirements.txt
```
Else you might later want to write the necessary dependencies for the app
```bash
pip freeze > requirements.txt
```


## Usage
## Developement
1. Open a  terminal to run Flask's server
```bash
flask run -p "PORT"
```
or when needed in developement
```bash
flask run --debug -p "PORT"
```
