#!/bin/bash
LC_ALL=C sort < wrongwords.txt > wrongwords2.txt
cp wrongwords2.txt wrongwords.txt
rm wrongwords2.txt
