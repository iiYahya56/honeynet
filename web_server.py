from flask import Flask, request, render_template_string
from honeynet.logger import log_attempt

app = Flask(__name__)

LOGIN_HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>Secure Login</title>
</head>
<body>
  <h2>Login Panel</h2>
  <form method="POST">
    <label>Username:</label><br>
    <input type="text" name="username"><br><br>
    <label>Password:</label><br>
    <input type="password" name="password"><br><br>
    <input type="submit" value="Login">
  </form>
  {% if error %}<p style="color:red">{{ error }}</p>{% endif %}
</body>
</html>
"""

@app.route('/', methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        ip = request.remote_addr
        username = request.form.get("username")
        password = request.form.get("password")
        user_agent = request.headers.get("User-Agent")
        log_attempt(ip, username, password, user_agent)
        error = "Invalid credentials."
    return render_template_string(LOGIN_HTML, error=error)
