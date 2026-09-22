---
deck_id: "卫宁健康-AI汇报"
kind: "deck"
category: "brand"
summary: "An AI-themed template for technology and data-related content, suitable for healthcare AI presentations"
keywords: ["Weining Health", "AI", "Technology", "Data", "Healthcare"]
primary_color: "#1565C0"
canvas_format: "ppt169"
canvas_width: 1280
canvas_height: 720
canvas_viewbox: "0 0 1280 720"
replication_mode: fidelity
native_structure_mode: structured
page_count: 5
---

# 卫宁健康-AI汇报模板 - 设计规范

> 适用于医疗信息化汇报、智慧医院建设方案、医疗AI产品发布、医疗行业峰会等场景。
---

## I. 模板概述

| 属性      | 描述                                            |
| -------------- | ------------------------------------------------------ |
| **模板名称** | 卫宁健康-AI汇报 (Weining Health AI Report Template) |
| **适用场景**  | 医疗信息化汇报、智慧医院建设方案、医疗AI产品发布、医疗行业峰会|
| **设计风格** | 专业医疗、科技感、现代化、结论先行|
| **主题模式** | 混合主题（深色封面/章节页+ 浅色内容页） |

---

## II. 画布规格

| 属性      | 值                        |
| -------------- | ----------------------------- |
| **格式**     | 标准 16:9                 |
| **尺寸** | 1280 × 720 px                |
| **viewBox**    | `0 0 1280 720`                |
| **安全边距** | 60px (左右), 50px (上下) |
| **内容区域** | x: 60-1220, y: 100-670     |
| **标题区域** | y: 50-100                     |
| **网格基准**  | 40px                          |

---

## III. 配色方案

### 主色调
| 角色             | 值      | 说明                            |
| ---------------- | ----------- | -------------------------------- |
| **卫宁蓝** | `#1565C0` | 品牌主色，标题强调，关键数据 |
| **深蓝背景** | `#1A1A2E` | 封面背景，正文文本，图表基底 |
| **科技蓝**    | `#4A90D9`   | 流程图，链接，交互元素|
| **健康绿**   | `#10B981`   | 推荐选项，积极指标，成功状态|
| **卫宁橙**    | `#D97757`   | 品牌标识，强调色，警告提示|

### 中性色

| 角色           | 值      | 用途                 |
| -------------- | ----------- | ---------------------- |
| **云白** | `#F8FAFC`  | 卡片背景        |
| **边框灰** | `#E2E8F0`  | 卡片边框，分隔线 |
| **板岩灰** | `#64748B`   | 次要文本，图表标签|
| **纯白** | `#FFFFFF`   | 页面背景        |

---

## IV. 字体系统

### 字体栈
**字体栈**: `Microsoft YaHei, PingFang SC, Arial, sans-serif`

### 字体大小层级

| 层级    | 用途           | 大小   | 字重  |
| -------- | ---------------- | ------ | ------- |
| H1       | 封面主标题| 56px   | Bold    |
| H2       | 页面标题       | 32-36px| Bold    |
| H3       | 副标题章节 | 24-28px| Semibold|
| H4       | 卡片标题       | 20-22px| Bold    |
| P        | 正文内容     | 16-18px| Regular |
| Data     | 高亮数据 | 40-48px| Bold    |
| Label    | 标签文本       | 14px   | 500     |
| Sub      | 图表标签/脚注 | 12-14px | Regular |

---

## V. 核心设计原则

### 顶级咨询风格

1. **结论先行（金字塔原理）**: 每页标题即为核心结论
2. **数据情境化**: 对比、趋势、基准，绝不孤立呈现数据
3. **SCQA框架**: 情境 → 冲突 → 问题 → 答案
4. **MECE原则**: 相互独立，完全穷尽
5. **专业留白**: 内容占比 < 65%，让信息"呼吸"

---

## VI. 页面结构

### 通用布局

| 区域           | 位置/高度 | 描述                            |
| -------------- | --------------- | -------------------------------------- |
| **顶部**        | y=0, h=6-8px    | 卫宁蓝装饰条        |
| **标签**      | y=50-70         | 页面类型标签（大写，蓝色）   |
| **标题区域** | y=80-140        | 页面标题（核心结论）             |
| **内容区域** | y=160-620     | 主内容区域                     |
| **页脚**     | y=680           | 页码（居中）                 |

### 装饰元素

- **顶部蓝色条**: 卫宁蓝(`#1565C0`)，高度 6px
- **左侧渐变条**: 蓝色渐变 (`#1565C0` → `#4A90D9`)
- **卡片边框**: 浅灰 (`#E2E8F0`)
- **卡片阴影**: 柔和阴影效果
- **网格装饰线**: 深色封面上的白色低透明度网格
---

