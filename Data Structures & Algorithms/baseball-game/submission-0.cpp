class Solution {
public:
    int calPoints(vector<string>& operations) {
        vector<int> records;
        for (string s : operations) {
            if (s == "+") {
                records.push_back(records.back() + records[records.size() - 2]);
            } else if (s == "C" ) {
                records.pop_back();
            } else if (s == "D" ) {
                records.push_back(records.back() * 2);
            } else {
                records.push_back(stoi(s));
            }
        }

        return accumulate(records.begin(), records.end(), 0);
    }
};