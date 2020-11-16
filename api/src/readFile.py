import os
import string
import random
import sys
import re
from flask import Flask, jsonify

class Reader:
    STORE_PATH = 'data'
    GENERATED_FILE_NAME = 'generated_file.txt'
    FILE_PATH = STORE_PATH + '/' + GENERATED_FILE_NAME

    def read_file():
        try:
            reader = open(Reader.FILE_PATH, 'r')
            content = reader.read()
            return content[:-1]
        finally:
            reader.close()

    def findTypes(fileContent):

        try:
            arr_split = fileContent.split(',')

            int_num = 0
            decimal_num = 0
            string_num = 0
            alphanumberic_num = 0

            for i in arr_split:
                if Reader.is_integer(i):
                    int_num += 1
                elif Reader.is_real_number(i):
                    decimal_num += 1
                elif re.match('^[a-z]+$', i):
                    string_num += 1
                elif re.match('^[a-z0-9_-]*$', i):
                    alphanumberic_num += 1
            out_put = {
                'int': int_num,
                'real_number': decimal_num,
                'string': string_num,
                'alphanumberic': alphanumberic_num
            }
            return jsonify(out_put)
        except ValueError:
            return 'Error'

    def is_integer(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def is_real_number(s):
        try:
            float(s)
            return True
        except ValueError:
            return False
