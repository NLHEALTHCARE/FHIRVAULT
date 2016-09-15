from html.parser import HTMLParser
import urllib.request


def html_to_string(url):
    html_string_list = []

    for word in urllib.request.urlopen(url):
        html_string_list.append(word.strip().decode('utf-8'))

    html_as_string = ''.join(str(e) for e in html_string_list)
    return html_as_string


# Kennelijk gebruikt  de HTMLParser strings als input. Echter de html data die binnenkomt dankzij 'urllib.request.urlopen' is in bytes.
# Om dit op te lossen wordt de data eerst in een list veranderd met ".decode('utf-8')" en vervolgens wordt deze list omgezet in een string



class NicTizParser(HTMLParser):
    """https://docs.python.org/3.0/library/urllib.request.html. "handle_starttag is 1 van de methodes die in htmlParser zit (en kan dus niet hernoemd worden naar get_xml_refs)" """
    """De class NizTizParser erft over van de class HTMLParser. Van deze laastste wordt de def handle_starttag overridden door eigen code
      Het zelfde geldt voor de def __init__ self, maar wordt door "super" aan te roepen van de oorspronkelijke init functie
      in de class HTMLParser aan wezige 'self.convert_charrefs' en 'self.reset()' toch behouden."""

    def __init__(self):
        # initializeer eerst de base class

        super().__init__()
        self.xml_refs = []

    def handle_starttag(self, tag, attrs):

        str = 'xml'

        # only parse the 'anchor' tag
        if tag == "a":
            # check the list of defined attributes.
            for name, value in attrs:
                # if href is defined en de value 'xml' bevat, stop het in de list "xml_refs" voor later gebruik.
                if name == "href" and str in value:
                    self.xml_refs.append(value)


html_as_string = html_to_string('https://decor.nictiz.nl/decor/services/ValueSetIndex?ref=2.16.840.1.113883.2.4.3.11.60.101')

if __name__ == "__main__":
    parser = NicTizParser()
    parser.feed(html_as_string)
    parser.close()

    xml_refs = parser.xml_refs
    print(xml_refs)
    print(xml_refs[0])
