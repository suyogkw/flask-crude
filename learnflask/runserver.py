"""
This script runs the learnflask application using a development server.
"""

from os import environ
from learnflask import app

if __name__ == '__main__':
    app.run(port=5000,debug=True)
