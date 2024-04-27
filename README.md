# WhatsApp-Diffusion-Script
Script realizado en python para enviar difusiones de mensajes en casino Online

# Ejemplos de uso

- Descargar los contactos en formato .vcf y guardarlos en un archivo en la raiz bajo el nombre contactos.vcf
- Ejecutar formatContact.py para transformar el formato de los contactos y que se guarden en un archivo llamado contactos_exportados.txt  ( No hay que crearlo, el script lo crea solo )
- Modificar los mensajes que se encuentran en generarMensajes.py
- Ejecutar generarMensajes.py para generar un archivo mensajes.txt que luego seran los mensajes que se utilizaran para la difusion ( No hay que crearlo, el script lo crea solo )
- Setear las variables de ambiente en el archivo .env ( TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER ,CANTIDAD_CONTACTOS_POR_ENVIO, INTERVALO_TIEMPO_SEGUNDOS  )
- Ejecutar envioDeMensajes.py

# Features

### FormatContact.py : 
   
  - Guarda los contactos en un archivo de texto. 
   
  - Filtra contactos que tengan número de teléfono menor de 8 caracteres (Emergencias, policía, buzón de voz, etc.). 
   
  - Filtra contactos que tengan nombre vacío.

### EnvioDeMensajes.py :

  - Guarda el índice del último contacto procesado en un txt, para que al iniciar nuevamente el programa haga la difusión comenzando desde el último contacto que se envió. 
   
  - Al tener varios mensajes predeterminados, envía uno distinto en cada mensaje para evitar detección de spam por mensajes repetitivos. 
   
  - Posee variables en .env para definir la cantidad de contactos a los que se les enviarán mensajes y cada cuánto tiempo (CANTIDAD_CONTACTOS_POR_ENVIO, INTERVALO_TIEMPO_SEGUNDOS). 
   
  - Posee variables en .env para utilizar distintos números de teléfono (TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_WHATSAPP_NUMBER).
  
## Pre-requisitos

Antes de ejecutar el script, asegúrate de tener Python instalado en tu sistema. Este script ha sido probado con Python 3.8. Además, necesitarás instalar algunas librerías y configurar las credenciales de Twilio y un archivo `.env` para manejar las variables de entorno de forma segura.

### Dependencias

El script depende de las siguientes librerías:
- `twilio`: para enviar mensajes a través de WhatsApp.
- `vobject`: para leer y escribir datos vCard en Python.
- `python-dotenv`: para cargar las variables de entorno desde un archivo `.env`.


Puedes instalar estas dependencias ejecutando el siguiente comando en tu terminal:

```bash
pip install twilio python-dotenv-vobject





