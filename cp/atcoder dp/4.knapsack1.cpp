// LINK to the problem: https://atcoder.jp/contests/dp/tasks/dp_d

#include <bits/stdc++.h>
using namespace std;

#define endl '\n'
using lli = long long;

int N, W;
vector<lli> w, p;

lli dp[101][100100];

lli rec(int i, int wleft){
	if(wleft<0){
		return -1e18;
	}
	if(i==N){
		return 0LL;
	}
	if(dp[i][wleft]!=-1){
		return dp[i][wleft];
	}
	lli ans= max(rec(i+1,wleft),rec(i+1,wleft-w[i])+p[i]);
	return dp[i][wleft]= ans;
}

void solve(){
	cin>>N>>W;
	w.resize(N);
	p.resize(N);
	for(int i=0;i<N;i++){
		cin>>w[i]>>p[i];
	}
	memset(dp,-1,sizeof(dp));
	cout<<rec(0,W)<<endl;
}

signed main() {

	ios::sync_with_stdio(0); 
	cin.tie(0); cout.tie(0);


	//int _t; cin>>_t; while(_t--)
	solve();
	
}