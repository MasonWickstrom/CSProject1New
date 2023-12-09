from PyQt6.QtWidgets import *
from Proj1gui import *
import csv


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.submitVote.clicked.connect(lambda: self.submit())

    def submit(self):
        name = self.typeName.text()
        counterJohn = 0
        counterJane = 0
        counterMichael = 0
        counterAmy = 0
        if name == '':
            self.nameGuide.setVisible(True)
        else:
            self.submitVote.setVisible(False)
            self.nameGuide.setVisible(False)
            self.thankYouLabel.setText(f'Thank you for voting, {name}!')
            self.nameLabel.setVisible(False)
            self.typeName.setVisible(False)
            self.voteGuide.setText('Current results:')
            self.voteJohn.setVisible(False)
            self.voteJane.setVisible(False)
            self.voteMichael.setVisible(False)
            self.voteAmy.setVisible(False)
            vote = ''
            if self.voteJohn.clicked:
                vote = 'John'
            elif self.voteJane.clicked:
                vote = 'Jane'
            elif self.voteMichael.clicked:
                vote = 'Michael'
            elif self.voteAmy.clicked:
                vote = 'Amy'
            row = [vote]
            with open('data.csv', 'a') as csvfile:
                content = csv.writer(csvfile)
                content.writerow(row)
            with open('data.csv', 'r') as csvfile:
                content = csv.reader(csvfile)
                for line in content:
                    if line == ['John']:
                        counterJohn += 1
                    elif line == ['Jane']:
                        counterJane += 1
                    elif line == ['Michael']:
                        counterMichael += 1
                    elif line == ['Amy']:
                        counterAmy += 1
            self.resultsJohn.setText(f'John: {counterJohn}')
            self.resultsJane.setText(f'Jane: {counterJane}')
            self.resultsMichael.setText(f'Michael: {counterMichael}')
            self.resultsAmy.setText(f'Amy: {counterAmy}')
            counterTotal = counterJohn + counterJane + counterMichael + counterAmy
            self.resultsTotal.setText(f'Total: {counterTotal}')
