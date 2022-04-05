---
theme: juejin
highlight: a11y-dark
---

# $JavaScript$ 语法糖及语法坑
> 作者：光火
>
> 邮箱：victor_b_zhang@163.com

- 先简单谈一谈自己创作这篇文章的初衷吧。作为一名零基础的科班生，我步入大学后最先接触的编程语言是`C/C++`。尽管随后又陆陆续续学习了数不尽的语言和框架，但是理解最为深刻的还是`C/C++`。不过，由于项目所需和个人兴趣使然，我在大二暑期开始涉足 `Web` 前端、微信小程序等领域。在这里，`JavaScript` 是绝对王者。因此，本文中，笔者尝试从自身角度出发，简要地总结一下个人在学习与使用 `JavaScript` 过程中遇到的语法糖及语法坑，还望各位读者批评指正，各倾陆海。（持续更新，建议追踪）

## 语法糖
### 可选链
- 有些时候，我们希望特定的调用在属性、方法不存在时返回`undefined`，而非报错，这时我们就可以考虑使用可选链`?.`；
- `?.`会检查左侧是否为`null/undefined`，如果不是则继续运算，否则就返回`undefined`；
```JavaScript
let player = {
    name: 'Alice',	
}

console.log(player?.birthday?.month); // undefined
```
### 类型转换
- `+` 可以发挥 `Number()`的作用；
- `!!`可以发挥 `Boolean()` 的作用；
```JavaScript
let a = '2';
let b = '4';
console.log(+a * +b);  // 8
console.log(!! null);  // false
console.log(!! a);     // true
```
### 数值提取
- 尽管对于字符串相关的问题，正则表达式几乎是通杀，但是在此还是要特别介绍一下`parseInt`及`parseFloat`函数。它们会从头开始在字符串中读取数字，倘若发生 `error`，则返回已收集到的数字。
```JavaScript
console.log(parseInt('100'));        // 100
console.log(parseInt('100px'));      // 100
console.log(parseFloat('12.5em'));   // 12.5

console.log(parseInt('a12345'));     // NaN
console.log(parseFloat('XYZ14.6'));  // NaN
```
- 可见，`parseInt`和`parseFloat`很擅长做一些去除单位，保留数值的工作；
- 当然，`parseInt`还有第二个参数，即`parseInt(str，base)` ，它可以将字符串 `str` 解析为给定的 `base` 数字系统中的整数，其中`2 ≤ base ≤ 36`；(36即`0-9` + `A-Z`)
```JavaScript
console.log(parseInt('100', 2));    // 4
console.log(parseInt('ff', 16));    // 255
console.log(parseInt('0xff', 16));  // 255
```
### 数组合并
```JavaScript
let a = [1, 7, 4, 9, 6, 1];
let b = [2, 1];
a.push.apply(a, b);
```
- 选择较长的数组作为 `a` ，较短的数组作为 `b`，这样性能会比较好； 
- 经过上述操作后，`a` 就是合并后的数组，内容为 `[1, 7, 4, 9, 6, 1, 2, 1]`； 
也可以根据具体需求，使用 `ES6` 的语法：
```JavaScript
let a = [1, 7, 4, 9, 6, 1];
let b = [2, 1];
c = [...a, ...b]; // 生成一个新的数组
a.push(...b);     // 直接在原数组进行操作
```
- 经过上述操作后，`a` 和 `c` 的内容均为 `[1, 7, 4, 9, 6, 1, 2, 1]`。

