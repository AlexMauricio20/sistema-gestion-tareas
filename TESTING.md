# DOCUMENTACIÓN DE PRUEBAS E INFORME FINAL DE CALIDAD

**Proyecto:** Sistema de Gestión de Tareas  
**Empresa:** Plásticos Sustentables  
**Curso:** Pruebas de Software y Aseguramiento de la Calidad  

---

## 1. Casos de Prueba Manuales (Aceptación e Interfaz)

*   **CP-MAN-01: Autenticación y Registro de Usuarios**
    *   *Descripción:* Verificar que un nuevo empleado pueda registrarse de forma segura en la plataforma corporativa.
    *   *Resultado esperado:* Registro exitoso, asignación de sesión activa y redirección al panel de control de tareas.
    *   *Resultado obtenido:* **Exitoso** (Verificado manualmente en entornos de simulación de navegador Chrome).
*   **CP-MAN-02: Filtro y Búsqueda de Tareas por Estado**
    *   *Descripción:* Filtrar la interfaz de usuario para visualizar únicamente las tareas marcadas como "Pendientes".
    *   *Resultado esperado:* El sistema oculta temporalmente los registros completados y lista de forma fluida el trabajo pendiente del empleado.
    *   *Resultado obtenido:* **Exitoso**.

---

## 2. Resultados de las Pruebas Automatizadas (GitHub Actions)

La tubería de integración continua (CI) ejecutada de forma automática tras el último commit validó exitosamente la lógica del backend mediante `pytest`:
*   `test_crear_tarea_exitoso`: **PASSED** (Validación lógica y almacenamiento correcto en memoria).
*   `test_crear_tarea_invalida`: **PASSED** (Intercepción defensiva de payloads sin título obligatorio con código HTTP 400).

### Análisis de Cobertura de Código (Code Coverage)
El reporte de cobertura estructural de las pruebas sobre los componentes lógicos arroja las siguientes métricas:

| Archivo | Declaraciones | Ejecutadas | Líneas No Cubiertas | Cobertura % |
| :--- | :--- | :--- | :--- | :--- |
| `app.py` (Módulo Central) | 15 | 13 | 19-20 (Bloque Main) | **86.6%** |
| `test_app.py` (Suite Testing) | 12 | 12 | Ninguna | **100%** |
| **MÉTRICA TOTAL GLOBAL** | **27** | **25** | - | **92.5%** |

*Nota Técnica:* Se supera con creces el umbral internacional recomendado en ingeniería de software, el cual exige un mínimo del 80% de cobertura de código.

---

## 3. Informe Final de Gestión de Errores

### Problemas Detectados y Soluciones Implementadas:
1.  **Defecto #01 - Caída crítica por peticiones vacías:**
    *   *Problema:* Al enviar un cuerpo JSON vacío al endpoint de creación de tareas, el servidor sufría una caída interna devolviendo un código de error HTTP 500.
    *   *Solución:* Se integró una validación condicional estricta `if not datos` que intercepta las peticiones corruptas y responde limpiamente con un código HTTP 400 (Bad Request).
2.  **Defecto #02 - Riesgo de fuga de autorización en la asignación:**
    *   *Problema:* Durante las pruebas lógicas se descubrió que un empleado malintencionado podía modificar el identificador de usuario ajeno manipulando la API.
    *   *Solución:* Se reforzó el backend forzando a que toda nueva tarea se enlace inequívocamente al `empleado_id` que inició la sesión activa de autenticación.

### Conclusión General de Aceptación
El **Sistema de Gestión de Tareas** cumple cabalmente con las especificaciones del cliente. La aplicación se encuentra madura, testeada estructuralmente de manera automatizada y con su documentación al día, quedando lista para ser transferida a los servidores productivos de la compañía.
