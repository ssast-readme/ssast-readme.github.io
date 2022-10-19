# 2022 夏季学期 Rust 课堂笔记 

<center><div style='height:2mm;'></div><div style="font-family:华文楷体;font-size:14pt;">未央软-11  鲁睿<div style='height:2mm;'>   </div></center>

## lecture 3（标准库）

### 编码

C艹 语言 11 比 98 增加 unordered_map 

C 里面的 string 为 ``\0`` 操作，即使是访问字符串长度也需要 $O(n)$ 的空间

而 C艹 使用 ``std::string`` 更加方法，对负数进行补码操作，便于加法

+ Rust 的字符串处理机制比较复杂。
  + 主要是用 UTF-8 编码的 Unicode 字符序列。
  + 不是空字符 '\0' 结尾的 C 风格字符串，可以包含空字符。
+ 主要有两大类： &str 和 String。

字符的标识，与信息论有关：

模拟电路（信号是连续变化的，模拟类型更多，但不抗干扰，教室里的钟表）

数字电路（低电位和高电位，0V 和 5V，能抗干扰，数字手表）

ASCII 码 0 是 48，A 是 65，a 是 97 

+ 编码：字符在计算机内部的表示方式
+ 早期： ASCII 码，以英文字符为主， 7 位二进制
+ 中文： GB 2312-1980《信息交换用汉字编码字符集》， 6,763 个汉字，两个字节

  + GB 18030-2005《信息技术中文编码字符集》， 70,244 个汉字，两个字节或四个字节

+ Unicode：试图把全世界的文字都纳入进来，收集了 144,697 个字符，四个字节
  + 常用 UTF-8 的形式来表示，**变长**一到四个字节，rust 便使用这种编码

+ 会出现乱码问题

<h3 align="center">Unicode 中文乱码速查表</h3>

| xxxxxx | 示例                                         | 特点                                                   | 产生原因                                                     |
| ------ | -------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| 古文码 | 鐢辨湀瑕佸ソ濂藉涔犲ぉ澶╁悜涓?               | 大都为不认识的古文，并加杂日韩文                       | 以 GBK 方式读取 UTF-8 编码的中文                             |
| 口字码 | ����Ҫ�¨2�ѧϰ������                            | 大部分字符为小方块                                     | 以 UTF-8 的方式读取 GBK 编码的中文                           |
| 符号码 | ç”±æœˆè\|å￥½å￥½å-\|ä1 å¤©å¤©å‘ä¸Š          | 大部分字符为各种符号                                   | 以 ISO8859-1 方式读取 UTF-8 编码的中文                       |
| 拼音码 | óéÔÂòaoÃoÃÑ§Ï°ììììÏòéÏ                       | 大部分字符为头顶带有各种类似声调符号的字母             | 以 ISO8859-1 方式读取 GBK 编码的中文                         |
| 问句码 | 由月要好好学习天天向??                       | 字符串长度为偶数时正确，长度为奇数时最后的字符变为问号 | 以 GBK 方式读取 UTF-8 编码的中文，然后又用 UTF-8 的格式再次读取 |
| 锟拷码 | 锟斤拷锟斤拷要锟矫猴拷学习锟斤拷锟斤拷锟斤拷 | 全中文字符，且大部分字符为“锟斤拷”这几个字符           | 以 UTF-8 方式读取 GBK 编码的中文，然后又用 GBK 的格式再次读取 |
| 烫烫烫 | 烫烫烫烫烫烫烫烫烫烫烫烫烫烫烫烫烫烫         | 字符显示为“烫烫烫”这几个字符                           | VC Debug 模式下，栈内存未初始化                              |
| 屯屯屯 | 屯屯屯屯屯屯屯屯屯屯屯屯屯屯屯屯屯屯         | 字符显示为“屯屯屯”这几个字符                           | VC Debug 模式下，堆内存未初始化                              |

### &str 和 String

&str

+ &str 是字符串切片，是切片的一种。
+ 形如 "string literals" 的字符串字面值是 &str 类型的1。
+ &str 是静态分配空间的，且固定大小。
+ 不能用方括号来做形如 some_str[i] 的索引，因为每个 Unicode 字符可能有多个字节。
+ 正确的做法是在 chars() 中迭代：
  + ``for c in "1234".chars() { ... }``

String

+ String 是分配在堆上的，可以动态增长。
  + 和 Vec 类似，实际上就是在 Vec\<u8\> 外面包了一层。
+ 也不能用下标来索引。
  + 可以通过 s.nth(i) 来访问某个字符。
+ 通过取引用的方式可以获得 &str。

### Option 枚举类型

```rust
enum Option<T> {
  None,
  Some(T),
}
```

+ Option<T> 是一个枚举类型，同时也是泛型类型。
+ 为某种已有类型提供了**表示没有或者空值的概念**。
+ 在 Rust 中，在需要返回空值时，推荐使用 Option<T>。
  + 而不是返回诸如 NaN、 -1、 null 等特殊的值。
+ 类型 T 可以是任何类型，没有限制。

一个处理除数为 0 的情况：

