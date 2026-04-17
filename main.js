const { app, BrowserWindow, ipcMain, Tray, nativeImage } = require('electron');
const path = require('path');

let mainWindow;
let tray = null;
let lastTime = '';

function createWindow() {
  mainWindow = new BrowserWindow({
    width: 260,
    height: 260,
    minWidth: 90,
    minHeight: 90,
    maxWidth: 250,
    maxHeight: 250,
    resizable: true,
    alwaysOnTop: true,
    frame: true,
    titleBarStyle: 'customButtonsOnHover',
    webPreferences: {
      preload: path.join(__dirname, 'preload.js'),
      contextIsolation: true,
      nodeIntegration: false,
    },
  });

  mainWindow.setAspectRatio(1);
  mainWindow.loadFile('index.html');
}

function createTray() {
  if (tray) return;
  const icon = nativeImage.createFromPath(path.join(__dirname, 'tray-icon.png'));
  tray = new Tray(icon);
  tray.setToolTip('Countdown Timer — click to restore window');
  tray.setTitle(lastTime ? ` ${lastTime}` : ' ⏱');

  tray.on('click', () => {
    undock();
  });
}

function destroyTray() {
  if (tray) {
    tray.destroy();
    tray = null;
  }
}

function dock() {
  createTray();
  if (mainWindow) mainWindow.hide();
}

function undock() {
  destroyTray();
  if (mainWindow) {
    mainWindow.show();
    mainWindow.focus();
  }
}

app.whenReady().then(createWindow);

app.on('window-all-closed', () => {
  app.quit();
});

ipcMain.on('set-always-on-top', (_event, value) => {
  if (mainWindow) mainWindow.setAlwaysOnTop(value);
});

ipcMain.on('dock-to-tray', (_event, timeStr) => {
  lastTime = timeStr || '';
  dock();
});

ipcMain.on('tray-update-time', (_event, timeStr) => {
  lastTime = timeStr || '';
  if (tray) tray.setTitle(timeStr ? ` ${timeStr}` : ' ⏱');
});
