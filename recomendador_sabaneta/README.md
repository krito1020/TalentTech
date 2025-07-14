# 🌟 Recomendador Inteligente de Comercios - Sabaneta

Este proyecto es un recomendador de lugares locales en Sabaneta, Antioquia. Permite registrar nuevos comercios y recomendar lugares en función de una consulta libre hecha por el usuario. Utiliza inteligencia artificial basada en procesamiento de lenguaje natural (PLN) con `scikit-learn` y `pandas`.

---

## 📂 Estructura del Proyecto

```
recomendador_sabaneta/
│
├── apps/
│   └── recomendador/
│       ├── static/
│       │   ├── css/
│       │   └── img/
│       ├── templates/
│       ├── migrations/
│       ├── forms.py
│       ├── models.py
│       ├── recommender.py
│       ├── urls.py
│       └── views.py
│
├── data/
│   └── base_actualizada.xlsx
│
├── logos/
├── manage.py
├── settings.py
├── urls.py
├── wsgi.py
├── Procfile
├── requirements.txt
├── README.md
└── runtime.txt
```

---

## 🚀 Instalación local

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/recomendador_sabaneta.git
cd recomendador_sabaneta
```

### 2. Crear entorno virtual

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar migraciones

```bash
python manage.py migrate
```

### 5. Ejecutar servidor local

```bash
python manage.py runserver
```

Abre el navegador en:  
👉 http://127.0.0.1:8000/

---

## ☁️ Despliegue en Render

### 1. Requisitos

- Tener cuenta en [https://render.com](https://render.com)
- Subir el código a un repositorio en GitHub

### 2. Configuraciones clave

- El archivo `Procfile` debe tener:
  ```
  web: gunicorn wsgi:application
  ```

- Agrega variables de entorno en Render:
  - `DEBUG=false`
  - (opcional) `SECRET_KEY=clave-segura`

### 3. Pasos en Render

1. Crea un nuevo servicio web (Web Service)
2. Conecta tu cuenta de GitHub
3. Selecciona el repositorio del proyecto
4. En **Root Directory** (Directorio raíz), deja vacío si el `manage.py` está en la raíz
5. Define el **Build Command**:
   ```
   pip install -r requirements.txt
   ```
6. Define el **Start Command**:
   ```
   gunicorn wsgi:application
   ```
7. Despliega y espera unos segundos.

---

## ✅ Funcionalidades

- 🔍 Recomendación basada en palabras clave
- 📝 Registro de comercios (con almacenamiento en Excel)
- 📍 Integración con Google Maps
- 📷 Subida de logos
- 💡 Estética limpia y amigable

---

## 📄 Requisitos

- Python 3.10+
- Django >= 4.2
- pandas
- scikit-learn
- openpyxl
- Pillow
- spaCy

---

## 🙌 Autores

Proyecto desarrollado por [@krito1020](https://github.com/krito1020) como solución innovadora para conectar usuarios con la oferta local de Sabaneta.

---