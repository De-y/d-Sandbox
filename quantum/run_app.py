"""
Create a application to run flask from any directory using argparse for the command with a required field for a app to run and an optional argument for a port.
"""

import argparse
import os
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Run a Flask app.')
    # parser.add_argument('app', help='The name of the app to run.')
    parser.add_argument('port', help='The port to run the app on.', default=5000)
    #    parser.add_argument('--folder', help='The location that the app is running on.') Make this have a string
    parser.add_argument('--folder', help='The location that the app is running on.', default=None)
    args = parser.parse_args()

    print(args.folder)
    # Change the current working directory to the folder that the app is running on.
    if args.folder is not None:
        cwd = args.folder
        os.chdir(args.folder)

    # Get the current working directory and add it to the path.
    if args.folder is None:
        cwd = os.getcwd()
    
    sys.path.append(cwd)

    #Import the app variable from the current working directory by scanning all the files in the root directory.
    app = None
    for file in os.listdir(cwd):
        print(file)
        if file.endswith('.py'):
            module = __import__(file[:-3])
            if hasattr(module, 'app'):
                app = module.app
                break
    
    if app is None:
        print('No app found. Make sure you have an app variable in your python files.')
        sys.exit(1)
    
    try:
        app.run(port=args.port)
    except:
        app.run()