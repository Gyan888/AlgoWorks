import threading
import logging


class question2(threading.Thread):
    def __init__(self, n, method):
        threading.Thread.__init__(self)
        self.threadID = method
        self.n = n
        self.method = method

    def A(self):
        for i in range(1, self.n+1):
            print("A{}".format(i))

    def B(self):
        for i in range(1, self.n+1):
            print("B{}".format(i))

    def C(self):
        for i in range(1, self.n+1):
            print("C{}".format(i))

    def D(self):
        for i in range(1, self.n+1):
            print("D{}".format(i))

    def run(self):
        methods = {
        'A': self.A,
        'B': self.B,
        'C': self.C,
        'D': self.D
        }
        methods[self.method]()

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = []
    for index in ['A', 'B', 'C', 'D']:
        logging.info("Main  : create and start thread %s.", index)
        x = question2(100, index)
        threads.append(x)
        x.start()
