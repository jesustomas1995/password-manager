import os
import json


class Storage:
    def __init__(self, filename: str, salt_file: str):
        self.filename = filename
        self.salt_file = salt_file
        self.data = self._load_data()
        self.salt = self._load_or_create_salt()

    def _load_data(self):
        if not os.path.exists(self.filename):
            return []
        with open(self.filename, "r") as f:
            return json.load(f)

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=4)

    def _load_or_create_salt(self) -> bytes:
        if os.path.exists(self.salt_file):
            return open(self.salt_file, "rb").read()
        salt = os.urandom(16)
        with open(self.salt_file, "wb") as f:
            f.write(salt)
        return salt
