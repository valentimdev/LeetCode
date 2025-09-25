/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    var broken_world = x.toString().split("").reverse()
    var final = broken_world.join("")
    return final == x;
};
var teste = 121
console.log(isPalindrome(teste))