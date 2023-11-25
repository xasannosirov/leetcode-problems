#include <stdio.h>

int main() {
    int n;
    scanf("%d", &n);
    if (n == 0) {
        printf("3");
        return 0;
    }
    char e[] = "2.7182818284590452353602875";
    e[n+1] += e[n+2] >= '5';
    for (int i = 0; i <= n+1; i++){
        printf("%c",e[i]);
    }
    return 0;
}
