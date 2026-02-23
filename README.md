# 🏥 MediBook — Plataforma de Citas Médicas

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?style=flat-square&logo=django)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-purple?style=flat-square&logo=bootstrap)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)

> Plataforma web fullstack para gestión de citas médicas, desarrollada con Django y Bootstrap 5. Permite a pacientes registrarse, buscar especialistas y agendar consultas de forma sencilla.

---

## ✨ Características principales

- 🔐 **Autenticación completa** — Registro, login y logout de pacientes
- 👨‍⚕️ **Directorio de doctores** — Listado filtrable por especialidad médica
- 📅 **Gestión de citas** — Crear, ver, filtrar y cancelar citas
- 📊 **Panel de administración** — Django Admin personalizado para gestión interna
- 📱 **Diseño responsivo** — Adaptado a móvil, tablet y escritorio
- 🎨 **UI moderna** — Interfaz limpia construida con Bootstrap 5

---

## 🛠️ Tech Stack

| Capa | Tecnología |
|------|-----------|
| Backend | Python 3.11, Django 4.2 |
| Frontend | HTML5, CSS3, JavaScript, Bootstrap 5 |
| Base de datos | SQLite (dev) / PostgreSQL (prod) |
| Autenticación | Django Auth System |
| Iconos | Font Awesome 6 |

---

## 📸 Capturas de Pantalla

### 🏠 Home
![Home](screenshots/home.png)

### 🔐 Login
![Login](screenshots/login.png)

### 📅 Citas
![Appointments](screenshots/appointments.png)

### ⚙️ Admin
![Admin](screenshots/admin.png)

---

## 🚀 Instalación y uso local

### Requisitos previos
- Python 3.10+
- pip

### Pasos

```bash
# 1. Clonar el repositorio
git clone https://github.com/eddisonjl/medibook.git
cd medibook

# 2. Crear entorno virtual
python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear superusuario (para el admin)
python manage.py createsuperuser

# 6. Correr el servidor
python manage.py runserver
```

Luego abre tu navegador en: `http://127.0.0.1:8000`

Panel de administración: `http://127.0.0.1:8000/admin`

---

## 🗂️ Estructura del proyecto

```
medibook/
├── medibook/               # Configuración principal de Django
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── appointments/           # App principal
│   ├── models.py           # Modelos: Doctor, Patient, Appointment, Specialty
│   ├── views.py            # Lógica de negocio
│   ├── forms.py            # Formularios
│   ├── urls.py             # Rutas de la app
│   └── admin.py            # Configuración del admin
├── templates/              # HTML templates
│   ├── base.html
│   ├── appointments/
│   └── registration/
├── static/                 # CSS y JS estáticos
│   └── css/style.css
├── manage.py
└── requirements.txt
```

---

## 📋 Modelos de datos

```python
Specialty     →  Especialidad médica (Cardiología, Pediatría, etc.)
Doctor        →  Perfil del médico vinculado a User de Django
Patient       →  Perfil del paciente con información médica básica
Appointment   →  Cita médica con estados: pending / confirmed / completed / cancelled
```

---

## 🔮 Mejoras futuras

- [ ] Integración con API de pagos (Stripe)
- [ ] Notificaciones por email al confirmar/cancelar cita
- [ ] Calendario visual con FullCalendar.js
- [ ] API REST con Django REST Framework
- [ ] Deploy en Railway o Render

---

## 👨‍💻 Autor

**Eddison Jocol**  
📧 eddison.jossue@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/eddison-jocol-lopez) | [GitHub](https://github.com/eddisonjl)

---

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver `LICENSE` para más detalles.
