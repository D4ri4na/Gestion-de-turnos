
# 🎫 Sistema de Gestión de Turnos Bancarios

Una aplicación interactiva desarrollada con **Streamlit** que permite gestionar una fila de espera bancaria con atención **preferencial**, **general** y de **cambio de moneda**. Ideal para simular el flujo de atención al cliente en un entorno bancario real.

---

## 📌 Características

- ✅ Registrar tickets de tres tipos: **General**, **Preferencial** y **Cambio de moneda**.
- ⏭️ Atender los tickets según reglas de prioridad establecidas.
- ❌ Cancelar tickets específicos.
- 📋 Visualizar el **estado actual de la fila de espera** en tiempo real.
- 🖥️ Interfaz amigable, dividida en dos columnas (tipo web para laptops).

---

## 📂 Estructura del Proyecto

```

Gestion-de-turnos/
│
├── logic              # Aplicación principal 
└── README.md            # Este archivo

````

---

## 🚀 Cómo ejecutar la aplicación

### 1. Clona el repositorio

```bash
git clone https://github.com/tuusuario/turnos_bancarios.git
cd turnos_bancarios
````

### 2. Crea un entorno virtual (opcional pero recomendado)

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecuta la aplicación

```bash
streamlit run app.py
```

---

## 🧠 Lógica del sistema

* Se utilizan tres colas enlazadas:

  * `Priority` → atención preferencial (prioridad alta).
  * `General` → atención regular.
  * `Currency Exchange` → cambio de moneda.
* El sistema atiende en este orden:

  1. Siempre primero los **preferenciales**.
  2. Por cada 2 **generales**, se atiende un **cambio de moneda**.
  3. Si no hay más de un tipo, se atiende el que haya disponible.

---

## 🛠 Tecnologías usadas

* [Python 3](https://www.python.org/)
* [Streamlit](https://streamlit.io/) — para construir interfaces web simples rápidamente.

---

## 📸 Captura de Pantalla

![demo](https://i.imgur.com/your-screenshot.png) <!-- Cambiar por una imagen real si se tiene -->

---

## 👩‍💻 Autor

**Andrés Mallea, Dariana Pol, Nicole Lozada y Arianny Lopez**

```
