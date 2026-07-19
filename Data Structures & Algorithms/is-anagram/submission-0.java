class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length()!=t.length()){
            return false;
        }
        HashMap<Character,Integer> Occurencies_s = new HashMap<>();
        HashMap<Character,Integer> Occurencies_t = new HashMap<>();
        for (char c : s.toCharArray()){
            int Current_Ocurrence = Occurencies_s.getOrDefault(c,0);
            Occurencies_s.put(c,Current_Ocurrence+1);

        }
        for (char c : t.toCharArray()){
            int Current_Ocurrence = Occurencies_t.getOrDefault(c,0);
            Occurencies_t.put(c,Current_Ocurrence+1);
        }
        for (Map.Entry<Character,Integer> entry : Occurencies_s.entrySet() ){
            char c = entry.getKey();
            if (Occurencies_t.getOrDefault(c,0)!=entry.getValue()){
                return false;
            }
        }
        return true;
    }
}
