/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const returnObject = {}
    for(let i = 0;i<this.length;i++){
        const key = fn(this[i])
        if(!returnObject[key]){
            returnObject[key]=[]
        }
        returnObject[key].push(this[i])
        
    }
    return returnObject
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
