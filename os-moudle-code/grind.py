import os

def show_directory_content(directory_name):
    os.system(f'ls l {directory_name}')

def print_matched(directory_name,match_text):
    os.system(f'ls -l {directory_name} | grep {match_text}')

def print_recursive(directory_name,match_text):
    os.system(f'ls -ltr {directory_name} | grep {match_text}')

if __name__ == '__main__':
  try:
    directory_name = input("Enter Directory name").strip()
    dir_mode = input("Enter Directory mode -d: ").strip()
    match_mode = input("Enter match mode -m: ").strip()
    recursive_mode = input("Enter recursive mode -r: ").strip()
    if os.path.isdir(directory_name):
        if dir_mode == '-d':
            show_directory_content(directory_name)
            if match_mode == '-m':
                match_text = input("Enter match text")
                print_matched(directory_name,match_text)
            elif match_mode == '-m' and recursive_mode == '-r':
                print_recursive(directory_name,match_text)
        else:
            print("invalid option")
    else:
        print("given directory does not exists")
  except Exception as e:
    print("invalid directory",e)