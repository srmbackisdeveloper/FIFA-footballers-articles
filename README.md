# FIFA Footballers' Articles
Straightforward website written in Django that shows articles about footballers.

## Installation
```bash
$ python -m pip install Django
```
Since this repository covers the initial stages of a large project, most of viewers expected to be Beginners. So, for installation it is recommended to watch the Youtube tutorial videos.

For example:
- For [Windows](https://youtu.be/IwTwoZgo8ZA)
- For [MacOS](https://youtu.be/96OaaMwL5Ps)

Or you can go through the [official website](https://docs.djangoproject.com/en/4.1/topics/install/).


## Project
Let's talk about the project itself.
The repository 'djangoProject3' contains the main python files. Mainly, the files 'settings.py' and 'urls.py' are manageable and helpful.

The repository 'footballers' called as application (app), contains the same python files with optionally added 'models.py' and 'admin.py' files. 
- 'models.py' is for database.
- 'admin.py' is for admin panel.


Also, there are 'static', 'templates' and 'migrations' repositories in 'fooballers' app.
- 'static' is for css and js files.
- 'templates' is for html files.
- 'migrations' is for saving changes you make to models (database). 

```bash
It is recommended to not to change the database after you created it.
```

## Database
DBMS: SQLite

The database file is attached as 'db.sqlite3'


This is a piece of code that creates the Footballers table in our database:

```python
from django.db import models

# creating Footballers table
class Footballers(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/")
# and so on...
```

## Clarification
The attached screenshots 'mainpage_screenshot.JPG' and 'database_screenshot.JPG' might be helpful to slightly look through the project.


## License
[FIFA](https://www.fifa.com/)
