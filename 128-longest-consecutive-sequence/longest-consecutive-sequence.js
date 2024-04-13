/**
 * @param {number[]} nums
 * @return {number}
 */
var longestConsecutive = function(nums) {
    const set = new Set(nums);

    ans = 0;
    for (let val of set) {
        if (!set.has(val - 1)) {
            let cnt = 0;
            let num = val + 1;
            while (set.has(num)) {
                cnt++;
                num++;
            }
            ans = Math.max(ans, cnt + 1);
        }
    }

    return ans;
};