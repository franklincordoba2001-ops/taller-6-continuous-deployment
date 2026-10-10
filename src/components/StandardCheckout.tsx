import React, { useState } from 'react';

interface Props {
  onSuccess: (latency: number) => void;
}

export const StandardCheckout: React.FC<Props> = ({ onSuccess }) => {
  const [step, setStep] = useState(1);
  const [loading, setLoading] = useState(false);
  const [formData, setFormData] = useState({
    predioId: 'PREDIO-MOCOA-2026-884',
    propietario: 'Franklin Sneider Córdoba',
    banco: 'Bancolombia',
    tarjeta: '**** **** **** 4892',
    cvv: '***',
    cuotas: '1'
  });

  const handleNext = () => {
    if (step < 3) {
      setStep(step + 1);
    } else {
      setLoading(true);
      const start = performance.now();
      // Simula el tiempo de procesamiento tradicional (lento y con pasos intermedios)
      setTimeout(() => {
        setLoading(false);
        const latency = performance.now() - start;
        onSuccess(latency);
      }, 1200);
    }
  };

  return (
    <div className="glass-card animate-fade-in" id="standard-checkout-container" style={{ borderLeft: '4px solid #ef4444' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
        <div>
          <span className="badge badge-red">Estado OFF: Pasarela Estándar (Multi-paso)</span>
          <h2 style={{ fontSize: 20, marginTop: 6, color: '#f8fafc' }}>
            Liquidación de Trámites Catastrales
          </h2>
        </div>
        <div style={{ textAlign: 'right' }}>
          <span style={{ fontSize: 13, color: '#94a3b8' }}>Tiempo Promedio de Trámite</span>
          <p style={{ fontSize: 16, fontWeight: 700, color: '#f87171' }}>~3 Minutos (Alta Fricción)</p>
        </div>
      </div>

      <p style={{ color: '#94a3b8', fontSize: 14, marginBottom: 20 }}>
        El Feature Flag <code>pagos-express-v1</code> se encuentra apagado. El ciudadano debe completar todos los formularios bancarios tradicionales antes de autorizar el débito.
      </p>

      {/* Indicador de Pasos */}
      <div style={{ display: 'flex', gap: 10, marginBottom: 24 }}>
        {['1. Datos del Predio', '2. Información Bancaria', '3. Confirmación'].map((title, idx) => (
          <div
            key={idx}
            style={{
              flex: 1,
              padding: '8px 12px',
              borderRadius: 8,
              fontSize: 13,
              fontWeight: 600,
              background: step === idx + 1 ? 'rgba(0, 102, 204, 0.25)' : 'rgba(255, 255, 255, 0.05)',
              border: step === idx + 1 ? '1px solid #60a5fa' : '1px solid transparent',
              color: step === idx + 1 ? '#60a5fa' : '#64748b',
              textAlign: 'center'
            }}
          >
            {title}
          </div>
        ))}
      </div>

      {step === 1 && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16, marginBottom: 20 }}>
          <div>
            <label style={{ fontSize: 13, color: '#94a3b8', display: 'block', marginBottom: 6 }}>Ficha Catastral</label>
            <input
              id="input-predio-id"
              type="text"
              readOnly
              value={formData.predioId}
              style={{ width: '100%', background: '#0a0f1d', border: '1px solid var(--border-color)', color: '#fff', padding: '10px 14px', borderRadius: 8 }}
            />
          </div>
          <div>
            <label style={{ fontSize: 13, color: '#94a3b8', display: 'block', marginBottom: 6 }}>Contribuyente Registrado</label>
            <input
              id="input-propietario"
              type="text"
              readOnly
              value={formData.propietario}
              style={{ width: '100%', background: '#0a0f1d', border: '1px solid var(--border-color)', color: '#fff', padding: '10px 14px', borderRadius: 8 }}
            />
          </div>
          <div style={{ gridColumn: 'span 2' }}>
            <label style={{ fontSize: 13, color: '#94a3b8', display: 'block', marginBottom: 6 }}>Concepto de Liquidación</label>
            <div style={{ background: '#0d1527', padding: '12px 16px', borderRadius: 8, border: '1px solid var(--border-color)', fontSize: 14 }}>
              Impuesto Predial Unificado Vigencia 2026 - Municipio de Mocoa: <strong>$ 342.500 COP</strong>
            </div>
          </div>
        </div>
      )}

      {step === 2 && (
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: 16, marginBottom: 20 }}>
          <div>
            <label style={{ fontSize: 13, color: '#94a3b8', display: 'block', marginBottom: 6 }}>Entidad Bancaria</label>
            <select
              id="select-banco"
              value={formData.banco}
              onChange={(e) => setFormData({ ...formData, banco: e.target.value })}
              style={{ width: '100%', background: '#0a0f1d', border: '1px solid var(--border-color)', color: '#fff', padding: '10px 14px', borderRadius: 8 }}
            >
              <option value="Bancolombia">Bancolombia PSE</option>
              <option value="Banco de Bogotá">Banco de Bogotá</option>
              <option value="Davivienda">Davivienda</option>
            </select>
          </div>
          <div>
            <label style={{ fontSize: 13, color: '#94a3b8', display: 'block', marginBottom: 6 }}>Número de Tarjeta / Cuenta</label>
            <input
              id="input-tarjeta"
              type="text"
              readOnly
              value={formData.tarjeta}
              style={{ width: '100%', background: '#0a0f1d', border: '1px solid var(--border-color)', color: '#fff', padding: '10px 14px', borderRadius: 8 }}
            />
          </div>
        </div>
      )}

      {step === 3 && (
        <div style={{ background: 'rgba(239, 68, 68, 0.05)', border: '1px solid rgba(239, 68, 68, 0.2)', padding: 16, borderRadius: 10, marginBottom: 20 }}>
          <p style={{ fontSize: 14, color: '#fca5a5' }}>
            ⚠️ <strong>Confirmación Requerida:</strong> Por favor revise meticulosamente los datos. Este proceso tradicional requiere redirección externa y validación de token de seguridad SMS (demora estimada: 180 segundos).
          </p>
        </div>
      )}

      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        {step > 1 ? (
          <button id="btn-prev-step" className="btn-outline" onClick={() => setStep(step - 1)}>
            ← Paso Anterior
          </button>
        ) : <div />}

        <button id="btn-next-step" className="btn-primary" onClick={handleNext} disabled={loading} style={{ background: '#2563eb', color: '#fff' }}>
          {loading ? 'Procesando en Pasarela Externa...' : step === 3 ? 'Completar Formulario y Pagar' : 'Continuar al Siguiente Paso →'}
        </button>
      </div>
    </div>
  );
};
