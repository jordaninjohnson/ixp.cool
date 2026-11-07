"""Contract tests for the zero-dependency IXP landing page."""
from html.parser import HTMLParser
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
HOME = (ROOT / "index.html").read_text(encoding="utf-8")
THANKS = (ROOT / "thank-you.html").read_text(encoding="utf-8")


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.fragments = []
        self.headings = []
        self.mains = 0
        self.meta = {}
        self.links = []

    def handle_starttag(self, tag, attrs):
        props = dict(attrs)
        if props.get("id"):
            self.ids.append(props["id"])
        if tag == "main":
            self.mains += 1
        if tag in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.headings.append(tag)
        if tag == "a":
            href = props.get("href", "")
            self.links.append(href)
            if href.startswith("#"):
                self.fragments.append(href[1:])
        if tag == "meta":
            name = props.get("name") or props.get("property")
            if name:
                self.meta[name] = props.get("content")

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)


class LandingPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.page = PageParser()
        cls.page.feed(HOME)

    def test_structure_and_fragments(self):
        page = self.page
        self.assertEqual(page.mains, 1)
        self.assertEqual(page.headings.count("h1"), 1)
        self.assertEqual(len(page.ids), len(set(page.ids)), "Duplicate HTML id")
        self.assertTrue(all(target in page.ids for target in page.fragments))
        self.assertIn("#main", page.links, "Missing keyboard skip navigation")
        self.assertIn("a:focus-visible", HOME)

    def test_discoverability(self):
        page = self.page
        self.assertTrue(page.meta.get("description"))
        self.assertEqual(page.meta.get("og:type"), "website")
        self.assertIn('<link rel="canonical" href="https://ixp.cool/"', HOME)
        self.assertIn('name="viewport"', HOME)
        self.assertIn("prefers-reduced-motion", HOME)

    def test_no_stale_or_misleading_status(self):
        self.assertIn("v0.3 — Admin Interface", HOME)
        self.assertIn("Working locally".lower(), HOME.lower())
        self.assertIn("no API authentication", HOME)
        self.assertIn("repository is private", HOME)
        self.assertIn("PostgreSQL 17", HOME)
        for outdated in ("pre-v0.1", "Now building", "current Data Foundation"):
            self.assertNotIn(outdated, HOME)
        self.assertNotIn("is an open-source digital signage", HOME)

    def test_no_private_repository_links_or_unsafe_external_windows(self):
        page = self.page
        self.assertNotIn("https://github.com/ixp-tech/ixp", page.links)
        self.assertIn("https://github.com/jordaninjohnson/ixp.cool", page.links)
        self.assertEqual(HOME.count('target="_blank"'), HOME.count('rel="noopener noreferrer"'))

    def test_search_discovery_and_current_content_milestone(self):
        import xml.etree.ElementTree as ET

        robots = (ROOT / "robots.txt").read_text(encoding="utf-8")
        self.assertIn("Sitemap: https://ixp.cool/sitemap.xml", robots)
        sitemap = ET.parse(ROOT / "sitemap.xml")
        ns = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
        locations = [node.text for node in sitemap.findall("s:url/s:loc", ns)]
        self.assertEqual(locations, ["https://ixp.cool/"])
        self.assertIn("draft content metadata", HOME)
        self.assertNotIn("next</span><span>content metadata", HOME)
        self.assertNotIn('og:title" content="IXP — Open-source', HOME)

    def test_archived_confirmation_is_honest(self):
        self.assertIn('name="robots" content="noindex"', THANKS)
        self.assertIn("no active contact", THANKS.lower())
        self.assertNotIn("Your message has been sent", THANKS)


if __name__ == "__main__":
    unittest.main()
