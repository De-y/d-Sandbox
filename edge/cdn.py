from flask import Flask, request, send_from_directory
import hashlib

app = Flask(__name__)

# Route to serve static files from the 'static' directory
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

# Create an upload route that upload files from the get request

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        password = 'Salt Test' + request.form['password'] + 'This isnt really a salt, but it does get the job done with the hash.'
        password = hashlib.sha3_512(password.encode()).hexdigest()
        print(password)
        if password != 'fcfb5a245b0252b9b45ec7ed10cc9ccf0066696ca3a7921c3691764a658869db481a1d28655496880c534aba29829c623275fbf8f27fd112731b5101c255a0b7':
            return 'Wrong password'
        
        
        file = request.files['file']
        file.save('static/' + file.filename)
        return 'File uploaded successfully'
    
    if request.method == 'GET':
        return """
        <!DOCTYPE html>
        <html>
        <body>
        <form action="/upload" method="post" enctype="multipart/form-data">
        <center>
        Select image to upload:<br><br>
        <input type="file" name="file" id="file"><br><br>
        <input type="text" value="Password" name="password"><br><br>
        <input type="submit" value="Upload Image" name="submit">
        </center>
        </form>
        </body>
        </html>
    
        """


if __name__ == '__main__':
    app.run(debug=True, port=3000)