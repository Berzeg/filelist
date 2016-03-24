import os
import re
import fnmatch
import copy

def filelist(absolute_dir, absolute_filenames=True, standard_ignore_rules=[], ignore_file=".pyignore"):
    """ Get all files in a directory that aren't to be ignored

    Compiles ignore rules (in shell-style format) as it traverses down a
    directory, and returns a list of absolute filepaths that pass the
    filter (the files that shouldn't be ignored are returned).

    absolute_dir - The absolute path of the root directory at which to
        start the walk. All .pyignore files in addresses above this one
        in the filetree will be ignored.
    absolute_filenames - Whether the returned file paths should be
        relative to the provided root directory (absolute_dir), or
        whether they should be absolute paths.
    standard_ignore_rules - An array of (string) ignore rules.
    ignore_file - The standard name of all files that contain ignore
        rules in shell-style format.
    """
    leaves = _filelist(absolute_dir, ".", standard_ignore_rules, ignore_file)

    if not absolute_filenames:
        leaves = _relative_filelist(absolute_dir, leaves)

    return leaves

def _filelist(absolute_path, relative_path, ignore_rules, ignore_file):
    ignore_rules = copy.copy(ignore_rules)
    pwd_nodes = os.listdir(absolute_path)

    # Add new ignore rules, if any exist
    if ignore_file in pwd_nodes:
        ignore_filepath = os.path.join(absolute_path, ignore_file)
        ignore_file_handler = open(ignore_filepath, 'r')
        new_rules = ignore_file_handler.read().splitlines()

        ignore_rules.extend(new_rules)

    pwd_files = []

    for node in pwd_nodes:
        absolute_node_path = os.path.join(absolute_path, node)
        relative_node_path = os.path.join(relative_path, node)

        if _should_ignore(relative_node_path, ignore_rules):
            continue

        if os.path.isdir(absolute_node_path):
            child_files = _filelist(absolute_node_path, relative_node_path, ignore_rules, ignore_file)
            pwd_files.extend(child_files)
        else:
            pwd_files.append(absolute_node_path)

    return pwd_files

def _relative_filelist(root_dir, filelist):
    new_filelist = []

    for f in filelist:
        start_index = f.find(root_dir)
        end_index = start_index + len(root_dir)
        new_filelist.append('.' + f[end_index:])

    return new_filelist

def _should_ignore(filepath, ignore_rules):
    for rule in ignore_rules:
        # Megahack: fnmatch doesn't know how to match certain filepaths.
        # e.g. pattern = ".git", path_to_test = "a/.git", match => False
        #      pattern = "*/.git", path_to_test = "a/.git", match => True
        lax_rule = os.path.join("*", rule)
        lax_expression = fnmatch.translate(lax_rule)
        lax_re = re.compile(lax_expression)

        if lax_re.match(filepath):
            return True

    return False