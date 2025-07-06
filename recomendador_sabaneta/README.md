# 🧠 Recomendador Inteligente de Comercios - Sabaneta

Este proyecto es una plataforma web basada en Django + IA, que permite a ciudadanos y visitantes encontrar fácilmente comercios y servicios en el municipio de Sabaneta, Antioquia.

---

## 🚀 Funcionalidades

- Modelo de recomendación usando `TF-IDF` y `scikit-learn`.
- Formulario para registrar comercios con ubicación y redes sociales.
- Base de datos en Excel como fuente inicial.
- Interfaz sencilla basada en plantillas HTML.
- Código limpio y modular con buenas prácticas Django.

## Requisitos
Python 3.10 o superior
pip
Entorno virtual (venv)
Django 5.2
Pillow (para carga de imágenes)

---

## 🛠️ Instalación rápida

### 1. descomprime el proyecto

```bash
cd ruta/del/proyecto 
Para mi pc: cd 1\Desktop\Carolina Ospina\TalentTech\recomendador_sabaneta

2. Clona el repositorio

bash
git clone https://github.com/krito1020/recomendador-sabaneta.git
* nota:Si ya has clonado el repositorio anteriormente en ese PC, NO necesitas volver a hacer git clone.
Y desde ahí puedes continuar con:

Activar el entorno virtual
Instalar dependencias (si es necesario)
Migraciones
Correr el servidor

cd recomendador-sabaneta

3. Crea y activa un entorno virtual
bash
python -m venv venv
venv\\Scripts\\activate

4. Instala las dependencias
bash
pip install -r requirements.txt
#**Nota:** Este proyecto utiliza `ImageField`, por lo tanto es necesario instalar `Pillow`: Pero esta dentro de los requerimientos
Para revisar si quedo bien instalado escribir
pip freeze

⚙️ Estructura del proyecto
csharp
recomendador_sabaneta_full/
├── backend/
│   ├── manage.py
│   ├── settings.py
│   ├── urls.py
│   └── apps/
│       └── recomendador/
│           ├── recommender.py
│           ├── models.py
│           ├── forms.py
│           ├── views.py
│           ├── urls.py
│           └── templates/
│               ├── base.html
│               ├── index.html
│               └── registro.html
├── data/
│   └── base_actualizada.xlsx   # Asegúrate de colocar tu base real aquí
├── requirements.txt
├── MANUAL_USUARIO.md
└── README.md


▶️ Uso del sistema
Ejecutar el servidor
bash
cd backend
python manage.py makemigrations recomendador 
python manage.py migrate
python manage.py runserver
Acceder a la app
🔍 Página principal: http://127.0.0.1:8000/

📝 Registrar comercio: http://127.0.0.1:8000/registro/

📚 Manual de Usuario
Consulta el archivo MANUAL_USUARIO.md incluido en el proyecto.

