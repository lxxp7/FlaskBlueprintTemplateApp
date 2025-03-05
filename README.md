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

