import React, { useState } from 'react';

interface Props {
  onSuccess: (latency: number) => void;
}

export const ExpressCheckout: React.FC<Props> = ({ onSuccess }) => {
  const [loading, setLoading] = useState(false);
  const [completed, setCompleted] = useState(false);

  const handlePay = () => {
    setLoading(true);
    const start = performance.now();
    setTimeout(() => {
      setLoading(false);
      setCompleted(true);
      const latency = performance.now() - start;
      onSuccess(latency);
    }, 400); // Rápido < 500 ms
  };

  return (
    <div className="glass-card animate-fade-in pulse-glow" id="express-checkout-container" style={{ borderLeft: '4px solid var(--accent-cyan)' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
        <div>
          <span className="badge badge-green">🟢 Estado ON: Pagos Express Activo</span>
          <h2 style={{ fontSize: 22, marginTop: 6, color: '#f8fafc' }}>
            Liquidación Catastral en 1 Clic
          </h2>
        </div>
        <div style={{ textAlign: 'right' }}>
          <span style={{ fontSize: 13, color: '#94a3b8' }}>Tiempo Estimado</span>
          <p style={{ fontSize: 18, fontWeight: 800, color: 'var(--accent-cyan)' }}>&lt; 10 Segundos</p>
        </div>
      </div>

      <p style={{ color: '#94a3b8', fontSize: 14, marginBottom: 20 }}>
        ¡El Feature Toggle <code>pagos-express-v1</code> está <strong>ACTIVO en ConfigCat</strong>! No tuviste que reconstruir la app ni redesplegar en Render: la interfaz se adaptó automáticamente en caliente.
      </p>

      {/* Tarjeta de Token y Firma Digital */}
      <div style={{ background: 'rgba(0, 212, 178, 0.06)', border: '1px solid rgba(0, 212, 178, 0.25)', borderRadius: 12, padding: 18, marginBottom: 22 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 4 }}>
              <span style={{ fontSize: 18 }}>🔑</span>
              <strong style={{ color: '#fff', fontSize: 15 }}>Firma Digital Autorizada & Token Guardado</strong>
            </div>
            <p style={{ fontSize: 13, color: '#94a3b8' }}>
              Contribuyente: <strong>Franklin Sneider Córdoba</strong> | Cédula vinculada a pasarela bancaria segura.
            </p>
          </div>
          <span className="badge badge-cyan">Pre-Autorizado</span>
        </div>

        <div style={{ marginTop: 14, paddingTop: 12, borderTop: '1px solid rgba(255,255,255,0.06)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div>
            <span style={{ fontSize: 12, color: '#64748b' }}>TOTAL A LIQUIDAR (PREDIAL 2026):</span>
            <div style={{ fontSize: 22, fontWeight: 800, color: '#fff' }}>$ 342.500 COP</div>
          </div>
          <div style={{ textAlign: 'right' }}>
            <span style={{ fontSize: 12, color: '#64748b' }}>CANAL DE PAGO:</span>
            <div style={{ fontSize: 13, color: 'var(--accent-cyan)', fontWeight: 600 }}>Débito Directo Express ⚡</div>
          </div>
        </div>
      </div>

      {completed ? (
        <div style={{ background: 'rgba(16, 185, 129, 0.12)', border: '1px solid rgba(16, 185, 129, 0.3)', borderRadius: 10, padding: 16, textAlign: 'center' }}>
          <h3 style={{ color: '#34d399', fontSize: 18, marginBottom: 6 }}>🎉 ¡Trámite Catastral Liquidado con Éxito!</h3>
          <p style={{ fontSize: 13, color: '#94a3b8' }}>
            Comprobante oficial N° <strong>EXP-2026-99120</strong> emitido en 8.4 segundos. Firma digital certificada para el municipio de Mocoa.
          </p>
          <button
            className="btn-outline"
            style={{ marginTop: 12, fontSize: 13 }}
            onClick={() => setCompleted(false)}
          >
            Hacer Otra Simulación
          </button>
        </div>
      ) : (
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
          <div style={{ fontSize: 12, color: '#64748b' }}>
            Protegido con cifrado TLS 1.3 & Feature Flag seguro
          </div>
          <button
            id="btn-pagar-un-clic"
            className="btn-primary"
            style={{ fontSize: 16, padding: '14px 28px' }}
            onClick={handlePay}
            disabled={loading}
          >
            {loading ? 'Liquidando en 1 Clic...' : '⚡ Pagar en 1 Clic con Pagos Express'}
          </button>
        </div>
      )}
    </div>
  );
};
