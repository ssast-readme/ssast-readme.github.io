# 2022 夏季学期 Rust 课堂笔记 

<center><div style='height:2mm;'></div><div style="font-family:华文楷体;font-size:14pt;">未央软-11  鲁睿<div style='height:2mm;'>   </div></center>

## lecture 2

Rust 语言最 core 的语法，语言 = 核心语法 + 标准库

### 所有权

+ 资源管理的需求：内存使用的安全和性能

  内存资源：$\begin{cases}全局对象：事先分配的内存空间段，启动时分配，结束时回收\\局部对象：分配在栈上，进入函数时分配，退出函数时回收\\动态对象：分配在堆上，需要时分配，不需要时回收\end{cases}$

+ 对于小型程序，``new`` 之后不 ``delete`` 无所谓，程序结束之后会自动删除；但是对于大型 24h 网络服务端程序，容易出现问题，总有分配内存失败的时候

+ 内存管理方式，**用户指定和垃圾回收**，前者要求编写者的严谨，后者分为小回收和大回收，

  安卓手机卡的原因：处于大回收状态，逻辑不明确，性能差

+ C艹 将构造和分配集成在一起：

  + 拷贝构造：在语义上实现一个对象变两个对象（二进制串的拷贝）。

  + 移动构造：在语义上实现将一个对象的资源转移给另一个对象。

+ 空指针、悬垂指针（指针所指对象被释放，但指针没有做修改）、双重释放（两个对象的指针指向同一块内存空间，两个对象均释放）等问题导致运行时错误。

计算机技术本质上是实现一个 ``Trade-off`` 

+ Rust 中的每个值都有所有者 (owner)。

+ 同一时刻**只有一个**所有者。

+ 当所有者失效，值也将被丢弃。

这是

一份数据只有一个所有者，如果超出作用域，其绑定数据自动释放  

```rust
fn foo() {
  // Creates a Vec object.
  // Gives ownership of the Vec object to v1.
  let mut v1 = vec![1, 2, 3];
  v1.pop();
  v1.push(4);
  // At the end of the scope, v1 goes out of scope.
  // v1 still owns the Vec object, so it can be cleaned up.
}
```

以下代码在编译过程中出错，所有权的转移

```rust
  let v1 = vec![1, 2, 3];
  // Ownership of the Vec object moves to v2.
  let v2 = v1;
  println!("{}", v1[2]); // error: use of moved value `v1`
----------------------Compile Error-----------------------
error[E0382]: borrow of moved value: `v1`
  |
2 |     let v1 = vec![1, 2, 3];
  |         -- move occurs because `v1` has type `Vec<i32>`, which does not implement the `Copy` trait
3 |     // Ownership of the Vec object moves to v2.
4 |     let v2 = v1;
  |              -- value moved here
5 |     println!("{}", v1[2]); // error: use of moved value `v1`
  |                    ^^ value borrowed here after move
```

在函数调用的时候，如果传入参数过多，还要将所有权还回去，比较麻烦

使用**借用**，所有权本身没有变化，相当于是借用一下数据

```rust
  let v = vec![1, 2, 3];
  // v_ref is a reference to v.
  let v_ref = &v;
  // Moving ownership to v_new would invalidate v_ref.
  // error: cannot move out of `v` because it is borrowed
  let v_new = v;
  // Cancel the effect of NLL (non-lexical lifetime)
  println!("{:?}", v_ref);
```

rust 语言是一门**面向编译器语言**，可以认为写不出运行有问题的代码

```rust
// 借用与函数
fn length(vec_ref: &Vec<i32>) -> usize {
  // vec_ref is auto-dereferenced when you call methods on it.
  vec_ref.len()
}
// 可变借用
fn push(vec_ref: &mut Vec<i32>, x: i32) {
	vec_ref.push(x);
}
// Copy (特型)
// i32、f64、char、bool 可以拷贝
// 生命周期检查
let y: &i32;
{
  let x = 5;
  y = &x; // error: `x` does not live long enough
}
println!("{}", *y);
```

向量的三种迭代方式，不可变借用 ``&V``、可变借用 ``&mut V``、所有权 ``V``

