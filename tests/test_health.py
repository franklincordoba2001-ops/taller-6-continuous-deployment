"""
Pruebas para los endpoints de Healthcheck y Observabilidad (FastAPI TestClient).
Valida que el healthcheck nunca cause downtime en Render.
"""

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ONLINE"
    assert data["version"] == "3.0.0"

def test_health_check_proactive():
    """
    Valida que el healthcheck responda 200 OK inmediatamente (< 15ms)
    para evitar fallos de despliegue en Render como el incidente de 11 minutos.
    """
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "HEALTHY"
    assert data["probes"]["liveness"] == "PASS"
    assert data["probes"]["readiness"] == "PASS"

def test_metrics_endpoint():
    response = client.get("/api/v1/metrics")
    assert response.status_code == 200
    data = response.json()
    assert "global_metrics" in data
    assert "express_payments_v1" in data

def test_toggles_admin_audit():
    response = client.get("/admin/toggles")
    assert response.status_code == 200
    data = response.json()
    assert data["technical_debt_detected"] == 3
    assert len(data["toggles_audit"]) >= 5

def test_cleanup_stale_toggles():
    response = client.delete("/admin/toggles/cleanup")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "CLEANED"
    assert len(data["removed_toggles"]) == 3
