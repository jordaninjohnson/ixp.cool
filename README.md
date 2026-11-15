# ixp.cool — IXP public project site

[**Live site: ixp.cool**](https://ixp.cool/) · [**GitHub organization**](https://github.com/ixp-tech) · [**Site source**](https://github.com/jordaninjohnson/ixp.cool)

This is the public, static landing page for **IXP**, a digital-signage operations project. The site explains the problem, what the local prototype can do, what is planned, and how to follow the work.

## Current public claims (reviewed November 14, 2026)

**Implemented in a private local-development application:** PostgreSQL 17 schema/migrations, a FastAPI REST service, a React/TypeScript admin for organization → building → location → screen inventory, logical-screen inventory-status edits, building reports/CSV/JSON exports, draft content-metadata records, and automated integration/browser tests. The v0.3 admin milestone remains unfinished; the API package is `0.2.0.dev0`.

**Not available:** public application source, an application license, a tagged product release, customer hosting, public production installation, authentication/RBAC, actual player provisioning, playback, media uploads, scheduling execution, backup/restore services or field pilots.

**Crucial distinction:** An active *logical screen* is an inventory record, not proof that a device is online or playing content. Organization-scoped SQL is not API authorization. The development stack must be kept on localhost with fictional records.

**Public source vs private source:** This site repository is public, but the application repository `ixp-tech/ixp` is private and has no open-source redistribution terms. Never imply the site source can install IXP.

## Site map

| File | Purpose |
| --- | --- |
| [`index.html`](index.html) | Single-page landing site: purpose, workflow, capability scope, milestone roadmap, FAQ and public links |
| [`thank-you.html`](thank-you.html) | Unused historical URL. Clearly states it is **not** confirmation of a message or subscription |
| [`CNAME`](CNAME) | Existing GitHub Pages custom domain (do not remove) |
| [`robots.txt`](robots.txt), [`sitemap.xml`](sitemap.xml) | Search discovery for the single canonical landing page |
| [`tests/test_site.py`](tests/test_site.py) | No-dependency checks for structure, metadata, internal links and truthful status |
| [`.github/workflows/site.yml`](.github/workflows/site.yml) | Automated tests for changes to the static site |

## Preview and verify

No npm installation or build system is required.

```bash
python3 -m http.server 8765
# In a browser, visit http://127.0.0.1:8765/
```

In another terminal:

```bash
python3 -m unittest discover -s tests -v
```

Test mobile and desktop sizes, keyboard Tab navigation, visible focus, expandable FAQ answers, and reduced-motion preferences. Check that the landing page is readable without JavaScript; the small footer script only refreshes the copyright year.

## Publishing and accuracy checklist

1. Cross-check feature claims with **merged** `ixp-tech/ixp` code, the engineering status, roadmap, and successful CI. Do not count unmerged pull requests or planned schema tables as active product capabilities.
2. Keep the hero, status console, capabilities, roadmap, FAQ, SEO description, organization profile and site README consistent.
3. Link only to real public destinations: [ixp.cool](https://ixp.cool/), [IXP organization](https://github.com/ixp-tech), [site source](https://github.com/jordaninjohnson/ixp.cool), and [builder](https://github.com/jordaninjohnson). **Do not link anonymous visitors to private application files** or imagined repos/services.
4. Clearly label local development, no authentication, no public release, and no public application license. Never advertise subscription, purchases, support, or an actual deployment that does not exist.
5. Preserve accessibility, mobile layout, the `CNAME`, canonical URL, no-index archival page, robots and sitemap.
6. Run tests and inspect the GitHub Pages result after merging. Update the content review date when verified claims change.

## Project identity

IXP is a **project name**, not a statement that an active legal company or commercial service is operating. This site intentionally avoids unverified customer counts, service pricing, legal entity claims or contribution URLs.

The goal is an honest, compelling public entry point that can mature alongside the software—one verified milestone at a time.
