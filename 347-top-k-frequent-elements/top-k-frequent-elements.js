/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var topKFrequent = function(nums, k) {
    const map = new Map();
    for(let i = 0; i < nums.length; i++) {
        if (map.has(nums[i]))
            map.set(nums[i], map.get(nums[i]) + 1);
        else
            map.set(nums[i], 1);
    }

    const helper = []
    for(const [key, value] of map) {
        helper.push([key, value])
    }

    helper.sort( (first, second) => { return second[1] - first[1]; });
    ans = [];
    for(let i in helper) {
        ans.push(helper[i][0]);
        if (ans.length === k)
            break;
    }
    return ans;
};