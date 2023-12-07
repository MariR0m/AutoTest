import subprocess
import pytest


def subprocess_file(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0 and text in out:
        return True
    return False

def test_step_1():
    result_1 = subprocess_file(f"cd /home/mari/folder_in; touch file_1", "")
    result_2 = subprocess_file(f"cd /home/mari/folder_in; touch file_2", "")
    result_3 = subprocess_file(f"cd /home/mari/folder_in; touch file_3", "")
    assert result_1 and result_2 and result_3, "test1 FAIL"

def test_step_2():
    result_1 = subprocess_file(f"cd /home/mari/folder_in; 7z a /home/mari/folder_out/arx_2", "")
    assert result_1, "test2 FAIL"

def test_step_3():
    result_1 = subprocess_file(f"cd /home/mari/folder_out; 7z l arx_2.7z", "")
    print(result_1)
    assert result_1, "test3 FAIL"

def test_step_4():
    result_1 = subprocess_file(f"cd /home/mari/folder_out; 7z x arx_2.7z -o/home/mari/folder_ex", "")
    assert result_1, "test4 FAIL"

if __name__ == '__main__':
    pytest.main(["-vv"])