# Vue

作者：陆离马鹿

- `package.json:` 项目名、项目版本、npm脚本、依赖与开发时依赖版本等信息的配置
    - `script` 是npm运行的脚本
    - `dependencies` 与`devDependencies` 为依赖与开发时依赖
- `public/index.html` 代码的入口，其中有一个id为app的div元素（锚点）
- `src/main.js` 启动执行的代码，初始完毕后，将Vue组件App渲染到了`public/index.html` 中id为app的div上
- `App.vue` 初始的一个全局组件，代表整个页面，其内部使用了其他组件实现渲染
- 组件
    - Vue使用组件作为每个单元的基本元素，每个组件有较好的封装，通过指标的绑定和传入参数的不同控制其各自的具体表现
    - 每个 .vue 组件一般主要包含template、script、style几部分，其中template部分为待渲染的内容；script部分根据外部参数、自身的数据和函数回调将template中的内容渲染，供外部使用；style部分为css样式
    - vue的组件之间可以嵌套，大的组件可以包含小的组件，例如初始项目内App内就使用了一个其他组件