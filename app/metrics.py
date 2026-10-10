"""
Módulo de Métricas y Telemetría Operativa y de Negocio.
Proporciona observabilidad para el ciclo de vida de Feature Toggles y Rollouts Seguros.
"""

import time
from typing import Dict, Any

class TelemetryCollector:
    def __init__(self):
        self.start_time = time.time()
        self.total_requests = 0
        self.health_checks = 0
        self.deploy_count = 1
        
        # Métricas de Checkout & Pagos
        self.standard_checkout_attempts = 0
        self.standard_checkout_success = 0
        self.standard_checkout_errors = 0
        
        self.express_checkout_attempts = 0
        self.express_checkout_success = 0
        self.express_checkout_errors = 0
        
        # Historial de latencias (en milisegundos)
        self.latencies_ms = []

    def reset(self):
        """Reinicia los contadores para aislamiento en suites de prueba."""
        self.total_requests = 0
        self.health_checks = 0
        self.standard_checkout_attempts = 0
        self.standard_checkout_success = 0
        self.standard_checkout_errors = 0
        self.express_checkout_attempts = 0
        self.express_checkout_success = 0
        self.express_checkout_errors = 0
        self.latencies_ms = []

    def record_checkout(self, is_express: bool, success: bool, latency_ms: float):
        self.total_requests += 1
        self.latencies_ms.append(latency_ms)
        if len(self.latencies_ms) > 1000:
            self.latencies_ms.pop(0)  # Mantener ventana deslizante

        if is_express:
            self.express_checkout_attempts += 1
            if success:
                self.express_checkout_success += 1
            else:
                self.express_checkout_errors += 1
        else:
            self.standard_checkout_attempts += 1
            if success:
                self.standard_checkout_success += 1
            else:
                self.standard_checkout_errors += 1

    def record_healthcheck(self):
        self.health_checks += 1

    def get_summary(self) -> Dict[str, Any]:
        uptime_seconds = round(time.time() - self.start_time, 2)
        
        total_checkouts = self.standard_checkout_attempts + self.express_checkout_attempts
        total_errors = self.standard_checkout_errors + self.express_checkout_errors
        total_success = self.standard_checkout_success + self.express_checkout_success
        
        global_conversion_rate = (
            round((total_success / total_checkouts) * 100, 2) if total_checkouts > 0 else 100.0
        )
        
        express_conversion_rate = (
            round((self.express_checkout_success / self.express_checkout_attempts) * 100, 2)
            if self.express_checkout_attempts > 0 else 0.0
        )
        
        error_rate = (
            round((total_errors / total_checkouts) * 100, 2) if total_checkouts > 0 else 0.0
        )
        
        avg_latency_ms = (
            round(sum(self.latencies_ms) / len(self.latencies_ms), 2)
            if self.latencies_ms else 45.0
        )

        return {
            "uptime_seconds": uptime_seconds,
            "total_health_checks": self.health_checks,
            "global_metrics": {
                "total_checkouts": total_checkouts,
                "successful_transactions": total_success,
                "failed_transactions": total_errors,
                "error_rate_pct": error_rate,
                "conversion_rate_pct": global_conversion_rate,
                "avg_latency_ms": avg_latency_ms
            },
            "express_payments_v1": {
                "attempts": self.express_checkout_attempts,
                "successes": self.express_checkout_success,
                "errors": self.express_checkout_errors,
                "conversion_rate_pct": express_conversion_rate,
                "status_threshold": "HEALTHY" if error_rate < 1.0 else "UNSTABLE"
            },
            "standard_payments": {
                "attempts": self.standard_checkout_attempts,
                "successes": self.standard_checkout_success,
                "errors": self.standard_checkout_errors
            }
        }

telemetry = TelemetryCollector()
