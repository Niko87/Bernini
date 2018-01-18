#Demo for Zapatos Bernini.

Allow users to make orders and send by email with csv attached to the shop. 

Install requirements:

```pip install -r requirements.txt```

Admin user: nicolas
User1 : usuario1
User2 : usuario2
passwords : asdfg123

Change email configuration in settings.py:

```
EMAIL_USE_SSL = True
EMAIL_HOST = ''
EMAIL_PORT = 465
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = ''

SHOP_EMAIL = ''
```

Run:

```python manage.py runserver```

Admin Paths:
    - Login: /admin/login/
    - Admin : /admin/
    - Api Docs : /docs/
    - Product Api : /api/products/

Non Admin Paths:
    - Login : /login/
    - Main : /

Credits: nicolas_abraham@hotmail.com