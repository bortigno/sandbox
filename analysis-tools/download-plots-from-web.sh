#!/bin/bash
cern-get-sso-cookie -o cook --url $1
for d in $(curl -L -s -k -b cook $1 | grep -oP '(?<=<a class="file" href=").*?(?=\"\>\[.pdf\]</a>)'); do
  echo $d
  curl -O -L -s -k -b ../cook $1/$d 
done
