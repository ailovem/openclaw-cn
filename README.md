# OpenClaw 中国社区网站

## 📁 文件结构

```
openclaw-cn/
├── index.html              # 原版首页（保留）
├── index-spa.html          # ✅ SPA 版首页（推荐使用）
├── smart-schedule.html     # 智能日程
├── smart-writing.html      # AI 写作
├── smart-investment.html   # 智能投研
├── smart-home.html         # 智能家居
├── genomics.html           # 基因分析
├── quality-inspection.html  # 质量检测
├── medical-diagnosis.html   # 辅助诊断
├── all-cases.html          # 全部案例
├── smart-travel.html       # 旅行规划（保留）
└── generate_pages.py        # 页面生成脚本
```

## 🚀 使用方法

### 方式1: 直接打开 SPA 版本（推荐）
```
双击: openclaw-cn/index-spa.html
```

### 特性
- ✅ **SPA 无刷新跳转** - 页面切换平滑流畅
- ✅ **角色切换系统** - 4 种角色可选，保存到本地存储
- ✅ **统一导航** - 首页、场景、招聘、资讯一键切换
- ✅ **动画效果** - 平滑的过渡动画

### 方式2: 传统多页面
```
双击: openclaw-cn/index.html
```

子页面从 index.html 跳转到各场景页面。

## 🎯 SPA 版本功能

### 页面导航
- 首页: `index-spa.html#home`
- 场景实验室: `index-spa.html#scenes`
- 大咖招聘: `index-spa.html#jobs`
- 实时资讯: `index-spa.html#news`

### 角色切换
1. 点击右上角角色按钮
2. 选择角色（探索者/开发者/研究者/企业家）
3. 选择保存到本地存储，下次访问自动恢复

## 🔧 自定义修改

### 添加新页面
1. 在 `index-spa.html` 的 `<div class="page-container">` 中添加新页面
2. 参考现有页面的结构
3. 使用 `router.navigate('pageName')` 跳转

### 修改角色
在 `index-spa.html` 的 `roleDropdown` div 中修改角色选项。

## 📦 部署到 GitHub Pages

1. 提交代码到 GitHub 仓库
2. 进入 Settings → Pages
3. Source 选择 `main branch`
4. 访问: `https://你的用户名.github.io/仓库名/`

## 🎨 技术栈

- **HTML5** - 语义化标签
- **CSS3** - 渐变、动画、响应式
- **Vanilla JavaScript** - SPA 路由 + 角色系统
- **本地存储** - 角色偏好持久化

## 📝 更新日志

**v2.0** (2026-02-10)
- ✅ SPA 版本发布
- ✅ 角色切换系统
- ✅ 统一导航
- ✅ 无刷新页面切换
- ✅ 响应式设计

**v1.0** (之前)
- 基础多页面版本
- 独立 HTML 文件
