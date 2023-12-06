import subprocess
import pytest

def subprocess_file(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0 and text in out:
        return True
    return False


def test_step_1():
    assert subprocess_file("cd /home/mari/Work_t/AutoTest/folder_ex; touch file_x", "")

if __name__ == '__main__':
    pytest.main(["-vv"])