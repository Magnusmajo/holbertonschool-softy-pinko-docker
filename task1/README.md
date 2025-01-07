From task0, we want to modify the Dockerfile to install Python3, pip3, and Flask. You may not have used Flask yet, but don't worry; for this project, we will provide all the necessary Flask code to get you started. We’ll validate the installation by running a Flask server with one endpoint that returns “Hello, World!” when called.

### Steps to Follow

1. **Install Python3, pip3, and Flask**
    - Use the `-y` flag with `apt-get` to automatically install and skip user input.
    - Install Flask using `pip3`, not `apt-get`.

    ```Dockerfile
    RUN apt-get update && apt-get install -y python3 python3-pip
    RUN pip3 install flask
    ```

    - If you encounter a `This environment is externally managed` error when installing Python packages, add the following line before calling `pip` in your Dockerfile:

    ```Dockerfile
    RUN rm /usr/lib/python*/EXTERNALLY-MANAGED
    ```

2. **Create a Python File**
    - Locally, create a Python file named `api.py` and paste the following script. This script uses Flask to create one endpoint that returns “Hello, World!” when called.

    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
         return 'Hello, World!'

    if __name__ == '__main__':
         app.run(host='0.0.0.0', port=5252)
    ```

    - Hosting this Flask app on `0.0.0.0` instead of `127.0.0.1` makes it reachable outside of the current machine (the current machine being a Docker container running inside your laptop/desktop).
    - Host this Flask app on port `5252`.