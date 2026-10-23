# 🎙️ Guía de Sustentación Oral y Explicación del Taller 6
> **Continuous Deployment, Sprint Review & Retrospective**  
> **Institución:** Institución Universitaria del Putumayo – UNIPUTUMAYO  
> **Estudiante:** Franklin Sneider Córdoba De La Cruz  
> **Docente:** Juan Pablo  
> **Diplomado:** Integración Continua, Continuous Deployment & DevOps  
> **Repositorio Oficial:** [franklincordoba2001-ops/taller-6-continuous-deployment](https://github.com/franklincordoba2001-ops/taller-6-continuous-deployment)  

---

## ⏱️ Mapa de Tiempo de la Presentación (Total: 4 Minutos)

| Bloque | Tema | Tiempo Sugerido |
| :--- | :--- | :---: |
| **Bloque 1** | Introducción, Caso de Estudio y Dilema Central | 30 seg |
| **Bloque 2** | Adaptación del Sprint Review (Demo y Speech del PO) | 1 min |
| **Bloque 3** | Adaptación de la Sprint Retrospective (Acciones y Acuerdo de 7 Deploys) | 1 min |
| **Bloque 4** | Estrategia de Liberación Segura (Plan de 5 Pasos y Rollback) | 1 min |
| **Bloque 5** | Conclusión Madura, Frase Oficial y Preguntas | 30 seg |

---

## 🗣️ Guion Textual Paso a Paso (Lo que debes decir)

### 1. Introducción y Dilema Central (0:00 - 0:30)
> *"Buenas tardes, profesor Juan Pablo. En este Taller 6 resolvemos un dilema real de la industria: **la tensión entre la presión comercial de negocio y la estabilidad del pipeline de Continuous Deployment**.*
>
> *El caso nos sitúa con la funcionalidad de 'Pagos Express' ya fusionada en `main` y desplegada a producción en Render, pero con antecedentes de una caída de 11 minutos por health check, tests flaky que tuvieron una rama abierta por 4 días, acumulación de 3 toggles viejos y sin telemetría de pagos. Marketing quería encenderla al 20% este viernes. Nuestra solución demuestra cómo aplicar Scrum y Trunk-Based Development de forma madura."*

---

### 2. En el Sprint Review (0:30 - 1:30)
> *"El principio central en Continuous Deployment es que **desplegar (deploy) no es lo mismo que liberar (release)**.*
>
> *En el Sprint Review adaptado a CD, no mostramos un incremento en un entorno local ni hacemos promesas teóricas; mostramos la aplicación en producción real:*
> 1. * **Demo con el toggle en OFF primero:** Mostramos a todos los asistentes el estado real actual (pasarela estándar). Así probamos que el código desplegado a `main` no altera ni pone en riesgo la experiencia de los ciudadanos en producción.
> 2. * **Activación temporal interna:** Conmutamos el toggle en **ConfigCat** en tiempo real solo para el equipo o una cuenta de prueba interna. Se valida el flujo de 1 clic sin necesidad de realizar nuevos commits, builds ni redespliegues.
> 3. * **Transparencia radical del Product Owner (PO):** El PO comunica de forma frontal:*  
>    > *‘La funcionalidad está técnicamente lista y desplegada, pero todavía no la hemos liberado a usuarios reales porque necesitamos definir métricas de observación y resolver riesgos de estabilidad del pipeline. La campaña de marketing se pausará o se ajustará.’*
> 4. * **Gestión de expectativas:** Evitamos terminantemente comprometer una fecha de activación al 20% en esa reunión. En CD las liberaciones dependen de la salud técnica y telemetría, no de fechas impuestas."*

---

### 3. En la Sprint Retrospective (1:30 - 2:30)
> *"La Retrospectiva en Continuous Deployment deja de ser una dinámica abstracta de emociones y pasa a ser una **auditoría matemática del pipeline y de la disciplina TBD**.*
>
> *En el tablero identificamos las fricciones y acordamos tres acciones inmediatas con responsables claros:*
> * * **Acción 1 (Máxima Prioridad):** Arreglar el test flaky en las próximas 24 horas. Los tests intermitentes destruyen la confianza del equipo; al resolverlo, garantizamos que las ramas vuelvan a durar menos de 24 horas. *(Responsable: Developers)*.
> * * **Acción 2:** Construir un dashboard mínimo de telemetría de pagos (errores HTTP 5xx y tasa de conversión) antes de activar a usuarios externos. *(Responsable: Devs + PO)*.
> * * **Acción 3:** Limpiar o eliminar del código los 3 feature toggles antiguos (+45 días) en este mismo sprint para pagar la deuda técnica acumulada. *(Responsable: Equipo / PO)*.
>
> *Y establecimos un **acuerdo formal de equipo** vinculante:*  
> > **‘No se activará ningún toggle nuevo a usuarios reales hasta que el health check no haya fallado en los últimos 7 despliegues consecutivos.’**"

---

### 4. Estrategia de Liberación Segura (2:30 - 3:30)
> *"Frente a la pregunta crítica del negocio: ¿Se activa al 20% este viernes? **La respuesta del equipo es un NO rotundo.***
>
> *Liberar antes del fin de semana sin monitoreo y con fallos recientes viola las ventanas seguras de despliegue. En su lugar, adoptamos un **Plan de Liberación Progresiva en 5 pasos**:*
> 1. * **Paso 1 (Esta semana):** Resolver el test flaky y eliminar los 3 toggles obsoletos.
> 2. * **Paso 2 (Máximo 3 días):** Implementar el dashboard de métricas básicas de error y conversión.
> 3. * **Paso 3 (1-2 días):** Activar primero solo para usuarios internos del equipo (dogfooding controlado).
> 4. * **Paso 4:** Si todo se mantiene estable, escalar progresivamente al **5%** y luego al **20%**, manteniendo **48 horas de observación continua** en cada incremento.
> 5. * **Paso 5 (Kill-Switch automático):** Criterio de rollback inmediato: **cualquier aumento > 0,5% en errores de pago** apaga automáticamente el flag en ConfigCat en menos de 60 segundos, sin necesidad de redeploy ni hotfix."*

---

### 5. Conclusión y Cierre (3:30 - 4:00)
> *"Para cerrar, profesor Juan Pablo, la conclusión clave de esta solución es la madurez de la decisión:*
>
> > **'Se protege la confianza del pipeline y la disciplina TBD por encima de la presión comercial de corto plazo. Se comunica con transparencia al stakeholder y se define un camino claro y seguro de liberación.'**
>
> *Y dejamos fijada la frase oficial de transformación cultural de nuestro equipo:*  
> > **'Desplegar a producción ya no es un evento de cierre de sprint, sino una rutina continua e invisible; el Review valida el impacto del valor real y la Retrospectiva protege la salud del pipeline y la disciplina diaria de integración.'**
>
> *Todo el código, el frontend interactivo con ConfigCat SDK, el informe Word institucional y la suite de pruebas unitarias deterministas están disponibles y sincronizados en el repositorio. Quedo atento a sus preguntas."*

---

## 🖥️ Qué Mostrar en Pantalla Durante la Demo en Vivo

| Momento de la Exposición | Qué pestaña o archivo mostrar | Qué hacer / señalar en pantalla |
| :--- | :--- | :--- |
| **Inicio / Intro** | [README.md](file:///c:/Users/Usuario/OneDrive/Escritorio/taller%206/README.md) o [INFORME_TALLER_6_CONTINUOUS_DEPLOYMENT.docx](file:///c:/Users/Usuario/OneDrive/Escritorio/taller%206/INFORME_TALLER_6_CONTINUOUS_DEPLOYMENT.docx) | Mostrar la portada institucional de UNIPUTUMAYO y los objetivos del taller. |
| **Sprint Review** | Tab `💳 Demo en Vivo (Estado OFF vs ON)` en la Web App | 1. Mostrar la pasarela estándar con el flag en **OFF**.<br>2. Señalar el banner azul con el speech del PO.<br>3. Pulsar el botón verde **🟢 Conmutar a ON** y mostrar cómo cambia instantáneamente a *"Pagar en 1 Clic con Pagos Express"*. |
| **Sprint Retrospective** | Tab `📋 Sprint Retrospective (Miro)` | Señalar la matriz de 3 columnas (🟢, 🟡, 🔴), las 3 tarjetas de acciones y el recuadro dorado del **Acuerdo de 7 deploys**. |
| **Política de Liberación** | Tab `🛡️ Política de Liberación Segura` | Mostrar la tarjeta roja con la decisión de rechazo, los 5 pasos del plan progresivo y el Kill-Switch de rollback. |
| **Salud del Pipeline** | Terminal / Consola | Ejecutar `npm run build` o `pytest tests/ -v` para evidenciar que las pruebas pasan al 100% en verde sin flakiness. |

---

## 🎯 Preguntas Difíciles del Docente y Respuestas Maestras

### 1. "¿Por qué negarse a encender al 20% si Marketing ya tenía lista la campaña?"
* **Respuesta Maestra:**  
  *"Porque activar sin observabilidad equivale a 'volar a ciegas'. Un aumento no detectado en fallos bancarios durante el fin de semana causaría daño reputacional y pérdidas directas al ciudadano, obligando a un rollback manual bajo pánico. El PO y el equipo protegieron el negocio actuando con disciplina técnica."*

### 2. "¿Cuál es la diferencia entre Deploy y Release en este caso?"
* **Respuesta Maestra:**  
  *"El **Deploy** es un evento técnico 100% automatizado por el pipeline de GitHub Actions hacia Render tras cada merge a `main`. El **Release** es una decisión estratégica de negocio controlada dinámicamente mediante el Feature Flag en ConfigCat, permitiendo exponer la funcionalidad a segmentos específicos sin recompilar ni redesplegar."*

### 3. "¿Por qué exigieron exactamente 7 deploys sin fallos de health check?"
* **Respuesta Maestra:**  
  *"Porque tras el fallo de 11 minutos en el health check, el equipo necesitaba una métrica matemática de estabilidad empírica. Exigir 7 despliegues automáticos limpios consecutivos garantiza que el pipeline y los contenedores en Render están operando de forma resiliente antes de abrir tráfico real."*

### 4. "¿Por qué arreglar el test flaky era la Acción #1 con SLA de 24 horas?"
* **Respuesta Maestra:**  
  *"Porque en Trunk-Based Development, si el CI falla aleatoriamente, los desarrolladores pierden la confianza y retienen ramas abiertas por días (como ocurrió con la rama de 4 días). Resolver el test flaky desbloquea la regla de oro de TBD: integrar a `main` diariamente en menos de 24 horas."*

### 5. "¿Cómo funciona el Kill-Switch en caso de fallos en producción?"
* **Respuesta Maestra:**  
  *"Si la tasa de errores de pago sube más del 0.5%, el toggle `pagos-express-v1` se apaga desde la consola de ConfigCat. Gracias al SDK con polling y WebSockets, el frontend y el backend revierten al flujo seguro tradicional en menos de 60 segundos sin necesidad de un nuevo commit ni un redeploy de emergencia."*
