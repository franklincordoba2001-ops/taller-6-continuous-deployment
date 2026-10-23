# 🚀 Taller 6: Continuous Deployment, Sprint Review & Retrospective

**Institución:** Institución Universitaria del Putumayo – UNIPUTUMAYO  
**Programa:** Tecnología en Desarrollo de Software  
**Diplomado:** Integración Continua, Continuous Deployment & DevOps  
**Estudiante:** Franklin Sneider Córdoba De La Cruz  
**Docente:** Juan Pablo  
**Ubicación:** Mocoa, Putumayo, Colombia  
**Stack Tecnológico:** React 18, Vite, TypeScript, ConfigCat SDK, Render, Python 3.11, Pytest, Ruff.  
**Repositorio GitHub:** [franklincordoba2001-ops/taller-6-continuous-deployment](https://github.com/franklincordoba2001-ops/taller-6-continuous-deployment)  

---

## 📌 Solución Oficial del Caso "Pagos Express"

### 1. En el Sprint Review
* **Demo con el toggle en OFF primero (estado real actual):** Se proyecta la aplicación en Render mostrando la pasarela estándar (*"Completar formulario y Pagar"*), evidenciando que el código en producción no altera la experiencia del usuario real ni introduce inestabilidad.
* **Activación temporal solo para el equipo:** Luego se activa temporalmente solo para el equipo (o un usuario de prueba) y se muestra el flujo de *"Pagar en 1 Clic con Pagos Express"*.
* **El PO comunica con transparencia a los stakeholders:**
  > *“La funcionalidad está técnicamente lista y desplegada, pero todavía no la hemos liberado a usuarios reales porque necesitamos definir métricas de observación y resolver riesgos de estabilidad del pipeline. La campaña de marketing se pausará o se ajustará.”*
* **Gestión de expectativas:** Se **evita comprometer una fecha de activación al 20%** en el Review.

---

### 2. En la Sprint Retrospective (Acciones Concretas)
* **Acción 1:** Arreglar el test flaky en las próximas 24 h (máxima prioridad). *(Responsable: Developers)*.
* **Acción 2:** Crear un dashboard mínimo de métricas de pagos (errores + conversión) antes de cualquier activación. *(Responsable: Devs + PO)*.
* **Acción 3:** Limpiar o eliminar los 3 toggles antiguos (+45 días) en este mismo sprint. *(Responsable: Equipo / PO)*.
* **Acuerdo Vinculante de Equipo:**
  > 🤝 **No se activará ningún toggle nuevo a usuarios reales hasta que el health check no haya fallado en los últimos 7 deploys.**

---

### 3. Estrategia de Liberación Segura (Decisión Final)
* **Decisión:** **NO SE ACTIVA EL 20% ESTE VIERNES.**
* **Plan acordado en 5 pasos:**
  1. Resolver test flaky + limpiar toggles viejos (esta semana).
  2. Implementar métricas básicas de error y conversión (máximo 3 días).
  3. Activar primero solo para usuarios internos / equipo (1-2 días de observación).
  4. Si todo está estable → subir al 5% → 20% con observación de 48 h en cada paso.
  5. Criterio de rollback automático: **cualquier aumento > 0,5% en errores de pago** activa el Kill-Switch inmediato en ConfigCat (< 60 segundos).

---

### 💡 Resumen de la Decisión Madura
> **Se protege la confianza del pipeline y la disciplina TBD por encima de la presión comercial de corto plazo. Se comunica con transparencia al stakeholder y se define un camino claro y seguro de liberación.**

---

### 🧩 Análisis de Complejidad y Negociación del Caso
> *“Este caso es suficientemente difícil porque combina presión de negocio, deuda técnica, fallos recientes de pipeline, falta de métricas y ruptura de disciplina TBD. Obliga al equipo a negociar, priorizar y aplicar todo lo aprendido en los cuatro talleres.”*

---

## 🛠️ Ejecución y Pruebas

### 1. Frontend React 18 + Vite + ConfigCat
```bash
# Instalar dependencias
npm install

# Compilar para producción (DoD Técnico)
npm run build

# Iniciar en modo desarrollo
npm run dev
```

### 2. Backend FastAPI / Tests Deterministas (Python)
```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar pruebas unitarias deterministas (test flaky resuelto)
pytest tests/ -v

# Linter de código
ruff check .
```

### 3. Generar el Informe Oficial Word (.docx)
```bash
python build_docx_report.py
```
Genera: `INFORME_TALLER_6_CONTINUOUS_DEPLOYMENT.docx` con estilos institucionales de UNIPUTUMAYO.

---

## 📁 Estructura del Proyecto

```text
├── .github/workflows/ci-cd.yml      # Pipeline CI/CD con auto-deploy a Render
├── src/                             # Aplicación React 18 + Vite + TypeScript
│   ├── components/
│   │   ├── SprintReviewBanner.tsx   # Protocolo de Demo y Speech transparente del PO
│   │   ├── ConfigCatControls.tsx    # Conmutación de Feature Flags y Kill-Switch
│   │   ├── RetrospectiveMiroBoard.tsx # Tablero Miro con las 3 acciones y el acuerdo de 7 deploys
│   │   ├── CanaryPolicyCard.tsx     # Plan de 5 pasos, decisión madura y complejidad
│   │   ├── MetricsDashboard.tsx     # Telemetría de pagos (errores, latencia y conversión)
│   │   ├── StandardCheckout.tsx     # Flujo estándar de pago (Toggle OFF)
│   │   └── ExpressCheckout.tsx      # Flujo express en 1 clic (Toggle ON)
│   ├── services/configcat.ts        # Integración con ConfigCat SDK
│   └── App.tsx                      # Componente raíz con navegación por tabs
├── app/                             # Módulos Python FastAPI (Healthcheck, Telemetría, Pagos)
├── tests/                           # Tests unitarios deterministas sin flakiness
├── build_docx_report.py             # Generador automatizado del informe oficial Word
├── INFORME_TALLER_6_CONTINUOUS_DEPLOYMENT.docx # Documento formal Word institucional
├── SCRUM_TBD_PLAYBOOK_v3.md          # Playbook Scrum + TBD Versión 3.0
├── TALLER_6_INFORME_COMPLETO.md     # Informe completo en Markdown
└── README.md                        # Documentación principal del repositorio
```

---

### Frase Oficial de Transformación Cultural:
> *“Desplegar a producción ya no es un evento de cierre de sprint, sino una rutina continua e invisible; el Review valida el impacto del valor real y la Retrospectiva protege la salud del pipeline y la disciplina diaria de integración.”*
