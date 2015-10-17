#!/bin/bash

IP=10.186.18.228

a=0
while[ a < 2000 ]
do
	telnet 10.186.18.228 8080
	sleep .1
done
