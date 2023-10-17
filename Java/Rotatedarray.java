public void Rotatedarray(int[] nums, int k) {
    k = k % nums.length;
    int[] copy = nums.clone();
    
    for (int i = 0; i < nums.length; i++) {
        nums[(i + k) % nums.length] = copy[i];
    }
}