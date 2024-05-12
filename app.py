from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.tailwindcss.com"></script>
    <title>Index</title>
</head>
<body>
    <main class="bg-black mx-auto text-center min-h-screen min-w-full">
        <h1 class="text-4xl text-pink-500">Hello world</h1>
    </main>
</body>
</html>
    '''
