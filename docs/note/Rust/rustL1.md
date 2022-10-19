# 2022 夏季学期 Rust 课堂笔记 

<center><div style='height:2mm;'></div><div style="font-family:华文楷体;font-size:14pt;">未央软-11  鲁睿<div style='height:2mm;'>   </div></center>

## Lecture 1

### 语言特性

**高效：**Python 解释器，java 虚拟机，而 rust **没有运行时**，在 bare metal（裸机）上运行。

安卓基于 java，苹果 swift，有相应的垃圾回收机制，易卡顿，而 rust 没有垃圾收集机制。

**可靠：**用**类型系统和所有权模型**来确保内存安全性和线程安全性，在编译时消除各种潜在的问题。

**好用：**文档丰富，编译器（提供更改方法）。

### Rust 语言应用

+ Servo 浏览器引擎，Redox 操作系统，Linux 操作系统驱动和模块的支持

+ 清华大学：操作系统教学 rCore，性能所 MadFS 文件系统，IO 500 遥遥领先

+ Cargo 能够大规模添加依赖（第三方库），不需要像 C++ 花时间去寻找并下载源码

### rust 基础语法

C++ cin cout 读取失败时，将流转换为非法，而 rust 则会显式地处理异常

```rust
  io::stdin()
    .read_line(&mut guess)
    .expect("Failed to read line");
  println!("You guessed: {guess}");
```

猜数获取数字以及猜测语句

```rust
  // (1..=100) 代表 1-100 左闭右闭
  let secret_number = rand::thread_rng().gen_range(1..=100);
  // trim()前后处理空格，parse() 解析（转换类型）
  let guess: u32 = guess.trim().parse().expect("Please type a number!");
```

变量绑定

```rust
  let x = 17; // 变量绑定，且隐式推断类型
  let x: i16 = 17; // 显式绑定类型
  let x = 5;
  x += 1; // error: re-assignment of immutable variable x
  let mut y = 5;
  y += 1; // OK!
```

变量类型

- 布尔 bool：两个值 true/false。
- 字符 char：用单引号，例如 'R'、' 计', 是 Unicode 的。
- 数值：分为整数和浮点数，有不同的大小和符号属性。
  - i8、i16、i32、i64、isize
  - u8、u16、u32、u64、usize
  - f32、f64
- 其中 isize 和 usize 是指针大小的整数，因此它们的大小与机器架构相关。
- 字面值 (literals) 写为 10i8、10u16、10.0f32、10usize 等。
- 字面值如果不指定类型，则默认整数为 i32，浮点数为 f64。
- 数组 (arrays)、切片 (slices)、str 字符串 (strings)、元组 (tuples)。

```rust
// 数组
let arr1 = [1, 2, 3]; // (array of 3 elements)
let arr2 = [2; 32]; // (array of 32 `2`s)
// 切片
let arr = [0, 1, 2, 3, 4, 5];
let total_slice = &arr; // Slice all of `arr`
let total_slice = &arr[..]; // Same, but more explicit
let partial_slice = &arr[2..5]; // [2, 3, 4]
// 字符 String 和 &str，可以分别当做 C++ 中的 string 和 const char*
let s: &str = "galaxy";
let s2: String = "galaxy".to_string();
let s3: String = String::from("galaxy");
let s4: &str = &s3;
// 向量
// Explicit typing
let v0: Vec<i32> = Vec::new();
// v1 and v2 are equal
let mut v1 = Vec::new();
v1.push(1);
v1.push(2);
v1.push(3);
let v2 = vec![1, 2, 3];
// v3 and v4 are equal
let v3 = vec![0; 4];
let v4 = vec![0, 0, 0, 0];
// 输出向量中的所有元素
println!("Task 10: The array is {:?}", v2);
```

类型转换

```rust
// 使用 as 进行类型转换 (cast)
let x: i32 = 100;
let y: u32 = x as u32;
// 一般来说只能在可以安全转换的类型之间进行转换操作
```

引用

+ 在类型前面写 & 表示引用类型： &i32。
+ 用 & 来取引用（和 C++ 类似）。
+ 用 * 来解引用（和 C++ 类似）。
+ rust 中引用和一般意义的指针是不一样的。

条件语句

```rust
if x > 0 {
	10
} else if x == 0 {
	0
} else {
	println!("Not greater than zero!");
	-10
}
```

循环语句，三种循环 $\begin{cases}\text{while}\\\text{loop = while true
} \\\text{for}\end{cases}$

迭代器

+ n..m 创建一个从 n 到 m 半闭半开区间的迭代器。
+ n..=m 创建一个从 n 到 m 闭区间的迭代器。
+ 很多数据结构可以当做迭代器来使用，比如数组、切片，还有向量 Vec 等等。

```rust
let xs = [0, 1, 2, 3, 4];
// Loop through elements in a slice of `xs`.
for x in &xs {
	println!("{}", x);
}
```

匹配语句，其中 ``_`` 匹配所有情况

```rust
// 单变量版本
let x = 3;
match x {
  1 => println!("one fish"), // <- comma required
  2 => {
    println!("two fish");
    println!("two fish");
  }, // <- comma optional when using braces
  _ => println!("no fish for you"), // "otherwise" case
}
// 元组版本
let x = 3;
let y = -3;
match (x, y) {
  (1, 1) => println!("one"),
  (2, j) => println!("two, {}", j),
  (_, 3) => println!("three"),
  (i, j) if i > 5 && j < 0 => println!("On guard!"),
  (_, _) => println!(":<"),
}
```

模式绑定

```rust
let (a, b) = ("foo", 12);
```

函数

```rust
// 函数头
fn foo(x: T, y: U, z: V) -> T {
	// ...
}
// T 类型参数 x ，U 类型参数 y ，V 类型参数 z，返回 T 类型
// Rust 必须显式定义函数的参数和返回值的类型。
// 实际上编译器是可以推断函数的参数和返回值的类型的，但是 Rust 的设计者认为显式指定更好

// 函数返回
// 函数最后一个表达式是其返回值，可以使用 return 提前返回
fn square(n: i32) -> i32 {
	n * n
}
fn squareish(n: i32) -> i32 {
	if n < 5 { return n; }
	n * n
}
```

print! 和 println!

```rust
let x = "foo";
print!("{}, {}, {}", x, 3, true);
// => foo, 3, true
println!("{:?}, {:?}", x, [1, 2, 3]);
// => "foo", [1, 2, 3]
let y = 1;
println!("{0}, {y}, {0}", x);
// => foo, 1, foo

```

format!

```rust
let fmted = format!("{}, {:x}, {:?}", 12, 155, Some("Hello"));
// fmted == "12, 9b, Some("Hello")"
```

panic! 处理错误的方式，并不优雅

```rust
if x < 0 {
	panic!("Kaboom!");
}
```

assert! 和 assert_eq!

+ 如果条件 condition 不成立， assert!(condition) 会导致**恐慌**。
+ 如果 left != right， assert_eq!(left, right) 会导致**恐慌**。

unreachable! 用于表达不会达到的分支，如果达到就会导致**恐慌**

unimplemented! 标注没有实现的功能，panic!("not yet implemented") 的简写

