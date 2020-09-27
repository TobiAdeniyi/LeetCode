package LengthOfLastWord;

class LengthOfLastWord {
    public int lengthOfLastWord(String s) {
        int cnt = 0;
        new StringBuilder(s).reverse().toString();
        char[] S = s.toCharArray();
        for (char i : S) {
            if (Character.isWhitespace(i) || cnt != 0) {
                break;
            }
            cnt ++;
        }
        return cnt;
    }
}