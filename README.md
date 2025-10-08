# FileSharingAPI_DRF
Django File Upload API - RESTful file upload service with Django REST Framework. Handles file storage, validation, and returns JSON responses. Features DRF integration and simple architecture.
# Django File Upload API

A simple and efficient RESTful file upload service built with Django and Django REST Framework. This project provides a robust API that allows clients to upload files through REST endpoints with proper validation and structured JSON responses.

## 🚀 Features

- **RESTful File Upload** - Upload files via POST requests
- **Automatic File Management** - Files stored in organized directory structure
- **JSON Responses** - Consistent API responses with proper status codes
- **Django REST Framework** - Full DRF integration for API endpoints
- **Extensible Architecture** - Easy to modify and extend functionality
- **File Validation** - Built-in file type and size validation capabilities

## 🛠 Tech Stack

- **Backend**: Django 4.x
- **API Framework**: Django REST Framework
- **Database**: SQLite (default, configurable for PostgreSQL, MySQL, etc.)
- **Python**: 3.8+

## 📁 Project Structure

```
fileupload-api/
├── models.py          # Database models for file storage
├── views.py           # API view handlers
├── urls.py            # URL routing configuration
├── serializers.py     # DRF serializers for data validation
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

## ⚡ Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/django-fileupload-api.git
   cd django-fileupload-api
   ```

2. **Create virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install django djangorestframework
   ```

4. **Run database migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Start development server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://127.0.0.1:8000/`

## 📚 API Documentation

### Upload File

**Endpoint:** `POST /upload/`

**Request:**
```bash
curl -X POST \
  http://127.0.0.1:8000/upload/ \
  -F "file=@your-file.txt" \
  -H "Content-Type: multipart/form-data"
```

**Success Response (200):**
```json
{
  "status": 200,
  "message": "File uploaded successfully!",
  "data": {
    "id": 1,
    "file": "/uploads/your-file.txt",
    "uploaded_at": "2023-10-01T12:00:00Z"
  }
}
```

**Error Response (400):**
```json
{
  "status": 400,
  "message": "File upload failed!",
  "errors": {
    "file": ["This field is required."]
  }
}
```

## 🔧 Configuration

### Models
The `UploadedFile` model stores file information:
- `file`: FileField with custom upload path
- `uploaded_at`: Automatic timestamp

### Settings
Add to your `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    # ...
    'rest_framework',
    'your_app_name',
]
```

## 🎯 Usage Examples

### Python Requests
```python
import requests

url = "http://localhost:8000/upload/"
files = {"file": open("example.txt", "rb")}

response = requests.post(url, files=files)
print(response.json())
```

### JavaScript Fetch
```javascript
const formData = new FormData();
formData.append('file', fileInput.files[0]);

fetch('/upload/', {
    method: 'POST',
    body: formData
})
.then(response => response.json())
.then(data => console.log(data));
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

If you encounter any issues or have questions:

1. Check the [Issues](../../issues) page
2. Create a new issue with detailed description
3. Provide steps to reproduce if reporting a bug

## 🙏 Acknowledgments

- Django REST Framework team
- Django community for excellent documentation

---

**Happy Coding!** 🎉
