# 2022 夏季学期 Rust 课堂笔记 

<center><div style='height:2mm;'></div><div style="font-family:华文楷体;font-size:14pt;">未央软-11  鲁睿<div style='height:2mm;'>   </div></center>

## Lecture 7

> 当今许多设备都是多核的，并发是现代语言必须具备的特性，

### 闭包

#### 概念与类型推导

闭包的概念和匿名函数、lambda 函数相似，其可以绑定在变量上：

```rust
let square = |x: i32| -> i32 { x * x };
println!("{}", square(3));
// => 9
```

类型可以推导，参数类型和返回值类型都可以不显示地给出

```rust
let square_v4 = |x: u32| { (x * x) as i32 };
let square = |x| { x * x };
println!("{}", square(-2.4));
// => 5.76
```

#### 捕捉

闭包还可以包含其所在的环境（可以调用外面的参数，称为**捕捉**）

```rust
let magic_num = 5;
let magic_johnson = 32;
let plus_magic = |x: i32| x + magic_num;
```

闭包绑定后如果尝试借用，如果在上述代码后面加入以下代码，借用编译器则会报错

```rust
let more_magic = &mut magic_num; // Err!
```

#### 移动闭包

可以使用 ``{...}``  让闭包超过作用域来恢复，调用函数和被调用函数 Caller, Callee，也可以使用 ``move`` 关键字强制闭包获得环境变量的所有权，为**移动闭包**

```rust
fn make_closure(x: i32) -> Box<dyn Fn(i32) -> i32> {
  let f = move |y| x + y;
  Box::new(f)
}
let f = make_closure(2);
println!("{}", f(3));
// => 5
```

#### 特型闭包

闭包与所有权，只能调用一次，满足 rust 借用规则。与所有权相似，闭包也具有闭包特型，``Fn, FnMut, FnOnce`` 分别代表借用、可变借用、所有权

如何正确地返回闭包？如下，使用动态的生命周期以及移动语义解决

```rust
fn box_up_your_closure_and_move_out() -> Box<dyn Fn(i32) -> i32> {
  let local = 2;
  Box::new(move |x| x * local)
}
```

Lambda 函数本质上是 C++/Rust 在调用处创建一个未知名字的类/结构体，然后传入环境的相关值，最后调用一个未知名字的函数。

### 并发

#### 线程进程、并发并行概念

二进制可执行文件在执行之后，成为进程，在 CPU 中存放：**寄存器，堆，栈，操作系统指令**。

**Program Point** 指向进程下一个指令（在X86 中称为 PC）

线程是**轻量级**，有 CPU 存放的寄存器、堆、栈、操作系统指令单元，但内存是相互共享的，但不引入通信的开销（网络、进程通信）

并发是程序同时有多个正在运行的线程，而并行是指多个处理单元，要求更高，真正意义的同时处理。

#### 并发执行

考虑下面代码，假设两个线程，一个执行 ``foo()``，一个执行 ``bar()`` 

```rust
let mut x = 0;
fn foo() {
  let mut y = &mut x; *y = 1;
  println!("{}", *y); // foo expects 1
}
fn bar() {
  let mut z = &mut x; *z = 2;
  println!("{}", *z); // bar expects 2
}
```

这两个线程的执行顺序不是每次都能保证的，如果将两个函数当做两台 ATM 机，则会发生严重的后果。

并发编程的难点：**数据共享**、**数据竞争**、**同步**（保证所有线程都有正确的世界观，共享缓冲区）、**死锁**

死锁发生有四个条件：**互斥、持有资源、非抢占、等待成环**

一个形象的例子：

*N* 个哲学家坐在一张圆桌周围，交替地进行吃饭和思考。每个哲学家需要一双筷子用来吃饭，但是一共只有 *N* 根筷子，每两个哲学家之间有一根。

哲学家的行为用算法描述如下：

+ 拿起他左侧的那根筷子（获取一个资源的锁）。
+ 拿起他右侧的那根筷子（获取一个资源的锁）。
+ 吃饭（使用资源）。
+ 将两根筷子放回原处（释放资源的锁）。

对所有哲学家来说，依据算法，所有人都拿到左侧的筷子，而此时桌上没有筷子，从而所有人卡在第二步

### 线程

Rust 标准库提供了线程 ``std::thread``，每个线程有自己的栈和状态，使用闭包来指定线程的行为

#### 线程句柄

```rust
use std::thread;
let handle = thread::spawn(|| {
  "Hello, world!"
});
println!("{:?}", handle.join());
```

![](https://lr-tsinghua11.github.io/img/video_editor/blackboard.png)

``join()`` 会阻塞当前线程的执行，直到句柄对应的线程终止，其返回 ``Ok`` 或者 ``Err``

``thread::park()`` 可以暂停自己的执行，之后可以通过现成的 ``unpark()`` 来继续执行

#### 线程与所有权

线程的创建也要满足所有权的规则（包括闭包和所有权的规则），例如使用 ``move`` 来创建移动闭包，获得所有权

```rust
use std::thread;
for i in 0..10 {
  thread::spawn(move || {
  	println!("I'm #{}!", i);
}
```

### 共享线程状态

Rust 类型系统包含要求满足并发承诺的特型

+ Send 表示可以在线程间安全转移

+ Sync 表示可以在线程间（通过引用）安全共享

Send 类型可以将它的所有权在线程间转移，如果一种类型没有实现 Send，那么它只能留在原来的线程里。

Sync 类型在多个线程使用时不会引发内存安全问题，基本所有类型都是 Sync 的。以下为一个共享线程状态示例

```rust
use std::thread;
use std::time::Duration;
fn main() {
  let mut data = vec![1, 2, 3];
  for i in 0..3 {
    thread::spawn(move || {
      data[i] += 1;
    });
  }
  thread::sleep(Duration::from_millis(50));
}
```

此时 data 有多个所有者，使用 ``Arc<T>`` ，代表原子性的引用计数指针（Atomic Reference-Counted），但如果只是在初始化加入 Arc，编译也不通过。

Arc 也不具有内部可变性，需要添加**互斥锁**（Mutual Exclusion），保证它包含的值只有一个线程能够访问；如果一个线程锁定了互斥锁，但是发生了恐慌，此时该互斥锁进入中毒状态，该锁不会被释放

高并发任务、超算比赛主要资源共享，Open Np，消息传递 npi

### 通道

通道（channels）可以用来**同步线程之间的状态**，用于在线程之间传递消息，也可以用来提醒其他现成关于数据就绪、事件已经发行的情况

``std::sync::mpsc`` 实现多生产者、单消费者的通信功能

**同步：**不同进程之间是需要等待的，**异步：**发送的东西放入（相当于无限大的）缓冲区，相互之间不需要等待

使用 ``channel<T>()`` 函数创建一对连接的 ``(Sender<T>, Receiver<T>)``

``go`` 语言有 ``GC`` 机制，导致编程开销大

对哲学家筷子问题，可以使用最后一个哲学家用相反方向拿筷子或者传递令牌规定拿筷子的哲学家。
