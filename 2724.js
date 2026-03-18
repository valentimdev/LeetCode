/**
 * @param {Array} arr
 * @param {Function} fn
 * @return {Array}
 */
var sortBy = function(arr, fn) {
    const ascend = (a, b) => fn(a) - fn(b)
    return arr.sort(ascend)
};
