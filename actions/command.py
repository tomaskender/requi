import subprocess


def execute_command(action, wd, return_code, output):
    ret = 0, None
    try:
        ret = 0, subprocess.check_output([action], shell=True, cwd=wd)
    except subprocess.CalledProcessError as err:
        ret = err.returncode, err.output

    is_ok = 1
    if return_code is not None:
        is_ok = ret[0] == return_code

    if is_ok == 1 and output is not None:
        is_ok = ret[1] == output

    return is_ok