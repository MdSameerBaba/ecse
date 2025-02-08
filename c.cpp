#include <bits/stdc++.h>
using namespace std;
void p(const vector<int>&a,int o,int n){
    if(o==n)
        return;
    p(a,o++,n);
    cout<<a[o]<<" ";
}

int main() { 
    int n;
    cin>> n;
    vector<int> a(n);
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    p(a,0,n);
    return 0;
}