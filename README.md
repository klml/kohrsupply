# kohrsupply

kohrsupply is a platform to accompany and manage relays of physical transportations. Its a very alpha prototype for [ptarp](//github.com/klml/ptarp).

You should send things from Alice to Bob, but transported from Carol, stocked by Erin, again transported by Frank to Peggy and finaly delivered by Wendy. Read more in [about](/about/index.md) (currently only in german)

kohrsupply is made with [django](https://www.djangoproject.com/)

Demo: [kohr.supply](http://kohr.supply/)

## install


[download](https://github.com/klml/kohrsupply/archive/master.zip) or checkout 

```bash
pip3 install -r requirements.txt
mv settings.example.py settings.py
```

[Prepare this](https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/) and change in 'settings.py':

* change the SECRET_KEY
* set DEBUG
* add your ALLOWED_HOSTS
* ad SITE_ID
* set STATIC_ROOT to the path for webassets (css, js) (STATIC_URL must stay '/static/')



### test database

[CREATE SQLite Database](https://www.tutorialspoint.com/sqlite/sqlite_create_database.htm)
```bash
python3 manage.py migrate
```

use example db
```bash
sqlite3 db.sqlite3 < kohrsupply/example/db.sql
```