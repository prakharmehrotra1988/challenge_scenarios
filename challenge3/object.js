let objects = {
    a: {
            b: {
                    c: 'd',
            },
    },
    x: {
            y:
     {
       z: 'a'
     },
    },
};


function getObjectKeys(object, key) {
    const keys = key.split('/');
    let objects = object;
    for (let i of keys) {
            for (let [objKey, value] of Object.entries(objects)) {
                    if (!keys.includes(objKey)) {
                            continue;
                    }
                    objects = value;
            }
    }
    return objects;
}

console.log(getObjectKeys(objects, 'a/b/c'));

console.log(getObjectKeys(objects, 'x/y/z'));