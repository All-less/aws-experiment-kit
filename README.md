# exp-kit

A CLI tool facilitating experimentation on AWS.

### TODO

- add support for multiple instance types
- add prerequisite checking

### Installation

It is recommended to install the package with `pip`.

```bash
pip install exp-kit 
```

### Prerequisites

- Python 3.5+
- MongoDB
- AWS credentials used by [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html). Below is a quick fix.
```bash
pip install awscli
aws configure
```
- Create the file `~/.exp-kit/config.json` with configurations as follows.
```javascript
{
    // key pair name on AWS
    "key_name": "key-pair-name",
    // path to your private key
    "key_path": "/path/to/key-pair-name.pem",
    // public key associated with your key pair
    "public_keys": [ "ssh-rsa XXXX key-pair-name" ]
    // IAM role to create spot request
    "iam_fleet_role": "something:like:this::<aws-id>:role/aws-ec2-spot-fleet-tagging-role",
    // host of MongoDB uri
    "mongo_host": "localhost",
    // port of MongoDB uri
    "mongo_port": 27017
}
```

### Usage

##### Create a new cluster

```
exp-kit new -c cluster_configuration.json
```

A sample `cluster_configuration.json` looks as follows.

```json
{
    "name": "cluster",
    "size": 3,
    "instance_type": "m4.large",
    "image_id": "ami-a51f27c5",
    "snapshot_id": "snap-0907c7634681bc477",
    "security_group_id": "sg-c36280ba",
    "disk_size": 20,
    "spot_price": 0.251,
    "user_name": "ec2-user"
}
```

The `instance_type` can include multiple types.

```json
{ 
    "instance_type": [ "m4.large", "m3.large", "m4.xlarge", "m3.xlarge" ]
}
```

You can specify number of nodes for each type.
```json
{
    "instance_type": {
        "m4.large": 1, 
        "m3.large": 2, 
        "m4.xlarge": 3, 
        "m3.xlarge": 4
    }
}
```

##### Destroy a cluster

```
exp-kit rm <cluster_name>
```


##### List cluster information

To list all clusters, use `ls` command directly.

```
exp-kit ls
```

To inspect a specific cluster, add its name as an option.

```
exp-kit ls <cluster_name>
```

### Under the hood

1. cluster
2. `master`
