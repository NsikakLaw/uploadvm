#include <bits/stdc++.h>
#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <linux/random.h>
#include <errno.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string>

#define MAX 10
using namespace std;

#include <sstream>

template <typename T>
	std::string NumberToString ( T Number )
	{
	 std::ostringstream ss;
	 ss << Number;
	 return ss.str();
	}

vector<string> streets_vec;
map<string, vector<pair<pair<int,int>, pair<int,int> > > > street_line_seg;
set<pair<pair<int,int>, pair<int,int> > > line_seg;

int urandom_fd;
int rand_int()
{
	int num;
	read(urandom_fd, &num, sizeof(int));
	return abs(num);
}

int noofstreets = 10, noofsegments = 5, seconds = 5, coordinates = 20, A=0;

void generate_street(string &street, int len)
{
	int i = 0,num;
	char ch;
	num = rand_int()%52;
	if(num <= 25)
		ch = (char)('A'+ num);
	else
		ch = (char)('a'+ num-26);
	street +=  ch;
	while(i<len)
	{
		num = rand_int()%53;
		if(num <= 25)
			ch = (char)('A'+ num);
		else if(num<=51)
			ch = (char)('a'+ num-26);
		else
			ch = ' ';
		street +=  ch;
		i++;
	}
}

void generate_pair(int &a, int &b)
{
	a = rand_int()%(2*coordinates+1);
	a = a - coordinates;
	b = rand_int()%(2*coordinates+1);
	b = b - coordinates;
	return ;
}

void insert_pair(string &command, int a, int b)
{
	command += ' ';
	command += '(';
	command += NumberToString(a);
	//command += to_string(a);
	command += ',' ;
	command += NumberToString(b);
	//command += to_string(b);
	command += ')';
}

void generate_a_command(string &command)
{
	command += 'a';
	command += ' ';
	command += '"';
	string street = "";
	int len = rand_int()%(MAX-1);
	len = len + 1;
	generate_street(street,len);
	command += street;
	streets_vec.push_back(street);
	command += '"';
	int points = rand_int()%noofsegments , preva, prevb;
	points++;
	generate_pair(preva,prevb);
	insert_pair(command,preva,prevb);
	int j = 1;
	int a,b;
	while(j++ <= points)
	{
		generate_pair(a,b);
		insert_pair(command,a,b);

		if(line_seg.find(make_pair(make_pair(preva,prevb), make_pair(a,b))) == line_seg.end())
		{
			line_seg.insert(make_pair(make_pair(preva,prevb), make_pair(a,b)));
			street_line_seg[street].push_back(make_pair(make_pair(preva,prevb), make_pair(a,b)));
			preva = a;
			prevb= b;
			A = 0;
		}
		else
		{
			A++;
			j--;
			if(A==25)
			{
				cout<<"error too many attempts taken by random function"<<endl;
				exit(0);
			}
		}
	}
	return ;
}

void generate_r_command(string &command)
{
	int size = streets_vec.size();
	int street_no = rand_int()%size;
	command += 'r';
	command += ' ';
	command += '"';
	int i = 3, j = 0;
	command += streets_vec[street_no];
	command += '"';
	string street = streets_vec[street_no];
	int size_line_seg = street_line_seg[street].size();
	// removing line segments present due to these street initially
	for(int s=0; s<size_line_seg; s++)
		line_seg.erase(street_line_seg[street][s]);

	street_line_seg.erase(street);
	streets_vec.erase(streets_vec.begin()+street_no);
	return ;
}

int main(int argc, char* argv[])
{
	int i=1, A=25;
	urandom_fd = open("/dev/urandom",O_RDONLY);
	while(i < argc)
	{
		if(strcmp(argv[i],"-s") == 0)
		{
			i++;
			sscanf(argv[i],"%d",&noofstreets);
			i++;
		}
		else if(strcmp(argv[i],"-n") == 0)
		{
			i++;
			sscanf(argv[i],"%d",&noofsegments);
			i++;
		}
		else if(strcmp(argv[i],"-l") == 0)
		{
			i++;
			sscanf(argv[i],"%d",&seconds);
			i++;
		}
		else
		{
			i++;
			sscanf(argv[i],"%d",&coordinates);
			i++;
		}
	}

	ofstream myfile;
	while(1)
	{


		while(streets_vec.size() != 0)
		{
			command = "";
			generate_r_command(command);
			cout<<command<<endl;
		}

		command = "g";
		cout<<command;

		int total,noofa = 0;
		total = rand_int()%(noofstreets-2);
		total += 2;
		while(noofa < total)
		{
			noofa++;
			command = "";
			generate_a_command(command);
			myfile<<command<<endl;
		}
		command = "g";
		myfile<<command<<endl;
		command = "q";
		myfile<<command<<endl;
		myfile.close();
		sleep(seconds);
	}

	return 0;
}
