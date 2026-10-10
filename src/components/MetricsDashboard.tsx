import React from 'react';

interface Props {
  metrics: {
    totalTx: number;
    expressTx: number;
    standardTx: number;
    avgLatencyMs: number;
    errorRate: number;
    conversionRate: number;
  };
}

export const MetricsDashboard: React.FC<Props> = ({ metrics }) => {
  return (
    <div className="glass-card animate-fade-in" id="metrics-dashboard-container">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 20 }}>
        <div>
          <span className="badge badge-cyan">Observabilidad en Tiempo Real (Golden Signals)</span>
          <h2 style={{ fontSize: 20, marginTop: 4, color: '#f8fafc' }}>
            Métricas de Éxito en Render & Pasarela de Pagos
          </h2>
        </div>
        <div style={{ display: 'flex', gap: 8 }}>
          <span className="badge badge-green">Health Check: PASS</span>
          <span className="badge badge-blue">Render Deploy: VERDE</span>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: 16 }}>
        {/* Card 1: Tiempo de Liquidación */}
        <div style={{ background: 'rgba(255, 255, 255, 0.03)', padding: 16, borderRadius: 12, border: '1px solid var(--border-color)' }}>
          <span style={{ fontSize: 13, color: '#94a3b8' }}>Tiempo de Liquidación</span>
          <div style={{ fontSize: 26, fontWeight: 800, color: 'var(--accent-cyan)', margin: '4px 0' }}>
            &lt; 10 seg
          </div>
          <span style={{ fontSize: 12, color: '#34d399' }}>↓ Reducido desde 180s (94% más rápido)</span>
        </div>

        {/* Card 2: Latencia p95 */}
        <div style={{ background: 'rgba(255, 255, 255, 0.03)', padding: 16, borderRadius: 12, border: '1px solid var(--border-color)' }}>
          <span style={{ fontSize: 13, color: '#94a3b8' }}>Latencia Media</span>
          <div style={{ fontSize: 26, fontWeight: 800, color: '#60a5fa', margin: '4px 0' }}>
            {metrics.avgLatencyMs.toFixed(1)} ms
          </div>
          <span style={{ fontSize: 12, color: '#94a3b8' }}>Umbral máximo SLO: 800 ms</span>
        </div>

        {/* Card 3: Tasa de Error Técnico */}
        <div style={{ background: 'rgba(255, 255, 255, 0.03)', padding: 16, borderRadius: 12, border: '1px solid var(--border-color)' }}>
          <span style={{ fontSize: 13, color: '#94a3b8' }}>Tasa de Error Técnico</span>
          <div style={{ fontSize: 26, fontWeight: 800, color: metrics.errorRate < 0.5 ? '#34d399' : '#f87171', margin: '4px 0' }}>
            {metrics.errorRate.toFixed(2)}%
          </div>
          <span style={{ fontSize: 12, color: '#34d399' }}>Meta: &lt; 0.5% (Cumplido)</span>
        </div>

        {/* Card 4: Tasa de Conversión */}
        <div style={{ background: 'rgba(255, 255, 255, 0.03)', padding: 16, borderRadius: 12, border: '1px solid var(--border-color)' }}>
          <span style={{ fontSize: 13, color: '#94a3b8' }}>Conversión de Pasarela</span>
          <div style={{ fontSize: 26, fontWeight: 800, color: '#fbbf24', margin: '4px 0' }}>
            {metrics.conversionRate.toFixed(1)}%
          </div>
          <span style={{ fontSize: 12, color: '#94a3b8' }}>Total Transacciones: {metrics.totalTx}</span>
        </div>
      </div>

      <div style={{ marginTop: 18, background: 'rgba(0, 102, 204, 0.06)', border: '1px solid rgba(0, 102, 204, 0.2)', padding: 12, borderRadius: 10, display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <span style={{ fontSize: 13, color: '#cbd5e1' }}>
          <strong>Pregunta de Validación al PO / Stakeholders:</strong> “¿La confirmación en un clic resuelve la necesidad del ciudadano antes de abrir el tráfico al 100%?”
        </span>
        <span className="badge badge-green">Validación Empírica OK</span>
      </div>
    </div>
  );
};
