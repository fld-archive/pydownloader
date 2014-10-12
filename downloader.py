#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Python2.x compatibility
from __future__ import print_function

import os, sys
import argparse
import urllib.request

def download(filename, destination=None):
    """ Downloader method.
    
    Keyword arguments:
    
    filename - The remote file URL
    destination - Destination filename (including path)
    """
    # Download to the current folder if no destination is specified.
    if destination is None:
        destination = os.getcwd()
        
    print('Downloading', filename, 'to', destination, '...')
    
    destination_filename = os.path.join(destination, os.path.basename(filename))
    
    urllib.request.urlretrieve( filename, destination_filename )
    print('[OK]', filename)
        
def main(argz):
    try:
        f = open(argz.filename, 'r')
        files = f.readlines()
        f.close()
        
        for file in files:
            download(file, argz.output_dir)
    except IOError:
        print('ERROR: the file', argz.filename, 'cannot be opened.')
        return
    finally:
        print('Exiting.')


if __name__ == '__main__':
    # Entry point
    parser = argparse.ArgumentParser(description='Batch file downloader')
    
    parser.add_argument('filename', type=str,
        help='A file which contains URLs of files to be downloaded.')
    parser.add_argument('output_dir', nargs='?', help='Output directory')
    
    main(parser.parse_args())