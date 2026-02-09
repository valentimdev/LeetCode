/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const retorno = [];
    for(let i=0;i<arr.length;i++){
        retorno.push(fn(arr[i],i))
    }
    return retorno
};
