/**
 * @param {number[]} flowerbed
 * @param {number} n
 * @return {boolean}
 */
var canPlaceFlowers = function(flowerbed, n) {
    var gap_size = 0;
    for(i=0;i<flowerbed.length;i++){
        if(flowerbed[i]==0 && (flowerbed[i-1]==0 || i==0)  && (flowerbed[i+1]==0 || flowerbed[i+1]==undefined)){
            flowerbed[i]=1
            gap_size++
        }
    }
    return gap_size>=n
};
var flowerbed = [1,0,0,0,1,0,0]
var n= 2
console.log(canPlaceFlowers(flowerbed,n))
