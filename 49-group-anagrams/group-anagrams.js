/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const ansMap = new Map();

    for(let i = 0; i < strs.length; i++) {
        let str_sorted = strs[i].split('').sort().join('');
        if (ansMap.has(str_sorted)) {
            ansMap.get(str_sorted).push(strs[i]);
        } else {
            ansMap.set(str_sorted, [strs[i]]);
        }
    } 

    const ans = [];
    for (const [key, value] of ansMap) {
        ans.push(value);
    }
    return ans;
};