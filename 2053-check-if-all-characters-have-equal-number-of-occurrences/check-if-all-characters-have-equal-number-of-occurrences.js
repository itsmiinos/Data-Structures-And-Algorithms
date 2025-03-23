/**
 * @param {string} s
 * @return {boolean}
 */
var areOccurrencesEqual = function(s) {
    let map = new Map();
    const arr = s.split('');
    for(let i=0; i<arr.length ; i++){
        map.set(arr[i] , map.get(arr[i])+1 || 1);
    }
    let occurrence = map.get(arr[0]);
    for(let [key , value] of map){
        if(value!==occurrence){
            return false;
        }
    }
    return true;
};