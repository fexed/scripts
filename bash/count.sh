#!/bin/bash

find . -maxdepth 2 -type d | sort | while read -r dir
do printf "%s\t" "$dir"; find "$dir" -type f | wc -l; done
