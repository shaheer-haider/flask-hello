from flask import Flask

app = Flask(__name__)

template = """
<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>RUNNING FLASK ON GCE</title>
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    </head>
    <body>
        <div class="container">
            <div class="jumbotron text-center">
                <h2>FLASK APPLICATION RUNNING ON GCE</h4>
                <p>Conventionally, Flask looks for view files in a folder with specific name. For the same reason we need to create a folder with the `templates` name and add our view files. In the `templates` folder, create a new file and name it `home.html`. This file contains the code snippets rendered on the homepage of our application.
                </p>
            </div>
        </div>
    </body>
</html>
"""
@app.route('/')
def index():
    return template

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
