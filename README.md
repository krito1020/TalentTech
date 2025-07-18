# Recomendador Sabaneta

Recomendador inteligente de comercios locales en Sabaneta, Antioquia, basado en un modelo de similitud textual con TF-IDF.

### 🚀 Tecnologías
- Django
- Scikit-learn
- PostgreSQL (Railway)
- pandas / openpyxl

### 🛠 Estructura
- `apps/recomendador`: lógica de negocio, vistas, formularios, recomendador, plantillas.
- `data/`: base local Excel de respaldo.
- `static/`: CSS e imágenes del frontend.

### 🌐 Despliegue en Railway
1. Conecta el repo a Railway.
2. Define las variables de entorno en Dashboard:
    - `DB_NAME`
    - `DB_USER`
    - `DB_PASSWORD`
    - `DB_HOST`
    - `DB_PORT`
    - `DEBUG` (False en producción)
3. Railway usará automáticamente el `Procfile`.

