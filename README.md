# Service Template

This project is a boilerplate for an asynchronous service with a REST API in front-end, based on Flask.

## Features
- Front-End API using Flask
- API versioning (using Flask Blueprint)
- Runs without extra configuration
- Flask best practices
- Development/Production environments
- Scalable and ready to deploy

## Prerequisites
- Python 3.x (compatible with 2.7 but 3.x recommended)
- pip (Python package manager)
- Virtualenv (optional but recommended)

## Installation
1. Clone the repository
```bash
git clone <REPO_URL>
cd <PROJECT_NAME>
```
2. Open two separate terminals, one for the API and one for the frontend, or use different tabs:
```bash
cd PathToApi/Front
```
3. (Optional) Replace template names with your service names (folders, filenames, code).
4. Create a virtual environment to manage dependencies:
```bash
python -m venv venv
```
5. Activate the virtual environment:
   - Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   - macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
6. Install required dependencies if a `requirements.txt` file is present:
```bash
pip install -r requirements.txt
```
If `requirements.txt` does not exist, you can save the installed dependencies:
```bash
pip freeze > requirements.txt
```

## Setup SQLite Database
To use a simple database in your project, you can easily setup a SQLite database using Python

To create one, create a new file named "schema.sql" and write sql code to create the tables you need, in our example it will be 
```bash
DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);
```

Now create another file named "init_db.py" and write
```bash
import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('First Post', 'Content for the first post')
            )

cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
            ('Second Post', 'Content for the second post')
            )

connection.commit()
connection.close()
```

Then run :
```bash
python init_db.py
```
It will create a database named database.db and create your tables as well as inserting some values.

## Usage
### Development Mode
1. Open a terminal to run the Flask server:
```bash
flask run -p <PORT>
```
2. To enable debug mode during development:
```bash
flask run --debug -p <PORT>
```

