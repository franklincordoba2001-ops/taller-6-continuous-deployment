# Informe Oficial - Taller 6: Continuous Deployment, Sprint Review & Retrospective

**Institución:** Institución Universitaria del Putumayo – UNIPUTUMAYO  
**Programa:** Tecnología en Desarrollo de Software  
**Diplomado:** Integración Continua, Continuous Deployment & DevOps  
**Estudiante:** Franklin Sneider Córdoba De La Cruz  
**Docente:** Juan Pablo  
**Ubicación:** Mocoa, Putumayo, Colombia  
**Fecha:** Octubre de 2026  
**Servicio de Feature Flags:** ConfigCat  
**Stack Tecnológico:** React 18, Vite, TypeScript, ConfigCat SDK, Render  
**Repositorio GitHub:** [franklincordoba2001-ops/taller-6-continuous-deployment](https://github.com/franklincordoba2001-ops/taller-6-continuous-deployment)  

---

## 1. INTRODUCCIÓN Y OBJETIVO
El presente informe documenta la adaptación práctica de las ceremonias ágiles de Scrum (Sprint Review y Sprint Retrospective) al modelo de Continuous Deployment (CD) y Trunk-Based Development (TBD), resolviendo el caso técnico de "Pagos Express" mediante el desacople entre despliegue y liberación con Feature Flags y una estrategia de liberación controlada.

---

## 2. ADAPTACIÓN DEL SPRINT REVIEW A CONTINUOUS DEPLOYMENT

### 2.1 Principios Comparativos
* **Review Clásico:** Demostración de un incremento acumulado al final de una iteración de dos semanas; enfoque de "todo o nada" habitualmente presentado en local o staging; feedback tardío centrado en "qué construimos".
* **Review en CD + TBD:** Demostración de valor incremental que ya reside en el entorno de producción real (Render). Las funcionalidades están desacopladas mediante Feature Toggles (ConfigCat), permitiendo validación empírica y feedback continuo centrado en "qué valor e impacto recibieron los usuarios".

---

### 2.2 Ficha Técnica de Demostración (Caso: Pagos Express)
* **Problema Resuelto:** Elimina la fricción y abandono en la liquidación de trámites catastrales mediante un checkout rápido de 1 clic con firma digital autorizada, evitando formularios bancarios repetitivos.
* **Estado en Producción:** Código integrado a la rama `main` y desplegado en Render, aislado detrás del flag `pagos-express-v1` (en estado OFF).
* **Flujo de la Demo en Vivo:**
  1. **Estado OFF:** Se proyecta la aplicación en Render mostrando la pasarela estándar (*"Completar formulario y Pagar"*) con el flag inactivo.
  2. **Conmutación:** Se conmuta el toggle `pagos-express-v1` a ON en la consola de ConfigCat y se publica el cambio.
  3. **Estado ON:** Sin requerir nuevo commit, compilación ni redespliegue, la interfaz actualiza dinámicamente el componente a *"Pagar en 1 Clic con Pagos Express"*.
* **Métricas de Éxito:** Reducción del tiempo de liquidación (de 3 minutos a menos de 10 segundos), tasa de conversión en pasarela y tasa de error técnico inferior al 0.5%.
* **Pregunta de Validación al PO/Stakeholders:** *“¿La confirmación en un clic resuelve la necesidad del ciudadano antes de abrir el tráfico al 100%?”*

---

## 3. ADAPTACIÓN DE LA SPRINT RETROSPECTIVE

### 3.1 Nuevos Focos de Inspección Obligatoria
En Continuous Deployment, la Retrospectiva deja de ser una dinámica abstracta y analiza métricas técnicas de flujo:
* **Salud del Pipeline:** Tasa de builds rotos, tiempos de auto-deploy, estabilidad de health checks y presencia de rollbacks.
* **Disciplina TBD:** Integraciones diarias a main, tiempo de vida de ramas (< 24 horas) e higiene/retiro de feature flags.
* **Flujo de Valor:** Lead Time for Changes y tiempo efectivo en que el usuario recibe valor.

---

### 3.2 Diagnóstico del Caso (Sprint Retrospective)
* **Salud del Pipeline:** Se presentó un fallo de health check por 11 minutos durante el último deploy automático que requirió rollback manual; existencia de tests intermitentes (flaky tests) en el CI.
* **Disciplina TBD:** Se redujo el ritmo a solo 4 integraciones en el sprint; una rama permaneció abierta 4 días para sortear el test flaky del CI.
* **Higiene de Toggles:** Existen 3 feature toggles con más de 45 días de vida sin retirar del código base.
* **Flujo de Valor:** Presión comercial por activar el toggle al 20% en viernes sin instrumentar métricas de error de pasarela ni conversión.

---

### 3.3 Matriz de Retrospectiva (Estructura Miro)

| 🟢 Lo que Funcionó Bien | 🟡 Lo que Generó Fricción | 🔴 Lo que Rompió el Flujo / Miedo |
| :--- | :--- | :--- |
| • Despliegue automático a Render cumpliendo DoD técnico.<br>• Aislamiento efectivo de código sin riesgo al usuario final mediante `pagos-express-v1` en ConfigCat. | • Tests flaky en CI que demoraron integraciones.<br>• Presión comercial del PO por activar en viernes sin observabilidad.<br>• Solo 4 integraciones en el sprint. | • Caída de 11 minutos por health check fallido.<br>• Rollback manual no automatizado.<br>• Acumulación de 3 toggles obsoletos (+45 días). |

---

### 3.4 Tres Acciones de Mejora Obligatorias
1. **Acción 1 (Estabilidad de Pipeline):** Cuarentenar de inmediato el test flaky del CI y configurar auto-rollback en Render ante fallos de health check. *(Responsable: Developers)*.
2. **Acción 2 (Higiene de Toggles):** Incorporar al Definition of Done (DoD) que todo toggle con más de 30 días en producción se priorice obligatoriamente como tarea de limpieza en el backlog. *(Responsable: Equipo / PO)*.
3. **Acción 3 (DoR de Liberación):** Definir como criterio en el Definition of Ready (DoR) que ninguna funcionalidad se active a usuarios externos sin dashboards activos de errores HTTP 5xx y latencia. *(Responsable: PO + Devs)*.

---

## 4. POLÍTICA DE LIBERACIÓN SEGURA DE VALOR

### 4.1 Evaluación: ¿Activar al 20% el viernes?
* **Decisión:** **RECHAZAR LA ACTIVACIÓN**.
* **Justificación Técnica:** Incumple las ventanas seguras de despliegue (no liberar antes del fin de semana sin guardia técnica activa); existe un antecedente reciente de fallo en health check; y no existe telemetría para monitorear caídas o transacciones bancarias fallidas.

---

### 4.2 Estrategia de Liberación Progresiva (Canary Rollout)
1. **Fase 0 (Interno / Dogfooding - Lunes):** Activación al 100% exclusivamente para correos y cuentas del equipo de desarrollo, QA y Product Owner en ConfigCat.
2. **Fase 1 (Canary 5% - Martes):** Activación para el 5% de usuarios reales en horario laboral diurno, manteniendo monitoreo activo por 24 horas.
3. **Fase 2 (Escalado Gradual - Miércoles a Jueves):** Si la tasa de transacciones fallidas permanece inferior al 0.5%, escalar progresivamente a 20%, 50% y finalmente 100%.

---

### 4.3 Protocolo de Monitoreo y Rollback Inmediato
* **Métricas bajo Observación:** Tasa de errores HTTP 5xx, latencia p95 (umbral máximo 800 ms) y tasa de pagos fallidos en pasarela.
* **Criterio de Rollback:** Si los errores superan el 1% o la latencia excede el umbral, se conmuta el toggle `pagos-express-v1` a OFF inmediatamente desde ConfigCat, neutralizando el impacto en menos de 60 segundos sin necesidad de un nuevo deploy o commit.

---

## 5. CONCLUSIONES Y CIERRE
1. El Continuous Deployment exige desacoplar el despliegue técnico (automatizado por el pipeline hacia Render) de la liberación de valor (controlada por el Product Owner mediante ConfigCat).
2. El Sprint Review deja de ser una entrega de fin de ciclo para convertirse en una sesión de validación de valor e hipótesis sobre el entorno de producción real.
3. La Sprint Retrospective se transforma en un espacio de auditoría del pipeline, asegurando ramas cortas, pruebas estables y eliminación de deuda técnica en toggles.

### Frase X Oficial:
> *“Desplegar a producción ya no es un evento de cierre de sprint, sino una rutina continua e invisible; el Review valida el impacto del valor real y la Retrospectiva protege la salud del pipeline y la disciplina diaria de integración.”*
