# ThreadPool worker in PyQt5

Multithreading process in PyQt5 which allows You to read signals from threads.

# How its work

1. Initialize class: [threadpool = QtCore.QThreadPool()]
2. In other function initialize worker: [worker = Worker('function to start thread')]
3. You can add signals: ex. [worker.signals.finished.connect('function when thread finish')]
                            [worker.signals.progress.connect('function to count progress')]
4. Start thread: [threadpool.start(worker)]