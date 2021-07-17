import time
import yaml
import tempfile
import shutil
import argparse
from utils.progressbar import progress
from actions import archive, command

class Worker:
    def __init__(self):
        self.working_dir = tempfile.TemporaryDirectory()

    def load(self, rule_file, checked_file):
        shutil.copy2(checked_file, self.working_dir.name)
        self.checked_file = checked_file
        with open(rule_file, 'r') as stream:
            self.rule = yaml.safe_load(stream)

    def execute(self, options=None):
        total = len(self.rule["steps"])
        i = 0
        while i < total:
            step = self.rule["steps"][i]
            progress(i, total, status='Executing step ' + step['name'])
            self.__handle_step(step)
            time.sleep(0.5) # execute step
            i += 1
        progress(i, total, status='Finished')

    def __handle_step(self, step):
        step_action = step['action']
        if step_action == 'check-files':
            pass
        elif step_action == 'unzip':
            archive.unzip(self.checked_file, self.working_dir.name)
        elif step_action == 'custom':
            ret_code = None
            if 'action-code' in step:
                ret_code = step['action-code']
            ret_output = None
            if 'action-output' in step:
                ret_output = step['action-output']
            
            success = command.execute_command(step['action-cmd'], self.working_dir.name, ret_code, ret_output)
            if not success:
                raise Exception('Step ' + step['name'] + ' failed.')
        else:
            raise Exception('Unrecognized action in step "' + step['name'] + '".')



if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--rule', help='Filname for project rules', required=True)
    arg_parser.add_argument('--project', help='Filename for checked project', required=True)

    args = arg_parser.parse_args()

    w = Worker()
    w.load(args.rule, args.project)
    w.execute()