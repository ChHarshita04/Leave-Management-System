# Leave-Management-System

A web-based Leave Management System built using Flask and SQLite that allows employees to submit leave requests and enables HR to approve or reject them.

## Features

- Employee leave request submission
- HR login panel
- View all leave requests
- Approve or reject leave requests
- Leave status tracking
- Simple and user-friendly interface

## Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS

## Project Structure
leave_request_system/
│
├── app.py
├── leave.db
├── static/
│ ├── style.css
│ └── leave_background.jpg
│
├── templates/
│ ├── index.html
│ ├── home.html
│ ├── hr_login.html
│ ├── hr_page.html
│ ├── success.html
│ └── view_leaves.html

## How to Run

### 1. Install Flask

```bash
pip install flask
```

### 2. Run the application

```bash
python app.py
```

### 3. Open browser and visit

```text
http://127.0.0.1:5000
```
