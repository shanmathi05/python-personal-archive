#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

import os

FOLDER_NAME = "C:/Users/shanmathi_2/Downloads"

for file in os.listdir(FOLDER_NAME): 
    if file .endswith("png"):
        print(os.path.join(FOLDER_NAME,file))