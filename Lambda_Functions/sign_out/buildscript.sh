#!/bin/bash
export num=1.0
docker build -t techfest-signout:$num .
docker tag techfest-signout:$num 020308349020.dkr.ecr.ap-south-1.amazonaws.com/techfest-signout:$num
docker push 020308349020.dkr.ecr.ap-south-1.amazonaws.com/techfest-signout:$num
