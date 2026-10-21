#!/usr/bin/env python3
"""
Enterprise Power BI Analytics Portfolio — Release Packaging Script
Generates versioned release zip archives under releases/ for GitHub Release v1.0.0
"""

import os
import sys
import zipfile
import shutil

def create_releases():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, '..'))
    releases_dir = os.path.join(repo_root, 'releases', 'v1.0.0')
    os.makedirs(releases_dir, exist_ok=True)

    print("================================================================================")
    print("ENTERPRISE POWER BI ANALYTICS PORTFOLIO — RELEASE PACKAGING (v1.0.0)")
    print(f"Target Directory: {releases_dir}")
    print("================================================================================")

    # 1. Dataset Release Pack
    dataset_zip = os.path.join(releases_dir, 'enterprise-powerbi-datasets-v1.0.0.zip')
    with zipfile.ZipFile(dataset_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        data_raw = os.path.join(repo_root, 'data', 'raw')
        for f in os.listdir(data_raw):
            if f.endswith('.csv'):
                z.write(os.path.join(data_raw, f), arcname=os.path.join('data', f))
        z.write(os.path.join(repo_root, 'data', 'data-dictionary.md'), arcname='data-dictionary.md')
    print(f"[PACKAGED] Datasets: {dataset_zip} ({os.path.getsize(dataset_zip):,} bytes)")

    # 2. SVG Icons Release Pack
    icons_zip = os.path.join(releases_dir, 'enterprise-powerbi-svg-icons-v1.0.0.zip')
    with zipfile.ZipFile(icons_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        icons_dir = os.path.join(repo_root, 'assets', 'icons')
        for root, dirs, files in os.walk(icons_dir):
            for f in files:
                if f.endswith(('.svg', '.md')):
                    fpath = os.path.join(root, f)
                    rel = os.path.relpath(fpath, repo_root)
                    z.write(fpath, arcname=rel)
    print(f"[PACKAGED] SVG Icons: {icons_zip} ({os.path.getsize(icons_zip):,} bytes)")

    # 3. Dashboard Designs Release Pack
    dashboards_zip = os.path.join(releases_dir, 'enterprise-powerbi-dashboard-designs-v1.0.0.zip')
    with zipfile.ZipFile(dashboards_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        dash_dir = os.path.join(repo_root, 'assets', 'dashboards')
        for f in os.listdir(dash_dir):
            if f.endswith(('.png', '.webp')):
                z.write(os.path.join(dash_dir, f), arcname=os.path.join('dashboards', f))
    print(f"[PACKAGED] Dashboard Designs: {dashboards_zip} ({os.path.getsize(dashboards_zip):,} bytes)")

    # 4. DAX & Handbook Release Pack
    handbook_zip = os.path.join(releases_dir, 'enterprise-powerbi-handbook-dax-v1.0.0.zip')
    with zipfile.ZipFile(handbook_zip, 'w', zipfile.ZIP_DEFLATED) as z:
        z.write(os.path.join(repo_root, 'excel', 'powerbi-implementation-handbook.xlsx'), arcname='powerbi-implementation-handbook.xlsx')
        dax_dir = os.path.join(repo_root, 'dax')
        for root, dirs, files in os.walk(dax_dir):
            for f in files:
                if f.endswith(('.dax', '.md')):
                    fpath = os.path.join(root, f)
                    rel = os.path.relpath(fpath, dax_dir)
                    z.write(fpath, arcname=os.path.join('dax', rel))
    print(f"[PACKAGED] DAX & Handbook: {handbook_zip} ({os.path.getsize(handbook_zip):,} bytes)")

    print("\n================================================================================")
    print("ALL V1.0.0 RELEASE PACKAGES CREATED SUCCESSFULLY")
    print("================================================================================")
    return 0

if __name__ == '__main__':
    sys.exit(create_releases())
