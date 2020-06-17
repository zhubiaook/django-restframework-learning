from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter

code = "print('hello world')"
print(highlight(code, get_lexer_by_name('python'), HtmlFormatter()))