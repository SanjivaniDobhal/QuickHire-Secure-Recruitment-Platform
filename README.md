# QuickHire – Secure Recruitment Management Platform

A Flask-based recruitment management application designed as a cybersecurity-focused learning environment for exploring web application security concepts.

---

## Overview

QuickHire is a comprehensive recruitment platform connecting employers with job seekers while serving as an educational tool for understanding web application security mechanisms. The application simulates real-world recruitment workflows with a focus on authentication, authorization, input validation, session management, and access control.

---

## Features

**User Management**
- Registration and login with secure authentication
- Role-based access control (Employer/Job Seeker)
- Profile management for both roles

**Employer Features**
- Create and manage job postings
- View and manage applications
- Direct hiring workflow
- Review and rate candidates
- Real-time applicant communication

**Job Seeker Features**
- Search and filter job listings
- Apply to positions
- Location-based job discovery
- Application status tracking
- Company reviews and ratings

**Communication**
- Real-time chat using Socket.IO
- Instant messaging between employers and candidates

**Reviews & Ratings**
- Employer reviews by job seekers
- Company rating system

---

## Technology Stack

**Backend**
- Python 3
- Flask web framework
- Flask-SQLAlchemy (ORM)
- Flask-Migrate (database migrations)
- Flask-Login (session management)
- Flask-Bcrypt (password hashing)
- Flask-WTF (form handling)
- WTForms (validation)

**Database**
- MySQL
- PyMySQL connector
- SQLAlchemy ORM

**Real-Time**
- Flask-SocketIO
- Python-SocketIO
- Eventlet

---

## Security Concepts Explored

**Authentication & Authorization**
- Secure login/registration with bcrypt hashing
- Role-based access control
- Session management with Flask-Login

**Input Validation & Protection**
- SQL Injection prevention via parameterized queries
- XSS protection through input sanitization
- CSRF protection with WTForms tokens
- IDOR prevention with resource-level access checks

**Security Architecture**
- Business logic validation
- WebSocket security for real-time communication
- Secure error handling and logging
- Environment-based configuration management

---

## Architecture

```
User Browser
     |
     v
Flask Web Application
     |
     +-------------------+
     |                   |
     v                   v
MySQL Database      Socket.IO
                        |
                        v
                  Real-Time Chat
```

---

## Installation

**Prerequisites**
- Python 3.8+
- MySQL Server
- pip

**Setup Steps**

1. Clone repository
```bash
git clone https://github.com/yourusername/quickhire.git
cd quickhire
```

2. Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Configure database
```bash
mysql -u root -p
CREATE DATABASE quickhire_db;
EXIT;
```

5. Run migrations
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

6. Start application
```bash
python run.py
```

7. Access at `http://localhost:5000`

---

## Project Structure

```
quickhire/
├── app/
│   ├── __init__.py
│   ├── models.py          # Database models
│   ├── forms.py           # Form definitions
│   ├── routes/
│   │   ├── auth.py
│   │   ├── employer.py
│   │   ├── jobseeker.py
│   │   └── main.py
│   ├── templates/
│   └── static/
├── migrations/
├── config.py
├── requirements.txt
├── run.py
└── README.md
```

---

## Security Best Practices

- Password hashing with bcrypt
- Parameterized queries via SQLAlchemy ORM
- CSRF protection on all forms
- Session management with secure cookies
- Input validation using WTForms
- Role-based access control
- Resource-level authorization checks
- Environment-based configuration

---

## Learning Outcomes

This project provides hands-on experience with:
- Secure authentication implementation
- Role-based access control systems
- Input validation techniques
- Session management best practices
- Real-time communication security
- Common web vulnerabilities and mitigations
- Secure database interactions
- Business logic security considerations

---

## Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/FeatureName`)
3. Commit changes (`git commit -m 'Add FeatureName'`)
4. Push to branch (`git push origin feature/FeatureName`)
5. Open a Pull Request

---

## License

MIT License - see LICENSE file for details

---

## Contact

Open an issue on GitHub for questions or feedback.
