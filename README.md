<div align="center">

# Social Media Database

### A full-stack social media web application built with Streamlit & MySQL

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-Framework-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com)

---

**Login** | **Browse Images** | **Like & Comment** | **Engage**

</div>

## About

A lightweight social media platform where users can sign up, browse an image feed, like photos, and leave comments — all powered by a Streamlit frontend and a MySQL backend.

## Features

- **User Authentication** — Secure login and sign-up with duplicate username prevention
- **Image Feed** — Browse a curated gallery of images displayed in a clean layout
- **Like System** — Like your favorite images (one like per user per image)
- **Comments** — Leave comments on any image and see what others have to say
- **Session Management** — Persistent user sessions with logout support

## Tech Stack

| Layer      | Technology                  |
| ---------- | --------------------------- |
| Frontend   | Streamlit                   |
| Backend    | Python 3.11                 |
| Database   | MySQL                       |
| Imaging    | Pillow (PIL)                |
| Connector  | mysql-connector-python      |

## Project Structure

```
Social-media-Database/
├── user_auth.py             # Main app — login, signup & home page (Streamlit UI)
├── database_functions.py    # Database operations — likes, comments, user queries
├── database.py              # Core DB connection & query execution layer
├── session_state.py         # Custom session state management
└── images/
    ├── sample_image_1.jpg
    ├── sample_image_2.jpg
    └── sample_image_3.jpg
```

## Getting Started

### Prerequisites

- Python 3.11+
- MySQL Server running locally

### 1. Clone the repository

```bash
git clone git@github.com:ShashiBanagere/Social-media-Database.git
cd Social-media-Database
```

### 2. Install dependencies

```bash
pip install streamlit mysql-connector-python Pillow
```

### 3. Set up the MySQL database

Connect to your MySQL server and create the required database and tables:

```sql
CREATE DATABASE social_media;
USE social_media;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255)
);

CREATE TABLE likes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    image_id INT,
    username VARCHAR(255),
    like_count INT DEFAULT 1,
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE TABLE comments (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    image_id INT,
    comment TEXT,
    username VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

### 4. Configure database credentials

Update the connection details in `database.py` and `database_functions.py` with your MySQL credentials:

```python
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="social_media"
)
```

### 5. Run the application

```bash
streamlit run user_auth.py
```

The app will open in your browser at `http://localhost:8501`.

## Usage

1. **Sign Up** — Create a new account from the sidebar
2. **Login** — Enter your credentials to access the feed
3. **Browse** — Scroll through the image gallery
4. **Like** — Hit the heart button to like an image
5. **Comment** — Share your thoughts on any image
6. **Log Out** — End your session from the home page

## Database Schema

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│    users     │       │    likes     │       │  comments    │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ id (PK)     │──┐    │ id (PK)     │       │ id (PK)     │
│ username    │  ├───>│ user_id (FK)│       │ user_id (FK)│<──┐
│ password    │  │    │ image_id    │       │ image_id    │   │
│ first_name  │  │    │ username    │       │ comment     │   │
│ last_name   │  │    │ like_count  │       │ username    │   │
└─────────────┘  │    └─────────────┘       └─────────────┘   │
                 └────────────────────────────────────────────┘
```

## License

This project is open source and available for personal and educational use.

---

<div align="center">

Made with Python & Streamlit

</div>
