#include <iostream>
#include <vector>
#include <climits>


void merge(vector<int>::iterator left, vector<int>::iterator mid, vector<int>::iterator right){
	vector<int> l(left,mid), r(mid,right);
	l.insert(l.end(),INT_MAX);
	r.insert(r.end(),INT_MAX);
	vector<int>::iterator l_ptr = l.begin(), r_ptr = r.begin();

	for (auto i=left; i!=right; ++i){
		if (*l_ptr<=*r_ptr){
			*i = *l_ptr;
			++l_ptr;
		}
		else{
			*i = *r_ptr;
			++r_ptr;
		}
	}

}

void mergeSort(vector<int>::iterator left, vector<int>::iterator right){
	if (left>=right-1) return;

	vector<int>::iterator mid = left + distance(left, right)/2;

	mergeSort(left, mid);
	mergeSort(mid, right);

	merge(left, mid, right);
}

int main(){
	vector<int> a{3,2,4,1,7,6,5};
	mergeSort(a.begin(),a.end());
	for (auto i:a){
		cout<<a<<' ';
	}
	return 0;
}