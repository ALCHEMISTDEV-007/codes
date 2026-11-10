
%{
#include<stdio.h>
#include<stdlib.h>
int COMMENT=0;
%}

identifier [a-zA-Z][a-zA-Z0-9]*

%%
"#" {
    printf("\n%s is a preprocessor directive", yytext);
}

int|float|char|double|while|for|struct|typedef|do|if|break|continue|void|switch|return|else|goto {
    printf("\n\t%s is a keyword", yytext);
}

"/*"([^*]|\n)*"*/" {
    printf("\n\t%s is a COMMENT", yytext);
    COMMENT=1;
}

{identifier}"(" {
    printf("\nFUNCTION \n\t%s", yytext);
}

"{" {
    printf("\n BLOCK BEGINS");
}

"}" {
    printf("BLOCK ENDS ");
}

{identifier}(\[[0-9]*\])? {
    printf("\n %s IDENTIFIER", yytext);
}

\".*\" {
    printf("\n\t %s is a literal", yytext);
}

[0-9]+ {
    printf("\n %s is a NUMBER ", yytext);
}

"=" {
    printf("\n\t %s is an ASSIGNMENT OPERATOR", yytext);
}

"<="|">="|"<"|"=="|"!="|">" {
    if(!COMMENT)
        printf("\n\t%s is a RELATIONAL OPERATOR", yytext);
}

%%
int main(int argc, char **argv)
{
    FILE *file;
    file = fopen("input.c", "r");

    if(!file)
    {
        printf("could not open the file");
        exit(0);
    }

    yyin = file;
    yylex();
    printf("\n");
    return 0;
}

int yywrap()
{
    return 1;
}

//output

flex lex.l
gcc lex.yy.c -lfl -o lexer
./lexer






//INPUT File

#include<stdio.h>
void main()
{
    int a,b,c;
    a=1;
    b=2;
    c=a+b;
    printf("Sum:%d",c);
}
