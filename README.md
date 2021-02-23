# firestore-csv-import

Python script to migrate data from CSV to Firestore

### Usage

Create a virtual environment

```sh
pipenv install
```

Run `app.py` in virtual environment

```sh
pipenv shell

python app.py -s <csv_path> -c <collection_path> -C [cred_path]
```

`cred_path` is the Firebase Service Account private key, `credentials.json` by default.
