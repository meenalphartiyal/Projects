#include<iostream>
#include<bits/stdc++.h>
using namespace std;
/*
       |       |       
 (0,0) | (0,1) | (0,2) 
-------|-------|-------
 (1,0) | (1,1) | (1,2)
-------|-------|-------
 (2,0) | (2,1) | (2,2)
       |       | 
 
 win: {(00,01,02),(10,11,12),(20,21,22),(00,10,20),(01,11,21),(02,12,22),(00,11,22),(02,11,20)}
 */
 
void intro(){
	cout<<"\n\t       TicTacToe Game"<<endl<<endl;
}

void game(char a[][3]){
	system("cls");
	cout<<"\n\t       TicTacToe Game"<<endl<<endl;
	cout<<"\n\n\t\t "<<a[0][0]<<" | "<<a[0][1]<<" | "<<a[0][2]<<" "<<endl;
	cout<<"\t\t---|---|---"<<endl;
	cout<<"\t\t "<<a[1][0]<<" | "<<a[1][1]<<" | "<<a[1][2]<<" "<<endl;
	cout<<"\t\t---|---|---"<<endl;
	cout<<"\t\t "<<a[2][0]<<" | "<<a[2][1]<<" | "<<a[2][2]<<" "<<endl;
}

int player(string str[]){
	string strn;
	cout<<"\tWho playes first "<<str[1]<<" or "<<str[2]<<" ?"<<endl;
	cout<<"\t";	
	getline(cin,strn);
	if(strn==str[1])
		return 1;
	else if(strn==str[2])
		return 2;
	else{
		cout<<"\t"<<strn<<" is not a registered player."<<endl;
		player(str);
	}
}

void play(char a[][3], int p){
	int r,c;
	cout<<"\n\tChoose a row number (0 to 2): ";
	cin>>r;
	if(r>2 || r<0){
		cout<<"\n\t"<<r<<" is not a valid row."<<endl;
		play(a,p);
	}
	cout<<"\n\tChoose a column number (0 to 2): ";
	cin>>c;
	if(c>2 || c<0){
		cout<<"\n\t"<<c<<" is not a valid column."<<endl;
		play(a,p);
	}
	if(p==1 && a[r][c]!='X' && a[r][c]!='O'){
		a[r][c]='X';
	}
	else if (p==2 && a[r][c]!='X' && a[r][c]!='O'){
		a[r][c]='O';
	}
	else
		play(a,p);
}

int check(char a[][3]){
	if(a[0][0]==a[0][1] && a[0][1]==a[0][2] && a[0][0]!='.' && a[0][1]!='.' && a[0][2]!='.')
		return 1;
	else if(a[1][0]==a[1][1] && a[1][1]==a[1][2] && a[1][0]!='.' && a[1][1]!='.' && a[1][2]!='.')
		return 1;
	else if(a[2][0]==a[2][1] && a[2][1]==a[2][2] && a[2][0]!='.' && a[2][1]!='.' && a[2][2]!='.')
		return 1;
	else if(a[0][0]==a[1][0] && a[1][0]==a[2][0] && a[0][0]!='.' && a[1][0]!='.' && a[2][0]!='.')
		return 1;
	else if(a[1][1]==a[0][1] && a[0][1]==a[2][1] && a[0][1]!='.' && a[1][1]!='.' && a[2][1]!='.')
		return 1;
	else if(a[2][2]==a[1][2] && a[1][2]==a[0][2] && a[0][2]!='.' && a[1][2]!='.' && a[2][2]!='.')
		return 1;
	else if(a[0][0]==a[1][1] && a[1][1]==a[2][2] && a[0][0]!='.' && a[1][1]!='.' && a[2][2]!='.')
		return 1;
	else if(a[0][2]==a[1][1] && a[1][1]==a[2][0] && a[2][0]!='.' && a[1][1]!='.' && a[0][2]!='.')
		return 1;
	else if(a[0][0]!='.' && a[0][1]!='.' && a[0][2]!='.' && a[1][0]!='.' && a[1][1]!='.' && a[1][2]!='.' && a[2][0]!='.' && a[2][1]!='.' && a[2][2]!='.')
		return 0;
	else
		return -1;
}

int play_again(){
	char ch;
	while(ch!='Y' && ch!='N'){
		cout<<"\t\tWould you like to play again? (Y/N): ";
		cin>>ch;
		cin.ignore();
		if(toupper(ch)=='Y'||toupper(ch)=='N'){
			if(toupper(ch)=='Y')
				return 1;
			else if(toupper(ch)=='N'){
				cout<<"\t\tBye!"<<endl;
				return 0;
			}
		}
		else if(toupper(ch)!='Y'||toupper(ch)!='N')
			cout<<"\t\t"<<ch<<" is not a valid answer."<<endl;
	}
}

int main(){
	int run=1;
	while(run==1){
		system("cls");
		char a[3][3]={{'.','.','.'},{'.','.','.'},{'.','.','.'}};
		int p,i;
		string str[3];
		intro();
		cout<<"\n\tEnter a name for X player: ";
		getline(cin,str[1]);
		cout<<"\tEnter a name for O player: ";
		getline(cin,str[2]);
		p=player(str);
		do{
			game(a);
			p=(p%2)?1:2;
			cout<<"\n\tPlayer of current turn: "<<str[p];
			play(a,p);
			i=check(a);
			p++;
		}while(i== -1);
		game(a);
		cout<<"\n\t\t\aGame Over: "<<endl;
		if(i==1)
			cout<<"\t\t"<<str[--p]<<" wins!"<<endl;
		else
			cout<<"\t\tIt is a tie!"<<endl;
		run=play_again();
	}
	return 0;
}
