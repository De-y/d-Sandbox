from flask import Flask, request, send_from_directory
import hashlib, os

app = Flask(__name__)

# Route to serve static files from the 'static' directory
@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('/tmp/', filename)

# Create an upload route that upload files from the get request

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        try:
            # Create 'static' directory if it doesn't exist
            if not os.path.exists('/tmp/'):
                os.makedirs('/tmp/')
            
            password = 'Welcome to the de-y"s personal CDN' + request.form['password'] + 'aviance SALT.'
            password = hashlib.sha3_512(password.encode()).hexdigest()
            print(password)
            if password != '9f82007a073647ef7c36669eafba878cb82f68f285f923f5a3ee22aaf3e524fb8e95f60bf6f11caa846e6ad7ed6e1661a5eca939b02c4e449747b70b47c1c59c':
                return 'Wrong password'
            
            file = request.files['file']
            file.save('/tmp/' + file.filename)
            return 'File uploaded successfully, go see it at: <a href="https://de-yscdn.vercel.app/' + file.filename + '">https://de-yscdn.vercel.app/' + file.filename + '</a>'
        except Exception as e:
            print(e)
            return 'Error uploading file, error:' + str(e)
    
    if request.method == 'GET':
        return """
        <!DOCTYPE html>
        <html>
        <body>
        <form action="/upload" method="post" enctype="multipart/form-data">
        <center>
        Select file to upload and enter the key:<br><br>
        <input type="file" name="file" id="file"><br><br>
        <input type="text" value="Password" name="password"><br><br>
        <input type="submit" value="Upload" name="submit">
        </center>
        </form>
        </body>
        </html>
    
        """


if __name__ == '__main__':
    app.run(debug=True, port=3000)