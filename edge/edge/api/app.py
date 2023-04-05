from flask import Flask, request, send_from_directory
import hashlib, os

app = Flask(__name__)

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('/tmp/', filename)

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        try:
            if not os.path.exists('/tmp/'):
                os.makedirs('/tmp/')
            
            password = 'TestCDN' + request.form['password'] + 'Welcome to the TestCDN.'
            password = hashlib.sha3_512(password.encode()).hexdigest()
            print(password)
            if password != '3367a2008005663d366f6b4d239d0a90417490991c445293061900b851516b43a7d2c5146368a96f052768c0c81353d4aa979d9f39955ee0327c29d124b40c99':
                return 'Wrong password'
            
            file = request.files['file']
            filename = file.filename.replace(' ', '-')
            file.save('/tmp/' + filename)
            return 'File uploaded successfully, go see it at: <a href="https://testflaskcdn.vercel.app/' + filename + '">https://testflaskcdn.vercel.app/' + filename + '</a>'
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
        <p>Test flask CDN </p><br><br>
        Select file to upload and enter the key:<br><br>
        <input type="file" name="file" id="file"><br><br>
        <input type="text" value="TestPassword" name="password"><br><br>
        <input type="submit" value="Upload" name="submit">
        </center>
        </form>
        </body>
        </html>
    
        """

@app.route('/delete/<filename>', methods=['POST', 'GET'])
def delete_file(filename):
    if request.method == 'POST':
        try:
            password = 'TestCDN' + request.form['password'] + 'Welcome to the TestCDN.'
            password = hashlib.sha3_512(password.encode()).hexdigest()
            print(password)
            if password != '3367a2008005663d366f6b4d239d0a90417490991c445293061900b851516b43a7d2c5146368a96f052768c0c81353d4aa979d9f39955ee0327c29d124b40c99':
                return 'Wrong password'

            filepath = '/tmp/' + filename
            if os.path.exists(filepath):
                os.remove(filepath)
                return 'File deleted successfully'
            else:
                return 'File does not exist'
        except Exception as e:
            print(e)
            return 'Error deleting file, error:' + str(e)

    if request.method == 'GET':
        return """
        <!DOCTYPE html>
        <html>
        <body>
        <form action="/delete/""" + filename + """" method="post">
        <center>
        <p>Test flask CDN </p><br><br>
        Enter the key to delete the file:<br><br>
        <input type="text" value="TestPassword" name="password"><br><br>
        <input type="submit" value="Delete" name="submit">
        </center>
        </form>
        </body>
        </html>"""

if __name__ == '__main__':
    app.run(debug=True, port=3000)