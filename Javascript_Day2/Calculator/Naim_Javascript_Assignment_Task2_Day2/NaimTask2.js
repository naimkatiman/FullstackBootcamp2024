function maxProductOfThree(nums) {
    
    if (nums.length < 3) {
        return null;
    }

    
    let max1 = -Infinity, max2 = -Infinity, max3 = -Infinity;
    let min1 = Infinity, min2 = Infinity;

    
    for (let i = 0; i < nums.length; i++) {
        const n = nums[i];
       
        if (n > max1) {
            max3 = max2;
            max2 = max1;
            max1 = n;
        } else if (n > max2) {
            max3 = max2;
            max2 = n;
        } else if (n > max3) {
            max3 = n;
        }

       
        if (n < min1) {
            min2 = min1;
            min1 = n;
        } else if (n < min2) {
            min2 = n;
        }
    }

    
    const product1 = max1 * max2 * max3; 
    const product2 = max1 * min1 * min2; 

    
    return Math.max(product1, product2);
}
