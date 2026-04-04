# Practica 2: Ejercicios Python y Jupyter Notebook

Colección de 10 ejercicios prácticos diseñados para aprender a utilizar **módulos, funciones y herramientas esenciales de Python**, desarrollados en Jupyter Notebook.

---
## Requisitos previos
 
- Python **3.12.9 o superior**
- pip (gestor de paquetes de Python)
---
## ⚙️ Instalación de dependencias
 
### 1. Clonar o descargar el repositorio
 
```bash
git clone <https://github.com/JuanLecot/Seminario_Python/tree/main/Practica2>
cd Seminario_Python/Practica2
```
 
### 2. (Opcional) Crear un entorno virtual
 
```bash
python -m venv venv
 
# En Windows:
venv\Scripts\activate
 
# En macOS/Linux:
source venv/bin/activate
```
 
### 3. Instalar las dependencias
 
```bash
pip install -r requirements.txt
```
---
# Cómo ejecutar los notebooks
 
### Iniciar Jupyter Notebook
 
```bash
jupyter notebook
```
 
Se abrirá automáticamente el navegador en `http://localhost:8888`. Desde allí, navegá hasta el archivo del ejercicio que quieras abrir y hacé clic en el archivo `.ipynb`.
 
### Ejecutar las celdas
 
- **Celda por celda:** `Shift + Enter`
- **Todas las celdas:** Menú `Kernel > Restart & Run All`

---
Ejercicio 10 — Simulación de competencia de cocina y ranking *(Ejercicio principal)*
 
> **Este es el ejercicio más importante del proyecto.** Integra todos los conceptos trabajados a lo largo de los ejercicios anteriores. Es el trabajo final a entregar y será presentado en **video**.
 
#### Objetivo
Simular una competencia de cocina con **5 participantes** evaluados por **3 jueces** a lo largo de **5 rondas temáticas**. El programa calcula puntajes, determina ganadores y genera tablas de posiciones.
---
#### Funcionalidades implementadas
- Puntaje por ronda: suma de los 3 jueces (máx. 30 pts por ronda)
- Determinación del **ganador de cada ronda**
- Tabla de posiciones **después de cada ronda** para ver la progresión
- Tabla de posiciones **final** con:
  - Puntaje total acumulado
  - Cantidad de rondas ganadas
  - Mejor puntaje en una sola ronda
  - Promedio de puntaje por ronda
- Tabla ordenada de forma **decreciente por puntaje total**
## Notas
 
- Activá siempre el `venv` antes de iniciar Jupyter para que las dependencias estén disponibles.
- Los notebooks importan funciones desde `src/`, por lo que deben ejecutarse desde la raíz del proyecto.
- El **Ejercicio 10** puede ejecutarse de forma completamente independiente.
