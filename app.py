from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Create Database
conn = sqlite3.connect("leave.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS leave_requests(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    employee_id TEXT,
    leave_type TEXT,
    from_date TEXT,
    to_date TEXT,
    status TEXT
)
""")

conn.commit()
conn.close()


@app.route("/employee")
def employee():
    return render_template("index.html")


@app.route("/submit_leave", methods=["POST"])
def submit_leave():

    name = request.form["name"]
    employee_id = request.form["employee_id"]
    leave_type = request.form["leave_type"]
    from_date = request.form["from_date"]
    to_date = request.form["to_date"]

    conn = sqlite3.connect("leave.db")
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO leave_requests
    (name, employee_id, leave_type, from_date, to_date, status)
    VALUES (?, ?, ?, ?, ?, ?)
    """,
    (name, employee_id, leave_type, from_date, to_date, "pending"))

    conn.commit()
    conn.close()

    return render_template("success.html")


@app.route("/view_leaves")
def view_leaves():

    conn = sqlite3.connect("leave.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM leave_requests")
    rows = cursor.fetchall()

    conn.close()

    return render_template("view_leaves.html", rows=rows)


@app.route("/delete/<int:id>")
def delete_leave(id):

    conn = sqlite3.connect("leave.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM leave_requests WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect("/view_leaves")


@app.route("/hr")
def hr_page():

    conn = sqlite3.connect("leave.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM leave_requests")
    rows = cursor.fetchall()

    conn.close()

    return render_template("hr_page.html", rows=rows)


@app.route("/approve/<int:leave_id>")
def approve_leave(leave_id):

    conn = sqlite3.connect("leave.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE leave_requests SET status='approved' WHERE id=?",
        (leave_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("hr_page"))


@app.route("/reject/<int:leave_id>")
def reject_leave(leave_id):

    conn = sqlite3.connect("leave.db")
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE leave_requests SET status='rejected' WHERE id=?",
        (leave_id,)
    )

    conn.commit()
    conn.close()

    return redirect(url_for("hr_page"))
@app.route("/")
def home():
    return render_template("home.html")
@app.route("/hr_login")
def hr_login():
    return render_template("hr_login.html")

if __name__ == "__main__":
    app.run(debug=True)