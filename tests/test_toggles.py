"""
Pruebas del Administrador de Feature Toggles y Targeting.
"""

from app.toggles import ToggleManager

def test_default_toggle_state_is_off():
    manager = ToggleManager()
    assert manager.is_enabled("pagos-express-v1", user_id="user-123") is False

def test_toggle_override_to_on():
    manager = ToggleManager()
    manager.set_local_override("pagos-express-v1", True)
    assert manager.is_enabled("pagos-express-v1", user_id="user-123") is True

def test_internal_user_canary_whitelisting():
    manager = ToggleManager()
    manager.set_local_override("pagos-express-v1", False)
    manager.set_local_override("canary_internal_active", True)
    
    # Usuario público regular: recibe False (toggle apagado)
    assert manager.is_enabled("pagos-express-v1", user_id="user-999", user_email="cliente@gmail.com") is False
    
    # Usuario interno corporativo: recibe True (acceso anticipado seguro)
    assert manager.is_enabled("pagos-express-v1", user_id="dev-001", user_email="franklin@empresa.com") is True
    assert manager.is_enabled("pagos-express-v1", user_id="po-001", user_email="po@uniputumayo.edu.co") is True

def test_user_specific_override():
    manager = ToggleManager()
    manager.set_local_override("pagos-express-v1", False)
    manager.set_user_override("qa-tester-vip", True)
    
    assert manager.is_enabled("pagos-express-v1", user_id="qa-tester-vip") is True
    assert manager.is_enabled("pagos-express-v1", user_id="other-user") is False
