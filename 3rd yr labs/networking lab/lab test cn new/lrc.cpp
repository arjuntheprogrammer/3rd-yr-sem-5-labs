#include<bits/stdc++.h>
using namespace std;
int main()
{
	string str,str1,str2,str3,str4,str5,str6,str7;
	int i,cnt=0;
	cin>>str;
	cin>>str1;
	cin>>str2;
	cin>>str3;
	if(str.length()!=8){
	for(i=0;i<8-str.length();i++)
	str4+='0';}
	str4=str4+str;
	
	if(str1.length()!=8){
	for(i=0;i<8-str1.length();i++)
	str5+='0';}
	str5=str5+str1;
	
	if(str2.length()!=8){
	for(i=0;i<8-str2.length();i++)
	str6+='0';}
	str6=str6+str2;
	
	if(str3.length()!=8){
	for(i=0;i<8-str3.length();i++)
	str7+='0';}
	str7=str7+str3;
	
	int ma;
	cout<<"1: for even"<<endl<<"2:for odd"<<endl;
	cin>>ma;
	for(i=0;i<8;i++)
	{
			if(str4[i]=='1')
			cnt++;
			if(str5[i]=='1')
			cnt++;
			if(str6[i]=='1')
			cnt++;
			if(str7[i]=='1')
			cnt++;
	//	cout<<i<<" "<<cnt<<endl;
		if(ma==1)
		{
			if(cnt%2!=0){
			cout<<1;
			cnt=0;
			}
			else
			{
				cout<<0;
				cnt=0;
			}
		}
		else
		{
			if(cnt%2==0){
			cout<<0;
			cnt=0;
			}
			else
			{
				cout<<1;
				cnt=0;
			}
		}
	}
}