```rust
let mut vs = vec![0,1,2,3,4,5,6];
// Borrow immutably
for v in &vs { // Can also write `for v in vs.iter()`
  println!("I'm borrowing {}.", v);
}
// Borrow mutably
for v in &mut vs { // Can also write `for v in vs.iter_mut()`
  *v = *v + 1;
  println!("I'm mutably borrowing {}.", v);
}
// Take ownership of the whole vector
for v in vs { // Can also write `for v in vs.into_iter()`
  println!("I now own {}! AHAHAHAHA!", v);
}
```

切片是一种特殊的引用，代表序列中的一个指定片段

```rust
let a = [1, 2, 3, 4, 5];
let slice = &a[1..3];
```

### 结构化数据

有两种 struct 和 enum，mod 相当于 C艹 中的 namespace

结构体用 CamelCase 命名方式，里面的域用 snake_case 命名方式。

语法糖，对别的方法进行一种实现，写起来简便

```rust
struct Foo { a: i32, b: i32, c: i32, d: i32, e: i32 }
let mut x = Foo { a: 1, b: 1, c: 2, d: 2, e: 3 };
let x2 = Foo { e: 4, .. x };
// Useful to update multiple fields of the same struct:
x = Foo { a: 2, b: 2, e: 2, .. x };
```

Rust 的枚举要强很多，是**和类型**，用来表示多选一的数据（**代数数据类型**，如笛卡尔坐标系）

变体 $无数据、有命名的数据域(结构体)、无命名的数据域(元组变体)$，如

```rust
enum Resultish {
  Ok,
  Warning { code: i32, message: String },
  Err(String)
}
// 使用 Resultish::each 来访问并匹配数据
match make_request() {
  Resultish::Ok =>
  println!("Success!"),
  Resultish::Warning { code, message } =>
  println!("Warning: {}!", message),
  Resultish::Err(s) =>
  println!("Failed with error: {}", s),
}
```

枚举类型还可以递归

```rust
enum List {
	Nil,
	Cons(i32, List),
}
// 但上述枚举类型会报错，会趋于无穷大，使用 Box 加以限制
let boxed_five = Box::new(5);
enum List {
  Nil,
  Cons(i32, Box<List>), // OK!
}
```

方法与所有权

方法的第一个参数（名字为 self）决定这个方法需要的所有权种类，分类更加细致：

+ &self：方法借用对象的值。
  一般情况下尽量使用这种方式，类似于 C++ 中的常成员函数。
+ &mut self：方法可变地借用对象的值。
  在方法需要修改对象时使用，类似于 C++ 中的普通成员函数。
+ self：方法获得对象的所有权。
  方法会消耗掉对象，同时可以返回其他的值。

```rust
impl Point {
  fn distance(&self, other: Point) -> f32 {
    let (dx, dy) = (self.x - other.x, self.y - other.y);
    ((dx.pow(2) + dy.pow(2)) as f32).sqrt()
  }
  fn translate(&mut self, x: i32, y: i32) {
    self.x += x;
    self.y += y;
  }
  fn mirror_y(self) -> Point {
    Point { x: -self.x, y: self.y }
  }
}
```

+ 一般会创建一个名为 new 的关联函数起到构造函数的作用。

  Rust 没有内置的构造函数语法，也不会自动构造。

+ 方法、关联函数不能重载、方法不能继承

### 模式匹配

对结构体进行解构

```rust
pub struct Point {
  x: i32,
  y: i32,
}
match p {
  Point { x, y } => println!("({}, {})", x, y)
}
```

使用引用的方式匹配

```rust
let x = 17;
// 打印数值或者修改值
let mut x = 17;
match x {
  ref r if x == 5 => println!("{}", r),
  ref mut r => *r = 5
}
```

内部绑定（使用 ``@`` ）

模式匹配的穷尽性，否则会报错（使用 ``_`` 表示其他情况）

``for`` 循环的模式匹配

```rust
let v = vec![1, 2, 3];
for (i, x) in v.iter().enumerate() {
  print!("v[{i}] = {x} ");
}
// v[0] = 1 v[1] = 2 v[2] = 3 
```

