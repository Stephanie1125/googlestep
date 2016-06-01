

// First week's practice for Google STEP:
// Given 16 letters and try to find all words which len(word) > 8 that output from 16 letters.
// Set the length limit in order to decrease the number of output
//
// Example:
// Input: aehmnooqqrrstzzz
// Output:
// astronomer
// hoarstone
// anorthose
// resonator


#include <iostream>
#include <map>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
using namespace std;
map<char,int> count(string s);


vector<string> create_lst(string path){
    vector<string> dict;
    string word;
    ifstream file(path);
    if (file.is_open()){
        while (getline(file,word)){
            dict.push_back(word);
        }
    }
    return dict;
}


map<char,int> count(string s){
    map<char, int> d;
    for (int i = 0; i < s.size(); i++) {
        if(d.count(s[i]) == 0){
            d[s[i]] = 1;
        }
        else d[s[i]]++;
    }
    return d;
}


bool valid(string input, string word){
    map<char, int> input_dict = count(input);
    map<char, int> word_dict = count(word);
    for(map<char, int>::iterator iter = word_dict.begin(); iter != word_dict.end();iter++){
        if (!input_dict.count(iter->first)) {
            return 0;
        }
        if (word_dict[iter->first] > input_dict[iter->first]) {
            return 0;
        }
    }
    return true;
}


int main() {
    vector<string>dict = create_lst("/usr/share/dict/words");
    string input;
    cout <<"please input: ";
    cin >> input;
    for (vector<string>::iterator iter=dict.begin(); iter != dict.end(); iter++) {
        if (valid(input, *iter)) {
            if ((*iter).length() > 8) {
                cout << (*iter) <<endl;
            }
        }
    }
}
