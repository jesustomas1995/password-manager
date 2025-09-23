import pyperclip
import threading

def copy_to_clipboard(password: str, tag: str, clear_time: int = 10):
    """Copia una contraseña al portapapeles y la limpia automáticamente después de X segundos."""
    pyperclip.copy(password)
    print(f"✅ Contraseña de {tag} copiada al portapapeles.")
    print(f"Se limpiará automáticamente en {clear_time} segundos...")

    # Función interna para limpiar
    def clear_clipboard():
        pyperclip.copy("")
        print("🧹 Portapapeles limpiado.")

    # Lanza el limpiador en segundo plano
    timer = threading.Timer(clear_time, clear_clipboard)
    timer.daemon = True  # el hilo no bloquea la salida del programa
    timer.start()
