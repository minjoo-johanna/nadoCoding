package chap_02;

public class _01_Operator1 {
    public static void main(String[] args) {
        // 산술 연산자

        // 일반 연산
        System.out.println(4 + 2); // 6
        System.out.println(4 - 2); // 2
        System.out.println(4 * 2); // 8 
        System.out.println(4 / 2); // 2
        System.out.println(5 / 2); // 2.5 // 결과가 정수로 나옴. 뒤에 있는 소숫점은 버려짐. 
        System.out.println(2 / 4); // 0
        System.out.println(4 % 2); // 0 // 4를 2로 나눴을때 나머지 출력
        System.out.println(5 % 2); // 1

        // 우선 순위 연산
        System.out.println(2 + 2 * 2); // 6
        System.out.println((2 + 2) * 2);

        // 증감 연산 ++, --
        int val;
        val = 10;
        System.out.println(val); // 10
        System.out.println(++val); // 11 // val + 1 후에 문장 출력
        System.out.println(val); // 11
        
        val = 10;
        System.out.println(val); // 10
        System.out.println(val++); // 10 // 먼저 문장 출력 후에 val에 1이 더해짐. 
        System.out.println(val); // 11

        val = 10;
        System.out.println(val); // 10
        System.out.println(--val); // 9
        System.out.println(val); // 9

        val = 10;
        System.out.println(val); // 10
        System.out.println(val--); // 10
        System.out.println(val); // 9

        // 은행 대기번호 표
        int waiting = 0;
        System.out.println("대기 인원 : " + waiting++); // 대기 인원 : 0 
        System.out.println("대기 인원 : " + waiting++); // 대기 인원 : 1
        System.out.println("대기 인원 : " + waiting++); // 대기 인원 : 2
        System.out.println("대기 인원 : " + waiting); // 총 대기 인원 : 3
 

    }
}
