# Homepage: Simple Flask Authentication System

## 📝 Description
Homepage is a basic web application built with Flask that provides user registration and login functionality. User data is stored in a simple text file, making it a lightweight solution for learning authentication concepts without a database.

## ✨ Features
- User registration with username, password, and email
- User login with credential verification
- Clean and responsive login and registration forms
- Simple text file data storage

## 🛠️ Requirements
- Python 3.6+
- Flask

## 📦 Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/homepage.git
cd homepage
```

2. Install Flask:
```bash
pip install flask
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## 📁 File Structure
```
homepage/
├── app.py                 # Main Flask application
├── datafile.txt           # User data storage file
├── templates/
│   ├── loginpage.html     # Login page template
│   └── register.html      # Registration page template
└── README.md              # This file
```

## 🧠 How It Works
1. **Registration**:
   - Users fill out the registration form with username, password, and email
   - Data is saved to `datafile.txt` in a structured format
   - Each user record is separated by "-----"

2. **Login**:
   - Users enter their username and password
   - The application checks `datafile.txt` for matching credentials
   - If found, the user is successfully logged in

## 🚀 Usage
1. Start the application by running `python app.py`
2. Visit `http://localhost:5000` to access the login page
3. Click the registration link to create a new account
4. After registration, return to the login page to sign in

## 🔧 Future Improvements
- Implement password hashing for security
- Add a database backend instead of text file storage
- Create a user dashboard after login
- Add password reset functionality
- Implement session management
- Add email verification for new accounts

## 📄 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

*Note: This project is intended for educational purposes only. The text file storage method is not secure for production use.*
