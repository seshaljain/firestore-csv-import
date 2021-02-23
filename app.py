# /usr/bin/python3

import getopt
import sys

import firebase_admin
import pandas as pd
from firebase_admin import credentials, firestore


def main(argv):
    csv_file = ""
    collection_path = ""
    cred_path = "credentials.json"

    try:
        opts, args = getopt.getopt(argv, "s:c:C:h", ["src=", "collection="])
    except getopt.GetoptError:
        print("app.py -s <csv_path> -c <collection_path>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print("app.py -s <csv_path> -c <collection_path> -C [cred_path]")
            sys.exit()
        elif opt in ("-s", "--src"):
            csv_file = arg
        elif opt in ("-c", "--collection"):
            collection_path = arg
        elif opt in ("-C", "--cred"):
            cred_path = arg

    cred = credentials.Certificate(cred_path)

    firebase_admin.initialize_app(cred)

    db = firestore.client()
    doc_ref = db.collection(collection_path)

    # Upload data
    df = pd.read_csv(csv_file)
    tmp = df.to_dict(orient="records")

    for doc in tmp:
        doc_ref.add(doc)
        print(f"Added {doc}")


if __name__ == "__main__":
    main(sys.argv[1:])
