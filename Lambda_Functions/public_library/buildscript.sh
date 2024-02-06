#!/bin/bash
export num=1.0
docker build -t techfest-public-library:$num .
docker tag techfest-public-library:$num 020308349020.dkr.ecr.ap-south-1.amazonaws.com/techfest-public-library:$num
docker push 020308349020.dkr.ecr.ap-south-1.amazonaws.com/techfest-public-library:$num
