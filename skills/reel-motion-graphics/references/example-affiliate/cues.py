# Sound cues for the affiliate announcement. Executed by scripts/sfx.py with T, DUR, cue() in scope.
# ── intro / cover ──
cue(0.05, 'impact-bass-1')                       # GREETINGS lands on the green
cue(0.7, 'whoosh-short', 0.8)                    # "my friends." slides in
cue(T['today'] - 0.5, 'whoosh', 1.0, 'peak')     # green wipes up
cue(T['huge'] + 0.25, 'impact-bass-2')   # AFFILIATE assembles
cue(T['program'], 'pop')
cue(T['program'] + 0.3, 'click-soft')            # barcode
cue(T['thinking'] - 0.3, 'whoosh-short', 0.7, 'peak')
# ── genesis chat ──
cue(T['genesis'], 'whoosh-short')
cue(T['genesis'] + 0.4, 'typing')
cue(T['genesis'] + 2.1, 'typing', 0.8)
# ── course / acclaim / stores ──
cue(T['latest'], 'whoosh-short')
cue(T['latest'] + 0.9, 'pop', 0.7)
for i in range(5): cue(T['acclaim'] + i * 0.09, 'pop', 0.55)
cue(T['acclaim'] + 0.45, 'sparkle')
for i in range(5):  # review cards land on the pile
    cue(T['acclaim'] + 0.55 + i * 1.25, 'whoosh-short', 0.6); cue(T['acclaim'] + 0.75 + i * 1.25, 'pop', 0.7)
cue(T['oldstore'] - 0.6, 'whoosh-short')
cue(T['scratch'] - 0.5, 'whoosh-short', 0.9)
cue(T['scratch'] - 0.3, 'error', 0.6)            # old store gets struck through
cue(T['scratch'] - 0.2, 'pop')
# ── simple / who ──
cue(T['simple'] + 0.1, 'impact-bass-1', 0.6)
cue(T['iflike'], 'whoosh-short')
cue(T['enrolled'], 'pop'); cue(T['friends'], 'pop'); cue(T['friends'] + 2.2, 'pop', 0.6)
# ── phone walkthrough ──
cue(T['gostore'] - 0.2, 'whoosh')
cue(T['gostore'], 'pop', 0.7)
cue(T['product'] - 0.05, 'click'); cue(T['product'], 'pop', 0.7); cue(T['product'] + 0.1, 'whoosh-short', 0.6)
cue(T['icon'] - 0.05, 'click'); cue(T['icon'], 'pop', 0.7); cue(T['icon'] + 0.35, 'whoosh-short', 0.6)
cue(T['asaff'] + 1.2, 'click')
cue(T['yourpage'], 'notification'); cue(T['yourpage'], 'pop', 0.7)
# ── share chips ──
cue(T['videos'] - 0.2, 'whoosh-short', 0.7)
cue(T['videos'], 'pop'); cue(T['posts'], 'pop'); cue(T['live'], 'pop')
# ── why list ──
cue(T['point'], 'whoosh-short')
for k in ('outlet', 'cut', 'thanks', 'word'): cue(T[k], 'pop', 0.8)
# ── clock (ticks each second while it counts down) ──
cue(T['oneperson'], 'whoosh-short')
s = T['h24']
while s < T['friendsjoin'] - 0.4: cue(s, 'key-press', 0.8); s += 1.0
# ── friends multiplying ──
cue(T['friendsjoin'], 'pop')
for i in range(10): cue(T['friendsjoin'] + 0.5 + i * 0.12, 'pop' if i % 2 else 'click-soft', 0.45)
cue(T['friendsjoin'] + 1.8, 'pop', 0.6)
# ── incentives ──
cue(T['brandnew'], 'pop', 0.7)
cue(T['incent'] - 0.3, 'sparkle', 1.2)
# ── 30% hero: riser crests on the number landing, counter ticks, bass hit ──
land = T['p30'] + 0.4
cue(land, 'riser', 1.0, 'end')
cue(T['currently'], 'whoosh-short', 0.8)
for i in range(8): cue(T['p30'] - 0.6 + i * 0.11, 'key-press', 0.6)
cue(land, 'impact-bass-2')
cue(T['p30'] + 0.5, 'whoosh-short', 0.7)
# ── follow pill ──
cue(T['evenif'], 'whoosh-short')
cue(T['followme'] + 0.15, 'click')
cue(T['followme'] + 0.2, 'ping')
# ── deadline ──
cue(T['p30b'], 'whoosh-short')
cue(T['endyear'], 'whoosh-short', 0.6)
cue(T['twomonths'] - 0.2, 'pop', 0.7)
# ── 5 FREE hero ──
cue(T['five'], 'impact-bass-1')
cue(T['five'] + 0.6, 'pop', 0.6)
cue(T['five'] + 1.0, 'sparkle', 1.2)
# ── win-a-slot checklist ──
cue(T['wayslot'], 'whoosh-short')
for k in ('h_follow', 'h_comment', 'h_post', 'h_tag'): cue(T[k], 'pop', 0.7); cue(T[k] + 0.25, 'click-soft', 0.8)
cue(T['h_bot'], 'pop', 0.6)
# ── top 5 ──
cue(T['top5'], 'pop'); cue(T['promote'], 'pop', 0.6)
# ── refund flow ──
cue(T['onlyfive'], 'pop', 0.6)
cue(T['sample'] - 0.3, 'pop')
cue(T['twosales'] - 0.4, 'whoosh-short', 0.6); cue(T['twosales'], 'pop')
cue(T['refunded'] - 0.3, 'whoosh-short', 0.6); cue(T['refunded'], 'pop'); cue(T['refunded'] + 0.1, 'chime')
cue(T['forfree'] + 0.5, 'pop', 0.7)
cue(T['made30'] + 0.3, 'ping', 0.8)
# ── everybody wins ──
cue(T['wins'] + 0.1, 'impact-bass-2')
cue(T['wins'] + 0.5, 'sparkle', 1.2)
# ── group chat ──
cue(T['group'] - 0.3, 'whoosh-short')
for k in ('talkabout', 'kindposts', 'kindvideos', 'yourideas'): cue(T[k], 'pop', 0.7)
# ── live / give back / see you ──
cue(T['golive'], 'whoosh-short'); cue(T['golive'] + 0.5, 'ping', 0.6); cue(T['nothing'], 'pop', 0.6)
cue(T['giveback'], 'whoosh-short', 0.8); cue(T['giveback'] + 2.2, 'pop', 0.6)
cue(T['seeyou'], 'whoosh-short'); cue(T['commentsec'], 'pop'); cue(T['groupchat'], 'pop')
# ── RedNote eligibility ──
cue(T['steps'], 'whoosh-short')
cue(T['steps'] + 0.6, 'pop', 0.7); cue(T['rednote'] + 1.0, 'pop', 0.7)
cue(T['instantly'], 'pop', 0.7); cue(T['instantly'] + 0.1, 'ping', 0.7); cue(T['followers'], 'pop', 0.6)
# ── end CTA ──
cue(T['letmeknow'], 'whoosh-short')
cue(T['letmeknow'] + 0.5, 'typing')

