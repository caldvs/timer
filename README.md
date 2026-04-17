# Countdown Timer

A minimal always-on-top countdown timer for macOS. Set a duration, hit start, dock it to your menu bar when you need the screen space.

## Download

Grab the latest `.dmg` from the [Releases](../../releases) page.

## Install

1. Open the DMG and drag **Countdown Timer** into Applications.
2. First launch: macOS will warn that the app is from an unidentified developer — this build is unsigned.
   - **Right-click** the app in Applications → **Open** → click **Open** in the dialog.
   - After that, launching normally works from Spotlight (⌘-Space → "Countdown Timer").

## Features

- Set minutes / seconds, click Start.
- Progress ring counts down visually.
- Hover the ring to reveal Stop.
- Dock button hides the window and shows the live countdown in the menu bar.
- Click the menu bar entry to restore the window.

## Build from source

```bash
npm install
npm start          # dev mode
npm run dist       # build DMG + zip into dist/
```
