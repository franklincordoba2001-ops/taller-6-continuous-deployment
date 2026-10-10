# 🚀 Taller 6: Sprint Review, Retrospective y Liberación Segura en Continuous Deployment

**Estudiante:** Franklin Sneider Córdoba De La Cruz  
**Docente:** Juan Pablo  
**Institución:** Institución Universitaria del Putumayo – UNIPUTUMAYO  
**Diplomado:** Integración Continua, Continuous Deployment & DevOps  
**Tecnologías:** Python 3.11, FastAPI, ConfigCat Feature Flags, Render, GitHub Actions, Docker, Pytest, Ruff.

---

## 📌 Descripción del Proyecto
Este repositorio contiene la solución completa, técnica y metodológica para el **Taller 6**:
- **Simulación y resolución del caso de estudio:** *"La funcionalidad de Pagos Express ya está en main, pero nadie se atreve a activarla"*.
- **Código ejecutable:** API en FastAPI con integración al SDK de **ConfigCat**, endpoints de **Checkout con Feature Toggle (`pagos-express-v1`)**, **Healthcheck proactivo desacoplado (`/health`)** para evitar fallos de despliegue en Render, y **Telemetría en tiempo real (`/api/v1/metrics`)**.
- **Suite de pruebas automatizadas deterministas:** Eliminación definitiva del test flaky que bloqueaba el pipeline en CI.
- **Pipeline de CI/CD:** GitHub Actions `.github/workflows/ci-cd.yml` con auto-deploy a Render.
- **Scrum + TBD Playbook Versión 3.0:** Protocolo oficial de Sprint Review en CD, nueva Sprint Retrospective enfocada en salud de pipeline y disciplina TBD, gobernanza de toggles con límite a 30 días, y cierre de Fase 1 al 100%.
- **Entregables:** Documento oficial Word `INFORME_TALLER_6_CONTINUOUS_DEPLOYMENT.docx` e informe detallado `TALLER_6_INFORME_COMPLETO.md`.

---

## 🛠️ Ejecución Local

### 1. Clonar e Instalar Dependencias
```bash
git clone https://github.com/franklincordoba2001-ops/taller-6-continuous-deployment.git
cd taller-6-continuous-deployment
pip install -r requirements.txt
```

### 2. Ejecutar Pruebas Automatizadas (DoD Técnico)
```bash
pytest tests/ -v
ruff check .
```

### 3. Iniciar el Servidor de Desarrollo
```bash
uvicorn app.main:app --reload --port 8000
```

Acceder en el navegador a:
- **Dashboard Interactivo de Demo:** `http://localhost:8000/demo/dashboard`
- **Documentación Swagger / OpenAPI:** `http://localhost:8000/docs`
- **Healthcheck Proactivo:** `http://localhost:8000/health`
- **Telemetría y Golden Signals:** `http://localhost:8000/api/v1/metrics`
- **Auditoría de Feature Toggles:** `http://localhost:8000/admin/toggles`

---

## 📁 Estructura del Repositorio

```text
├── .github/
│   └── workflows/
│       └── ci-cd.yml             # Pipeline de CI/CD con auto-deploy a Render
├── app/
│   ├── __init__.py
│   ├── main.py                  # API principal FastAPI y endpoints de negocio
│   ├── payments.py              # Servicio de pagos con bifurcación por Feature Toggle
│   ├── toggles.py               # Integración con ConfigCat y targeting por usuario/canary
│   └── metrics.py               # Observabilidad y Golden Signals en tiempo real
├── tests/
│   ├── __init__.py
│   ├── test_health.py           # Pruebas de liveness/readiness
│   ├── test_payments.py         # Pruebas de checkout y erradicación de test flaky
│   └── test_toggles.py          # Pruebas de targeting y fallback de flags
├── build_docx_report.py         # Script generador del informe institucional en Word
├── Dockerfile                   # Imagen Docker lista para producción en Render/GHCR
├── INFORME_TALLER_6_CONTINUOUS_DEPLOYMENT.docx # Documento formal para UNIPUTUMAYO
├── SCRUM_TBD_PLAYBOOK_v3.md     # Playbook Scrum + TBD Versión 3.0 oficial
├── TALLER_6_INFORME_COMPLETO.md # Informe técnico y metodológico detallado
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Guía principal del proyecto
```
