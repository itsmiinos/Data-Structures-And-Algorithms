/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    let sum = 0
    for(let i = 1; i< s.length ; i++){
        sum = sum + Math.abs(s[i-1].charCodeAt() - s[i].charCodeAt())
    } 
    return sum
};