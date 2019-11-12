import os
import json
import sys
import os.path


def full_merge_dict(d1, d2):
    for key, value in d1.items():
        if key in d2:
            if type(value) is dict:
                full_merge_dict(d1[key], d2[key])
            else:
                if type(value) in (int, float, str):
                    d1[key] = [value]
                if type(d2[key]) is list:
                    d1[key].extend(d2[key])
                else:
                    d1[key].append(d2[key])
    for key, value in d2.items():
        if key not in d1:
            d1[key] = value
    return d1


def main():
    file_ext = '.json'
    os_path = input('Enter the folder path >>')
    inp_base_name = input('Enter input base file name >>')
    out_base_name = input('Enter input base file name >>')
    max_file_size = int(input('Enter the maximum file size >>'))
    os.chdir(os_path)
    res = {}
    out_file_count = 0
    for root, sub, files in os.walk(os.getcwd()):
        for file in files:
            if file.startswith(inp_base_name) and file.endswith(file_ext):
                with open(file, "r") as f:
                    data = json.load(f)
                res = full_merge_dict(res, data)

    if sys.getsizeof(res) < max_file_size:
        if not os.path.exists(os.getcwd() + out_base_name + str(out_file_count) + file_ext):
            out_file_count += 1
            with open(os.path.join(os.getcwd(), out_base_name + str(out_file_count) + file_ext), "w") as fo:
                json.dump(res, fo)


if __name__ == '__main__':
    main()
