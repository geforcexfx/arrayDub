#include <stdio.h>
int cell[4] = {0,1,1,0};
int cell_new[4];
int K=2;
int cell_size=4;

int left_neighbor(int index){
    
    int num; 
    num = index-1;
    if(index==0){
        num = cell_size-1;
        
    }
    return cell[num];
}

int right_neighbor(int index){
    int num;
    num = index +1;
    if(index==cell_size-1){
        num=0;
        
    }
    return cell[num];
}

int main(){
    printf("Initial cell: ");
    for(int q=0; q<cell_size;q++){
            printf("%d",cell[q]);
    }
    printf("\n");
    for(int j=0; j<K;j++){
        printf("Step %d:",j+1);
        for (int i=0; i<cell_size;i++){
            
            if(left_neighbor(i)==right_neighbor(i)){
                cell_new[i]=0;
                
            }
            else{
                cell_new[i]=1;
            }
            printf("%d", cell_new[i]);
            
        }
        printf("\n");
        
        for (int u=0;u<cell_size;u++){
        cell[u]=cell_new[u];
        }
        if(j==K-1){
            printf("output: ");
            for (int t=0; t<cell_size; t++){
                printf("%d",cell_new[t]);
            }
            printf("\n");
        }
    }
}
   

    
    