### 清空数组
- 在`JavaScript`中，数组的`length`属性是可写的，如果我们手动减少它，数组就会发生截断，且该过程不可逆。因此，倘若我们需要清空数组，可以简单使用`arr.length = 0`。
```JavaScript
let base = [1, 2, 3, 4, 5, 6];

base.length = 0;
console.log(base);      // []

base.length = 6;
console.log(base[2]);   // undefined
```
### splice方法
- 在`JavaScript`中，`splice`方法几乎可以完成对数组的任意操作，如添加、删除、替换、插入元素，该方法会改变原始数组：
```JavaScript
let base = [1, 2, 3, 4, 5, 6];
base.splice(1, 2); // 自索引 1 开始, 删除 2 个元素
console.log(base); // [1, 4, 5, 6]

base.splice(1, 0, 2, 3); // 自索引 1 开始, 删除 0 个元素, 插入元素 2 和 3
console.log(base); // [1, 2, 3, 4, 5, 6]

base.splice(-1, 0, 'hey'); // 支持负索引, -1 即尾端的前一位
console.log(base); // [1, 2, 3, 4, 5, 'hey', 6]
```
### 嵌套函数
- `JavaScript`支持在一个函数中创建另一个函数，而且还可以返回一个嵌套函数，用于变量的共享：倘若对此感兴趣，可以自行查阅“闭包”相关内容。
```JavaScript
function initCounter() {
    let count = 0;

    return function() {
        return count ++;
    }
}


let counter = initCounter();
console.log(counter()); // 0
console.log(counter()); // 1
console.log(counter()); // 2
```
### 筛选对象数组
- 对象数组在`JavaScript`中有着广泛应用，特别是在列表渲染以及前后端通信上，该格式最为常见。`find`及`filter`方法可以有效地作用于对象数组并完成筛选工作，两者的主要区别为`find`返回第一个匹配的元素，而`filter`可返回多个元素。
```JavaScript
let rtn_data = [
    {id: 1, name: 'Alice'},
    {id: 2, name: 'Bob'},
    {id: 3, name: 'Carol'},
    {id: 4, name: 'Dave'},
    {id: 5, name: 'Eve'},
]

let top_1 = rtn_data.find(item => item.name === 'Alice');
let top_3 = rtn_data.filter(item => item.id <= 3);


console.log(top_1);
/* { id: 1, name: 'Alice' } */

console.log(top_3);
/*
[
  { id: 1, name: 'Alice' },
  { id: 2, name: 'Bob' },
  { id: 3, name: 'Carol' }
]
*/
```
### 跳出多重循环
```JavaScript
outer:
for(let i = 0; i < 3; i ++) {
	for(let j = 0; j < 3; j ++) {
		let value = prompt('Input value', '');
		if(!value) break outer;
	}
}	
```
- `break outer`：当用户输入空串抑或是点击取消后，会直接跳出两层循环。
### 逻辑运算符的返回值
- `||`：可用于返回第一个真值，`result = value1 || value2 || value3`；
- `&&`：可用于返回第一个假值，`result = value1 && value2 && value3`；
- `??`：可用于返回第一个已定义值，对于`a ?? b`，倘若`a`是已定义的，则结果为`a`，反之则为`b`；
***

## 语法坑
### 浮点数
- 浮点数误差是一个经典话题，利用有限的位数表示无限的数字显然会产生一些潜在问题，不过这也没有什么好的解决方法。在计算机组成原理中，针对浮点数有着专门的论述，感兴趣的读者可以阅读阅读$CSAPP$。说回$JavaScript$，新手时常会犯如下错误：
```JavaScript
// 归并排序
let m = (l + r) / 2;   
```
- 在归并排序中，我们需要二分数组，但这里的`m`很可能会是一个浮点数，最终导致结果出现大量的`undefined`，正确的方法利用`Math.floor`函数。
### typeof
- `typeof` 可以用于确定变量的类型，它的返回值有 `undefined、object、boolean、number、bigint string、symbol、function、object` 八种，具体使用方式如下所示： 
  ```JavaScript
  console.log(typeof(null));         // object
  console.log(typeof(function(){}))  // function
  ```
- 另外，如果要判断一个变量的类型是否为数组，应使用`Array.isArray()`函数，因为`typeof`会返回`object`，这在于数组是基于对象实现的。

### 值的比较
`JavaScript` 在比较不同类型的数据时，可能会产生难以预料的结果。再加上`null`、`undefine`以及`NaN`的存在，这个语法坑可谓常见且不友善，需要我们特别注意。
  ```JavaScript
console.log('2' > 1);            // true
console.log('001' == 1);         // true
console.log('001' === 1);        // false
console.log(null == 0);          // false
console.log(false == 0);         // true
console.log(false === 0);        // false
console.log(null == undefined);  // true
console.log(null === undefined); // false


console.log('02' != 2);             // false
console.log('02' !== 2);            // true
console.log(2 > undefined);         // false
console.log('0x123' > null);        // true
console.log(NaN == NaN);            // false
console.log(NaN === NaN);           // false
console.log(Object.is(NaN, NaN));   // true
  ```
