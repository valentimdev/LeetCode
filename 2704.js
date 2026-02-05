/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    let value = val;
  const methods = {
    toBe: function(val) {
        if(val===value){
            return true
        }else{
            throw new Error("Not Equal")
        }
    },
    notToBe: function(val) {
        if(val!==value){
            return true
        }else{
            throw new Error("Equal")
        }

    },
  };

  return methods;
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */