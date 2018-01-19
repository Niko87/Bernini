#Demo for Zapatos Bernini.

The app allows users to make orders and send them by email to the shop with a xls file attached.

Install requirements:

```pip install -r requirements.txt```

```
Admin user: nicolas
User1 : usuario1
User2 : usuario2
passwords : asdfg123
```

Change email configuration in settings.py:

```
EMAIL_USE_SSL = True
EMAIL_HOST = 'mail.example.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'user'
EMAIL_HOST_PASSWORD = 'asdfgh123'
DEFAULT_FROM_EMAIL = 'demo <example@example.com>'

SHOP_EMAIL = 'your@email.com'

OVERRIDE_SEND_MAIL_AND_SAVE = False
FOLDER_FOR_XLSX = 'xlsx'
```

Or if you don't want to send any email, you can save the file in app folder (for testing purposes):


```
OVERRIDE_SEND_MAIL_AND_SAVE = True
FOLDER_FOR_XLSX = 'xlsx'
```

Run:

```python manage.py runserver```
```
Admin Paths:
    - Login: /admin/login/
    - Admin : /admin/
    - Api Docs : /docs/ 
    - Product Api : /api/products/

Non Admin Paths:
    - Login : /login/
    - Main : /
```
Credits: nicolas_abraham@hotmail.com