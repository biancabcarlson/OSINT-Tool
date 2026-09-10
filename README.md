# OSINT Assistant

**🔗 Tool:** https://biancabcarlson.github.io/OSINT-Tool/

Given a subject's public identifiers (name, email, phone, town/county, age, a
known associate — you supply them), generates a ready-to-click list of investigator-relevant
lookups grouped by identifier type — social media checks (LinkedIn, X/Twitter, Facebook
mutual-connection search), general checks (email/phone reputation lookups), and public-record
checks (obituary, police record) — plus a Markdown checklist for tracking what's been
reviewed. Works for any case typology, not just account takeover.

Builds query strings only — it does not query, scrape, or authenticate against any site.
`index.html` generates the clickable links instantly, entirely client-side, in your browser,
and is pre-filled with the `simulated-account` fixture (Jane Doe) as a working demo. A name
alone is rarely enough to confirm identity — supplying a town, age, or known
associate narrows the record and relationship checks well beyond a generic name search.

## Other tools in this series

- [Case Calculator](https://biancabcarlson.github.io/Case-Calculator/)
- [Report Template Filler](https://biancabcarlson.github.io/Report-Template-Filler/)
- [OSINT Assistant](https://biancabcarlson.github.io/OSINT-Tool/) *(this repo)*
- [Case Doc Tracker](https://biancabcarlson.github.io/Case-Doc-Tracker/)
- [Entity Name Matcher](https://biancabcarlson.github.io/Entity-Name-Matcher/)
- [Case Timeline Builder](https://biancabcarlson.github.io/Case-Timeline-Builder/)