```rust
fn divide(numerator: f64, denominator: f64) -> Option<f64> {
if denominator == 0.0 {
    None
  } else {
    Some(numerator / denominator)
  }
}
// The return value of the function is an option
let result = divide(2.0, 3.0);
// Pattern match to retrieve the value
match result {
  // The division was valid
  Some(x) => println!("Result: {x}"),
  // The division was invalid
  None => println!("Cannot divide by 0"),
}
```

典型用途：

初始值（求列表最大值）、函数定义域不是全集、表示简单的错误情况（未定义）、结构体的可选域或者可拿走的域、可选的函数参数、空指针

### 错误处理

+ 对于不可恢复的错误，使用恐慌 panic!。
  + 数组越界、栈越界、算术运算溢出……
+ 对于可恢复的错误，使用 Result。
  + 文件操作、网络操作、字符串解析……

```rust
enum Result<T, E> {
  Ok(T),
  Err(E)
}
```

+ Result 与 Option 类似，除了正常结果外，还可以表示错误状态。
+ 也定义了 unwrap 和 expect 等方法。
+ 可以通过 ok 或 err 等方法转换成 Option。
  + 把 Ok 或者 Err 的值作为 Some，另一种变成 None。
+ 也可以进行类似 Option 的操作。
  + and、 or……

其处理原则，对返回值为 Result 的函数，一定要显式地处理（否则编译器报 ``warning`` ）

```rust
use std::io::Error;
type Result<T> = Result<T, Error>;
```

### ?操作符

配合 Result 类型

```rust
fn read_username_from_file() -> Result<String, io::Error> {
  let mut username = String::new();
  File::open("hello.txt")?.read_to_string(&mut username)?;
  Ok(username)
}
```

配合 Opition 类型

```rust
fn last_char_of_first_line(text: &str) -> Option<char> {
  text.lines().next()?.chars().last()
}
```

相当于可以提前传播错误，对上述两种类型对于 ``Err`` 和 ``None`` 就可以提前返回

**究竟是恐慌还是不恐慌？**就看能否给调用代码恢复的机会。

**unwrap/expect 的场合：**作为原型代码中的错误处理占位符

### 容器

**Vec\<T\>**：连续空间、可增长的序列，末尾可以高效增删、会发生增长和收缩

**VecDeque\<T\>**：双端向量，两端可以高效增删，用环状缓冲区

**LinkedList\<T\>**：双向链表，不能随机索引

**HashMap<K, V> / BTreeMap<K, V>**：字典（映射）类型，一般使用 **HashMap<K, V>**，需要满足 K: Hash + Eq，需要有序的时候用 **BTreeMap<K, V>** ，需要满足 K: Ord

两者访问复杂度分别为 $O(1)$ 和 $O(\log n)$ ，哈希表的使用举例

```rust
use std::collections::HashMap;
let mut scores = HashMap::new();
// 添加元素
scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);
// 访问字典
let team_name = String::from("Blue");
let score = scores.get(&team_name);
// 遍历元素
for (key, value) in &scores {
	println!("{}: {}", key, value);
}
// 用于统计字母出现次数
let mut count: BTreeMap<char, usize> = BTreeMap::new();
for ch in "abcbcddef".chars() {
  // {'a': 1, 'b': 2, 'c': 2, 'd': 2, 'e': 1, 'f': 1}
  count.entry(ch).and_modify(|e| *e += 1).or_insert(1);
}
```

collect() 的使用

```rust
// 将数据从列表转化为 BTreeSet
let mut data = vec![0, 1, 2, 3, 0];
let set: BTreeSet = data.iter().collect();
// 将数据中每个数乘以原来的两倍
let input = vec![1, 2, 3];
let result: Vec<i32> = input.iter().map(|x| x * 2).collect();
// 使用 zip() 将两个数据叠加
let a = vec![1, 2, 3];
let b = vec![2, 3, 4];
let result: Vec<i32> = a.iter().zip(b.iter()).map(|(x, y)| x + y).collect();
```

early，向量 lazy

B树外存，二叉树内存

### 迭代器


对**序列**的一种抽象

```rust
pub trait Iterator {
  type Item;
  fn next(&mut self) -> Option<Self::Item>;
  // More fields omitted
}
```

大数据方法 map revuse

### 自动测试

软件工程：**回归测试**（列出对所有的情况，每次开发判断能否通过）

**评测系统**是独立于程序的系统，用于测试；**单元测试**嵌入程序当中，在内部进行测试

cargo 提供了相应测试 test，在函数前面加上 ``#[test]`` 以标注这是一个测试函数

```rust
#[test]
fn it_works() {
  let result = 2 + 2;
  assert_eq!(result, 4);
}
```

习惯每写一个函数，就在文件后面实现对它的单元测试，也可以调换过来，测试驱动编程

```rust
fn vector_length(data: &Vec<i32>) -> usize {
  vector_length.len()
}
#[test]
fn test_vector_length() {
  assert_eq!(vector_length(&vec![1, 2, 3]), 3);
}
```

持续集成，CICD，每次 push 一次就会自动跑脚本，判断测试是否失败