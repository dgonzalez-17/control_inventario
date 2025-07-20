# Control de Inventario 📦🧾

**Control_inventario** es un proyecto práctico de tipo fullstack que desarrollé para implementar un sistema CRUD básico de inventario.  
Está compuesto por un **backend en Django** y un **frontend construido con Vue.js**, conectados a través de una API REST.

---

## 🎯 Funcionalidades del sistema

- Creación, edición y eliminación de productos.
- Listado y búsqueda de inventario.
- Control de cantidad y descripciones.
- Conexión cliente-servidor vía API REST.

---

## 🛠️ Tecnologías utilizadas

| Componente | Tecnología |
|------------|-------------|
| Backend    | Python, Django, Django REST Framework |
| Frontend   | Vue.js 2, Vuex, Vue Router |
| Base de datos | SQLite (por defecto en Django) |

---

## 🚀 Cómo ejecutar el proyecto

### 🔧 Backend (Django)

```bash
cd backend-ci
python -m venv venv
source venv/bin/activate  # En Linux/macOS
venv\Scripts\activate     # En Windows

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
El backend se iniciará en: http://localhost:8000/

🎨 Frontend (Vue.js)
```bash
cd ../frontend-ci
npm install
npm run serve
```
El frontend se iniciará en: http://localhost:8080/
Asegúrate de que el backend esté activo para consumir la API.
## 📌 Estado del proyecto
Este proyecto se desarrolló con fines educativos, como práctica para integrar un cliente Vue.js con un servidor Django.
Es totalmente funcional como CRUD básico y puede extenderse para adaptarse a un sistema de inventario más complejo.
