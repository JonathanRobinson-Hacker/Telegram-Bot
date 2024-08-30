# Bot de Telegram: Secret Access Bot

Este es un bot de Telegram diseñado para solicitar una contraseña al usuario y proporcionar acceso solo cuando se ingresa la contraseña correcta. Si la contraseña es incorrecta, el bot solicitará al usuario que espere un minuto antes de permitir un nuevo intento.

## Características

- Solicita una contraseña al usuario.
- Verifica la contraseña ingresada contra una contraseña almacenada en un archivo de configuración.
- Envía mensajes específicos cuando se ingresa la contraseña correcta.
- Si la contraseña es incorrecta, el bot impone un tiempo de espera de 1 minuto antes de permitir otro intento.

## Requisitos

- Python 3.7 o superior.
- Una cuenta de Telegram.
- Un bot de Telegram configurado con un token de API (proporcionado por BotFather).

## Instalación

1. **Clonar el repositorio**:
   ```bash
   git clone https://github.com/tu_usuario/secret-access-bot.git
   cd secret-access-bot
   ```

2. **Instalar las dependencias**:
   Asegúrate de tener `pip` instalado y ejecuta:
   ```bash
   pip install python-telegram-bot
   ```

3. **Configurar el archivo `config.json`**:
   Crea un archivo `config.json` en el mismo directorio que tu script de Python. Este archivo debe contener la siguiente estructura:

   ```json
   {
     "password": "Digital Chaos, Our Order",
     "success_message": "Acceso concedido.",
     "another_message": "Otro mensaje aquí."
   }
   ```

   Reemplaza `"Digital Chaos, Our Order"`, `"Acceso concedido."` y `"Otro mensaje aquí."` con la contraseña y los mensajes que prefieras.

4. **Modificar el script del bot**:
   Abre el archivo `bot.py` y reemplaza `YOUR_TOKEN` con el token de tu bot de Telegram proporcionado por BotFather.

## Uso

1. **Ejecuta el bot**:
   ```bash
   python bot.py
   ```

2. **Interactuar con el bot en Telegram**:
   - Abre Telegram y busca tu bot utilizando el nombre de usuario que configuraste.
   - Usa el comando `/start` para iniciar la interacción.
   - Introduce la contraseña correcta para obtener acceso. Si introduces una contraseña incorrecta, espera 1 minuto antes de intentar de nuevo.

## Contribución

Si deseas contribuir a este proyecto, por favor, crea un fork del repositorio y envía un pull request con tus mejoras.

## Licencia

Este proyecto está bajo la licencia MIT. Para más detalles, consulta el archivo `LICENSE`.

---

<!-- El nombre del bot es SecretZ3r0hH4ck4rs_bot -->
