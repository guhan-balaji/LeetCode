/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    if (prices.length === 0) {
        return 0;
    }

    let min = prices[0];
    let profit = 0;

    for (price of prices) {
        if (price < min) {
            min = price;
        } else if (profit < price - min) {
            profit = price - min;
        }
    }
    
    return profit;
};
