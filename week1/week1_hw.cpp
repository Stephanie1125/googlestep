

//  First week's homework for Google STEP:
//  与えられてあ16文字からなるべく長い単語を出力するプログラムをつくろう！
//  Given 16 letters and try to output the longest word using 16 letters.
//
//  Example:
//  Input: aehmnooqqrrstzzz
//  Output: astronomer


#include <iostream>
#include <map>
#include <string>
#include <sstream>
#include <fstream>
#include <vector>
using namespace std;
map<char,int> count(string s);


// this c++ program is created based on the week1_hw.py
// for more detail explanation of functions, please check the week1_hw.py


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


string anagram(string input, vector<string> dict){
    string answer = "";
    for (vector<string>::iterator iter=dict.begin(); iter != dict.end(); iter++) {
        if (valid(input, *iter)) {
            if (answer.length() < (*iter).length()) {
                answer = *iter;
            }
        }
    }
    return answer;
}


int main() {
    vector<string>dict = create_lst("/usr/share/dict/words");
    string input;
    cout <<"please input: ";
    cin >> input;
    cout <<"longest word: ";
    string answer = anagram(input, dict);
    cout << answer<<endl;
}
