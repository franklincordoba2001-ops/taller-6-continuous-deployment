import React, { useState, useEffect } from 'react';
import { featureFlagService, ToggleState } from '../services/configcat';

export const ConfigCatControls: React.FC = () => {
  const [state, setState] = useState<ToggleState>(featureFlagService.getState());
  const [customKey, setCustomKey] = useState('');

  useEffect(() => {
    const unsub = featureFlagService.subscribe(setState);
    return unsub;
  }, []);

  const handleToggle = (enabled: boolean) => {
    featureFlagService.setToggle(enabled);
  };

  const handleKillSwitch = () => {
    featureFlagService.setToggle(false);
    featureFlagService.setCanaryPercentage(0);
  };

  const handleInitSdk = () => {
    if (customKey.trim()) {
      featureFlagService.initSdk(customKey.trim());
    }
  };

  return (
    <div className="glass-card" id="configcat-panel" style={{ borderTop: '3px solid #7928ca' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 16 }}>
        <div>
          <span className="badge badge-purple" style={{ background: 'rgba(121, 40, 202, 0.15)', color: '#c084fc', border: '1px solid rgba(121, 40, 202, 0.3)' }}>
            Consola de Control: ConfigCat Feature Flags
          </span>
          <h3 style={{ fontSize: 18, marginTop: 4, color: '#f8fafc' }}>
            Desacoplamiento entre Deploy y Release
          </h3>
        </div>
        <div style={{ display: 'flex', alignItems: 'center', gap: 10 }}>
          <span style={{ fontSize: 13, color: '#94a3b8' }}>Último pulso:</span>
          <span style={{ fontFamily: 'monospace', fontSize: 13, color: 'var(--accent-cyan)' }}>{state.lastUpdated}</span>
        </div>
      </div>

      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: 16, marginBottom: 18 }}>
        {/* Toggle Switch Principal */}
        <div style={{ background: 'rgba(255, 255, 255, 0.03)', padding: 16, borderRadius: 12, border: '1px solid var(--border-color)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
            <div>
              <div style={{ fontWeight: 600, fontSize: 14 }}>Flag: <code>pagos-express-v1</code></div>
              <span style={{ fontSize: 12, color: '#64748b' }}>Release Toggle (Catastro)</span>
            </div>
            <span className={state.pagosExpressV1 ? 'badge badge-green' : 'badge badge-red'}>
              {state.pagosExpressV1 ? 'ON (100%)' : 'OFF (Inactivo)'}
            </span>
          </div>

          <div style={{ display: 'flex', gap: 10 }}>
            <button
              id="btn-toggle-on"
              onClick={() => handleToggle(true)}
              style={{
                flex: 1,
                padding: '8px 12px',
                borderRadius: 8,
                fontSize: 13,
                fontWeight: 700,
                background: state.pagosExpressV1 ? 'var(--accent-green)' : 'rgba(255,255,255,0.06)',
                color: state.pagosExpressV1 ? '#000' : '#94a3b8'
              }}
            >
              🟢 Conmutar a ON
            </button>
            <button
              id="btn-toggle-off"
              onClick={() => handleToggle(false)}
              style={{
                flex: 1,
                padding: '8px 12px',
                borderRadius: 8,
                fontSize: 13,
                fontWeight: 700,
                background: !state.pagosExpressV1 ? '#ef4444' : 'rgba(255,255,255,0.06)',
                color: !state.pagosExpressV1 ? '#fff' : '#94a3b8'
              }}
            >
              🔴 Conmutar a OFF
            </button>
          </div>
        </div>

        {/* Canary Rollout Porcentual */}
        <div style={{ background: 'rgba(255, 255, 255, 0.03)', padding: 16, borderRadius: 12, border: '1px solid var(--border-color)' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: 10 }}>
            <span style={{ fontWeight: 600, fontSize: 14 }}>Canary Rollout Progresivo</span>
            <span className="badge badge-yellow">{state.canaryPercentage}% Usuarios</span>
          </div>
          <div style={{ display: 'flex', gap: 6 }}>
            {[0, 5, 20, 50, 100].map((pct) => (
              <button
                key={pct}
                onClick={() => {
                  featureFlagService.setCanaryPercentage(pct);
                  if (pct > 0) featureFlagService.setToggle(true);
                  else featureFlagService.setToggle(false);
                }}
                style={{
                  flex: 1,
                  padding: '6px 4px',
                  borderRadius: 6,
                  fontSize: 12,
                  fontWeight: 600,
                  background: state.canaryPercentage === pct ? 'var(--accent-yellow)' : 'rgba(255,255,255,0.06)',
                  color: state.canaryPercentage === pct ? '#000' : '#94a3b8'
                }}
              >
                {pct}%
              </button>
            ))}
          </div>
        </div>
      </div>

      {/* Protocolo de Kill-Switch Inmediato */}
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', background: 'rgba(239, 68, 68, 0.08)', border: '1px solid rgba(239, 68, 68, 0.25)', borderRadius: 10, padding: '12px 16px' }}>
        <div>
          <strong style={{ color: '#f87171', fontSize: 14 }}>🚨 Protocolo de Rollback Inmediato (Kill-Switch)</strong>
          <p style={{ fontSize: 12, color: '#94a3b8' }}>
            Si los errores superan el 1% o la latencia excede 800 ms, neutraliza el impacto en &lt; 60 segundos sin nuevo deploy.
          </p>
        </div>
        <button id="btn-kill-switch" className="btn-danger" onClick={handleKillSwitch}>
          ⚡ APAGAR FLAG AHORA
        </button>
      </div>

      {/* SDK Key opcional para conectar con nube real de ConfigCat */}
      <div style={{ marginTop: 14, paddingTop: 10, borderTop: '1px solid var(--border-color)', display: 'flex', gap: 10, alignItems: 'center' }}>
        <input
          type="text"
          placeholder="Pegar ConfigCat SDK Key real (opcional)..."
          value={customKey}
          onChange={(e) => setCustomKey(e.target.value)}
          style={{ flex: 1, background: '#0a0f1d', border: '1px solid var(--border-color)', color: '#fff', padding: '6px 12px', borderRadius: 8, fontSize: 12 }}
        />
        <button className="btn-outline" onClick={handleInitSdk} style={{ fontSize: 12, padding: '6px 14px' }}>
          Conectar SDK
        </button>
      </div>
    </div>
  );
};
