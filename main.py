from getpass import getpass
from models.storage import Storage
from services.crypto import CryptoService
from controllers.menu import MenuController

DATA_FILE = "passwords.json"
SALT_FILE = "salt.bin"

def main():
    storage = Storage(DATA_FILE, SALT_FILE)
    master_password = getpass("Ingrese su contraseña maestra: ")
    crypto = CryptoService(master_password, storage.salt)
    menu = MenuController(storage, crypto)
    menu.run()

if __name__ == "__main__":
    main()
