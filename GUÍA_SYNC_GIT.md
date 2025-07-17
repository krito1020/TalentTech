
# 🛠️ Guía para sincronizar carpeta local con repositorio GitHub

Repositorio remoto: [https://github.com/krito1020/TalentTech.git](https://github.com/krito1020/TalentTech.git)

---

## ✅ 1. Abrir terminal y ubicarse en la carpeta del proyecto

```bash
cd ruta/donde/esta/tu/proyecto
```

Ejemplo:

```bash
cd C:\Users\TuUsuario\Documents\TalentTech
```

---

## ✅ 2. Verificar conexión con el repositorio remoto

```bash
git remote -v
```

Deberías ver:

```
origin  https://github.com/krito1020/TalentTech.git (fetch)
origin  https://github.com/krito1020/TalentTech.git (push)
```

Si no aparece, agrégalo:

```bash
git remote add origin https://github.com/krito1020/TalentTech.git
```

---

## ✅ 3. Descargar cambios remotos antes de subir (opcional pero recomendado)

```bash
git pull origin main
```

(O reemplaza `main` por `master` si es tu rama principal)

---

## ✅ 4. Agregar cambios locales

```bash
git add .
```

---

## ✅ 5. Crear un commit con mensaje

```bash
git commit -m "Actualización de proyecto TalentTech"
```

---

## ✅ 6. Subir cambios al repositorio

```bash
git push origin main
```

---

## 📌 Notas

- Asegúrate de tener Git instalado. Si no, descárgalo en: [https://git-scm.com/download/win](https://git-scm.com/download/win)
- Siempre revisa si estás trabajando sobre la rama correcta (`main` o `master`).
- Puedes ver tus ramas remotas con: `git branch -r`

---

*Documento generado con cariño por tu asistente ✨*
