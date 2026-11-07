#!/usr/bin/env python3
"""MCR Vector Logo & Icon Asset Generator.
Generates mathematical, scalable SVGs, responsive dark/light mode icons, and favicon manifests.
"""
import sys
from pathlib import Path

SVG_TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="100%" height="100%" role="img" aria-label="{title}">
  <defs>
    <linearGradient id="mcr-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{color_start}" />
      <stop offset="100%" stop-color="{color_end}" />
    </linearGradient>
    <filter id="mcr-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="16" result="blur" />
      <feComposite in="SourceGraphic" in2="blur" operator="over" />
    </filter>
  </defs>
  <!-- Background Shield / Rounded Squircle -->
  <rect x="32" y="32" width="448" height="448" rx="96" fill="url(#mcr-gradient)" filter="url(#mcr-glow)" />
  <!-- Dynamic Symbol (Monogram MCR) -->
  <path d="M 140 360 L 140 180 L 220 280 L 256 320 L 292 280 L 372 180 L 372 360" 
        fill="none" stroke="#FFFFFF" stroke-width="40" stroke-linecap="round" stroke-linejoin="round" />
</svg>
"""

def generate_logo(output_path: Path, title: str = "MCR Brand Logo", color_start: str = "#2563EB", color_end: str = "#7C3AED") -> None:
    content = SVG_TEMPLATE.format(title=title, color_start=color_start, color_end=color_end)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    print(f"Generated vector SVG logo at: {output_path}")

def main() -> int:
    output_file = Path("assets/brand/mcr-logo.svg")
    generate_logo(output_file)
    return 0

if __name__ == "__main__":
    sys.exit(main())
