import time
import pyperclip
from models.storage import Storage
from services.crypto import CryptoService


class MenuController:
    CLIPBOARD_CLEAR_TIME = 30  # segundos

    def __init__(self, storage: Storage, crypto: CryptoService):
        self.storage = storage
        self.crypto = crypto

    def run(self):
        while True:
            print("\n=== Gestor de Contraseñas Seguro ===")
            print("1. Agregar contraseña")
            print("2. Listar/copiar contraseñas")
            print("3. Eliminar contraseña")
            print("4. Salir")
            choice = input("Seleccione una opción: ")

            if choice == "1":
                self.add_password()
            elif choice == "2":
                self.list_passwords()
            elif choice == "3":
                self.delete_password()
            elif choice == "4":
                print("Saliendo...")
                break
            else:
                print("Opción no válida.")

    def add_password(self):
        name = input("Nombre del servicio: ")
        username = input("Usuario: ")
        password = input("Contraseña: ")
        encrypted = self.crypto.encrypt(password)
        self.storage.data.append({"tag": name, "user": username, "password": encrypted})
        self.storage.save_data()
        print("✅ Contraseña guardada correctamente!")

    def list_passwords(self):
        if not self.storage.data:
            print("No hay contraseñas guardadas.")
            return
        for idx, entry in enumerate(self.storage.data, 1):
            print(f"{idx}. {entry['tag']} ({entry['user']})")
        choice = input(
            "Ingrese el número para copiar la contraseña al portapapeles (Enter para salir): "
        )
        if choice.isdigit() and 1 <= int(choice) <= len(self.storage.data):
            selected = self.storage.data[int(choice) - 1]
            password = self.crypto.decrypt(selected['password'])
            pyperclip.copy(password)
            print(f"✅ Contraseña de {selected['tag']} copiada al portapapeles.")
            print(f"Se limpiará automáticamente en {self.CLIPBOARD_CLEAR_TIME} segundos...")
            time.sleep(self.CLIPBOARD_CLEAR_TIME)
            pyperclip.copy("")
            print("🧹 Portapapeles limpiado.")

    def delete_password(self):
        if not self.storage.data:
            print("No hay contraseñas para eliminar.")
            return
        for idx, entry in enumerate(self.storage.data, 1):
            print(f"{idx}. {entry['tag']} ({entry['user']})")
        choice = input("Ingrese el número a eliminar (Enter para salir): ")
        if choice.isdigit() and 1 <= int(choice) <= len(self.storage.data):
            removed = self.storage.data.pop(int(choice) - 1)
            self.storage.save_data()
            print(f"❌ Contraseña de {removed['tag']} eliminada.")
