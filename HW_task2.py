import subprocess

PUNCTUATION = '''!()-[]{};?@#$%:'"\,./^&;*_ ='''


def subprocess_file(directory: str, find_name: str, find_word = 'Yes'):
    result = subprocess.run(directory, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if result.returncode == 0:
        if find_name in out:
            for i in find_name:
                if i in PUNCTUATION:
                    find_name = find_name.replace(i, " ")
            if find_word in find_name:
                print('Find')
            else:
                print('No find')
            return True
        return False
    return False


if __name__ == '__main__':
    print(subprocess_file('cat /etc/os-release', 'VERSION_CODENAME=jammy', 'dhdhdh'))