#!/usr/bin/env python3
"""
osint_search_builder.py
Builds a batch of public search-engine query URLs for a subject, plus a
review checklist. Does not perform any requests itself.

Tool: https://biancabcarlson.github.io/OSINT-Search-Builder/

Usage:
    python osint_search_builder.py --name "Jane Doe" --email "jane.doe@example.com" -o queries.md
"""

import argparse
from urllib.parse import quote_plus


def build_queries(name=None, email=None, phone=None):
    queries = []

    def add(label, url):
        queries.append((label, url))

    if name:
        q = quote_plus(f'"{name}"')
        add("Google — exact name", f"https://www.google.com/search?q={q}")
        add("Google — name + site:linkedin.com", f"https://www.google.com/search?q={q}+site:linkedin.com")
        add("Google — name + site:facebook.com", f"https://www.google.com/search?q={q}+site:facebook.com")
        add("Bing — exact name", f"https://www.bing.com/search?q={q}")

    if email:
        qe = quote_plus(f'"{email}"')
        add("Google — exact email", f"https://www.google.com/search?q={qe}")

    if phone:
        qp = quote_plus(f'"{phone}"')
        add("Google — exact phone", f"https://www.google.com/search?q={qp}")

    return queries


def build_markdown(queries):
    lines = ["# OSINT Query Checklist", ""]
    for label, url in queries:
        lines.append(f"- [ ] **{label}**: {url}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Build a batch of public search queries for a subject.")
    ap.add_argument("--name", help="Subject full name")
    ap.add_argument("--email", help="Subject email address")
    ap.add_argument("--phone", help="Subject phone number")
    ap.add_argument("-o", "--output", default="queries.md", help="Output Markdown checklist")
    args = ap.parse_args()

    if not any([args.name, args.email, args.phone]):
        ap.error("Provide at least one of --name, --email, --phone")

    queries = build_queries(args.name, args.email, args.phone)
    md = build_markdown(queries)

    with open(args.output, "w") as f:
        f.write(md)

    print(f"{len(queries)} queries written to {args.output}")


if __name__ == "__main__":
    main()
