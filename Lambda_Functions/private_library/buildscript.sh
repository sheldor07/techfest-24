#!/bin/bash
export num=1.0
docker build -t techfest-private-library:$num .
docker tag techfest-private-library:$num 020308349020.dkr.ecr.ap-south-1.amazonaws.com/techfest-private-library:$num
docker push 020308349020.dkr.ecr.ap-south-1.amazonaws.com/techfest-private-library:$num
