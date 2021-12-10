import webbrowser
from pathlib import Path

OUTPUT_PATH = Path("djur.html")

# DEFINIERA CLASS Djur!


# Vilka egenskaper skall Djur ha?
class Djur:
    name: str
    carnivore: bool
    wiki_url: str
    def __init__(self, name, carnivore, wiki_url):
        self.name = name
        self.carnivore = carnivore
        self.wiki_url = wiki_url

    def carnivore_or_vegetarian(self):
        if self.carnivore:
            return "Köttätare"
        else:
            return "Vegetarian"

    def get_hml_table_row(self):
        return f'<tr><td><a href="{self.wiki_url}">{self.name}</td><td>{self.carnivore_or_vegetarian()}</td></tr>\n'


if __name__ == '__main__':
    djur = []
    zebra = Djur('Zebra', False, 'https://sv.wikipedia.org/wiki/Zebror')
    tiger = Djur('Tiger', True, 'https://sv.wikipedia.org/wiki/Tiger')
    djur.append(zebra)
    djur.append(tiger)
    html = '<html><table>'
    for d in djur:
        html += d.get_hml_table_row()
    html += '</table></html>'
    OUTPUT_PATH.write_text(html, encoding='utf8')
    webbrowser.open(str(OUTPUT_PATH))
