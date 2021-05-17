''' Classes for Thread Worker with signals in PyQt5 with QThreadPool '''

import sys
import traceback

from PyQt5 import QtCore


class WorkerSignals(QtCore.QObject): # pylint: disable=(c-extension-no-member)
    ''' Workers signals '''
    finished = QtCore.pyqtSignal() # pylint: disable=(c-extension-no-member)
    error = QtCore.pyqtSignal(tuple) # pylint: disable=(c-extension-no-member)
    result = QtCore.pyqtSignal(object) # pylint: disable=(c-extension-no-member)
    progress = QtCore.pyqtSignal() # pylint: disable=(c-extension-no-member)

class Worker(QtCore.QRunnable): # pylint: disable=(c-extension-no-member)
    ''' Thread Worker '''
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        # Store constructor arguments (re-used for processing)
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        # Add the callback to our kwargs
        self.kwargs['progress_callback'] = self.signals.progress

    @QtCore.pyqtSlot() # pylint: disable=(c-extension-no-member)
    def run(self):
        '''
        Initialise the runner function with passed args, kwargs.
        '''
        # Retrieve args/kwargs here; and fire processing using them
        try:
            result = self.fn(*self.args, **self.kwargs)
        except Exception:  # pylint: disable=broad-except
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc()))
        else:
            self.signals.result.emit(result)  # Return the result of the processing
        finally:
            self.signals.finished.emit()  # Done
