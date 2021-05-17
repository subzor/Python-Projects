''' Imporved completer for PyQt5 '''


from PyQt5 import QtCore, QtWidgets

class Completer(QtWidgets.QCompleter): # pylint: disable=(c-extension-no-member)
    '''Imporved completer'''
    def __init__(self, *args, **kwargs):
        super(Completer, self).__init__(*args, **kwargs)

        self.setCaseSensitivity(QtCore.Qt.CaseInsensitive) # pylint: disable=(c-extension-no-member)
        self.setCompletionMode(QtWidgets.QCompleter.PopupCompletion) # pylint: disable=(c-extension-no-member)
        self.setWrapAround(False)

    # Add texts instead of replace
    def pathFromIndex(self, index):
        ''' ? '''
        path = QtWidgets.QCompleter.pathFromIndex(self, index) # pylint: disable=(c-extension-no-member)
        lst = str(self.widget().text()).split(',')
        if len(lst) > 1:
            path = '%s, %s' % (','.join(lst[:-1]), path)
        return path

    def splitPath(self, path):
        ''' ? '''
        path = str(path.split(',')[-1]).lstrip(' ')
        return [path]


''' Initialize in program '''

# self._completer = Completer('list of words')
# self.'object name(ex. QlineEdit)'.setCompleter(self._completer)