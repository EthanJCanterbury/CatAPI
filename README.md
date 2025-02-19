
# Random Cat API

A simple Flask API that serves random cat pictures. Made by Ethan!

## Features
- Random cat image endpoint
- Landing page with usage instructions
- Simple to deploy and use

## Self-Hosting on Replit (Or any other hosting thingy idrc)

1. Fork this repl
2. Click the Run button
3. Your API will be available at your repl's URL

The API will be accessible at:
- Landing page: `https://your-repl-url/`
- Random cat endpoint: `https://your-repl-url/api/cat`

## Usage

Make a GET request to the `/api/cat` endpoint to receive a random cat image.

Python example:
```python
import requests
response = requests.get('https://your-repl-url/api/cat')
with open('cat.jpg', 'wb') as f:
    f.write(response.content)
```
