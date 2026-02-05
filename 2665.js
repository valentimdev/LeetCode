/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    const start = init
    const methods = {
        increment: function() {
            return ++init 
        },
        reset: function() {
            init = start
            return init
        },
        decrement: function() {
            return --init 
        }
    }
    return methods;
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */