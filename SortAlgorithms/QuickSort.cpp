#include <iostream>
#include <vector>
#include <climits>


void quickSort(vector<int>::iterator left, vector<int>::iterator right){
	if (left>=right) return;
	vector<int>::iterator l=left, r=right-1;
	
	while(true){
		while (*l<=*right and l<right) l++;
		while (*r>=*right and r>l) r--;
		if (l>=r) break;
		swap(*l,*r);
	}
	swap(*l,*right);
	quickSort(left, l-1);
	quickSort(l+1, right);
}

int main(){
	vector<int> a{3,2,4,1,7,6,5};
	quickSort(a.begin(),a.end()-1);
	for (auto i:a){
		cout<<a<<' ';
	}
	return 0;
}