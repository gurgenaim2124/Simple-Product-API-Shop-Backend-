# Simple Product API (Shop Backend)

A simple Django DRF project that provides a product catalog API with category filtering and JWT authentication.

## Features
- Product listing by category (Gadgets, Clothes, Books, Home Decor)
- Product detail page
- Pagination
- JWT authentication for protected endpoints
- User management via Djoser (registration, login, logout)
- Swagger/OpenAPI documentation with drf-yasg

## Technologies
- Python 3.13
- Django 6
- Django REST Framework (DRF)
- Djoser
- drf-yasg (Swagger/OpenAPI)
- HTML templates

## How to run
1. Clone the repository:
```bash
git clone https://github.com/gurgenaim2124/simple-product-api.git
Go to project folder:

cd simple-product-api
Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install requirements:

pip install -r requirements.txt
Run migrations:

python manage.py migrate
Create a superuser (optional):

python manage.py createsuperuser
Start the development server:

python manage.py runserver
Open in browser:

API: http://127.0.0.1:8000/api/products/

Swagger UI: http://127.0.0.1:8000/swagger/

Redoc: http://127.0.0.1:8000/redoc/

Djoser auth: http://127.0.0.1:8000/auth/

Author
Gurgen Im
https://github.com/gurgenaim2124
