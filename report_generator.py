import sqlite3
from honeynet import config

def generate_html_report(output_file="reports/report.html"):
    conn = sqlite3.connect(config.DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT ip, username, password, user_agent, timestamp FROM logins ORDER BY timestamp DESC")
    rows = cursor.fetchall()
    conn.close()

    html = """
    <html><head><title>HoneyNet Report</title></head><body>
    <h1>HoneyNet Activity Report</h1>
    <table border="1">
    <tr><th>IP</th><th>Username</th><th>Password</th><th>User-Agent</th><th>Timestamp</th></tr>
    """
    for row in rows:
        html += "<tr>" + "".join(f"<td>{x}</td>" for x in row) + "</tr>"
    html += "</table></body></html>"

    with open(output_file, "w") as f:
        f.write(html)
