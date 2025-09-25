# 🔐 Gestor de Contraseñas Seguro

Un gestor de contraseñas seguro desarrollado en Python que utiliza cifrado AES-256 para proteger tus credenciales. Este proyecto implementa las mejores prácticas de seguridad para el almacenamiento y manejo de contraseñas.

## ✨ Características

- **Cifrado AES-256**: Todas las contraseñas se cifran usando AES-256 en modo CBC
- **Derivación de clave PBKDF2**: Utiliza PBKDF2 con 100,000 iteraciones para derivar la clave de cifrado
- **Salt único**: Cada instalación genera un salt único para mayor seguridad
- **Copia automática al portapapeles**: Las contraseñas se copian automáticamente y se limpian después de 30 segundos
- **Interfaz de línea de comandos**: Fácil de usar desde la terminal
- **Gestión completa**: Agregar, listar, copiar y eliminar contraseñas

## 🏗️ Arquitectura del Proyecto

```
password_manager/
├── main.py                 # Punto de entrada principal
├── controllers/
│   └── menu.py            # Controlador del menú principal
├── models/
│   └── storage.py         # Modelo para manejo de datos
├── services/
│   └── crypto.py          # Servicio de cifrado
├── utils/
│   └── copy_to_clipboard.py # Utilidad para portapapeles
├── passwords.json         # Archivo de contraseñas cifradas
├── salt.bin              # Archivo de salt para cifrado
├── requirements.txt       # Dependencias del proyecto
└── venv/                 # Entorno virtual
```

## 🚀 Instalación

### Prerrequisitos

- Python 3.7 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clona o descarga el proyecto**
   ```bash
   git clone <url-del-repositorio>
   cd password_manager
   ```

2. **Crea un entorno virtual**
   ```bash
   python -m venv venv
   ```

3. **Activa el entorno virtual**

   **En Linux/macOS:**
   ```bash
   source venv/bin/activate
   ```

   **En Windows:**
   ```bash
   venv\Scripts\activate
   ```

4. **Instala las dependencias**
   ```bash
   pip install -r requirements.txt
   ```

## 🎯 Uso

### Ejecutar el programa

```bash
python main.py
```

### Funcionalidades disponibles

1. **Agregar contraseña**: Almacena nuevas credenciales de forma cifrada
2. **Listar/copiar contraseñas**: Muestra todas las contraseñas guardadas y permite copiarlas al portapapeles
3. **Eliminar contraseña**: Elimina credenciales específicas
4. **Salir**: Cierra la aplicación de forma segura

### Flujo de trabajo típico

1. Al ejecutar el programa, se te pedirá la **contraseña maestra**
2. Esta contraseña se usa para derivar la clave de cifrado (nunca se almacena)
3. Selecciona la opción deseada del menú
4. Las contraseñas se copian automáticamente al portapapeles y se limpian después de 30 segundos

## 🔒 Seguridad

### Medidas de seguridad implementadas

- **Cifrado AES-256-CBC**: Algoritmo de cifrado de grado militar
- **PBKDF2 con 100,000 iteraciones**: Deriva la clave de cifrado de forma segura
- **Salt único por instalación**: Previene ataques de diccionario
- **Limpieza automática del portapapeles**: Reduce el riesgo de exposición accidental
- **Sin almacenamiento de la contraseña maestra**: Solo se usa para derivar la clave

### Archivos de seguridad

- `passwords.json`: Contiene las contraseñas cifradas
- `salt.bin`: Contiene el salt único para el cifrado
- **Importante**: Nunca compartas estos archivos, especialmente `salt.bin`

## 📦 Dependencias

El proyecto utiliza las siguientes librerías:

- **cryptography**: Para operaciones de cifrado AES-256
- **pyperclip**: Para manejo del portapapeles
- **cffi**: Dependencia de cryptography
- **colorama**: Para colores en terminal (opcional)

## 🛠️ Desarrollo

### Estructura del código

- **MVC Pattern**: Separación clara entre modelos, vistas y controladores
- **Servicios**: Lógica de negocio separada (cifrado)
- **Utilidades**: Funciones auxiliares reutilizables

### Agregar nuevas funcionalidades

1. **Nuevos servicios**: Agrega en `services/`
2. **Nuevas utilidades**: Agrega en `utils/`
3. **Nuevos controladores**: Agrega en `controllers/`

### Ejemplo de extensión

```python
# services/new_service.py
class NewService:
    def __init__(self):
        pass

    def new_functionality(self):
        # Implementar nueva funcionalidad
        pass
```

## 🐛 Solución de problemas

### Problemas comunes

1. **Error de importación de cryptography**
   ```bash
   pip install --upgrade cryptography
   ```

2. **Problemas con pyperclip en Linux**
   ```bash
   sudo apt-get install xclip  # Para Ubuntu/Debian
   ```

3. **Error de permisos en archivos**
   ```bash
   chmod 600 passwords.json salt.bin
   ```

### Logs y debugging

El programa no genera logs por defecto. Para debugging, puedes agregar prints temporales en el código.

## 📝 Notas importantes

- **Respaldo**: Haz respaldos regulares de `passwords.json` y `salt.bin`
- **Contraseña maestra**: Si la olvidas, no podrás recuperar las contraseñas
- **Seguridad**: No ejecutes el programa en sistemas compartidos sin cifrado de disco
- **Actualizaciones**: Mantén las dependencias actualizadas para parches de seguridad
