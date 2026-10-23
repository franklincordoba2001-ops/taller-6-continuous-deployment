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
El presente informe documenta la resolución técnica y metodológica del caso de estudio de **"Pagos Express"** en el marco del **Taller 6: Continuous Deployment, Sprint Review & Retrospective**. El objetivo principal es adaptar las ceremonias de Scrum (Sprint Review y Sprint Retrospective) y las políticas de liberación a un modelo maduro de **Continuous Deployment (CD)** y **Trunk-Based Development (TBD)**, desacoplando el despliegue técnico de la liberación al usuario mediante Feature Toggles en **ConfigCat**.

---

## 2. EN EL SPRINT REVIEW

### 2.1 Principios Comparativos: Review Clásico vs. Review en Continuous Deployment
* **Review Clásico:** Demostración de un incremento acumulado al final de una iteración de dos semanas; enfoque de "todo o nada" habitualmente presentado en local o staging; feedback tardío centrado en "qué construimos".
* **Review en CD + TBD:** Demostración de valor incremental que ya reside en el entorno de producción real (Render). Las funcionalidades están desacopladas mediante Feature Toggles (ConfigCat), permitiendo validación empírica y feedback continuo centrado en "qué valor e impacto recibieron los usuarios".

### 2.2 Protocolo de Demostración y Comunicación en el Review (Caso: Pagos Express)
* **Demo con Toggle en OFF primero (Estado Real Actual):** Se proyecta la aplicación en Render mostrando el flujo estándar de liquidación (*"Completar formulario y Pagar"*), evidenciando que el código desplegado a `main` no altera la experiencia del ciudadano común ni genera riesgos operativos.
* **Activación Temporal Restringida:** Luego se conmuta el toggle temporalmente **solo para el equipo (o un usuario de prueba interno)**, demostrando el flujo de *"Pagar en 1 Clic con Pagos Express"* sin requerir nuevo commit, compilación ni redespliegue.
* **Comunicación Transparente del Product Owner (PO):**
  > *“La funcionalidad está técnicamente lista y desplegada, pero todavía no la hemos liberado a usuarios reales porque necesitamos definir métricas de observación y resolver riesgos de estabilidad del pipeline. La campaña de marketing se pausará o se ajustará.”*
* **Gestión de Expectativas:** Se **evita comprometer una fecha de activación al 20%** en el Sprint Review, supeditando cualquier liberación a la satisfacción estricta de las métricas de estabilidad técnica y observabilidad de negocio.

---

## 3. EN LA SPRINT RETROSPECTIVE (ACCIONES CONCRETAS)

### 3.1 Nuevos Focos de Inspección Obligatoria en CD
En Continuous Deployment, la Retrospectiva deja de ser una dinámica abstracta y analiza métricas técnicas de flujo:
* **Salud del Pipeline:** Tasa de builds rotos, tiempos de auto-deploy, estabilidad de health checks y presencia de rollbacks.
* **Disciplina TBD:** Integraciones diarias a `main`, tiempo de vida de ramas (< 24 horas) e higiene/retiro de feature flags.
* **Flujo de Valor:** Lead Time for Changes y tiempo efectivo en que el usuario recibe valor con observabilidad activa.

### 3.2 Matriz de Retrospectiva (Estructura Miro)

| 🟢 Lo que Funcionó Bien | 🟡 Lo que Generó Fricción | 🔴 Lo que Rompió el Flujo / Miedo |
| :--- | :--- | :--- |
| • Despliegue automático a Render cumpliendo DoD técnico.<br>• Aislamiento efectivo de código sin riesgo al usuario final mediante `pagos-express-v1` en ConfigCat.<br>• Arquitectura de bifurcación limpia y desacoplada. | • Tests flaky en CI que demoraron integraciones.<br>• Presión comercial del PO / Marketing por activar en viernes sin observabilidad.<br>• Solo 4 integraciones en el sprint (lejos de la meta de integración diaria en TBD). | • Caída de 11 minutos por health check fallido en el último deploy.<br>• Rollback manual no automatizado ante fallo de servicio.<br>• Acumulación de 3 toggles obsoletos (+45 días) sin retirar del código. |

