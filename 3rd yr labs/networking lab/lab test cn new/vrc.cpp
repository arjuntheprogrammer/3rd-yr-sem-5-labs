#include<bits/stdc++.h>
using namespace std;
int main()
{
	string str,str1="";
	int i,arr[26]={0};
	cin>>str;
	for(i=0;i<str.length();i++)
	{
		arr[str[i]-'0']++;
	}
	cout<<"1: for even"<<endl<<"2: for odd"<<endl;
	int ma;
	cin>>ma;
	if(ma==1){
	if(arr[1]%2!=0)
		str1+='1';
	else
		str1+='0';
	}
	else
	{
		if(arr[1]%2==0)
		str1+='1';
		else
		str1+='0';	
	}
	cout<<str+str1;
}