/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    let i = 0;
    let j = s.length;

    while (i < j) {
        let code = s.charCodeAt(i);
        let codej = s.charCodeAt(j);
        if (! ((code >= 65 && code <= 90) || (code >= 97 && code <= 122) || (code >= 48 && code <= 57)) ) {
            i++;
            continue;
        }

        if (! ((codej >= 65 && codej <= 90) || (codej >= 97 && codej <= 122) || (codej >= 48 && codej<= 57)) ) {
            j--;
            continue;
        }

        if (s[i].toLowerCase() !== s[j].toLowerCase())
            return false;
        i++;
        j--;
    }
    return true;
};