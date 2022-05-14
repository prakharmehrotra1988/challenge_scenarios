# Assessment3
We have a nested object, we would like a function that you pass in the object and a key and get back the value.

**Example Inputs:**
```
object = {“a”:{“b”:{“c”:”d”}}}
key = a/b/c
object = {“x”:{“y”:{“z”:”a”}}}
key = x/y/z
value = a
```

**Solution to above challenge is as below:**

We are using JS editor to validate the output.

**Pre-requisite to run this script in Linux Instance**

```
curl -sL https://rpm.nodesource.com/setup_14.x | bash -
yum -y install nodejs
node object.js
```
Reference link: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/entries