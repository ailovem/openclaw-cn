import os

# 子页面配置
PAGES = {
    'smart-writing.html': {
        'icon': '✍️',
        'title': 'AI 写作',
        'subtitle': '文案、论文、邮件一键生成',
        'color': '#00f0ff',
        'demo_user': '帮我写一封产品发布通知',
        'demo_ai': '好的！这是一封专业的产品发布邮件：\n\n主题：【产品发布】XX v2.0 正式发布\n\n亲爱的用户，\n\n我们很高兴地宣布...'
    },
    'smart-investment.html': {
        'icon': '📈',
        'title': '智能投研',
        'subtitle': 'AI 辅助的投资研究与分析',
        'color': '#ffd700',
        'demo_user': '分析一下新能源板块的趋势',
        'demo_ai': '新能源板块分析报告：\n\n1. 短期：受政策影响波动\n2. 中期：技术突破带动增长\n3. 长期：碳中和目标明确\n\n建议关注：宁德时代、比亚迪'
    },
    'smart-home.html': {
        'icon': '🏡',
        'title': '智能家居',
        'subtitle': 'AI 驱动的智慧生活',
        'color': '#ff6b6b',
        'demo_user': '设置回家模式',
        'demo_ai': '已设置回家模式：\n\n✓ 空调调至 24°C\n✓ 灯光调至暖色调\n✓ 窗帘打开\n✓ 播放轻松音乐\n\n欢迎回家！🏠'
    },
    'genomics.html': {
        'icon': '🧬',
        'title': '基因分析',
        'subtitle': 'AI 辅助基因解读与预测',
        'color': '#a855f7',
        'demo_user': '解读我的基因检测报告',
        'demo_ai': '基因分析结果：\n\n健康风险：\n• 较低心血管疾病风险 ✓\n• 乳糖耐受可能性高 ✓\n\n营养建议：\n• 建议补充维生素 D\n• 蛋白摄入建议：80g/天'
    },
    'quality-inspection.html': {
        'icon': '🔍',
        'title': '质量检测',
        'subtitle': 'AI 驱动的智能质检系统',
        'color': '#00ff88',
        'demo_user': '检测这批产品的缺陷',
        'demo_ai': '质检完成！\n\n检测数量：1000件\n合格：987件\n异常：13件\n\n异常类型：\n• 划痕：8件\n• 色差：5件\n\n建议：调整第3道工序参数'
    },
    'medical-diagnosis.html': {
        'icon': '🩺',
        'title': '辅助诊断',
        'subtitle': 'AI 辅助医疗诊断分析',
        'color': '#ef4444',
        'demo_user': '分析这份检查报告',
        'demo_ai': '报告分析：\n\n关键指标：\n• 血压：120/80 正常\n• 血糖：5.2 正常\n• 胆固醇：4.8 偏低\n\n建议：\n• 保持当前饮食习惯\n• 适量增加运动\n• 3个月后复查'
    },
    'all-cases.html': {
        'icon': '📚',
        'title': '全部案例',
        'subtitle': '查看所有 18 个场景案例',
        'color': '#667eea',
        'demo_user': '查看所有案例',
        'demo_ai': 'OpenClaw 场景实验室包含：\n\n工作场景：5个\n生活场景：4个\n学习场景：3个\n专业场景：6个\n\n共 18 个完整案例'
    }
}

