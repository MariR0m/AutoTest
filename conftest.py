import pytest
import yaml
from test_111 import subprocess_file, get_out
import random
import string
from datetime import datetime

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture(scope='class')
def make_folders():
    return subprocess_file("mkdir {} {} {}".format(data.get("folder_in"), data.get("folder_out"), data.get("folder_ex")), "")


@pytest.fixture(scope='class')
def clear_folders():
    yield
    return subprocess_file("rm -rf {} {} {}".format(data.get("folder_in"), data.get("folder_out"), data.get("folder_ex")), "")


@pytest.fixture(scope='class')
def make_files():
    list_of_files = []
    for i in range(5):
        file_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if subprocess_file("cd {}; dd if=/dev/urandom of={} bs=1M count=1 iflag=fullblock".format(data.get("folder_in"), file_name), ""):
            list_of_files.append(file_name)
    return list_of_files


@pytest.fixture(scope='function')
def write_log():
    yield
    time = datetime.now().strftime("%H:%M:%s.%f")
    stat = get_out('cat /proc/loadavg')
    subprocess_file(f"echo 'time:{time} size; stat:{stat}' >> stat.txt", '')