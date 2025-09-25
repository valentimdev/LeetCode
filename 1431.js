/**
 * @param {number[]} candies
 * @param {number} extraCandies
 * @return {boolean[]}
 */
var kidsWithCandies = function (candies, extraCandies) {
  var biggest = Math.max(...candies);
  var final_return = [];
  for (i = 0; i < candies.length; i++) {
    if (candies[i] + extraCandies >= biggest) {
      final_return.push(true);
    } else {
      final_return.push(false);
    }
  }
  return final_return;
};
candies = [2, 3, 5, 1, 3];
extraCandies = 3;
kidsWithCandies(candies, extraCandies);
