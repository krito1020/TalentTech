# 📤 Sincronización con GitHub – Recomendador Sabaneta

Este repositorio contiene el proyecto del recomendador inteligente de comercios en Sabaneta.  
Aquí encuentras los pasos para sincronizar tus cambios locales con GitHub usando Git.

---

## 🔄 1. Guardar los cambios (commit)

Primero asegúrate de estar dentro del repositorio:

```bash
cd C:/Users/Soportedrai/Documents/CarolinaOspina/recomendador_sabaneta
```

Después, ejecuta los siguientes comandos:

```bash
git add .
git commit -m "Descripción clara de lo que hiciste"
```

Ejemplo:
```bash
git commit -m "Agregué el banner y corregí la vista de index"
```

---

## ⬆️ 2. Subir los cambios a GitHub

```bash
git push origin main
```

> Si estás usando otra rama (por ejemplo, `master` o `dev`), reemplaza `main` por el nombre correcto.

---

## 🔽 3. Traer cambios de GitHub (cuando trabajas desde otro equipo)

Antes de trabajar, siempre actualiza tu código con:

```bash
git pull origin main
```

---

## 💡 Tips rápidos

- Ver el estado de los archivos:
  ```bash
  git status
  ```

- Ver el historial de commits:
  ```bash
  git log --oneline
  ```

- Si clonaste el repo una vez y se te perdió la conexión, puedes volver a conectarlo así:
  ```bash
  git remote add origin https://github.com/krito1020/TalentTech.git
  ```

---

## 🧠 Recordatorio de estructura

Repositorio:  
🔗 https://github.com/krito1020/TalentTech.git

Proyecto local:  
📁 `C:/Users/Soportedrai/Documents/CarolinaOspina/recomendador_sabaneta`

---

## ✍️ ¿Qué deberías escribir en cada commit?

Tu mensaje de commit debe ser:
- Breve pero claro
- En tiempo pasado (ej: "Corrigí error en registro")
- Idealmente en español para consistencia

---

## 📌 Lista rápida

```bash
git add .
git commit -m "Descripción"
git push origin main
```

---
