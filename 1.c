# Dinesh.typeface
#include <stdio.h>
#include <math.h>
int main(){
  int d;
  scanf("%d",&d);
  int u=0;
  int l=0;
  while(d>0){
    int m=d%3;
    int j=pow(10,l);
    u=u+(m*j);
    d=d/3;
    l=l+1;
  }
  printf("%d",u);
         }
