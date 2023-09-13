package chap_02;

public class _04_Operator4 {
    public static void main(String[] args) {
        // 논리 연산자
        boolean kimchiStew = true;
        boolean egg = true;
        boolean friedPork = true;
        
        System.out.println(kimchiStew || egg || friedPork); // 하나라도 true 이면 true (괜찮은 식당)
        System.out.println(kimchiStew && egg && friedPork); // 모두 true 이면 true (최고의 식당)
        
        // And 연산
        System.out.println((5 > 3) && (3 > 1));
        System.out.println((5 > 3) && (3 < 1));

        // Or 연산
        System.out.println((5 > 3) || (3 > 1)); // true
        System.out.println((5 > 3) || (3 < 1)); // true
        System.out.println((5 < 3) || (3 < 1)); // false
        
        // System.out.println(1 < 3 < 5); // 불가능한 코드

        // 논리 부정 연산자
        System.out.println(!true); // false
        System.out.println(!false); // true
    }
}