- 以上这些千奇百怪的例子只是为了辅助说明，没有必要去专门背诵，我们记住一些基本的原则即可：
    - `JavaScript`对不同类型的值进行比较时，会将它们转化为`number`再判断大小；
    - 不要尝试使用`> < >= <=`去比较一个可能为`null`或者`undefined`的变量，这可能会导致结果失控；
    - 除非你确信自己的代码是无懈可击的，否则还是建议使用`===`、`!==`，因为它们不会进行类型转换，整体效率也好一些；
    - 在大部分情形下，`Object.is(a, b)` 与 `a === b` 效果相同，只是有两个特例，一是上文中所展示的`Object.is(NaN, NaN) = true`，另一个则是`Object.is(0, -0) === false`；
- 另外，如果你打算进行字符串的比较，请记住 (小写字母) 始终大于 (大写字母)：
```JavaScript
console.log('apple' > 'Zpple');  // true
```
### 对象拷贝
- 在`JavaScript`中，对象通过**引用**被赋值和拷贝，所有通过被拷贝的引用的操作，都将作用在同一对象上。倘若需要完成真正意义的拷贝（克隆），可以使用`Object.assign`或者深拷贝函数`_.cloneDeep(Obj)`；
- 由于数组也是基于对象实现的，因此数组也是通过引用来进行赋值的；
```JavaScript
let user = { name: 'John' };

let admin = user;
admin.name = 'Peter';
console.log(user.name); // Peter

let user = { name: "Alice" }
let permissions1 = { can_view: true };
let permissions2 = { can_edit: true };
Object.assign(user, permissions1, permissions2);
// user = { name: "John", can_view: true, can_edit: true }
```
- 应当注意的是，正如下述代码所展示的那样，`Object.assign`无法直接处理对象嵌套的情况。但可以考虑构建一个循环来检查每`user[key]`，倘若它是一个对象，则复制它的结构。当然，为了避免重复造轮子，我们也可以采用现有的实现，如`lodash`库中的`_cloneDeep(obj)`。
```JavaScript
let user = {
    name: 'John',
    size: {
        height: 182,
        weight: 60
    }
};

let clone = Object.assign({}, user);

console.log(user.size === clone.size) // true, 是同一个对象

user.size.height ++;
console.log(clone.size.height);      // 183, 即同样会被改变
```

### 字符串不可修改
- 在 `JavaScript` 中，字符串是不可更改的 (但可以拼接)：
```JavaScript
let str = 'Hello World';
str[6] = 'w';
console.log(str);  // Hello World

str += '!';
console.log(str);  // Hello World!
```
- 即`str`仍为原值，并没有发生变化。这个坑还蛮难受的，比如我们想要写一个将字符串首字母变为大写的函数，我们不能修改原字符串，只好创造一个新的：
```JavaScript
function toUppercase(str) {
	if(! str) return str;
	return str[0].toUpperCase() + str.slice(1);
}

console.log(toUppercase('aeiou'));  // Aeiou
console.log(toUppercase('1234a'));  // 1234a
```
### sort函数默认顺序
- `sort` 函数默认将元素按照字符串进行比较，因此当我们试图排序一个整数数组时，有可能会出现以下现象：
```JavaScript
let base = [1, 2, 15];
base.sort();
console.log(base);  // [1, 15, 2]
```
- 因此，我们需要自定义比较函数：
```JavaScript
base.sort((a, b) => {
    return a - b;
})

console.log(base);  // [1, 2, 15]
```
## 参考文献
- [现代 JavaScript 教程](https://zh.javascript.info/)

## 下载链接
- [点击转到Git仓库](https://github.com/ssast-readme/ssast-readme.github.io/tree/master/docs/tech)