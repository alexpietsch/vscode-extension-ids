import sys, os, json, getopt, argparse

def check_path(file_path):
    if not os.path.exists(file_path):
        print(f"Path '{file_path}' is not a valid file path.")
        exit(1)
    else:
        return True

def main():

    # opts, args = getopt.getopt(sys.argv[1:], 'f:i')
    parser = argparse.ArgumentParser()
    parser.add_argument('-f' '--file', type=str, required=True)
    parser.add_argument('-i' '--ids', action='store_true', required=False)
    args = parser.parse_args()

    FILE_PATH = args.f__file
    WITH_PREFIX = args.i__ids

    VALID_PATH = check_path(FILE_PATH)

    if VALID_PATH == True:
        file_data = None
        with open(FILE_PATH, 'r') as file:

            if len(file.readlines()) != 0:
                file.seek(0)
                file_data = json.load(file)

                if file_data != None:
                    for e in file_data:
                        ex_id = e['identifier']['id']
                        print(f'@id:{ex_id}' if WITH_PREFIX == True else f'{ex_id}')
            else:
                print('File is empty')
                exit(0)

if __name__ == '__main__':
    main()
