print('''#include <stdio.h>
int main() {
   int rows, coef = 1, space, i, j;
   printf("Enter the number of rows: ");
   scanf("%d", &rows);
   for (i = 0; i < rows; i++) {
      for (space = 1; space <= rows - i; space++)
         printf("  ");
      for (j = 0; j <= i; j++) {
         if (j == 0 || i == 0)
            coef = 1;
         else
            coef = coef * (i - j + 1) / j;
         printf("%4d", coef);
      }
      printf("\n");
   }
   return 0;
}''')
print("\n\n\n")
print('''1 2 3 4 5 
 2 3 4 5 
  3 4 5 
   4 5 
    5 
   4 5 
  3 4 5 
 2 3 4 5 
1 2 3 4 5''')
print('''                   
                            だから、
                     今日私はあなたに提示ゲーム　
                         ボードの様々 
　          なサイズを再生するツイストをオセロのゲーム，
　完全にプレイヤーする必要があります彼の利点を取得したい場合のアプローチを変更します
''')
# from playground import playground
# playground('C:\\Users\\tamal\\Downloads')
