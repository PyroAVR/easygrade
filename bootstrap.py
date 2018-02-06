import os
import re
from zipfile import ZipFile

"""
@return list(DirEntry)
"""

def enumerate_submissions(path):
    valid_files = list()
    for entry in os.scandir(path):
        if not entry.is_file(): continue
        if not entry.name.endswith('.zip'):
            print('found invalid file in', path,':', entry.name)
        else:
            print('adding submission', entry.name)
            valid_files.append(entry)
    return valid_files

"""
needs an update to support not-regex file scanning
@submissions list(DirEntry)
@return dict(pathname, new pathname)
"""
def build_name_map(submissions):
    prefix_re   = re.compile(r"[0-9]+-[0-9]+\s-\s", re.IGNORECASE)
    postfix_re  = re.compile(r"\s-\s.*\.zip", re.IGNORECASE)

    rename_map = dict()

    for entry in submissions:
        cleaned_name = postfix_re.sub("",prefix_re.sub("",entry.name))
        print(entry.name, ":\t", cleaned_name)
        rename_map[entry.name] = cleaned_name
    return rename_map


def unpack_and_rename(rename_map):
    for entry in rename_map.keys():
        with ZipFile(entry) as z:
            z.extractall(rename_map[entry])

def clean_zip(submissions):
    for submission in submissions:
        os.remove(submission)

if __name__ == '__main__':
    submissions = enumerate_submissions('.')
    rename_map = build_name_map(submissions)
    unpack_and_rename(rename_map)
    clean_zip(submissions)
