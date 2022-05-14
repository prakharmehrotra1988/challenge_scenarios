## What it does
- Query the metadata of an ec2 instance within AWS and provide a json formatted output.
- Retrieve the value of a particular data key.

## How to configure Instances in AWS and SSH
- [Create an EC2 Linux instance on AWS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html)
- [SSH into the instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html)

- Install Python 3 and git on your instance
    - `yum install python3 git -y`
- Clone this repository
  - `git clone <REPOS_NAME>`

- Open the repository on your instance
  - `cd CHALLENGE2`

## How to run the below scripts ?

- Run below script to get metadata information of Instance:
  - `python3 get_metadata.py` -> This will print metadata Information in JSON format. Refer output.json file (Example)
  - `python3 get_key.py`      -> This will ask user input for the key and will give the value back
  

## How it works
- It makes use of the http://169.254.169.254/latest/meta-data link-local address. Instance metatada is provided at this link, but only when you visit it from a running instance.
- A few simple Python scripts are used to extract the required information using the above API.

## Alternatives
If you need quick outputs from shell scripts use can use below reference commands too. The command format is different, depending on whether you use IMDSv1 or IMDSv2. By default, you can use both instance metadata services. To require the use of IMDSv2, see Use IMDSv2. 

- TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/

- curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/local-hostname

- curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/public-hostname

- curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/public-keys/

- curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/tags/instance/Name



Reference: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instancedata-data-retrieval.html
