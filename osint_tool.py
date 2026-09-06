#!/usr/bin/env python3
"""
osint_tool.py
Builds a batch of investigator-relevant public lookup query strings for a
subject — reputation checks, relationship checks, and public-record
searches, not just generic name search — plus a review checklist. Does not
perform any requests itself. Works for any case typology.

Tool: https://biancabcarlson.github.io/OSINT-Tool/

Usage:
    python osint_tool.py --name "Jane Doe" --email "jane.doe@example.com" \
        --phone "(415) 555-0148" --town "San Francisco, CA" --age 39 \
        --associate "Marcus" -o queries.md
"""

import argparse
from urllib.parse import quote_plus


def build_queries(name=None, email=None, phone=None, town=None, age=None, associate=None):
    queries = []

    def add(label, url):
        queries.append((label, url))

    if name:
        q = quote_plus(f'"{name}"')

        add("LinkedIn — professional profile confirmation", f"https://www.google.com/search?q={q}+site:linkedin.com")

        if associate:
            qa = quote_plus(f'"{associate}"')
            add("Facebook — mutual-connection check", f"https://www.google.com/search?q={q}+{qa}+site:facebook.com")
        else:
            add("Facebook — mutual-connection check (pass --associate to narrow this)", f"https://www.google.com/search?q={q}+site:facebook.com")

        if town:
            qt = quote_plus(f'"{town}"')
            age_suffix = f"+approx+age+{quote_plus(str(age))}" if age else ""
            add("Obituary search", f"https://www.google.com/search?q={q}+obituary+{qt}{age_suffix}")
            add("Public police-record search", f"https://www.google.com/search?q={q}+arrest+OR+booking+OR+%22police+report%22+{qt}")
        else:
            add("Obituary search (pass --town to narrow this)", f"https://www.google.com/search?q={q}+obituary")
            add("Public police-record search (pass --town to narrow this)", f"https://www.google.com/search?q={q}+arrest+OR+booking+OR+%22police+report%22")

    if email:
        qe = quote_plus(email)
        qe_exact = quote_plus(f'"{email}"')
        add("Reverse email reputation lookup (e.g. Emailage-style risk/fraud check)", f"https://www.google.com/search?q=email+reputation+lookup+{qe}")
        add("Google — exact email (breach/exposure check)", f"https://www.google.com/search?q={qe_exact}")

    if phone:
        qp = quote_plus(phone)
        qp_exact = quote_plus(f'"{phone}"')
        add("Reverse phone reputation lookup (spam/fraud-report check)", f"https://www.google.com/search?q=phone+reputation+lookup+{qp}")
        add("Google — exact phone", f"https://www.google.com/search?q={qp_exact}")

    return queries


def build_markdown(queries):
    lines = ["# OSINT Query Checklist", ""]
    for label, url in queries:
        lines.append(f"- [ ] **{label}**: {url}")
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Build a batch of investigator-relevant public lookup queries for a subject.")
    ap.add_argument("--name", help="Subject full name")
    ap.add_argument("--email", help="Subject email address")
    ap.add_argument("--phone", help="Subject phone number")
    ap.add_argument("--town", help="Subject town/county (narrows obituary and police-record searches)")
    ap.add_argument("--age", help="Subject approximate age (narrows obituary search)")
    ap.add_argument("--associate", help="Known associate first name (narrows Facebook mutual-connection search)")
    ap.add_argument("-o", "--output", default="queries.md", help="Output Markdown checklist")
    args = ap.parse_args()

    if not any([args.name, args.email, args.phone]):
        ap.error("Provide at least one of --name, --email, --phone")

    queries = build_queries(args.name, args.email, args.phone, args.town, args.age, args.associate)
    md = build_markdown(queries)

    with open(args.output, "w") as f:
        f.write(md)

    print(f"{len(queries)} queries written to {args.output}")


if __name__ == "__main__":
    main()
