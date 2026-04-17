const { contextBridge, ipcRenderer } = require('electron');

contextBridge.exposeInMainWorld('electronAPI', {
  setAlwaysOnTop: (value) => ipcRenderer.send('set-always-on-top', value),
  dockToTray: (timeStr) => ipcRenderer.send('dock-to-tray', timeStr),
  updateTrayTime: (timeStr) => ipcRenderer.send('tray-update-time', timeStr),
});
