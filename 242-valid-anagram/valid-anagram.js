/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    let myMapOne = new Map();
    let myMapTwo = new Map();
    if(s.length !== t.length)
        return false;
    for(let i = 0 ; i<s.length ; i++){
        myMapOne.set(s[i] , myMapOne.get(s[i])+1 || 1)
    }
    for(let i = 0 ; i<t.length ; i++){
        myMapTwo.set(t[i] , myMapTwo.get(t[i])+1 || 1)
    }
    for (let [key , value] of myMapOne){
        if(value!== myMapTwo.get(key)){
            return false
        }
    }
    return true;
};