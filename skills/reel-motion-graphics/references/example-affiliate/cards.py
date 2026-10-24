# CARDS / FG for the affiliate announcement (2026-10-20). Executed by scripts/build.py with
# T, DUR, zh(), row(), TICK, CURSOR, STAR in scope.
# real reviews: (avatar initial, cohort · name, verbatim line, English gloss)
REVIEWS = [
    ('许', '第三期学员 · 许馨尹', '每次作业都有特别精细的点评', 'Every assignment gets really detailed feedback'),
    ('希', '第三期学员 · 希言', '这种陪伴式的学英语 真的太棒了', 'Learning English together like this is amazing'),
    ('A', '第三期学员 · April', '感觉英语对我来说变得越来越立体，也变成我生活的一部分', 'English feels more real now — part of my life'),
    ('F', '第三期学员 · Felicia', '能用更精准地道的方式说出来', 'I can say what I mean more precisely and naturally'),
    ('A', '第二期学员 · April', '有输入有输出，学到的知识得到巩固，记忆也更深刻', 'Input and output — what I learn actually sticks'),
]

# (id, start, end, track, extra-class, html). Times are keys into T or numbers.
CARDS = [
 # 0–3.3  green cold-open: speaker cut out over forest green, title behind her
 ('intro', 'greet', 'today', 2, 'hero', '''
   <div class="greenbg" id="introbg"></div>
   <div class="hero-zh" id="introZ" style="top:170px">朋友们，大家好</div>
   <div class="hero-word" id="introA" style="top:250px">GREETINGS</div>
   <div class="hero-ital" id="introB" style="top:420px;padding-left:120px">my friends.</div>'''),
 # 3.3–8.5  magazine-cover title behind her head
 ('cover', 'today', 'thinking', 2, 'hero', '''
   <div class="mast" id="coverK"><span>ELLA聊美语</span><span>重磅宣布 · ANNOUNCEMENT</span></div>
   <div class="rule" id="coverR"></div>
   <div class="hero-word big" id="coverA" style="top:230px">AFFILIATE</div>
   <div class="hero-ital" id="coverB" style="top:440px;padding-left:480px">program</div>
   <div class="hero-zh" id="coverZ" style="top:478px;padding-right:520px">带货推广计划</div>
   <div class="barcode" id="coverBar"><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><i></i><b>NOW OPEN · 正式开启</b></div>'''),
 # chat bar typing the question
 ('genesis', 'genesis', 'latest', 3, '', '''
   <div class="chat" style="top:180px"><div class="chat-k">ASK ELLA · 问问 ELLA</div>
   <div class="chat-row"><span class="chat-t" id="genT"></span><span class="caret"></span><span class="send">&#8593;</span></div>
   <div class="chat-zh" id="genZ"></div></div>'''),
 # course card
 ('course', 'latest', 'acclaim', 3, '', f'''
   <div class="gcard course" style="top:130px">
     <div class="thumb"><span>VLOG</span><small>EN · 中文</small></div>
     <div><div class="kick">LATEST COURSE · 网课第三期</div>
     <div class="serif t1">Learn Spoken English</div><div class="serif t1"><em>with Vlogs</em></div>
     {zh('跟着 Vlog 学英语口语', 'lg')}
     <div class="pill">Bootcamp #3 · 第三期</div></div></div>'''),
 # 5 stars, then real student reviews (verbatim lines from her course group chat, 2026-09-19) pile up
 ('acclaim', 'acclaim', 'newstore', 3, '', f'''
   <div class="center-block" style="top:95px"><div class="stars" id="stars">{STAR*5}</div></div>
   <div class="pile" style="top:235px">{''.join(
     f'<div class="rev" id="rev{i}"><div class="r-av">{ini}</div><div class="r-body"><div class="r-who">{who}</div>'
     f'<div class="r-q">“{q}”</div><div class="r-en">{en}</div></div></div>'
     for i, (ini, who, q, en) in enumerate(REVIEWS))}</div>'''),
 # old store vs new store
 ('stores', 'newstore', 'simple', 3, '', f'''
   <div class="gcard store" id="oldS" style="top:120px;left:60px">
     <div class="kick">OLD STORE · 旧店铺</div><div class="stars sm">{STAR*5}</div>
     <div class="bars"><i></i><i></i><i></i></div><div class="lbl">reviews · testimonials{zh('好评 · 学员反馈')}</div><div class="strike" id="oldX"></div></div>
   <div class="gcard store new" id="newS" style="top:120px;left:560px">
     <div class="kick">NEW STORE · 新店铺</div><div class="zero">0</div><div class="lbl">reviews — starting from scratch{zh('条评价 · 从零开始')}</div></div>'''),
 ('simple', 'simple', 'iflike', 3, '', f'''
   <div class="center-block" style="top:200px"><div class="serif display">The idea is <em>simple.</em></div>{zh('其实很简单', 'blk xl')}</div>'''),
 # who can join
 ('who', 'iflike', 'gostore', 3, '', f'''
   <div class="gcard list" style="top:130px"><div class="kick">WHO CAN JOIN · 谁可以参加</div>
     {row('who1', "You've taken my course", '上过我的课')}
     {row('who2', "You think it'd help a friend", '觉得对朋友有帮助')}
     <div class="row dim" id="who3"><span class="hand">either one works &rarr; {zh('都可以！', 'hz')}</span></div></div>'''),
 # store -> product -> icon -> affiliate (phone mock)
 ('howto', 'gostore', 'videos', 3, '', f'''
   <div class="phone" style="top:80px;left:40px">
     <div class="ph-bar">Ella's store · 店铺</div>
     <div class="ph-grid" id="phGrid"><div class="ph-item hot" id="phItem"><div class="ph-img">VLOG</div><span>Bootcamp #3</span></div>
       <div class="ph-item"><div class="ph-img alt"></div><span>&nbsp;</span></div></div>
     <div class="ph-detail" id="phDet"><div class="ph-img big">VLOG</div><div class="ph-title">Learn Spoken English with Vlogs</div>
       <div class="ph-icons"><span class="ic"></span><span class="ic"></span><span class="ic aff" id="phIcon">%</span></div></div>
     <div class="ph-sheet" id="phSheet"><b>Promote as affiliate · 推广带货</b><span>Earn commission on every sale<br>每卖出一单都有佣金</span><div class="ph-btn" id="phBtn">Add to my page<br>添加到主页</div></div>
     <div class="ph-toast" id="phToast">{TICK}<span>Added to your page<br>已添加到你的主页</span></div>
     {CURSOR}</div>
   <div class="steps" style="top:130px;left:455px">
     <div class="step" id="st1"><b>1</b><span>Go to my store{zh('进我的店铺')}</span></div>
     <div class="step" id="st2"><b>2</b><span>Tap the product{zh('点进商品')}</span></div>
     <div class="step" id="st3"><b>3</b><span>Tap this icon{zh('点这个图标')}</span></div>
     <div class="step" id="st4"><b>4</b><span>It's on your page{zh('出现在你的主页')}</span></div></div>'''),
 # where to share
 ('share', 'videos', 'point', 3, '', f'''
   <div class="kick center" style="top:150px" id="shK">SHARE IT IN YOUR&hellip; · 分享到你的&hellip;</div>
   <div class="chips" style="top:210px"><div class="chip" id="ch1">Videos{zh('视频')}</div><div class="chip" id="ch2">Posts{zh('笔记')}</div><div class="chip live" id="ch3"><i></i>Live{zh('直播')}</div></div>'''),
 # why do this — builds 4 reasons
 ('why', 'point', 'oneperson', 3, '', f'''
   <div class="gcard list why" style="top:90px"><div class="kick">WHY AN AFFILIATE PROGRAM · 为什么做这个</div>
     {row('why1', 'An outlet to talk about the course', '有个渠道聊聊这门课', '<b class="num">01</b>')}
     {row('why2', 'You get a <em>cut</em>', '你能拿到分成', '<b class="num">02</b>')}
     {row('why3', 'A thank-you to my students', '感谢我的学员', '<b class="num">03</b>')}
     {row('why4', 'Spread the word', '让更多人知道', '<b class="num">04</b>')}</div>'''),
 # one person, 24 hours
 ('clock', 'oneperson', 'friendsjoin', 3, '', f'''
   <div class="clockbox" style="top:140px"><div class="kick">ONE PERSON · ONE DAY</div>{zh('只有我一个人 · 一天只有 24 小时', 'ck')}<div class="digits" id="clk">24:00:00</div></div>'''),
 # many friends
 ('friends', 'friendsjoin', 'brandnew', 3, '', f'''
   <div class="dots" style="top:150px" id="dots">
     <div class="av me">Ella</div>''' + ''.join(f'<div class="av f" style="--i:{i}"></div>' for i in range(10)) + f'''
     <div class="hand dlab" id="dlab">+ you {zh('+ 你', 'hz')}</div></div>
   <div class="kick center" style="top:520px" id="dK">MORE FRIENDS · 更多朋友一起来</div>'''),
 ('incent', 'brandnew', 'currently', 3, '', f'''
   <div class="center-block" style="top:180px"><div class="kick" id="inK">BRAND-NEW PROGRAM · 全新计划</div>
   <div class="serif display" id="inT">so&hellip; <em>incentives.</em>{zh('上福利！', 'blk xl')}</div></div>'''),
 # 30% behind her head
 ('p30', 'currently', 'evenif', 2, 'hero', '''
   <div class="mast" id="p30K"><span>LAUNCH OFFER · 首发福利</span><span>FOR EVERYONE · 人人有份</span></div>
   <div class="hero-word huge" id="p30N" style="top:190px"><span id="p30V">0</span>%</div>
   <div class="hero-ital" id="p30C" style="top:500px">commission <u class="zh hz-gold">佣金</u></div>'''),
 # follow pill
 ('follow', 'evenif', 'p30b', 3, '', f'''
   <div class="follow" style="top:220px"><div class="f-av">E</div><div class="f-name"><b>Ella聊美语</b><span>English · vlogs · courses</span><span>英语 · vlog · 网课</span></div>
     <div class="f-btn" id="fBtn"><span id="fTxt">Follow · 关注</span></div>{CURSOR}</div>'''),
 # deadline
 ('deadline', 'p30b', 'five', 3, '', f'''
   <div class="gcard dl" style="top:120px"><div class="kick">30% FOR EVERYBODY UNTIL</div>{zh('人人 30% 佣金，截止到', 'ck')}
     <div class="serif t1 big">Dec 31 <span class="zh-inline">12月31日</span></div>
     <div class="track"><div class="fill" id="dlFill"></div></div>
     <div class="dl-lbl"><span>NOV 11月</span><span id="dlLeft">~2 months left · 还剩约两个月</span><span>DEC 12月</span></div></div>'''),
 # 5 free behind her head
 ('five', 'five', 'wayslot', 2, 'hero', '''
   <div class="mast" id="fvK"><span>GIVEAWAY · 福利</span><span>5 SLOTS ONLY · 仅限 5 人</span></div>
   <div class="hero-word huge sm" id="fvN" style="top:225px">5 FREE</div>
   <div class="hero-ital" id="fvC" style="top:505px;font-size:104px">courses + textbooks</div>
   <div class="hero-zh" id="fvZ" style="top:160px;font-size:52px">免费送 5 套课程 + 教材</div>'''),
 # how to win a slot — checklist
 ('slot', 'wayslot', 'top5', 3, '', f'''
   <div class="gcard list slot" style="top:80px"><div class="kick">HOW TO WIN A FREE SLOT · 如何获得免费名额</div>
     {row('sl1', 'Follow me', '关注我')}
     {row('sl2', 'Comment <em>why</em> you want it', '留言说说你为什么想要')}
     <small class="botnote" id="slBot">no bot comments · 别发机器人式评论</small>
     {row('sl3', 'Make an authentic post', '发一篇真诚的笔记')}
     {row('sl4', 'Tag me', '@我')}</div>'''),
 ('top5', 'top5', 'onlyfive', 3, '', f'''
   <div class="center-block" style="top:140px"><div class="ribbon" id="t5R">I'll pick the <b>TOP 5</b> · 选出前 5 名</div>
   <div class="serif quote" id="t5Q">&ldquo;how can you promote it<br>without having it?&rdquo;{zh('没有产品，怎么推广？', 'blk lg')}</div></div>'''),
 # sample -> 2 sales -> refunded
 ('refund', 'onlyfive', 'wins', 3, '', f'''
   <div class="kick center" style="top:110px" id="rfK">DIDN'T GET A SLOT? · 没抢到名额？</div>
   <div class="flow" style="top:165px">
     <div class="node" id="rf1"><small>STEP 1</small>Buy / request<br>a sample{zh('购买 / 申请样品')}</div><div class="arr" id="rfA1"></div>
     <div class="node" id="rf2"><small>STEP 2</small>Make<br><b>2 sales</b>{zh('卖出 2 单')}</div><div class="arr" id="rfA2"></div>
     <div class="node gold" id="rf3"><small>STEP 3</small>Purchase<br><b>refunded</b>{zh('课程费退还')}</div></div>
   <div class="eq" style="top:470px" id="rfEq">course <b>FREE</b> &nbsp;+&nbsp; <b>30%</b> commission{zh('课程免费 + 30% 佣金', 'blk lg')}</div>'''),
 ('wins', 'wins', 'basic', 2, 'hero', '''
   <div class="hero-zh" id="wnZ" style="top:170px">皆大欢喜</div>
   <div class="hero-word" id="wnA" style="top:250px">EVERYBODY</div>
   <div class="hero-ital" id="wnB" style="top:470px;padding-left:200px">wins.</div>'''),
 # affiliate group chat
 ('group', 'basic', 'golive', 3, '', f'''
   <div class="gchat" style="top:90px"><div class="gc-head"><span class="gc-ic">&#9679;&#9679;&#9679;</span><b>Affiliate Club · 带货群</b><small>group chat</small></div>
     <div class="bub l" id="gb1">what should I talk about?{zh('该聊些什么？')}</div>
     <div class="bub r" id="gb2">ideas for posts{zh('笔记怎么写')}</div>
     <div class="bub l" id="gb3">and what videos to make{zh('拍什么视频')}</div>
     <div class="bub r" id="gb4">+ your ideas too{zh('也欢迎你的想法')}</div></div>'''),
 ('live', 'golive', 'giveback', 3, '', f'''
   <div class="livebox" style="top:130px"><div class="livepill" id="lvP"><i></i>LIVE · 直播</div>
     <div class="serif t1">Go live <em>with me</em></div>{zh('和我一起直播', 'blk xl')}
     <div class="hand" id="lvH">nothing's certain yet &mdash; let's brainstorm together{zh('还没定，一起头脑风暴', 'blk hz')}</div></div>'''),
 ('giveback', 'giveback', 'seeyou', 3, '', f'''
   <div class="center-block" style="top:150px"><div class="kick">REALLY, IT'S · 其实这是</div>
   <div class="serif display">a way to <em>give back</em></div>{zh('回馈大家的一种方式', 'blk xl')}
   <div class="hand" id="gbH">to students who already talk about it{zh('感谢一直在帮我宣传的学员', 'blk hz')}</div></div>'''),
 # see you in the comments
 ('seeyou', 'seeyou', 'steps', 3, '', f'''
   <div class="cbox" style="top:180px"><div class="kick">SEE YOU IN · 我们在这里见</div>
     <div class="c-row" id="sy1"><span class="c-dot"></span><span>the comment section{zh('评论区')}</span></div>
     <div class="c-row" id="sy2"><span class="c-dot"></span><span>the group chat{zh('群聊')}</span></div></div>'''),
 # RedNote eligibility
 ('rednote', 'steps', 'letmeknow', 3, '', f'''
   <div class="gcard list rn" style="top:90px"><div class="kick"><span class="rn-chip">小红书</span> AFFILIATE ELIGIBILITY · 带货资格</div>
     {row('rn1', 'A few steps to qualify', '需要完成几个步骤')}
     {row('rn2', "Shouldn't take long", '不会花太久')}
     {row('rn3', 'Ella: qualified <em>instantly</em>', '我是秒开通的')}
     {row('rn4', 'Maybe a follower minimum', '可能有粉丝数门槛', TICK, 'dim')}</div>'''),
 # end CTA
 ('end', 'letmeknow', DUR, 3, '', '''
   <div class="cta" style="top:120px"><div class="cta-t">Qualified? <em>Let me know</em> &darr;<u class="zh blk">开通了？评论区告诉我</u></div>
     <div class="cinput"><span class="c-av">U</span><span class="chat-t" id="endT"></span><span class="caret"></span><span class="send">&#8593;</span></div></div>'''),
]


# speaker cut-out windows (scripts/matte.py) under each hero title
FG = [('fg-intro', 0.0, 8.6), ('fg-30', 114.2, 123.0), ('fg-5free', 139.8, 147.6), ('fg-wins', 199.7, 202.4)]
