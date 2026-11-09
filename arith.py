//lex part 

%{
#include "y.tab.h"
%}
%%
[0-9]+ {return NUMBER;}
[a-zA-Z][a-zA-Z0-9]* {return ID;}
\n {return 0;}
. {return yytext[0];}
%%


//yacc part 


%{
#include<stdio.h>
#include<stdlib.h>
int yylex();
%}
%token NUMBER ID
%left '+' '-'
%left '*' '/'
%%
exp: exp'+'exp
| exp'-'exp
| exp'*'exp
| exp'/'exp
| '('exp')'
| NUMBER
| ID;
%%
int main(int argc,char *argv[])
{
printf("Enter the expression: ");
yyparse();
printf("\nValid Expression");
return 0;
}
int yyerror()
{
printf("\nInvalid Expression");
exit(1);
}
int yywrap()
{
return 1;
}

//output
gedit part.l
gedit part.y
yacc -d part.y
flex part.l
gcc lex.yy.c y.tab.c -ll -o part