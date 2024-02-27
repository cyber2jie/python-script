from bs4 import BeautifulSoup, Tag


def get_element(html, tag, attrs=None):
    soup = BeautifulSoup(html, 'html.parser')
    elements = soup.find_all(tag, attrs=attrs)
    return elements

def get_element_attr(element, attr):
    return element.get(attr)

def get_element_content(element):
    return element.text

class Selector:
    def __init__(self, soup):
        self.soup = soup

    def select_one(self, selector):
        element = self.soup.select_one(selector)
        if isinstance(element, Tag):
            return Selector(element)
        return element

    def select(self, selector):
        elements = self.soup.select(selector)
        return [Selector(element) if isinstance(element, Tag) else element for element in elements]

    def text(self):
        return self.soup.get_text()

    def attr(self, attr_name):
        return self.soup.get(attr_name, '')

    def __getattr__(self, name):
        return getattr(self.soup, name)


def select(html):
    soup = BeautifulSoup(html, 'html.parser')
    selector = Selector(soup)
    return selector
