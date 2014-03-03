#include <stdio.h>
#include <stdlib.h>

class A1 {
	public:
		int i;
};

// vtable is leaf
class A2 {
	public:
		int i;
		virtual void f();
};

// vtable is "non-virtual basses only"
// A2 is primary base of V1, A1 is non-polymorphic
class V1 : public A1, public A2 {
	public:
		int i;
};

class B1 {
	public:
		int i;
};

class B2 {
	public:
		int i;
};

// V2 has no primary base, V1 is secondary base
class V2 : public B1, public B2, public virtual V1 {
	public:
		int i;
};

class V3 {
	public:
		virtual void g();
};

// C1 has no primary base, V1 is secondary base
class C1 : public virtual V1 {
	public:
		int i;
};

// C2 has V3 primary (nearly-empty virtual) base,
// V2 is secondary base
class C2 : public virtual V3, virtual V2 {
	public:
		int i;
};

class X1 {
	public:
		int i;
};

class C3 : public X1 {
	public:
		int i;
};

// C1 is primary base, C2 is secondary base, C3 is non-polymorphic
class D : public C1, public C2, public C3 {
	public:
		int i;
};

void A2::f() {
	printf("A2::f()\n");
}

void V3::g() {
	printf("V3::g()\n");
}

int main() {
	A1 *a1 = new A1();
	A2 *a2 = new A2();
	V1 *v1 = new V1();
	B1 *b1 = new B1();
	B2 *b2 = new B2();
	V2 *v2 = new V2();
	V3 *v3 = new V3();
	C1 *c1 = new C1();
	C2 *c2 = new C2();
	X1 *x1 = new X1();
	C3 *c3 = new C3();
	D *d1 = new D();

	free(a1); free(a2); free(v1);
	free(b1); free(b2); free(v2);
	free(v3); free(c1); free(c2);
	free(x1); free(c3); free(d1);
	return 0;
}
