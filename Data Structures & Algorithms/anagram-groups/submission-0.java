class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<>();
        Map<String, Integer> sortedIndexMap = new HashMap<>();

        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sortedS = new String(chars);

            int index = sortedIndexMap.getOrDefault(sortedS, -1);
            if (index != -1) {
                res.get(index).add(s);
            } else {
                List<String> newList = new ArrayList<>();
                newList.add(s);
                res.add(newList);
                sortedIndexMap.put(sortedS, res.size() - 1);
            }
        }

        return res;
    }
}



