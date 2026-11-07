---
name: mcr-crossplatform-mobile-desktop
description: Build native and cross-platform applications for Android, iOS, Windows, macOS, and Linux using React Native, Expo, Flutter, Tauri, and Electron.
---

# MCR Cross-Platform Mobile & Desktop Engineering Skill

Use this skill when developing mobile apps for Android and iOS or native desktop applications for Windows, macOS, and Linux.

## Cross-Platform Engineering Stacks

### 1. Mobile Development (Android & iOS)
- **Primary Framework**: React Native with Expo (SDK 51+) or Flutter 3+.
- **Navigation**: Expo Router (file-based) or React Navigation with native platform transitions (iOS slide from right, Android fade/slide up).
- **Native Device APIs**:
  - Secure Store: Encrypted hardware keystore (`expo-secure-store` / Keychain / KeyStore) for JWT tokens.
  - Push Notifications: APNs (Apple) & FCM (Google) configuration.
  - Camera & Media: Permissions handled gracefully with fallbacks.
  - Offline Sync: SQLite / WatermelonDB with local-first optimistic updates.

### 2. Desktop Development (Windows & macOS)
- **Lightweight High-Performance**: Tauri 2.0 (Rust core + Web frontend).
  - Tiny binary size (<15MB), low RAM usage (<50MB), native OS windowing.
- **Rich Ecosystem Alternative**: Electron with Electron Forge / Vite.
- **macOS Polish**: Translucent vibrant sidebars, native menu bars, Touch Bar integration, universal binary builds (`arm64` Apple Silicon + `x64` Intel).
- **Windows Polish**: Fluent Design Mica/Acrylic effects, system tray minimizing, MSIX installer packaging.

### 3. Build & Packaging Automation
- Fastlane scripts for automated iOS TestFlight and Google Play Internal testing.
- GitHub Actions matrix building Windows `.exe` / `.msi`, macOS `.dmg`, and Linux `.AppImage`.
