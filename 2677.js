/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    let returnArray = [];
    while(arr.length>0){
        const removed = arr.splice(0, size);
        returnArray.push(removed);
    }
    return returnArray
};
