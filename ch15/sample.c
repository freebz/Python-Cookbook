/* sample.c */
#include <math.h>

/* 최대 공약수 계산 */
int gcd(int x, int y) {
  int g = y;
  while (x > 0) {
    g = x;
    x = y % x;
    y = g;
  }
  return g;
}

/* (x0, y0)이 맨들브로트 집합(Mandelbrot set)인지 확인한다. */
int in_mandel(double x0, double y0, int n) {
  double x=0,y=0,xtemp;
  while (n > 0) {
    xtemp = x*x - y*y + x0;
    y = 2*x*y + y0;
    x = xtemp;
    n -= 1;
    if (x*x + y*y > 4) return 0;
  }
  return 1;
}

/* 두 수를 나눔 */
int divide(int a, int b, int *remainder) {
  int quot = a / b;
  *remainder = a % b;
  return quot;
}

/* 배열 속 값의 평균 */
double avg(double *a, int n) {
  int i;
  double total = 0.0;
  for (i = 0; i < n; i++) {
    total += a[i];
  }
  return total / n;
}

/* C 자료 구조 */
typedef struct Point {
    double x,y;
} Point;

/* C 자료 구조 관련 함수 */
double distance(Point *p1, Point *p2) {
    return hypot(p1->x - p2->x, p1->y - p2->y);
}
