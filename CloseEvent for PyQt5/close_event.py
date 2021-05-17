''' Close event method for PyQt5 '''

from PyQt5 import QtWidgets

def closeEvent(self, event):
    ''' Close event method '''
    reply = QtWidgets.QMessageBox.question(self, 'Close window', # pylint: disable=(c-extension-no-member)
        'Are you sure you want to close the window?',
        QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No) # pylint: disable=(c-extension-no-member)

    if reply == QtWidgets.QMessageBox.Yes: # pylint: disable=(c-extension-no-member)
        event.accept()
        print('Window closed')
    else:
        event.ignore()


