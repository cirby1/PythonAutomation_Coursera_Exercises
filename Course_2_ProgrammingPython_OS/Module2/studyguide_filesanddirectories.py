import os

dest_dir = os.path.join(os.getcwd(), "test1")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

src_file = os.path.join(os.getcwd())
dest_file = os.path.join(os.getcwd())

os.rename(src_file, dest_file)
