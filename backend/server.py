from supertokens_python import get_all_cors_headers
from flask import Flask, abort
from flask_cors import CORS
from supertokens_python.framework.flask import Middleware

app = Flask(__name__)
Middleware(app)

# TODO: Add APIs

CORS(
    app=app,
    origins=[
        "http://localhost:3567"
    ],
    supports_credentials=True,
    allow_headers=["Content-Type"] + get_all_cors_headers(),
)

# This is required since if this is not there, then OPTIONS requests for
# the APIs exposed by the supertokens' Middleware will return a 404
@app.route('/', defaults={'u_path': ''})
@app.route('/<path:u_path>')
def catch_all(u_path: str):
    abort(404)

# TODO: start server