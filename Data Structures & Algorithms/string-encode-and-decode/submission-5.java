

class Solution {

    public String encode(List<String> strs) {
        StringBuilder newstr = new StringBuilder();
        for (String s : strs) {
            int l = s.length();
            newstr.append(String.valueOf(l));
            newstr.append("#");
            newstr.append(s);
        }
        return newstr.toString();
    }

    public List<String> decode(String str) {
        int n = str.length();
        int i = 0;
        List<String> res = new ArrayList<>();
        while (i < n) {
            int j = i;
            while (str.charAt(j) != '#') {
                j++;
            }
            String length = str.substring(i, j);
            int l = Integer.parseInt(length);
            res.add(str.substring(j + 1, l + j + 1));
            i = l + j + 1;
        }
        return res;
    }
}
