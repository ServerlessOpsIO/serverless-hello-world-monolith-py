#!/usr/bin/env python
'''Handler entry'''
import app

handler = app.create_app()

if __name__ == '__main__':
    # Entry point when run via Python interpreter.
    print("== Running in debug mode ==")
    app.create_app().run(host='0.0.0.0', port=8080, debug=True)

