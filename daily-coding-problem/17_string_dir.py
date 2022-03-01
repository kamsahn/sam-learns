"""
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.

Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2.
subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1.
subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system.
For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext",
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format,
return the length of the longest absolute path to a file in the abstracted file system.
If there is no file in the system, return 0.

Note:
The name of a file contains at least a period and an extension.
The name of a directory or sub-directory will not contain a period.
"""

# first approach will be to
# 1. find each file (return 0 if none)
# 2. assemble each string path
# 3. compare and return

w = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"

class DirUnpacker():
    def __init__(self, full_path):
        self.full_path = full_path
        self.dir_dict = {}

    def assemble_path(self, s):
        print(s)
        sub_s = ""
        for i in range(len(s)):
            if s[i] in ['\n', '\t']:
                # remove sub_s and return remaining string
                new_sub = f'/{s[i+1:]}'
                if not self.dir_dict.get(new_sub):
                    self.dir_dict[new_sub] = new_sub
                    self.assemble_path(new_sub)
            else:
                sub_s += s[i]

        self.dir_dict[sub_s] = sub_s

du = DirUnpacker(w)
du.assemble_path(du.full_path)
print(du.dir_dict.keys())
