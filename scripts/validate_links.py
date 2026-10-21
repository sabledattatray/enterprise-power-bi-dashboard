#!/usr/bin/env python3
"""
Enterprise Power BI Analytics Portfolio — Automated Markdown Link Validator
Scans all markdown files in the repository and verifies that local file/image links resolve.
"""

import os
import sys
import re

def validate_links():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    repo_root = os.path.abspath(os.path.join(script_dir, '..'))

    print("================================================================================")
    print("ENTERPRISE POWER BI ANALYTICS PORTFOLIO — MARKDOWN LINK AUDIT")
    print(f"Scanning Root: {repo_root}")
    print("================================================================================")

    broken_links = []
    checked_count = 0

    for root, dirs, files in os.walk(repo_root):
        if '.git' in root or 'releases' in root or '__pycache__' in root:
            continue
        for f in files:
            if f.endswith('.md'):
                fpath = os.path.join(root, f)
                rel_fpath = os.path.relpath(fpath, repo_root)
                with open(fpath, 'r', encoding='utf-8') as mf:
                    content = mf.read()

                # Extract markdown links [text](link) and image links ![alt](src)
                links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
                img_links = re.findall(r'!\[([^\]]*)\]\(([^)]+)\)', content)
                all_links = links + img_links

                for text, raw_link in all_links:
                    link = raw_link.strip()
                    # Skip external web URLs, anchors, mailto, etc.
                    if link.startswith(('http://', 'https://', 'mailto:', '#', 'tel:')):
                        continue
                    # Remove anchor fragment if present
                    clean_link = link.split('#')[0]
                    if not clean_link:
                        continue
                    # Remove query params if any
                    clean_link = clean_link.split('?')[0]

                    # Skip binary archive packages (generated dynamically or hosted on GitHub Releases)
                    if clean_link.endswith(('.zip', '.tar.gz', '.tgz')):
                        continue

                    target_path = os.path.normpath(os.path.join(root, clean_link))
                    checked_count += 1

                    if not os.path.exists(target_path):
                        broken_links.append((rel_fpath, link, target_path))
                        print(f"[FAIL] In {rel_fpath}: '{link}' -> File not found ({target_path})")

    print(f"\n[INFO] Checked {checked_count} internal document and asset links.")
    if not broken_links:
        print("[PASS] ALL INTERNAL MARKDOWN LINKS RESOLVED SUCCESSFULLY (0 broken links)")
        print("================================================================================")
        return 0
    else:
        print(f"[FAIL] Found {len(broken_links)} broken links:")
        for src, link, target in broken_links:
            print(f"  - {src}: {link}")
        print("================================================================================")
        return 1

if __name__ == '__main__':
    sys.exit(validate_links())
