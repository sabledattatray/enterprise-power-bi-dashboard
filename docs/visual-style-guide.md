# Visual Style Guide & Design System

This guide documents the UI/UX design system, color palette tokens, typography rules, and canvas standards implemented across the **Enterprise Power BI Analytics Portfolio**.

---

## 1. Microsoft Fabric Light Design Language

The design aesthetic is inspired by Microsoft Fabric and modern Fluent Design principles:
- High contrast, clean card containers
- Soft background canvases (`#F5F8FC`) to eliminate eye fatigue
- Subtle border lines (`#E2E8F0`) and 8px border radius
- Purposeful data color accents with consistent semantic meanings

---

## 2. Color Palette & Semantic Tokens

| Token Role | Name | Hex Code | RGB | Suggested Visual Usage |
|---|---|---|---|---|
| **Primary Accent** | Royal Fabric Blue | `#2563EB` | `37, 99, 235` | Primary revenue bars, active KPI cards, navigation focus |
| **Dark Header** | Deep Enterprise Navy | `#172554` | `23, 37, 84` | Left navigation bar, top header bar, high-contrast labels |
| **Secondary Accent**| Modern Teal | `#0D9488` | `13, 148, 136` | Average order value, secondary series lines, delivered status |
| **Success / Positive**| Emerald Green | `#16A34A` | `22, 163, 74` | Positive profit margin, revenue YoY growth, on-time delivery |
| **Warning / Alert**| Amber Orange | `#F59E0B` | `245, 158, 11` | Return rate alerts, processing orders, moderate variances |
| **Category Purple** | Violet Purple | `#7C3AED` | `124, 58, 237` | Customer segment metrics, apparel category accent |
| **Danger / Loss** | Crimson Red | `#DC2626` | `220, 38, 38` | Refund amounts, late shipments, negative variances |
| **Canvas Background**| Soft Ice Blue | `#F5F8FC` | `245, 248, 252` | Master report page background |
| **Card Container** | Pure White | `#FFFFFF` | `255, 255, 255` | KPI cards, chart visual cards |
| **Primary Text** | Deep Slate | `#1E293B` | `30, 41, 59` | Titles, KPI callout numbers, table headers |
| **Muted Text** | Slate Grey | `#64748B` | `100, 116, 139` | Subtitles, axis tick marks, field descriptors |

---

## 3. Typography Standards (Segoe UI)

| Hierarchy Level | Font Family | Size | Weight | Color |
|---|---|---|---|---|
| **Page Title** | Segoe UI | 20 pt | Bold | `#1E293B` |
| **Section Header** | Segoe UI | 14 pt | Semibold | `#1E293B` |
| **KPI Callout Value** | Segoe UI | 28 pt | Bold | `#1E293B` / `#2563EB` |
| **KPI Subtitle Label** | Segoe UI | 10 pt | Regular | `#64748B` |
| **Chart Title** | Segoe UI | 12 pt | Semibold | `#1E293B` |
| **Axis & Legend** | Segoe UI | 9 pt | Regular | `#64748B` |
| **Table Content** | Segoe UI | 10 pt | Regular | `#1E293B` |

---

## 4. Layout & Grid Standards

- **Canvas Size:** 16:9 Aspect Ratio (1280 x 720 px or 1920 x 1080 px).
- **Navigation Sidebar:** Fixed left width of 180–220 px containing Datta Sable branding and 9 page links.
- **Top Header Bar:** 60 px height displaying the page title, active filters summary, and date range.
- **Card Margins & Padding:** 12 px padding inside cards, 16 px spacing between visual tiles.
- **Card Corner Radius:** 8 px rounded corners for a modern, polished look.
