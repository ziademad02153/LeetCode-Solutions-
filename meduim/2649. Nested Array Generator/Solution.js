/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function*(arr) {
    const stack = [arr];

    while (stack.length > 0) {
        const current = stack.pop();

        if (typeof current === 'number') {
            yield current;
        } else {
            for (let i = current.length - 1; i >= 0; i--) {
                stack.push(current[i]);
            }
        }
    }
};