export num=1.1
docker build -t techfest-sign-in:$num .
docker tag techfest-sign-in:$num 020308349020.dkr.ecr.ap-south-1.amazonaws.com/techfest-sign-in:$num
docker push 020308349020.dkr.ecr.ap-south-1.amazonaws.com/techfest-sign-in:$num