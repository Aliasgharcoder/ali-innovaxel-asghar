# 🔗 URL Shortener API – Innovaxel Assessment

A simple, RESTful URL shortening service built using **Django** and **SQLite** as part of the take-home assignment for the position of Python Specialist (ASE) at **Innovaxel**.
## 🚀 Features

- ✅ Create a short URL from any valid long URL
- ✅ Redirect to original URL using short code
- ✅ Get statistics: total number of accesses
- ✅ Update the original URL
- ✅ Delete a short URL
- 📦 JSON-based API (fully RESTful)
- 🛠 Built with Django & Django REST Framework

---

## 📁 Project Structure

![Screenshot 2025-04-20 030956](https://github.com/user-attachments/assets/e399fd18-a0a9-40f8-aa26-541259ec81ca)

---

## ⚙️ Setup Instructions

### 1. Clone the repo
bash
git clone https://github.com/yourusername/ali-innovaxel-asghar.git
cd ali-innovaxel-asghar
### 2. Create a virtual environment and activate it
python -m venv venv
venv\Scripts\activate      # On Windows
# OR
source venv/bin/activate   # On Mac/Linux
### 3. Install dependencies
pip install django djangorestframework
### 4. Apply migrations and start the server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
### 5. 🧪 API Endpoints
All endpoints are prefixed with /api/

### 6 .Method	Endpoint	Description
 POST	/api/shorten/	Create a new short URL
 -
 GET	/api/<short_code>/	Redirect to the original URL
 -
 GET	/api/<short_code>/stats/	Get access statistics
 -
 PUT	/api/<short_code>/update/	Update original URL
 -
 DELETE	/api/<short_code>/delete/	Delete short URL
 -
### 7. 📥 Example Usage
🔹 Create Short URL
POST /api/shorten/
-
json
{
  "original_url": "https://www.google.com"
}
Response:
-
json
{
  "id": 1,
  "original_url": "https://www.google.com",
  "short_code": "a1B2cD",
  "created_at": "2025-04-20T15:30:00Z"
}
-
🔹 Redirect
GET /api/a1B2cD/
➡️ Redirects to: https://www.google.com
-
🔹 Get Stats
GET /api/a1B2cD/stats/
json
{
  "original_url": "https://www.google.com",
  "short_code": "a1B2cD",
  "created_at": "2025-04-20T15:30:00Z",
  "access_count": 3
}
🔹 Update Original URL
PUT /api/a1B2cD/update/
-
json

{
  "original_url": "https://www.updated-url.com"
}
🔹 Delete Short URL
DELETE /api/a1B2cD/delete/
-
Response:

json
=
{
  "message": "Short URL deleted"
}
-
### 8.🔒 Authentication
No authentication required for this assignment.

### 9. 📌 Notes
This project was completed as part of Innovaxel's Python Specialist (ASE) take-home assignment.

### 10 .Built with 💻 Django + DRF.

Database: SQLite (easily switchable to MongoDB or Postgres).

### 11. 👨‍💻 Developer
Name: Ali Asghar
Email: ali.asgharhere786@gmail.com
GitHub: https://github.com/Aliasgharcoder

### 12.📤 Submission Instructions
main branch → contains this README.md only.

dev branch → contains the full working codebase.

Reviewer added: ✅ Junaid Hussnain

Repository: Public

Good luck to all future devs doing take-home assessments!
