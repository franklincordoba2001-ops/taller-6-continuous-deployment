import React from 'react';

export const SprintReviewBanner: React.FC = () => {
  return (
    <div className="glass-card animate-fade-in" style={{ borderLeft: '4px solid #0066cc', marginBottom: 20 }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 12, flexWrap: 'wrap', gap: 10 }}>
        <div>
          <span className="badge badge-blue">Sprint Review en Continuous Deployment</span>
          <h3 style={{ fontSize: 17, marginTop: 4, color: '#f8fafc' }}>
            Protocolo Oficial de Demo & Comunicación de Producto
          </h3>
        </div>
        <span className="badge badge-yellow" style={{ fontSize: 12 }}>
          ⚠️ No se compromete fecha al 20% en el Review
        </span>
      </div>

      {/* Pasos de la Demo */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: 12, marginBottom: 16 }}>
        <div style={{ background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-color)', borderRadius: 8, padding: 12 }}>
          <strong style={{ color: '#93c5fd', fontSize: 13 }}>1. Demo en OFF Primero (Estado Real Actual)</strong>
          <p style={{ fontSize: 12, color: '#94a3b8', margin: '4px 0 0' }}>
            Se proyecta la app con toggle en OFF mostrando la pasarela estándar; demuestra que no hay afectación en producción.
          </p>
        </div>
        <div style={{ background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-color)', borderRadius: 8, padding: 12 }}>
          <strong style={{ color: '#34d399', fontSize: 13 }}>2. Activación Temporal Solo para el Equipo</strong>
          <p style={{ fontSize: 12, color: '#94a3b8', margin: '4px 0 0' }}>
            Se activa temporalmente para el equipo o usuario de prueba interno, validando el flujo de 1 clic sin redeploy.
          </p>
        </div>
      </div>

      {/* Speech Oficial Transparente del PO */}
      <div style={{ background: 'rgba(0, 102, 204, 0.08)', border: '1px solid rgba(0, 102, 204, 0.3)', borderRadius: 10, padding: 14 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}>
          <span style={{ fontSize: 18 }}>🗣️</span>
          <span style={{ fontSize: 12, textTransform: 'uppercase', letterSpacing: 0.8, color: '#60a5fa', fontWeight: 700 }}>
            El PO Comunica con Transparencia a los Stakeholders:
          </span>
        </div>
        <blockquote style={{ fontSize: 13.5, fontStyle: 'italic', color: '#e0f2fe', lineHeight: 1.5, margin: 0 }}>
          “La funcionalidad está técnicamente lista y desplegada, pero todavía no la hemos liberado a usuarios reales porque necesitamos definir métricas de observación y resolver riesgos de estabilidad del pipeline. La campaña de marketing se pausará o se ajustará.”
        </blockquote>
      </div>
    </div>
  );
};
