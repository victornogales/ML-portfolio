#include <fstream> 
#include <iostream> 
#include <string> 
#include <vector>

using namespace std; 

//
//    ENCODED_MSG CLASS
//  
class Encoded_msg {
    private:
        ifstream* inputFile;
        vector<string> lines;
    public:
        Encoded_msg();
        ~Encoded_msg();
        int open_file();
        int decode(string aFileName);
};

Encoded_msg::Encoded_msg() {
}

Encoded_msg::~Encoded_msg() {
    if (inputFile->is_open()) { 
        inputFile->close();  
    } 
}

//
//    THIS IS THE ASKED FUNCTION
//
int Encoded_msg::decode(string aFileName){

    // Some local variables
    string line;
    int linePos = 0;
    int vectorSize = 0;
    int vectorIndex = 0;
    int piramidLine = 0;
  
    // Open input file and check if it was successfully opened 
    inputFile = new ifstream(aFileName); 
    if (!inputFile->is_open()) { 
        cerr << "Error opening the file!" << endl; 
        return 1; 
    } 

    // Loop over all ines in file
    while (getline(*inputFile, line)) { 
        // Extract the number from the line
        linePos = line.find_first_of(' ');
        vectorIndex = stoi(line.substr(0,linePos))-1;

        // Resizing vector as needed
        if (vectorIndex > vectorSize) {
            lines.resize(vectorIndex+1);
            vectorSize = vectorIndex+1;
        }

        // Extract word from the line and storing in the "number" vector position
        lines[vectorIndex] = line.substr(linePos+1,line.find_last_not_of("\r\n")-linePos);
    }  

    // Loop through the right ends of each pyramid line, 
    // sending the corresponding vector item to cout
    vectorIndex = 0;
    piramidLine = 1;    
    do {
        cout << lines[vectorIndex] << " ";
        vectorIndex += piramidLine+1;
        piramidLine += 1;
    } while (vectorIndex <= vectorSize);
    cout << endl;

    return 0;
}

//
//    MAIN
//

int main() 
{ 
    
    string msg_file;
    Encoded_msg anEcoded_msg;
    
    // Get the message file name. It assumes the current folder.
    cout << "Enter message file name: ";
    getline(cin,msg_file);
  
    if(anEcoded_msg.decode(msg_file)) {
        return 0;
    }

return 0; 
}