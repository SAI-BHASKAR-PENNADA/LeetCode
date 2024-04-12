/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length !== t.length) {
        return false;
    }

    const myMapS = new Map();
    for (let i = 0; i < s.length; i++) {
        if (myMapS.has(s[i])) {
            myMapS.set(s[i], myMapS.get(s[i]) + 1);
        } else {
            myMapS.set(s[i], 1);
        }
    }

    const myMapT = new Map();
    for (let i = 0; i < t.length; i++) {
        if (myMapT.has(t[i])) {
            myMapT.set(t[i], myMapT.get(t[i]) + 1);
        } else {
            myMapT.set(t[i], 1);
        }
    }
    // console.log(myMapS, myMapT);
    for (const [key, value] of myMapS) {
        // console.log(myMapT.get(key), value);
        if (myMapT.get(key) !== value)
            return false;
    }
    for (const [key, value] of myMapT) {
        // console.log(value, myMapS.get(key));
        if (value !== myMapS.get(key))
            return false;
    }
    return true;
};