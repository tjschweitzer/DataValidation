
import argparse, sys
import json
import os


class LoadData(object):
    def __init__(self,args):
        self.input_config_json = None
        self.raw_input_lines = None
        self.InputFile = args.InputFile
        self.TableName = args.TableName
        self.InputConfig = args.InputConfig
        self.TableConfig = args.TableInfo

        self.read_input_config()

    def read_input_config(self):
        if self.InputConfig == 'None':
            quit("Input config file not defined")

        if not os.path.exists(self.InputConfig):
            quit("Input config file not found")

        with open(self.InputConfig) as input_config:
            self.input_config_json = json.load(input_config)
        return self

    def process_input_config(self):
        if not self.input_config_json:
            self.read_input_config()



    def read_input_file(self):
        if self.InputFile == 'None':
            quit("Input file not defined")

        if not os.path.isfile(self.InputFile):
            quit("Input file does not exist")

        with open(self.InputFile) as fp:
            self.raw_input_lines = fp.readlines()




def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--InputFile","--F", help="Path to input file", required=True)
    parser.add_argument("--InputConfig","--C", help="Path to input file config", required=True)
    parser.add_argument("--TableName","--N", help="OutPut table name", required=True)
    parser.add_argument("--TableInfo","--I ", help="OutPut table information")

    args = parser.parse_args()
    LoadData(args)
if __name__ == '__main__':
    main()
