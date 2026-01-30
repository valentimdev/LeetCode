/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    const cache = {};        
    return function(...args) {

        const check = JSON.stringify(args)
        if(check in cache){
            return cache[check]
        }
        cache[check]=fn(...args)
        return cache[check]
    }
}
