import React from 'react';

export const RetrospectiveMiroBoard: React.FC = () => {
  return (
    <div className="glass-card animate-fade-in" id="retrospective-miro-container">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
        <div>
          <span className="badge badge-blue">Sprint Retrospective Adaptada a Continuous Deployment</span>
          <h2 style={{ fontSize: 20, marginTop: 4, color: '#f8fafc' }}>
            Tablero Miro de Inspección de Flujo, Pipeline & TBD
          </h2>
        </div>
        <span className="badge badge-yellow">3 Acciones Obligatorias</span>
      </div>

      {/* Columnas de la Retrospectiva */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 16, marginBottom: 24 }}>
        {/* Columna Verde */}
        <div style={{ background: 'rgba(16, 185, 129, 0.05)', border: '1px solid rgba(16, 185, 129, 0.25)', borderRadius: 12, padding: 18 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 12 }}>
            <span style={{ fontSize: 18 }}>🟢</span>
            <strong style={{ color: '#34d399', fontSize: 15 }}>Lo que Funcionó Bien</strong>
          </div>
          <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: 10, fontSize: 13, color: '#cbd5e1' }}>
            <li style={{ background: 'rgba(0,0,0,0.2)', padding: '10px 12px', borderRadius: 8, borderLeft: '3px solid #10b981' }}>
              • Despliegue automático a <strong>Render</strong> cumpliendo el DoD técnico sin intervención manual.
            </li>
            <li style={{ background: 'rgba(0,0,0,0.2)', padding: '10px 12px', borderRadius: 8, borderLeft: '3px solid #10b981' }}>
              • Aislamiento efectivo de código sin riesgo al ciudadano mediante <code>pagos-express-v1</code> en <strong>ConfigCat</strong>.
            </li>
            <li style={{ background: 'rgba(0,0,0,0.2)', padding: '10px 12px', borderRadius: 8, borderLeft: '3px solid #10b981' }}>
              • Pruebas automáticas y linter ejecutándose en GitHub Actions en menos de 15 segundos.
            </li>
          </ul>
        </div>

        {/* Columna Amarilla */}
        <div style={{ background: 'rgba(245, 158, 11, 0.05)', border: '1px solid rgba(245, 158, 11, 0.25)', borderRadius: 12, padding: 18 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 12 }}>
            <span style={{ fontSize: 18 }}>🟡</span>
            <strong style={{ color: '#fbbf24', fontSize: 15 }}>Lo que Generó Fricción</strong>
          </div>
          <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: 10, fontSize: 13, color: '#cbd5e1' }}>
            <li style={{ background: 'rgba(0,0,0,0.2)', padding: '10px 12px', borderRadius: 8, borderLeft: '3px solid #f59e0b' }}>
              • Tests flaky en CI que demoraron las integraciones y generaron desconfianza en el equipo.
            </li>
            <li style={{ background: 'rgba(0,0,0,0.2)', padding: '10px 12px', borderRadius: 8, borderLeft: '3px solid #f59e0b' }}>
              • Presión comercial del PO por activar en viernes sin observabilidad de transacciones bancarias.
            </li>
            <li style={{ background: 'rgba(0,0,0,0.2)', padding: '10px 12px', borderRadius: 8, borderLeft: '3px solid #f59e0b' }}>
              • Solo se lograron 4 integraciones en el sprint (lejos de la meta de integración diaria en TBD).
            </li>
          </ul>
        </div>

        {/* Columna Roja */}
        <div style={{ background: 'rgba(239, 68, 68, 0.05)', border: '1px solid rgba(239, 68, 68, 0.25)', borderRadius: 12, padding: 18 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 12 }}>
            <span style={{ fontSize: 18 }}>🔴</span>
            <strong style={{ color: '#f87171', fontSize: 15 }}>Lo que Rompió el Flujo / Miedo</strong>
          </div>
          <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: 10, fontSize: 13, color: '#cbd5e1' }}>
            <li style={{ background: 'rgba(0,0,0,0.2)', padding: '10px 12px', borderRadius: 8, borderLeft: '3px solid #ef4444' }}>
              • <strong>Caída de 11 minutos</strong> en Render por fallo de health check no resiliente.
            </li>
            <li style={{ background: 'rgba(0,0,0,0.2)', padding: '10px 12px', borderRadius: 8, borderLeft: '3px solid #ef4444' }}>
              • Rollback manual no automatizado ante la indisponibilidad del servicio.
            </li>
            <li style={{ background: 'rgba(0,0,0,0.2)', padding: '10px 12px', borderRadius: 8, borderLeft: '3px solid #ef4444' }}>
              • Acumulación de 3 toggles obsoletos (+45 días) sin retirar del código base.
            </li>
          </ul>
        </div>
      </div>

      {/* Tres Acciones Obligatorias */}
      <h3 style={{ fontSize: 16, color: '#f8fafc', marginBottom: 12 }}>
        🚀 Las Tres Acciones de Mejora Obligatorias (Asignadas)
      </h3>
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 14 }}>
        <div style={{ background: 'rgba(0, 102, 204, 0.08)', border: '1px solid rgba(0, 102, 204, 0.25)', borderRadius: 10, padding: 14 }}>
          <span className="badge badge-blue">Acción 1: Estabilidad de Pipeline</span>
          <h4 style={{ fontSize: 14, margin: '8px 0 4px', color: '#fff' }}>Cuarentena & Auto-Rollback</h4>
          <p style={{ fontSize: 13, color: '#94a3b8' }}>
            Cuarentenar de inmediato el test flaky del CI y configurar auto-rollback en Render ante fallos de health check.
          </p>
          <div style={{ marginTop: 8, fontSize: 12, color: '#60a5fa', fontWeight: 600 }}>Responsable: Developers</div>
        </div>

        <div style={{ background: 'rgba(121, 40, 202, 0.08)', border: '1px solid rgba(121, 40, 202, 0.25)', borderRadius: 10, padding: 14 }}>
          <span className="badge badge-purple" style={{ background: 'rgba(121, 40, 202, 0.2)', color: '#c084fc' }}>Acción 2: Higiene de Toggles</span>
          <h4 style={{ fontSize: 14, margin: '8px 0 4px', color: '#fff' }}>Regla de Caducidad a 30 Días</h4>
          <p style={{ fontSize: 13, color: '#94a3b8' }}>
            Incorporar al Definition of Done (DoD) que todo toggle con más de 30 días en producción se priorice obligatoriamente como tarea de limpieza en el backlog.
          </p>
          <div style={{ marginTop: 8, fontSize: 12, color: '#c084fc', fontWeight: 600 }}>Responsable: Equipo / PO</div>
        </div>

        <div style={{ background: 'rgba(0, 212, 178, 0.08)', border: '1px solid rgba(0, 212, 178, 0.25)', borderRadius: 10, padding: 14 }}>
          <span className="badge badge-cyan">Acción 3: DoR de Liberación</span>
          <h4 style={{ fontSize: 14, margin: '8px 0 4px', color: '#fff' }}>Observabilidad Obligatoria</h4>
          <p style={{ fontSize: 13, color: '#94a3b8' }}>
            Definir como criterio en el Definition of Ready (DoR) que ninguna funcionalidad se active a usuarios externos sin dashboards activos de errores HTTP 5xx y latencia.
          </p>
          <div style={{ marginTop: 8, fontSize: 12, color: 'var(--accent-cyan)', fontWeight: 600 }}>Responsable: PO + Devs</div>
        </div>
      </div>
    </div>
  );
};
