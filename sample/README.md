# Sample Flask app

To run the application:

- Install the dependencies
`pip install -r requirements.txt`

- Set the `FLASK_APP` and `FLASK_DEBUG` environment variables.

   - In Windows:
    ` set FLASK_APP=sample.py` and `set FLASK_DEBUG=1` (1 for debug mode).

   - In Linux:
    ` set FLASK_APP=sample.py` and `set FLASK_DEBUG=1` (1 for debug mode).

- Initialize the migrations management engine:
`flask db init`

- Create first migration
`flask db migrate`

- Upgrade
`flask db upgrade`

- Once everything is set, run the app:
`flask run`