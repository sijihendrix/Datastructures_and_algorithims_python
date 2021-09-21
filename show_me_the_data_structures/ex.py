import os


def ex(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.isfile(path+suffix):
      return print (os.listdir(path))


# print (os.listdir("."))

# print (os.path.isfile("./show_me_the_data_structures/testdir/subdir1/a.c"))

ex( '/t1.c' , './show_me_the_data_structures/testdir')


#don't really understand the intsruction. 