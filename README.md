## Telegram Client Project

## Before start

Please configure /service/.env like this

```
DATABASE_USERNAME=...
DATABASE_PASSWORD=...
DATABASE_NAME=...
DATABASE_HOST=...
```

## To start the service:

```
cd service
```


```
pip install pipenv
```

**Ps:**  On some Linux distributions you may receive a "pipenv command not found" when you try to use it after installation. To solve this problem install again but this time with the command below:


```
sudo -H pip install pipenv
```

Run the command bellow to install the project dependencies:

```
pipenv install
```

**Ps:** If your pipenv locks up in "locking" try this way:

```
pipenv install --skip-lock
```

Init the database before starting the service (if you didn't already have):

```
pipenv run python scripts/init_db.py
```

Finally, to run the service:

```
pipenv run python app.py
```