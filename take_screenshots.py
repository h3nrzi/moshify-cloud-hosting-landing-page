from playwright.sync_api import sync_playwright
import os

def take_screenshot(url, output_path):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        # Force AOS elements to be visible
        page.add_init_script("""
            const style = document.createElement('style');
            style.innerHTML = `
                [data-aos] {
                    opacity: 1 !important;
                    transform: none !important;
                }
            `;
            document.head.appendChild(style);
        """)
        page.goto(f"file://{os.getcwd()}/{url}")
        page.set_viewport_size({"width": 1280, "height": 800})
        page.screenshot(path=output_path, full_page=True)
        browser.close()

if __name__ == "__main__":
    take_screenshot("domain.html", "domain_current.png")
    take_screenshot("pricing.html", "pricing_current.png")
    take_screenshot("index.html", "index_current.png")
