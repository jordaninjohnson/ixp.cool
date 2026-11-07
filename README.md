# ixp.cool — IXP project website

This public repository hosts the static landing page for [IXP](https://ixp.cool/), an early-stage digital signage and building-operations software project. It is a lightweight, accessible site without a build step, backend, analytics SDK, contact form, or product downloads.

## Accuracy and security

**Verified against the private application repository on 2026-11-06.**

- PostgreSQL 17, two migrations, synthetic seed data, SQL contract tests.
- FastAPI application package `0.2.0.dev0`; organization/building/location/logical screen create/list/read operations and screen-count reporting.
- Local React/TypeScript admin, with inventory hierarchy creation/browsing, screen counts, and draft content metadata management. The **v0.3 milestone remains in progress**.
- No authentication/RBAC, device provisioning, playback, media-file management, scheduler, production deployment, release tag, or public license.
- The main source repository is **private**. The public website repository is not equivalent to a publicly released application.
- Never connect this static site to the unauthenticated local API or publish real inventory data.

The site uses truthful wording such as “planned open-source project” rather than claiming that an open-source release is currently available. Engineering plans are documented in the private application repository; public links must not imply that anonymous visitors can browse its source.

## Editing and local preview

```bash
python3 -m http.server 8765
# open http://127.0.0.1:8765/
python3 -m unittest discover -s tests -v
```

Changes to the public status must be cross-checked against actual merged application code, current tests, `ROADMAP.md`, and `docs/STATUS.md`. **Do not advance milestone labels based only on open pull requests**. Document the verification date in the page and update this README when capabilities change.

The existing domain configuration in `CNAME` must be preserved for GitHub Pages. Keep `robots.txt` and `sitemap.xml` consistent with the canonical URL and do not index archived/unused pages. `thank-you.html` is an archival entry point; there is no active signup or message form on the website.

## Content and accessibility conventions

- Prefer native semantic HTML: one `h1`, headings in order, a landmark `main`, accessible focus indicators and skip navigation.
- Keep “working locally” separate from “planned”; never suggest the unauthenticated API is safe to host.
- Avoid dead links to the currently private app repository. Use the [GitHub organization](https://github.com/ixp-tech) or [public site source](https://github.com/jordaninjohnson/ixp.cool) instead.
- Preserve responsive behavior and `prefers-reduced-motion` support.
- Run the standard-library site tests before publication. They run in CI on PRs and merges.

## Links

- Website: https://ixp.cool/
- Public website source: https://github.com/jordaninjohnson/ixp.cool
- Organization: https://github.com/ixp-tech
- Builder: https://github.com/jordaninjohnson
