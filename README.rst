filelist
========

This module introduces functions that allow users to integrate
".gitignore"-like funcitonality while walking through a directory.

You can use shell-style matching patterns to define files that you want
to exclude from your directory crawl. These rules can be stored in files
throughout the crawl path, or they can be passed directly to a function
as an array of strings.