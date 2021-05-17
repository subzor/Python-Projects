# Completer for words in PyQt5

Auto-completer words from own list.

# How its work

1. Initialize completer: [self._completer = Completer('list of words')]
2. Add completer to object, ex. QLineEdit or QTextEdit: [self.'object name(ex. QlineEdit)'.setCompleter(self._completer)]