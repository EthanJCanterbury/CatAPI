
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

## API Endpoints

1. GET `/api/cat` - Get a random cat image
2. GET `/api/cats/count` - Get total number of cats
3. GET `/api/cats/list` - Get list of all cat filenames
4. GET `/api/cats/random/{count}` - Get multiple random cats (1-5)
5. POST `/api/cats/vote` - Vote for a cat (requires JSON body with cat_id)

### Examples

Get a random cat:
```python
import requests
response = requests.get('https://your-repl-url/api/cat')
with open('cat.jpg', 'wb') as f:
    f.write(response.content)
```

Vote for a cat:
```python
import requests
response = requests.post('https://your-repl-url/api/cats/vote', 
                        json={'cat_id': 'cat1.jpg'})
print(response.json())
```

Python example:
```python
import requests
response = requests.get('https://your-repl-url/api/cat')
with open('cat.jpg', 'wb') as f:
    f.write(response.content)
```
