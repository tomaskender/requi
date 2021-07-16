import time
import yaml
from utils.progressbar import progress

class Worker:
    def __init__(self):
        pass

    def load(self, rule_file):
        with open(rule_file, 'r') as stream:
            self.rule = yaml.safe_load(stream)

    def execute(self, options=None):
        total = len(self.rule["steps"])
        i = 0
        while i < total:
            progress(i, total, status='Executing step ' + self.rule["steps"][i]['name'])
            time.sleep(1) # execute step
            i += 1
        progress(i, total, status='Finished')

if __name__ == '__main__':
    w = Worker()
    w.load('example-rule.requi')
    w.execute()