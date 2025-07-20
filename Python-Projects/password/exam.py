from utils import unzip_with_7z  # pyright: ignore[reportImplicitRelativeImport]
from string import ascii_lowercase

zip_file_path = "congrats.7z"  # keep as is
dest_path = "."  # keep as is

find_me = ""  # 2 letters are missing!
secret_password = find_me + "bcmpda"

# WRITE YOUR CODE BELOW
# ----------------------------------------

for first in ascii_lowercase:
    for second in ascii_lowercase:
        find_me = first + second
        secret_password = find_me + "bcmpda"
        if unzip_with_7z(zip_file_path, dest_path, secret_password):
            print("The right letters are ", find_me, ".", sep="")
            break

