import string
import random
import sys
import os
import re
from .readFile import Reader

from flask import Flask, jsonify

class Generator:
    LENGTH_LIMIT = 10000
    REAL_NUMBER_LIMIT = 100000
    REAL_NUMBER_DECIMAL = 3
    INTEGER_LIMIT = 100000
    STORE_PATH = Reader.STORE_PATH
    GENERATED_FILE_NAME = Reader.GENERATED_FILE_NAME
    FILE_PATH = Reader.FILE_PATH
    FILE_SIZE_LIMIT = 1024 * 1024 * 2

    def random_string():
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(Generator.LENGTH_LIMIT))

    def random_real_numbers():
        return str(round(random.uniform(0, Generator.REAL_NUMBER_LIMIT), Generator.REAL_NUMBER_DECIMAL))

    def random_integers():
        return str(random.randint(0, Generator.INTEGER_LIMIT))

    def random_letters_and_digits():
        random_source = string.ascii_lowercase + string.digits
        out_put = ''.join(random.choice(random_source) for i in range(Generator.LENGTH_LIMIT))
        tmp_list = list(out_put)
        random.shuffle(tmp_list)
        out_put = '' . join(tmp_list)
        return out_put
    def file_size(filename):
        statinfo = os.stat(filename)
        return statinfo.st_size

    def write_to_file():
        if not os.path.isdir(Generator.STORE_PATH):
            os.mkdir(Generator.STORE_PATH)

        f = open(Generator.FILE_PATH, "w")
        f.write('')
        f.close()

        while Generator.file_size(Generator.FILE_PATH) < Generator.FILE_SIZE_LIMIT:
            list = [
                Generator.random_integers(),
                Generator.random_real_numbers(),
                Generator.random_string(),
                Generator.random_letters_and_digits()
            ]
            final_list1 = random.choice(list)
            new_list_size = sys.getsizeof(final_list1)
            file = open(Generator.FILE_PATH, "a")
            try:
                if Generator.file_size(Generator.FILE_PATH) + new_list_size < Generator.FILE_SIZE_LIMIT:
                    file.write(final_list1 + ',')
                else:
                    reader = [Reader.read_file()]
                    return jsonify(reader)
            except ValueError as e:
                print('Error while appending new string: ' + e)
            finally:
                file.close()