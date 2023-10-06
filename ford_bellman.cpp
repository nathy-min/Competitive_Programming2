#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n, m;
    cin >> n >> m;
    vector<int> dist(n, 30000);
    dist[0] = 0;
    vector<vector<int>> edges(m, vector<int>(3));

    for(int i = 0; i < m; i++) {
        cin >> edges[i][0] >> edges[i][1] >> edges[i][2];
        edges[i][0]--; // decrement to make it zero-indexed
        edges[i][1]--; // decrement to make it zero-indexed
    }

    for(int i = 0; i < n; i++) {
        for(auto& edge : edges) {
            int a = edge[0], b = edge[1], c = edge[2];
            if(dist[a] != 30000 && dist[a] + c < dist[b]) {
                dist[b] = dist[a] + c;
            }
        }
    }

    for(int i = 0; i < n; i++) {
        cout << dist[i] << " ";
    }

    return 0;
}
