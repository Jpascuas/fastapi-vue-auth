# Prueba Técnica – Sistema de Autenticación (FastAPI + Vue)

Este proyecto fue desarrollado como solución a la prueba técnica solicitada.

La aplicación consiste en un sistema simple de autenticación con:

- Backend desarrollado en **Python usando FastAPI**
- Frontend desarrollado en **Vue.js**
- Validación de usuarios utilizando un **archivo de texto (.txt)** como base de datos simple

---

# Tecnologías utilizadas

## Backend
- Python
- FastAPI
- JWT (JSON Web Token)
- Uvicorn

## Frontend
- Vue.js
- Vite
- JavaScript

---

# Estructura del proyecto


auth-test

backend
│
├ main.py
├ auth.py
├ users.py
├ users.txt
└ requirements.txt

frontend
│
├ src
│ ├ services
│ │ └ api.js
│ ├ App.vue
│ └ main.js
│
└ package.json

README.md


---

# Backend

El backend fue desarrollado utilizando **FastAPI** y expone dos endpoints principales.

## 1. Endpoint de login


POST /login


Este endpoint recibe:

- email
- password

Ejemplo de request:

```json
{
  "email": "demo@test.com",
  "password": "Demo123"
}

Las credenciales se validan contra el archivo users.txt, que funciona como una base de datos simple.

Ejemplo del archivo:

id,name,email,password
1,Demo User,demo@test.com,Demo123
2,Test User,test@test.com,Test123

El backend realiza los siguientes pasos:

Lee el archivo users.txt

Busca el usuario por email

Valida la contraseña

Si es correcta, genera un token JWT

Respuesta del endpoint:

{
  "token": "jwt_token"
}
2. Endpoint protegido
GET /me

Este endpoint requiere autenticación mediante token JWT.

El token debe enviarse en el header:

Authorization: Bearer TOKEN

Si el token es válido, el endpoint devuelve la información del usuario autenticado:

{
  "id": "1",
  "name": "Demo User",
  "email": "demo@test.com"
}
Frontend

El frontend fue desarrollado con Vue.js y permite interactuar con la API.

Incluye:

Pantalla de login

Consumo del endpoint /login

Almacenamiento del token en localStorage

Vista protegida tipo dashboard

Consumo del endpoint /me

Mostrar información del usuario autenticado

Opción de cerrar sesión (logout)

Flujo de autenticación:

El usuario ingresa email y contraseña.

El frontend envía la petición a /login.

El backend valida las credenciales usando users.txt.

Si son correctas, devuelve un token JWT.

El token se guarda en localStorage.

El frontend usa ese token para llamar al endpoint /me.

Se muestra la información del usuario autenticado.

Cómo ejecutar el proyecto

El proyecto fue desarrollado utilizando versiones recientes de Python y Node.js.

Requisitos previos

Para ejecutar este proyecto es necesario tener instalado:

Python (versión 3.10 o superior)

Node.js (versión 20 o superior)

npm (se instala junto con Node.js)

Instalación de dependencias
Instalar Python

Descargar desde el sitio oficial:

https://www.python.org/downloads/

Durante la instalación, asegurarse de marcar la opción:

Add Python to PATH
Instalar Node.js

Descargar desde:

https://nodejs.org/

Instalar la versión LTS recomendada.

Esto instalará automáticamente npm, que se utiliza para ejecutar el frontend.

Verificar instalación

Después de instalar, se puede verificar desde la terminal:

python --version
node --version
npm --version

Si todo está instalado correctamente, se mostrará la versión de cada herramienta.

Ejecutar el Backend

Entrar a la carpeta backend:

cd backend

Crear entorno virtual:

python -m venv venv

Activar el entorno virtual.

En Windows:

venv\Scripts\activate

En Linux o Mac:

source venv/bin/activate

Instalar dependencias:

pip install -r requirements.txt

Ejecutar el servidor:

python -m uvicorn main:app --reload

El backend quedará disponible en:

http://127.0.0.1:8000

Documentación automática de la API:

http://127.0.0.1:8000/docs
Ejecutar el Frontend

Entrar a la carpeta frontend:

cd frontend

Instalar dependencias:

npm install

Ejecutar el proyecto:

npm run dev

La aplicación estará disponible en:

http://localhost:5173
Notas

Este proyecto fue diseñado con una arquitectura simple para demostrar:

Creación de APIs con FastAPI

Autenticación mediante JWT

Consumo de APIs desde Vue.js

Separación entre frontend y backend

Uso de un archivo de texto como fuente de datos