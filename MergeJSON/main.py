import os
import json
import sys

# Utility for merging two dictionaries.


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
    # os walker for processing files in a specified directory.
    for root, sub, files in os.walk(os.getcwd()):
        for file in files:
            # check if file name has input file base name and is in JSON format.
            if file.startswith(inp_base_name) and file.endswith(file_ext):
                with open(file, "r") as f:
                    data = json.load(f)
                # converting the dictionary to full deep merged dictionary.
                res = full_merge_dict(res, data)

    # check if the resultant json doesn't exceed the maximum file size
    if sys.getsizeof(res) < max_file_size:
        # check if the resultant file with prefix as output file base name and suffix as  counter.
        if not os.path.exists(os.getcwd() + out_base_name + str(out_file_count) + file_ext):
            out_file_count += 1
            with open(os.path.join(os.getcwd(), out_base_name + str(out_file_count) + file_ext), "w") as fo:
                # write the resultant JSON object to the output file.
                json.dump(res, fo)


if __name__ == '__main__':
    main()
