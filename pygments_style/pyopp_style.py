from pygments.styles.nord import NordStyle
from pygments.token import Comment, Generic, Name, Token, Whitespace

styles = NordStyle.styles.copy()
# remove *italic* in the default
styles[Comment] = "#66696e"
styles[Generic.Output] = "#66696e"
styles[Name] = "#66696e"
styles[Name.Variable] = "#66696e"
styles[Whitespace] = "#66696e"
styles[Token] = "#66696e"


class Pyopp(NordStyle):
    styles = styles