TEMPLATE = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PLACEHOLDER_TITLE - OpenClaw 场景实验室</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root {
            --primary: #667eea;
            --secondary: #764ba2;
            --accent: #00f0ff;
            --green: #00ff88;
            --gold: #ffd700;
            --dark: #0a0a0f;
            --light: #ffffff;
        }
        body {
            font-family: 'SF Pro Display', -apple-system, sans-serif;
            background: var(--dark);
            color: var(--light);
            overflow-x: hidden;
        }
        .bg {
            position: fixed; top: 0; left: 0; width: 100%; height: 100%;
            z-index: -1;
            background: radial-gradient(ellipse at 20% 20%, PLACEHOLDER_COLOR_OPACITY 0%, transparent 50%),
                        radial-gradient(ellipse at 80% 80%, rgba(102, 126, 234, 0.15) 0%, transparent 50%);
        }
        nav {
            position: fixed; top: 0; width: 100%;
            padding: 15px 50px;
            display: flex; justify-content: space-between; align-items: center;
            background: rgba(10, 10, 15, 0.95);
            backdrop-filter: blur(20px);
            z-index: 1000;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
        }
        .logo { font-size: 20px; font-weight: bold; cursor: pointer; }
        .back-btn {
            padding: 8px 20px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 50px; color: var(--light);
            cursor: pointer; text-decoration: none; font-size: 14px;
            transition: 0.3s;
        }
        .back-btn:hover { background: rgba(255, 255, 255, 0.2); }
        .hero {
            min-height: 50vh;
            display: flex; flex-direction: column;
            justify-content: center; align-items: center;
            text-align: center;
            padding: 120px 20px 60px;
        }
        .hero-badge {
            padding: 8px 20px;
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.3);
            border-radius: 50px;
            font-size: 14px;
            margin-bottom: 25px;
        }
        .hero h1 { font-size: 48px; margin-bottom: 15px; }
        .hero h1 span {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        }
        .hero p { font-size: 18px; opacity: 0.8; max-width: 600px; }
        
        .content { padding: 50px; max-width: 1200px; margin: 0 auto; }
        .features { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 25px; margin-bottom: 50px; }
        .feature-card {
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 15px; padding: 30px;
            transition: 0.3s;
        }
        .feature-card:hover {
            transform: translateY(-5px);
            border-color: rgba(255, 255, 255, 0.3);
            background: rgba(255, 255, 255, 0.05);
        }
        .feature-icon { font-size: 36px; margin-bottom: 15px; }
        .feature-card h3 { margin-bottom: 10px; }
        .feature-card p { opacity: 0.7; font-size: 14px; line-height: 1.6; }
        
        .demo-section {
            background: rgba(255, 255, 255, 0.02);
            border: 1px solid rgba(255, 255, 255, 0.2);
            border-radius: 20px; padding: 40px; margin-bottom: 50px;
        }
        .demo-section h2 { margin-bottom: 20px; }
        .chat-demo {
            background: rgba(0, 0, 0, 0.3);
            border-radius: 15px; padding: 20px;
            font-family: monospace;
        }
        .chat-line { margin-bottom: 10px; padding: 10px; border-radius: 8px; }
        .chat-user { background: rgba(0, 240, 255, 0.1); margin-left: 20px; }
        .chat-ai { background: rgba(255, 255, 255, 0.1); margin-right: 20px; }
        
        footer {
            padding: 50px; text-align: center;
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }
        .footer-links { display: flex; justify-content: center; gap: 30px; margin-bottom: 20px; }
        .footer-links a { color: var(--light); text-decoration: none; opacity: 0.6; transition: 0.3s; }
        .footer-links a:hover { opacity: 1; }
    </style>
</head>
<body>
    <div class="bg"></div>
    
    <nav>
        <div class="logo" onclick="window.location.href='index-spa.html'" style="background: linear-gradient(135deg, var(--primary), var(--secondary)); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">← OpenClaw</div>
        <a href="index-spa.html" class="back-btn">返回首页</a>
    </nav>
    
    <section class="hero">
        <div class="hero-badge">PLACEHOLDER_ICON Placeholder_TITLE</div>
        <h1>AI 驱动的 <span>Placeholder_TITLE</span></h1>
        <p>Placeholder_SUBTITLE</p>
    </section>
    
    <div class="content">
        <div class="features">
            <div class="feature-card">
                <div class="feature-icon">🤖</div>
                <h3>智能分析</h3>
                <p>AI 深度分析，提供专业洞察和决策支持</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">⚡</div>
                <h3>快速响应</h3>
                <p>毫秒级响应，即时获取所需信息</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🎯</div>
                <h3>精准推荐</h3>
                <p>个性化推荐，匹配你的独特需求</p>
            </div>
        </div>
        
        <div class="demo-section">
            <h2>💬 使用示例</h2>
            <div class="chat-demo">
                <div class="chat-line chat-user">Placeholder_DEMO_USER</div>
                <div class="chat-line chat-ai">Placeholder_DEMO_AI</div>
            </div>
        </div>
        
        <div style="text-align: center;">
            <a href="index-spa.html" class="back-btn" style="padding: 14px 35px; font-size: 15px;">🚀 立即体验</a>
        </div>
    </div>
    
    <footer>
        <div class="footer-links">
            <a href="index-spa.html">首页</a>
            <a href="index-spa.html#scenes">场景实验室</a>
            <a href="https://docs.openclaw.ai">文档中心</a>
        </div>
        <div style="opacity: 0.4; font-size: 13px;">© 2026 OpenClaw 中国社区</div>
    </footer>
</body>
</html>
'''

def generate_page(filename, config):
    content = TEMPLATE
    content = content.replace('PLACEHOLDER_TITLE', config['title'])
    content = content.replace('PLACEHOLDER_ICON', config['icon'])
    content = content.replace('Placeholder_TITLE', config['title'])
    content = content.replace('Placeholder_SUBTITLE', config['subtitle'])
    content = content.replace('PLACEHOLDER_COLOR', config['color'])
    content = content.replace('PLACEHOLDER_COLOR_OPACITY', f'rgba({config["color"][1:]}, 0.1)')
    content = content.replace('Placeholder_DEMO_USER', config['demo_user'])
    content = content.replace('Placeholder_DEMO_AI', config['demo_ai'].replace('\n', '<br>'))
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'✓ Generated: {filename}')

# 生成所有页面
base_path = r'C:\Users\dongd\Desktop\01_Projects\openclaw-cn'

for filename, config in PAGES.items():
    generate_page(os.path.join(base_path, filename), config)
