#!/usr/bin/env python3
#app.py
# author: newini
# data: April 2020
# description: A python flask example application to use Javascript-ROOT@CERN.


from flask import Flask, render_template


# Define application
app = Flask(__name__)

# Set route
@app.route('/')
def route_index():
    # Render to templates/read_root_file.html
    return render_template("read_root_file.html")

# Main
if __name__ == "__main__":
    # Run flask
    app.run()
