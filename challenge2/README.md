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