import React from 'react';

export const CanaryPolicyCard: React.FC = () => {
  return (
    <div className="glass-card animate-fade-in" id="canary-policy-container" style={{ borderLeft: '4px solid #f59e0b' }}>
      {/* Header */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 18, flexWrap: 'wrap', gap: 12 }}>
        <div>
          <span className="badge badge-yellow">Estrategia de Liberación Segura</span>
          <h2 style={{ fontSize: 20, marginTop: 4, color: '#f8fafc' }}>
            Evaluación Técnica: ¿Activar al 20% el Viernes?
          </h2>
        </div>
        <span className="badge badge-red" style={{ fontSize: 13, padding: '6px 14px' }}>
          ⛔ DECISIÓN FINAL: NO SE ACTIVA EL 20% ESTE VIERNES
        </span>
      </div>

      {/* Justificación Técnica */}
      <div style={{ background: 'rgba(239, 68, 68, 0.08)', border: '1px solid rgba(239, 68, 68, 0.25)', borderRadius: 10, padding: 14, marginBottom: 20 }}>
        <strong style={{ color: '#f87171', fontSize: 14 }}>Justificación Técnica del Equipo:</strong>
        <p style={{ fontSize: 13, color: '#cbd5e1', marginTop: 4, lineHeight: 1.5 }}>
          Liberar antes del fin de semana sin guardia técnica activa viola las ventanas seguras; se presentó una caída de 11 minutos por health check fallido en el último deploy; persisten tests flaky en CI; y no existe dashboard de telemetría de errores bancarios ni conversión.
        </p>
      </div>

      {/* Plan Acordado de 5 Pasos */}
      <h3 style={{ fontSize: 16, color: '#f8fafc', marginBottom: 12 }}>
        📅 Plan Acordado de Liberación Segura (5 Pasos Oficiales)
      </h3>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: 14, marginBottom: 22 }}>
        <div style={{ background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-color)', borderRadius: 10, padding: 14 }}>
          <span className="badge badge-blue">Paso 1: Esta Semana</span>
          <h4 style={{ fontSize: 14, margin: '6px 0 2px', color: '#fff' }}>Estabilidad & Higiene TBD</h4>
          <p style={{ fontSize: 13, color: '#94a3b8' }}>
            Resolver test flaky de CI (&lt; 24h) + limpiar y retirar los 3 toggles viejos acumulados (+45 días).
          </p>
        </div>

        <div style={{ background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-color)', borderRadius: 10, padding: 14 }}>
          <span className="badge badge-cyan">Paso 2: Máximo 3 Días</span>
          <h4 style={{ fontSize: 14, margin: '6px 0 2px', color: '#fff' }}>Dashboard de Telemetría</h4>
          <p style={{ fontSize: 13, color: '#94a3b8' }}>
            Implementar métricas básicas de pagos: monitoreo en tiempo real de tasa de errores (HTTP 5xx) y tasa de conversión.
          </p>
        </div>

        <div style={{ background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-color)', borderRadius: 10, padding: 14 }}>
          <span className="badge badge-purple" style={{ background: 'rgba(121, 40, 202, 0.2)', color: '#c084fc' }}>Paso 3: 1-2 Días</span>
          <h4 style={{ fontSize: 14, margin: '6px 0 2px', color: '#fff' }}>Dogfooding Interno</h4>
          <p style={{ fontSize: 13, color: '#94a3b8' }}>
            Activar primero solo para usuarios internos / equipo en ConfigCat para observación y validación técnica sin riesgo público.
          </p>
        </div>

        <div style={{ background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-color)', borderRadius: 10, padding: 14 }}>
          <span className="badge badge-yellow">Paso 4: 48h Observación</span>
          <h4 style={{ fontSize: 14, margin: '6px 0 2px', color: '#fff' }}>Canary 5% → 20%</h4>
          <p style={{ fontSize: 13, color: '#94a3b8' }}>
            Si todo está estable → subir gradualmente al 5% y luego al 20% con observación rigurosa de 48 horas en cada paso.
          </p>
        </div>

        <div style={{ background: 'rgba(239, 68, 68, 0.05)', border: '1px solid rgba(239, 68, 68, 0.3)', borderRadius: 10, padding: 14 }}>
          <span className="badge badge-red">Paso 5: Kill-Switch</span>
          <h4 style={{ fontSize: 14, margin: '6px 0 2px', color: '#f87171' }}>Rollback Automático</h4>
          <p style={{ fontSize: 13, color: '#cbd5e1' }}>
            Criterio de rollback automático: <strong>cualquier aumento &gt; 0,5% en errores de pago</strong> desactiva de inmediato el toggle en &lt; 60 segundos.
          </p>
        </div>
      </div>

      {/* Resumen de la Decisión Madura */}
      <div style={{ background: 'linear-gradient(135deg, rgba(16, 185, 129, 0.12), rgba(5, 150, 105, 0.08))', border: '1px solid rgba(16, 185, 129, 0.35)', borderRadius: 12, padding: 16, marginBottom: 16 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
          <span style={{ fontSize: 20 }}>💡</span>
          <span style={{ fontSize: 13, textTransform: 'uppercase', letterSpacing: 0.8, color: '#34d399', fontWeight: 700 }}>
            Resumen de la Decisión Madura:
          </span>
        </div>
        <p style={{ fontSize: 14, color: '#ecfdf5', fontWeight: 600, lineHeight: 1.5, margin: 0 }}>
          “Se protege la confianza del pipeline y la disciplina TBD por encima de la presión comercial de corto plazo. Se comunica con transparencia al stakeholder y se define un camino claro y seguro de liberación.”
        </p>
      </div>

      {/* Análisis de Complejidad y Negociación del Caso */}
      <div style={{ background: 'linear-gradient(135deg, rgba(121, 40, 202, 0.12), rgba(99, 102, 241, 0.08))', border: '1px solid rgba(121, 40, 202, 0.35)', borderRadius: 12, padding: 16, marginBottom: 16 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10, marginBottom: 6 }}>
          <span style={{ fontSize: 20 }}>🧩</span>
          <span style={{ fontSize: 13, textTransform: 'uppercase', letterSpacing: 0.8, color: '#c084fc', fontWeight: 700 }}>
            Análisis de Complejidad y Negociación del Caso:
          </span>
        </div>
        <p style={{ fontSize: 13.5, color: '#f3e8ff', fontStyle: 'italic', lineHeight: 1.6, margin: 0 }}>
          “Este caso es suficientemente difícil porque combina presión de negocio, deuda técnica, fallos recientes de pipeline, falta de métricas y ruptura de disciplina TBD. Obliga al equipo a negociar, priorizar y aplicar todo lo aprendido en los cuatro talleres.”
        </p>
      </div>

      {/* Frase X */}
      <div style={{ background: 'linear-gradient(135deg, rgba(0, 102, 204, 0.15), rgba(0, 212, 178, 0.15))', border: '1px solid rgba(0, 212, 178, 0.3)', borderRadius: 12, padding: 18 }}>
        <span style={{ fontSize: 12, textTransform: 'uppercase', letterSpacing: 1, color: 'var(--accent-cyan)', fontWeight: 700 }}>
          Frase Oficial de Transformación Cultural:
        </span>
        <blockquote style={{ fontSize: 14.5, fontStyle: 'italic', color: '#fff', marginTop: 6, lineHeight: 1.6 }}>
          “Desplegar a producción ya no es un evento de cierre de sprint, sino una rutina continua e invisible; el Review valida el impacto del valor real y la Retrospectiva protege la salud del pipeline y la disciplina diaria de integración.”
        </blockquote>
      </div>
    </div>
  );
};
