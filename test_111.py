import subprocess
import pytest
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


def subprocess_file(command, text):
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0 and text in out:
        return True
    return False


def get_out(cmd):
    return subprocess.run(cmd,shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout


@pytest.mark.usefixtures('make_folders', 'clear_folders', 'make_files', 'write_log')
class TestSem:

# def test_step_1():
#     result_1 = subprocess_file(f"cd /home/mari/folder_in; touch file_1", "")
#     result_2 = subprocess_file(f"cd /home/mari/folder_in; touch file_2", "")
#     result_3 = subprocess_file(f"cd /home/mari/folder_in; touch file_3", "")
#     assert result_1 and result_2 and result_3, "test1 FAIL"

    def test_step_2(self):
        result_1 = subprocess_file("cd {}; 7z a {}/arh_1".format(data.get("folder_in"), data.get("folder_out")), "")
        assert result_1, "test2 FAIL"

    def test_step_3(self):
        result_1 = subprocess_file("cd {}; 7z l arh_1.7z".format(data.get("folder_out")), "")
        print(result_1)
        assert result_1, "test3 FAIL"

    def test_step_4(self):
        result_1 = subprocess_file("cd {}; 7z x arh_1.7z -o{}".format(data.get("folder_out"), data.get("folder_ex")), "")
        assert result_1, "test4 FAIL"


if __name__ == '__main__':
    pytest.main(["-vv"])