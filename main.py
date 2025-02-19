from flask import Flask, send_file, render_template_string
import random
import os

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>CatAPI (Cat-app-y)</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
        }
        .demo {
            margin: 20px 0;
            padding: 20px;
            background: #f5f5f5;
            border-radius: 8px;
        }
        code {
            background: #e0e0e0;
            padding: 2px 5px;
            border-radius: 3px;
        }
    </style>
</head>
<body>
    <h1>🐈 CatAPI (Cat-app-y)</h1>
    <p>A simple API to get random cat images. Made by Ethan C for RaspAPI!</p>
    <p>Get a random cat image from our collection!</p>
    
    <div class="demo">
        <h2>API Usage</h2>
        <p>Make a GET request to: <code>{{ request.host_url }}api/cat</code></p>
        <p>Try it now: <a href="/api/cat" target="_blank">Get Random Cat</a></p>
    </div>

    <div class="demo">
        <h2>Python Example</h2>
        <code>
            import requests<br>
            response = requests.get('{{ request.host_url }}api/cat')<br>
            with open('cat.jpg', 'wb') as f:<br>
            &nbsp;&nbsp;&nbsp;&nbsp;f.write(response.content)
        </code>
    </div>
</body>
</html>
'''


@app.route('/')
def index():
    return render_template_string(HTML)


@app.route('/api/cat')
def random_cat():
    cat_dir = 'cats'
    cat_files = [
        f for f in os.listdir(cat_dir)
        if f.startswith('cat') and f.endswith('.jpg')
    ]
    random_cat = random.choice(cat_files)
    return send_file(os.path.join(cat_dir, random_cat), mimetype='image/jpeg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
