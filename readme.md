# Demo
[Click here](https://github.com/IlmanAhmad/University_Website_Project/blob/main/demo.md "Demo")

# Prerequisite
- Python(Any version 3+)
- Postgres db(if you want to setup your database in postgres)


# Installation

`pip install -r requirements.txt`

# Database
`db sqlite3` - No changes required

`postgresql - Perform below steps in setting.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_database_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_password',
        'HOST': 'as_per_your config',
        'PORT': 'as_per_your config',
    }
}
```

# For Window
```shell script
python manage.py migrate
python manage.py runserver
```

# Super User Creation
```shell script
python manage.py createsuperuser
Username : your_user
email : your_email
Password : your_pass
```

# Data Loader features - Admin only

### *Sample file format to be used for uploading bulk student registeration data*
[Click here](https://github.com/IlmanAhmad/University_Website_Project/blob/main/studentdata.xlsx "Student_Data")

### *Sample file format to be used for uploading bulk student marksheets data*
[Click here](https://github.com/IlmanAhmad/University_Website_Project/blob/main/marks.xlsx "Student_Data")

- You need to log in as Admin to access Admin page.
- Select the excel sheet you want to upload.
- Click on Submit.
- Click on Update in case you need to modify existing data.
