/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let left = 0;
    let right = numbers.length - 1;

    while (left < right) {
        let num = numbers[left] + numbers[right];

        if (num == target)
            return [left + 1, right + 1];
        
        if (num < target) {
            left += 1;
        } else {
            right -= 1;
        }
    }
};