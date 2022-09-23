class Solution {
public:
    int numberOfSteps(int num) {
        int odd_count=0;
        int even_count=0;
        while(num!=0){
            if(num%2==0){
                num= num/2;
                even_count++;
            }
            else{
                num--;
                odd_count++;
            }
        }
        return (odd_count+even_count);
    }
};
int main(){
    Solution s;
    s
}