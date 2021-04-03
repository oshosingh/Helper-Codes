#include <iostream>
#include <algorithm>
#include <vector>

#define FAST_IO ios_base::sync_with_stdio(false), cin.tie(nullptr)
using namespace std;
const int INF = 1e9 + 5;

signed main() {
    FAST_IO;

    int n, k;
    cin >> n >> k;
    vector<int> stones(n);
    for (int i = 0; i < n; i++) cin >> stones[i];

    vector<int> dp(n, INF); // dp[i] : Minimum cost to reach stone i.
    dp[0] = 0; // Base case, we start on the first stone so cost to reach it is 0.

    for (int i = 0; i < n; i++) { // i represents the stone the frog is currently at.
        for (int j = i + 1; j <= i + k; j++) { // j represents a potential stone for the frog to jump to.
            if (j < n)
                // Storing the total minimum cost to reach stone j from stone i.
                dp[j] = min(dp[j], dp[i] + abs(stones[j] - stones[i]));
        }
    }
    cout << dp[n - 1];
    return 0;
}