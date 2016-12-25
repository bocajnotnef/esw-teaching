#!/bin/bash

ssh -nNT -R 5502:localhost:22 esw@highnoiseratio.org
echo "SSH tunnel running, access port 5502 on remote server"
echo "To end tunnel, hit ctrl-c"
