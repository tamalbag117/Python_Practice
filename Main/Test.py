print('''
      #include<stdio.h>
int main(){
   int tom[2][3];
   int i, j;
   for(i=0; i<2; i++) {
      for(j=0;j<3;j++) {
         printf("Enter value for tom[%d][%d]:", i, j);
         scanf("%d", &tom[i][j]);
      }
   }
   printf("Two Dimensional array elements:\n");
   for(i=0; i<2; i++) {
      for(j=0;j<3;j++) {
         printf("%d ", tom[i][j]);
            printf("\t");
         }
         printf("\n");
   } 
     int rangu[2][3];
   for(i=0; i<2; i++) {
      for(j=0;j<3;j++) {
         printf("Enter value for rangu[%d][%d]:", i, j);
         scanf("%d", &rangu[i][j]);
      }
   }
   printf("Two Dimensional array elements:\n");
   for(i=0; i<2; i++) {
      for(j=0;j<3;j++) {
         printf("%d ", rangu[i][j]);
         }     
      }
    int sum[2][3];
     for(i=0; i<2; i++) {
      for(j=0;j<3;j++) {
          sum[i][j]=tom[i][j]+rangu[i][j];
      }
    printf("The Sum of the elements:\n");
    for(i=0; i<2; i++) {
      for(j=0;j<3;j++) {
          printf("%d",sum[i][j]);
    }
    printf("\n");
    }
   return 0;
}''')
