fun main() = with(System.`in`.bufferedReader()) {
	// 정수 하나 읽기
	val num = readLine().toInt()
    for(i in 1..9){
        println("$num * $i = ${num*i}")
    }
}