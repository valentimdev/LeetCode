var createCounter = function(n) {
    let number=n
        return function() {
        number=n
        n++
        return number
    };
};

