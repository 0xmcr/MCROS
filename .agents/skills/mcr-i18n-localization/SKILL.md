---
name: mcr-i18n-localization
description: Implement multi-language internationalization (i18n), localized translation catalogs (English, Bengali, RTL), and regional formatting for web and mobile apps.
---

# MCR Internationalization (i18n) & Localization Skill

Use this skill when developing multi-language web or mobile applications, setting up localized translation files (JSON/YAML), handling Right-to-Left (RTL) layouts, or formatting regional currencies and dates.

## Multi-Language Engineering Architecture

### 1. Translation Catalog Architecture
Organize localized dictionaries under `locales/` or `messages/`:
```
messages/
├── en.json            # English (Default / Fallback)
├── bn.json            # Bengali (বাংলা)
├── es.json            # Spanish (Español)
└── ar.json            # Arabic (العربية - RTL)
```

Example `bn.json`:
```json
{
  "common": {
    "welcome": "স্বাগতম, {name}!",
    "save": "সংরক্ষণ করুন",
    "cancel": "বাতিল",
    "loading": "লোড হচ্ছে..."
  },
  "dashboard": {
    "totalRevenue": "সর্বমোট আয়",
    "activeUsers": "সক্রিয় ব্যবহারকারী",
    "itemsCount": "{count, plural, =0 {কোন আইটেম নেই} =1 {১টি আইটেম} other {#টি আইটেম}}"
  }
}
```

### 2. Framework Integration
- **Next.js (App Router)**: `next-intl` with localized route prefixes (`/[locale]/dashboard`) or middleware cookie detection.
- **React SPA**: `react-i18next` with `i18next-browser-languagedetector`.
- **Mobile (React Native / Expo)**: `expo-localization` + `i18n-js`.
- **Backend (Python / Node)**: Localized error envelopes based on `Accept-Language` HTTP request header.

### 3. Regional Formatting (Numbers, Currency, Dates)
- Never hardcode currency symbols or date formats.
- Use native `Intl` APIs:
  ```typescript
  // Localized Currency
  new Intl.NumberFormat('bn-BD', { style: 'currency', currency: 'BDT' }).format(1500); // ৳ ১,৫০০.০০
  new Intl.NumberFormat('en-US', { style: 'currency', currency: 'USD' }).format(1500); // $1,500.00

  // Localized Date & Time
  new Intl.DateTimeFormat('bn-BD', { dateStyle: 'full' }).format(new Date());
  ```

### 4. Right-to-Left (RTL) Layout Adaptability
- Support Arabic, Hebrew, Persian via CSS logical properties (`margin-inline-start` instead of `margin-left`).
- Set `<html dir="rtl">` dynamically when the active locale is RTL.
