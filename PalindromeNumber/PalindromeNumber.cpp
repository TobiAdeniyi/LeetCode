\\ Non String
class Solution {
public:
    bool isPalindrome(int x) {
        if (x < 0 || x >= pow(2,31) - 1)
            return false;
        else if (x == 0)
            return true;
        
        int length = log10(x);
        int tens = length;
        int y = 0;
        int power = 0;
      
        while (power <= length)
        {
            int divisor = pow(10,power);
            y = y + (((x/divisor) % 10) * pow(10, tens));
            --tens;
            ++power;
        }
            
       
        if (y==x)
            return true;
        
        return false;
    }
};
