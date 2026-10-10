/**
 * Servicio de Feature Flags con ConfigCat SDK y fallback local reactivo.
 * Taller 6: React 18, Vite, TypeScript, Render y ConfigCat.
 */

import * as configcat from 'configcat-js';

export interface ToggleState {
  pagosExpressV1: boolean;
  canaryPercentage: number;
  sdkConnected: boolean;
  lastUpdated: string;
}

type Listener = (state: ToggleState) => void;

class ConfigCatService {
  private client: configcat.IConfigCatClient | null = null;
  private listeners: Set<Listener> = new Set();
  private state: ToggleState = {
    pagosExpressV1: false, // Por defecto en OFF según el caso de estudio
    canaryPercentage: 0,
    sdkConnected: false,
    lastUpdated: new Date().toLocaleTimeString()
  };

  constructor() {
    const sdkKey = (import.meta as any).env?.VITE_CONFIGCAT_SDK_KEY;
    if (sdkKey) {
      this.initSdk(sdkKey);
    }
  }

  public initSdk(sdkKey: string) {
    try {
      this.client = configcat.getClient(sdkKey, configcat.PollingMode.AutoPoll, {
        pollIntervalSeconds: 30
      });
      this.state.sdkConnected = true;
      this.refreshFromSdk();
    } catch (err) {
      console.warn('ConfigCat SDK no pudo inicializarse con la key proporcionada. Modo simulación activo.', err);
      this.state.sdkConnected = false;
      this.notify();
    }
  }

  public async refreshFromSdk() {
    if (!this.client) return;
    try {
      const val = await this.client.getValueAsync('pagos-express-v1', false);
      this.state.pagosExpressV1 = Boolean(val);
      this.state.lastUpdated = new Date().toLocaleTimeString();
      this.notify();
    } catch (err) {
      console.error('Error al consultar ConfigCat:', err);
    }
  }

  public getState(): ToggleState {
    return { ...this.state };
  }

  public setToggle(enabled: boolean) {
    this.state.pagosExpressV1 = enabled;
    this.state.lastUpdated = new Date().toLocaleTimeString();
    this.notify();
  }

  public setCanaryPercentage(pct: number) {
    this.state.canaryPercentage = pct;
    this.state.lastUpdated = new Date().toLocaleTimeString();
    this.notify();
  }

  public subscribe(listener: Listener): () => void {
    this.listeners.add(listener);
    listener(this.getState());
    return () => {
      this.listeners.delete(listener);
    };
  }

  private notify() {
    this.listeners.forEach((l) => l(this.getState()));
  }
}

export const featureFlagService = new ConfigCatService();
