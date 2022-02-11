from crawler_window import Crawler
import sys
from PyQt5.QtWidgets import *

if __name__ == "__main__":
    window = QApplication(sys.argv)
    crawler = Crawler()
    crawler.show()
    sys.exit(window.exec_())
