class Missingnumber {
    public static void main(String[] args) {
        int arr[] = {1,2,3,4,5,6,7,8};

        int sum=0;
        for(int num: arr){
            sum = sum+num;
        }
        int len = arr.length;
        int nat = ((len+1)*(len+2))/2;

        System.out.println(nat-sum);

    }
}