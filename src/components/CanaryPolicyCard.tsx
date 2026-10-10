import React from 'react';

export const CanaryPolicyCard: React.FC = () => {
  return (
    <div className="glass-card animate-fade-in" id="canary-policy-container" style={{ borderLeft: '4px solid #f59e0b' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 18 }}>
        <div>
          <span className="badge badge-yellow">Decisión de Liberación Segura</span>
          <h2 style={{ fontSize: 20, marginTop: 4, color: '#f8fafc' }}>
            Evaluación Técnica: ¿Activar al 20% el Viernes?
          </h2>
        </div>
        <span className="badge badge-red" style={{ fontSize: 13, padding: '6px 14px' }}>
          ⛔ DECISIÓN: RECHAZAR LA ACTIVACIÓN
        </span>
      </div>

      <div style={{ background: 'rgba(239, 68, 68, 0.08)', border: '1px solid rgba(239, 68, 68, 0.25)', borderRadius: 10, padding: 14, marginBottom: 20 }}>
        <strong style={{ color: '#f87171', fontSize: 14 }}>Justificación Técnica del Equipo de Ingeniería:</strong>
        <p style={{ fontSize: 13, color: '#cbd5e1', marginTop: 4 }}>
          Incumple las ventanas seguras de despliegue (no liberar antes del fin de semana sin guardia técnica activa); existe un antecedente reciente de fallo en health check durante el último deploy; y no existe telemetría previa para monitorear caídas o transacciones bancarias fallidas.
        </p>
      </div>

      <h3 style={{ fontSize: 16, color: '#f8fafc', marginBottom: 12 }}>
        📅 Estrategia de Liberación Progresiva Aprobada (Canary Rollout)
      </h3>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: 14, marginBottom: 22 }}>
        <div style={{ background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-color)', borderRadius: 10, padding: 14 }}>
          <span className="badge badge-purple" style={{ background: 'rgba(121, 40, 202, 0.2)', color: '#c084fc' }}>Fase 0: Lunes</span>
          <h4 style={{ fontSize: 14, margin: '6px 0 2px', color: '#fff' }}>Interno / Dogfooding</h4>
          <p style={{ fontSize: 13, color: '#94a3b8' }}>
            Activación al 100% exclusivamente para correos del equipo de desarrollo, QA y Product Owner en ConfigCat.
          </p>
        </div>

        <div style={{ background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-color)', borderRadius: 10, padding: 14 }}>
          <span className="badge badge-blue">Fase 1: Martes</span>
          <h4 style={{ fontSize: 14, margin: '6px 0 2px', color: '#fff' }}>Canary 5% Tráfico Real</h4>
          <p style={{ fontSize: 13, color: '#94a3b8' }}>
            Activación para el 5% de usuarios reales en horario laboral diurno, manteniendo monitoreo activo por 24 horas.
          </p>
        </div>

        <div style={{ background: 'rgba(255, 255, 255, 0.03)', border: '1px solid var(--border-color)', borderRadius: 10, padding: 14 }}>
          <span className="badge badge-green">Fase 2: Miércoles - Jueves</span>
          <h4 style={{ fontSize: 14, margin: '6px 0 2px', color: '#fff' }}>Escalado Gradual a GA</h4>
          <p style={{ fontSize: 13, color: '#94a3b8' }}>
            Si los fallos permanecen &lt; 0.5%, escalar progresivamente al 20%, 50% y finalmente al 100% (General Availability).
          </p>
        </div>
      </div>

      {/* Frase X */}
      <div style={{ background: 'linear-gradient(135deg, rgba(0, 102, 204, 0.15), rgba(0, 212, 178, 0.15))', border: '1px solid rgba(0, 212, 178, 0.3)', borderRadius: 12, padding: 18 }}>
        <span style={{ fontSize: 12, textTransform: 'uppercase', letterSpacing: 1, color: 'var(--accent-cyan)', fontWeight: 700 }}>
          Frase Oficial de Transformación Cultural:
        </span>
        <blockquote style={{ fontSize: 15, fontStyle: 'italic', color: '#fff', marginTop: 6, lineHeight: 1.6 }}>
          “Desplegar a producción ya no es un evento de cierre de sprint, sino una rutina continua e invisible; el Review valida el impacto del valor real y la Retrospectiva protege la salud del pipeline y la disciplina diaria de integración.”
        </blockquote>
      </div>
    </div>
  );
};
