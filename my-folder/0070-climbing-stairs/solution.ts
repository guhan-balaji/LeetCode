function climbStairs(n: number): number {
    let mem = [0, 1, 2];

    for (let i = 3; i <= n; i++) {
        mem[i] = mem[i - 1] + mem[i - 2];
    }

    return mem[n];
};

// function rec(n, mem) {
//     if (mem[n] === undefined) {
//         mem[n] = climbStairs(n - 1) + climbStairs(n - 2);
//     }

//     return mem[n];
// }
