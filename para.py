
%{
#include<stdio.h>
int cnt1=0,cnt2=0,cnt3=0;
%}
%%
[(] {cnt1++;}
[)] {cnt1--;}
[\[] {cnt2++;}
[\]] {cnt2--;}
[{] {cnt3++;}
[}] {cnt3--;}
[a-z] {}
[A-Z] {}
[0-9] {}
[+,*,-/] {}
. {}
[\n] {
    if(!cnt1 && !cnt2 && !cnt3)
        printf("Paranthesis matching\n");
    else
        printf("paranthesis not matching\n");
    cnt1=0;cnt2=0;cnt3=0;
}
%%
main(int argc, char *argv[])
{
    yyin=fopen(argv[1],"r");
    yylex();
}

//output:
flex para.l
gcc lex.yy.c -lfl
./a.out exp.txt