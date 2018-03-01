#include <stdio.h>
int cell[4] = {1,0,1,1};
int cell_new[4];
int K=3;
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
    for(int j=0; j<K;j++){
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
    }
}
   

    
    

