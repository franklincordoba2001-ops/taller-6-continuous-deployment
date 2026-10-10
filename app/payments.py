"""
Módulo del Servicio de Pagos y Procesamiento de Checkout.
Implementa 'Pagos Express' tras Feature Flag y 'Checkout Estándar' como fallback.
"""

import time
from typing import Dict, Any, Optional
from app.toggles import toggle_manager
from app.metrics import telemetry

class PaymentService:
    def process_checkout(
        self,
        amount: float,
        user_id: str,
        user_email: Optional[str] = None,
        use_one_click: bool = True
    ) -> Dict[str, Any]:
        """
        Procesa una compra decidiendo si utiliza Pagos Express o el flujo tradicional,
        evaluando dinámicamente el Feature Flag 'pagos-express-v1'.
        """
        start_time = time.time()
        
        # 1. Evaluar si la funcionalidad está activa para este usuario o porcentaje
        is_express_enabled = toggle_manager.is_enabled(
            key="pagos-express-v1",
            user_id=user_id,
            user_email=user_email,
            default=False
        )

        # 2. Decisión de flujo
        if is_express_enabled and use_one_click:
            result = self._process_express_payment(amount, user_id, user_email)
        else:
            result = self._process_standard_payment(amount, user_id, user_email)

        # 3. Registrar latencia y métricas para observabilidad
        latency_ms = (time.time() - start_time) * 1000
        telemetry.record_checkout(
            is_express=result.get("is_express_flow", False),
            success=result.get("success", False),
            latency_ms=latency_ms
        )
        
        result["latency_ms"] = round(latency_ms, 2)
        return result

    def _process_express_payment(self, amount: float, user_id: str, user_email: Optional[str]) -> Dict[str, Any]:
        """Flujo de Pagos Express (1-Click Checkout)."""
        # Validación de negocio
        if amount <= 0:
            return {
                "success": False,
                "error": "El monto debe ser superior a 0",
                "is_express_flow": True,
                "flow_type": "EXPRESS_ONE_CLICK",
                "message": "Fallo en validación de monto"
            }

        return {
            "success": True,
            "transaction_id": f"EXP-{int(time.time()*1000)}-{user_id[:4]}",
            "amount": amount,
            "user_id": user_id,
            "user_email": user_email,
            "flow_type": "EXPRESS_ONE_CLICK",
            "is_express_flow": True,
            "payment_method": "Pre-authorized Token (Tokenized 1-Click)",
            "message": "¡Pago procesado exitosamente en 1 solo clic!"
        }

    def _process_standard_payment(self, amount: float, user_id: str, user_email: Optional[str]) -> Dict[str, Any]:
        """Flujo Tradicional / Estándar de 3 pasos."""
        if amount <= 0:
            return {
                "success": False,
                "error": "El monto debe ser superior a 0",
                "is_express_flow": False,
                "flow_type": "STANDARD_MULTI_STEP",
                "message": "Fallo en validación de monto"
            }

        return {
            "success": True,
            "transaction_id": f"STD-{int(time.time()*1000)}-{user_id[:4]}",
            "amount": amount,
            "user_id": user_id,
            "user_email": user_email,
            "flow_type": "STANDARD_MULTI_STEP",
            "is_express_flow": False,
            "payment_method": "Credit Card Gateway (Multi-step verification)",
            "message": "Pago procesado a través del flujo tradicional de 3 pasos."
        }

payment_service = PaymentService()
