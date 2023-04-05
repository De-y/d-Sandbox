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
        password = 'Welcome to the de-y"s personal CDN' + request.form['password'] + 'aviance SALT.'
        password = hashlib.sha3_512(password.encode()).hexdigest()
        print(password)
        if password != '121a07d9a00343dd1ecc5549ccdd92bbcbdabdb233dce77f66bc0b29c662d08a61f3ede8ca20f887fed14415ab4282f3f78862a846f32e4ac0b65f811b3fd1c0':
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