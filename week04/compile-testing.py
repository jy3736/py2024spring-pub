import compileall
import os
import shutil
import glob

def compile_and_move():
    # Define the directory to store compiled files
    tools_dir = './.tools'
    if not os.path.exists(tools_dir):
        os.makedirs(tools_dir)

    # Search for all directories matching 'prob*' and 'extra*'
    directories = glob.glob('./prob*') + glob.glob('./extra*')

    for dir_path in directories:
        # Compile testing.py in the directory
        compileall.compile_dir(dir_path, force=True)

        # The compiled file path pattern
        compiled_file_pattern = os.path.join(dir_path, '__pycache__', 'testing.*.pyc')

        # Find the compiled testing.py file
        compiled_files = glob.glob(compiled_file_pattern)

        if compiled_files:
            # Assuming there's only one match, as expected
            compiled_file_path = compiled_files[0]

            # Construct new filename based on the original directory
            new_file_name = os.path.basename(dir_path) + '_testing.pyc'
            new_file_path = os.path.join(tools_dir, new_file_name)

            # Move and rename the compiled file
            shutil.move(compiled_file_path, new_file_path)

            # Clean up the __pycache__ directory if needed
            shutil.rmtree(os.path.join(dir_path, '__pycache__'))

if __name__ == "__main__":
    compile_and_move()
