from bs4 import BeautifulSoup
mini_html = """
<a class="product-link" href="/product/mouse" data-product-id="001">
    wireless mouse
</a>
"""

mini_soup = BeautifulSoup(mini_html, "html.parser")
link=mini_soup.select_one("a.product-link")

print("visible text:", link.get_text(strip=True))