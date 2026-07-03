class Solution {
public:
    bool can(int x,
             vector<vector<pair<int, int>>>& adj,
             vector<int>& topo,
             vector<bool>& online,
             int n,
             long long k) {

        const long long INF = 1e18;
        vector<long long> dp(n, INF);
        dp[0] = 0;

        for (int u : topo) {
            if (dp[u] == INF) continue;

            for (auto [v, w] : adj[u]) {
                // Edge cost must be at least x
                if (w < x) continue;

                // Intermediate nodes must be online
                if (v != n - 1 && !online[v]) continue;

                dp[v] = min(dp[v], dp[u] + w);
            }
        }

        return dp[n - 1] <= k;
    }

    int findMaxPathScore(vector<vector<int>>& edges,
                         vector<bool>& online,
                         long long k) {
        int n = online.size();

        vector<vector<pair<int, int>>> adj(n);
        vector<int> indeg(n, 0);

        int hi = 0;

        for (auto& e : edges) {
            int u = e[0];
            int v = e[1];
            int w = e[2];

            adj[u].push_back({v, w});
            indeg[v]++;
            hi = max(hi, w);
        }

        // Topological sort
        queue<int> q;
        for (int i = 0; i < n; i++) {
            if (indeg[i] == 0)
                q.push(i);
        }

        vector<int> topo;

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            topo.push_back(u);

            for (auto [v, w] : adj[u]) {
                if (--indeg[v] == 0)
                    q.push(v);
            }
        }

        int lo = 0, ans = -1;

        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;

            if (can(mid, adj, topo, online, n, k)) {
                ans = mid;
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }

        return ans;
    }
};