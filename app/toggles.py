"""
Gestor de Feature Toggles con integración a ConfigCat y Fallback Local Resiliente.
Taller 6: Continuous Deployment & Liberación Segura.
"""

import os
import logging
from typing import Optional, Dict, Any

try:
    import configcatclient
    from configcatclient import User
    CONFIGCAT_AVAILABLE = True
except ImportError:
    CONFIGCAT_AVAILABLE = False
    User = None  # type: ignore

logger = logging.getLogger("toggles")

class ToggleManager:
    """
    Gestiona los Feature Flags con soporte para ConfigCat SDK en la nube
    y modo local/simulado para pruebas y contingencias offline.
    """

    def __init__(self, sdk_key: Optional[str] = None):
        self.sdk_key = sdk_key or os.getenv("CONFIGCAT_SDK_KEY", "")
        self.client = None
        self._local_overrides: Dict[str, Any] = {
            "pagos-express-v1": False,           # Feature Flag del Taller 6 (Caso Pagos Express)
            "checkout-telemetry-v1": True,       # Toggle activo para telemetría
            "healthcheck-proactivo-v2": True,    # Toggle para nuevo healthcheck sin fallas de 11 min
            "legacy-cart-ui": False,             # Toggle técnico deprecado (> 45 días)
            "v1-tax-calculator": False,          # Toggle técnico deprecado (> 45 días)
            "old-notification-hook": False       # Toggle técnico deprecado (> 45 días)
        }
        self._user_targeting: Dict[str, bool] = {}

        self._init_client()

    def _init_client(self):
        if self.sdk_key and CONFIGCAT_AVAILABLE:
            try:
                self.client = configcatclient.get(
                    sdk_key=self.sdk_key,
                    options=configcatclient.ConfigCatOptions(
                        poll_interval_seconds=60,
                        request_timeout_seconds=5
                    )
                )
                logger.info("ConfigCat SDK inicializado correctamente en modo cloud.")
            except Exception as e:
                logger.warning(f"Error al inicializar ConfigCat SDK: {e}. Usando fallback local resiliente.")
                self.client = None
        else:
            logger.info("Modo de Feature Toggles local/simulado activo (sin SDK Key o para pruebas).")

    def is_enabled(self, key: str, user_id: Optional[str] = None, user_email: Optional[str] = None, default: bool = False) -> bool:
        """
        Evalúa si un toggle está activo considerando targeting por usuario o porcentaje.
        """
        # Si hay override forzado para un usuario específico (ej: test interno o QA)
        if user_id and user_id in self._user_targeting:
            return self._user_targeting[user_id]
        
        # Si el usuario es empleado interno (Whitelisting para canary release interno)
        if user_email and (user_email.endswith("@empresa.com") or user_email.endswith("@uniputumayo.edu.co")):
            # Si el toggle está en evaluación activa (como pagos-express-v1), los internos tienen acceso anticipado
            if key == "pagos-express-v1" and self._local_overrides.get("canary_internal_active", True):
                return True

        if self.client and CONFIGCAT_AVAILABLE:
            try:
                user = User(identifier=user_id or "anonymous", email=user_email) if User else None
                return self.client.get_value(key, default, user)
            except Exception as e:
                logger.error(f"Error evaluando toggle '{key}' con ConfigCat: {e}. Usando valor local de fallback.")
                return self._local_overrides.get(key, default)

        return self._local_overrides.get(key, default)

    def set_local_override(self, key: str, value: bool):
        """Permite forzar o simular el toggle localmente (útil para demos y pruebas)."""
        self._local_overrides[key] = value
        logger.info(f"Toggle '{key}' actualizado localmente a: {value}")

    def set_user_override(self, user_id: str, value: bool):
        """Asigna un valor específico a un usuario para pruebas dirigidas (Targeting)."""
        self._user_targeting[user_id] = value

    def get_all_states(self) -> Dict[str, Any]:
        """Retorna el estado actual de todos los toggles gestionados."""
        return {
            "toggles": dict(self._local_overrides),
            "targeting_users_count": len(self._user_targeting),
            "cloud_connected": bool(self.client is not None),
            "sdk_configured": bool(bool(self.sdk_key))
        }

# Instancia singleton para la aplicación
toggle_manager = ToggleManager()
