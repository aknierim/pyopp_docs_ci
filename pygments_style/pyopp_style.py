from pygments.styles.solarized import SolarizedLightStyle
from pygments.token import Keyword, Comment, String

styles = SolarizedLightStyle.styles.copy()
styles[Comment.Multiline] = "#4a5454"
styles[String.Doc] = "#4a5454"
styles[Keyword] = "#31ce60"


class Pyopp(SolarizedLightStyle):
    styles = styles
