#include <stdio.h>

int main(){
    struct 
    {
        char text[5];
        short int code;
    }local;
    local.code = 0;
    gets(local.text);
    
    if(local.code == 97){
        puts("buffer overflow");
    }
    else{
        puts("no buffer overflow");
    }

}