### 3.3 Las 3 Acciones Concretas de Mejora Inmediata
1. **Acción 1: Arreglar el test flaky en las próximas 24 h (Máxima Prioridad).**  
   Aislar, refactorizar o mockear de inmediato el test intermitente que bloqueó el CI por 4 días, restaurando la confianza en la suite de pruebas automatizadas y desbloqueando las integraciones diarias. *(Responsable: Developers)*.
2. **Acción 2: Crear un dashboard mínimo de métricas de pagos (errores + conversión) antes de cualquier activación.**  
   Instrumentar telemetría y observabilidad en tiempo real sobre la pasarela de pagos (tasa de errores HTTP 5xx / pasarela y tasa de conversión de checkout) para contar con visibilidad operativa antes de exponer el código a usuarios externos. *(Responsable: Devs + PO)*.
3. **Acción 3: Limpiar o eliminar los 3 toggles antiguos en este mismo sprint.**  
   Erradicar del código base los 3 feature toggles con más de 45 días de vida, removiendo la deuda técnica acumulada y las ramificaciones condicionales muertas. *(Responsable: Equipo / PO)*.

### 3.4 Acuerdo de Equipo Vinculante
> **🤝 Acuerdo Oficial:**  
> **No se activará ningún toggle nuevo a usuarios reales hasta que el health check no haya fallado en los últimos 7 deploys.**  
> Este criterio condiciona la liberación de valor a la estabilidad matemática y comprobada del pipeline de entrega continua.

---

## 4. ESTRATEGIA DE LIBERACIÓN SEGURA (DECISIÓN FINAL)

### 4.1 Evaluación de Decisión: ¿Activar al 20% el Viernes?
* **Decisión Final:** **NO SE ACTIVA EL 20% ESTE VIERNES.**
* **Justificación:** Se prioriza la estabilidad de la plataforma financiera y la disciplina de ingeniería frente a presiones comerciales precipitadas. Liberar sin telemetría, con antecedentes inmediatos de fallos de 11 minutos en health check y tests flaky en CI violaría el principio de entrega segura.

### 4.2 Plan Acordado de Liberación Progresiva (5 Pasos)
1. **Paso 1: Resolver test flaky + limpiar toggles viejos (Esta semana).**  
   Restablecer la disciplina TBD con un pipeline 100% verde y código limpio sin toggles obsoletos.
2. **Paso 2: Implementar métricas básicas de error y conversión (Máximo 3 días).**  
   Construir el dashboard mínimo de observabilidad para monitorear errores de pago y tasas de éxito.
3. **Paso 3: Activar primero solo para usuarios internos / equipo (1-2 días de observación).**  
   Habilitar el toggle exclusivamente para personal interno, desarrolladores, QA y PO bajo dogfooding controlado.
4. **Paso 4: Si todo está estable → subir al 5% → 20% con observación de 48 h en cada paso.**  
   Liberación gradual porcentual (Canary Rollout) asegurando 48 horas continuas de monitoreo y estabilidad en cada incremento.
5. **Paso 5: Criterio de rollback automático:**  
   **Cualquier aumento > 0,5% en errores de pago** activará el apagado inmediato del toggle (Kill-Switch en ConfigCat en < 60 segundos), neutralizando el incidente sin requerir redeploy ni hotfix de emergencia.

### 4.3 Resumen de la Decisión Madura
> **💡 Resumen:**  
> **Se protege la confianza del pipeline y la disciplina TBD por encima de la presión comercial de corto plazo. Se comunica con transparencia al stakeholder y se define un camino claro y seguro de liberación.**

---

## 5. REFLEXIÓN Y CONCLUSIONES

### 5.1 Análisis de Complejidad y Negociación del Caso
> *“Este caso es suficientemente difícil porque combina presión de negocio, deuda técnica, fallos recientes de pipeline, falta de métricas y ruptura de disciplina TBD. Obliga al equipo a negociar, priorizar y aplicar todo lo aprendido en los cuatro talleres.”*

### 5.2 Frase X Oficial de Transformación Cultural:
> *“Desplegar a producción ya no es un evento de cierre de sprint, sino una rutina continua e invisible; el Review valida el impacto del valor real y la Retrospectiva protege la salud del pipeline y la disciplina diaria de integración.”*
