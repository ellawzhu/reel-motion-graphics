# NEUTRAL COLORS starter (demo on "how i've learned English", first ~40 s). Executed by build.py.
THEME = 'neutral-colors'
CARDS = [
 ('nTitle', 'howlearn', 'bg', 2, '', '''
   <div class="n-title" style="top:150px"><div class="big">How I <em>Learned</em></div><div class="caps">ENGLISH</div><div class="zh">我是怎么学英语的</div></div>
   <div class="n-pill" id="nPill" style="top:1250px;left:120px">3 Phases → Fluent<u class="zh">三个阶段，学到流利</u></div>'''),
 ('nIris', 'bg', 'chinese', 4, '', '<div class="n-iris" id="iris1"></div>'),
 ('nStep', 'chinese', 'math', 2, '', '''
   <div class="sparkles" style="top:150px"><i></i><i></i><i></i><i></i><i></i></div>
   <div class="n-step" style="top:200px"><span class="lbl">Step 0:</span><span class="ttl">My Background</span><u class="zh">我的背景</u></div>'''),
 ('nCard', 'seattle', 'math', 3, '', '''
   <div class="n-card" style="top:1200px;left:120px;width:760px"><div class="hd">The <em>short</em> version<u class="zh">简单来说</u></div>
     <div class="n-row" id="nr1">Born &amp; raised in China<u class="zh">土生土长的中国人</u></div>
     <div class="n-row" id="nr2">Seattle at 17<u class="zh">17 岁去了西雅图</u></div>
     <div class="n-row" id="nr3">1 year of self-study first<u class="zh">出国前自学一年</u></div></div>'''),
 ('nComment', 'math', 'reality', 3, '', '''
   <div class="n-card" style="top:1180px;left:120px;width:760px"><div class="hd">Comments<u class="zh">评论</u></div>
     <div class="n-row">“It's just the environment.”<u class="zh">只是因为语言环境</u></div>
     <div class="n-input"><span id="nType"></span><span class="send">&#8593;</span></div></div>'''),
]
FG = []
