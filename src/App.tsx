import React, { useState, useEffect } from 'react';
import { featureFlagService, ToggleState } from './services/configcat';
import { StandardCheckout } from './components/StandardCheckout';
import { ExpressCheckout } from './components/ExpressCheckout';
import { ConfigCatControls } from './components/ConfigCatControls';
import { MetricsDashboard } from './components/MetricsDashboard';
import { RetrospectiveMiroBoard } from './components/RetrospectiveMiroBoard';
import { CanaryPolicyCard } from './components/CanaryPolicyCard';
import { SprintReviewBanner } from './components/SprintReviewBanner';

export const App: React.FC = () => {
  const [toggleState, setToggleState] = useState<ToggleState>(featureFlagService.getState());
  const [activeTab, setActiveTab] = useState<'demo' | 'metrics' | 'retro' | 'policy'>('demo');
  const [metrics, setMetrics] = useState({
    totalTx: 142,
    expressTx: 89,
    standardTx: 53,
    avgLatencyMs: 44.8,
    errorRate: 0.12,
    conversionRate: 96.4
  });

  useEffect(() => {
    const unsub = featureFlagService.subscribe(setToggleState);
    return unsub;
  }, []);

  const handleCheckoutSuccess = (latency: number) => {
    setMetrics((prev) => {
      const isExpress = toggleState.pagosExpressV1;
      const newTotal = prev.totalTx + 1;
      const newExpress = isExpress ? prev.expressTx + 1 : prev.expressTx;
      const newStandard = !isExpress ? prev.standardTx + 1 : prev.standardTx;
      const newAvgLatency = (prev.avgLatencyMs * prev.totalTx + latency) / newTotal;

      return {
        totalTx: newTotal,
        expressTx: newExpress,
        standardTx: newStandard,
        avgLatencyMs: newAvgLatency,
        errorRate: Math.max(0, prev.errorRate - 0.01),
        conversionRate: Math.min(99.5, prev.conversionRate + 0.1)
      };
    });
  };

  return (
    <div className="container">
      {/* Top Header */}
      <header style={{ padding: '24px 0 16px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-color)', marginBottom: 24, flexWrap: 'wrap', gap: 14 }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
            <span style={{ fontSize: 24 }}>🏛️</span>
            <div>
              <h1 style={{ fontSize: 20, fontWeight: 800, color: '#f8fafc', letterSpacing: -0.5 }}>
                Liquidación Catastral Mocoa
              </h1>
              <p style={{ fontSize: 13, color: '#94a3b8' }}>
                UNIPUTUMAYO | Franklin Sneider Córdoba De La Cruz | Docente: Juan Pablo
              </p>
            </div>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <span className="badge badge-green">🚀 Render: ONLINE</span>
          <span className="badge badge-purple" style={{ background: 'rgba(121, 40, 202, 0.2)', color: '#c084fc', border: '1px solid rgba(121, 40, 202, 0.4)' }}>
            🐱 ConfigCat: {toggleState.sdkConnected ? 'Cloud SDK' : 'Live State'}
          </span>
          <span className="badge badge-blue">TBD: main</span>
        </div>
      </header>

      {/* Tabs */}
      <nav style={{ display: 'flex', gap: 8, marginBottom: 24, overflowX: 'auto', paddingBottom: 4 }}>
        {[
          { id: 'demo', label: '💳 Demo en Vivo (Estado OFF vs ON)' },
          { id: 'metrics', label: '📊 Golden Signals & Métricas' },
          { id: 'retro', label: '📋 Sprint Retrospective (Miro)' },
          { id: 'policy', label: '🛡️ Política de Liberación Segura' }
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setActiveTab(tab.id as any)}
            style={{
              padding: '10px 18px',
              borderRadius: 10,
              fontSize: 13,
              fontWeight: 600,
              background: activeTab === tab.id ? 'rgba(0, 212, 178, 0.15)' : 'rgba(255, 255, 255, 0.04)',
              border: activeTab === tab.id ? '1px solid var(--accent-cyan)' : '1px solid var(--border-color)',
              color: activeTab === tab.id ? 'var(--accent-cyan)' : '#94a3b8',
              whiteSpace: 'nowrap'
            }}
          >
            {tab.label}
          </button>
        ))}
      </nav>

      {/* Main Content Areas */}
      {activeTab === 'demo' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
          {/* Banner de Sprint Review en CD */}
          <SprintReviewBanner />

          {/* Panel de ConfigCat */}
          <ConfigCatControls />

          {/* Checkout Dinámico Conmutado por Feature Flag sin redespliegue */}
          {toggleState.pagosExpressV1 ? (
            <ExpressCheckout onSuccess={handleCheckoutSuccess} />
          ) : (
            <StandardCheckout onSuccess={handleCheckoutSuccess} />
          )}

          {/* Mini preview de métricas */}
          <MetricsDashboard metrics={metrics} />
        </div>
      )}

      {activeTab === 'metrics' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
          <MetricsDashboard metrics={metrics} />
          <ConfigCatControls />
        </div>
      )}

      {activeTab === 'retro' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
          <RetrospectiveMiroBoard />
        </div>
      )}

      {activeTab === 'policy' && (
        <div style={{ display: 'flex', flexDirection: 'column', gap: 24 }}>
          <CanaryPolicyCard />
        </div>
      )}

      {/* Footer */}
      <footer style={{ marginTop: 40, paddingTop: 20, borderTop: '1px solid var(--border-color)', textAlign: 'center', fontSize: 13, color: '#64748b' }}>
        Taller 6: Continuous Deployment & Trunk-Based Development | Stack: React 18 + Vite + TypeScript + ConfigCat SDK + Render
      </footer>
    </div>
  );
};
export default App;
