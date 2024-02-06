#!/bin/bash
export num=1.1
docker build -t techfest-signup:$num .
docker tag techfest-signup:$num 020308349020.dkr.ecr.ap-south-1.amazonaws.com/techfest-signup:$num
docker push 020308349020.dkr.ecr.ap-south-1.amazonaws.com/techfest-signup:$num