## VII. 页面类型

### 1. 封面页(01_cover.svg)

- 深色渐变背景 (`#1A1A2E` → `#16213E` → `#0F0F1A`)
- 网格装饰线（白色 3%不透明度）
- 蓝色和绿色光晕效果
- 医疗数据风格连接线和节点
- 居中主标题（白色）与副标题
- 蓝色装饰短线
- 底部日期和来源信息
### 2. 目录页(02_toc.svg)

- 白色背景
- 左侧蓝色渐变装饰条（8px）
- 蓝色圆形数字 + 章节标题
- 右侧复杂度递进图示

### 3. 章节页(02_chapter.svg)

- 深色渐变背景
- 网格装饰
- 居中大章节标题
- 蓝色装饰条
### 4. 内容页(03_content.svg)

- 白色背景
- 顶部蓝色装饰条
- 页面类型标签（蓝色大写）
- 标题作为核心结论
- 三列卡片布局（彩色顶部边框）
- 居中页码页脚

### 5. 结束页(99_ending.svg)

- 深色渐变背景
- 医疗数据装饰
- 居中感谢信息
- 联系方式

---

## VIII. 常用组件

### 卡片样式

```xml
<!-- 带阴影的卡片 -->
<g filter="url(#cardShadow)">
    <path fill="#F8FAFC" stroke="#E2E8F0" stroke-width="1"
          d="M72,180 H408 A12,12 0 0 1 420,192 V588 A12,12 0 0 1 408,600 H72 A12,12 0 0 1 60,588 V192 A12,12 0 0 1 72,180 Z"/>
</g>
<!-- 顶部彩色装饰条-->
<rect x="60" y="180" width="360" height="6" fill="#10B981"/>
```

### 圆形数字

```xml
<circle cx="90" cy="200" r="24" fill="#1565C0"/>
<text x="90" y="207" font-size="18" font-weight="bold" fill="#FFFFFF" text-anchor="middle">1</text>
```

### 图标背景圆
```xml
<circle cx="130" cy="250" r="35" fill="#10B981" fill-opacity="0.1"/>
```

---

## IX. 间距规范

| 元素          | 值 |
| ---------------- | ------ |
| 安全边距      | 60px   |
| 卡片间距         | 30-40px|
| 卡片圆角 | 8-12px |
| 卡片内边距    | 30px   |
| 网格基准        | 40px   |

---

## X. SVG技术约束

画布保持 `0 0 1280 720`。当前 SVG 编写和导出约束以 ppt-master-winppt 的 `references/shared-standards-core.md` 与所选运行流程为准。原版模板规范保留在旧格式模板目录中。

## XI. 占位符规范
| 占位符       | 描述        |
| ------------------ | ------------------ |
| `{{TITLE}}`        | 主标题        |
| `{{SUBTITLE}}`     | 副标题          |
| `{{COVER_QUOTE}}`  | 封面引语        |
| `{{SOURCE}}`       | 来源信息        |
| `{{DATE}}`         | 日期               |
| `{{PAGE_TITLE}}`   | 页面标题（核心结论） |
| `{{PAGE_LABEL}}`   | 页面类型标签    |
| `{{CONTENT_AREA}}` | 灵活内容锚点 |
| `{{CHAPTER_NUM}}`  | 章节号    |
| `{{CHAPTER_TITLE}}`| 章节标题      |
| `{{PAGE_NUM}}`     | 页码        |
| `{{TOTAL_PAGES}}`  | 总页数       |
| `{{TOC_ITEM_N_TITLE}}` | 目录项标题|
| `{{TOC_ITEM_N_DESC}}`  | 目录项描述|
| `{{THANK_YOU}}`    | 感谢信息  |
| `{{CONTACT_INFO}}` | 主要联系方式 |

---

## XII. 使用说明

1. 将模板复制到项目目录
2. 根据内容需求选择合适的页面模板
3. **标题即为核心结论** → 确保每页都有清晰的结论
4. 使用三种强调色区分内容类型（绿色=推荐，蓝色=流程，橙色=强调）
5. 通过执行器角色生成最终SVG


## Migration Roster

Original visual content is preserved; empty Master/Layout identities provide a stable structured package without relocating artwork. Templates are references for authoring, not permission to invent source facts.

| File | Master | Layout |
|---|---|---|
| `01_cover.svg` | win_1 | win_1_1 |
| `02_chapter.svg` | win_1 | win_1_2 |
| `02_toc.svg` | win_1 | win_1_3 |
| `03_content.svg` | win_1 | win_1_4 |
| `99_ending.svg` | win_1 | win_1_5 |
