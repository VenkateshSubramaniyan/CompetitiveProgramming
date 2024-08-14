package print;

public class LengthEncoding {

    public static void main(String[] args) {

        LengthEncoding encoding = new LengthEncoding();
        encoding.decode("a2b11");
        encoding.decode("a1b3");
        encoding.decode("a1b0");
        encoding.decode("");
ṅ
    }

    void decode(String input) {

        int charptr = 0;
        int countptr = 1;
        int counter ;
        char a = 'a';
        do {
            if (input.length() >= 2) {
                counter = input.charAt(countptr) - '0';
                while (countptr + 1 < input.length() && !Character.isAlphabetic(input.charAt(countptr + 1))) {
                    countptr++;
                    counter = counter * 10 + input.charAt(countptr) - '0';
                }
                print(input.charAt(charptr), counter);
            }
            countptr += 2;
            charptr += 2;

        } while (countptr <= input.length());
        System.out.println();

    }

    void print(char a, int count) {
//        System.out.println("char = "+ a +" count = "+count );
        for (int i = 0; i < count; i++) {
            System.out.print(a);
        }

    }


}
