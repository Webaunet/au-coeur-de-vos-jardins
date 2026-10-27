# Test unique : python3 outils/test.py [dossier_site]  -> n'affiche que les anomalies, sinon "tout est OK"
import sys,os,re,glob,http.server,threading,functools
from playwright.sync_api import sync_playwright
root=os.path.abspath(sys.argv[1] if len(sys.argv)>1 else '.')
H=functools.partial(http.server.SimpleHTTPRequestHandler,directory=root)
class Q(http.server.SimpleHTTPRequestHandler):
    def log_message(self,*a):pass
H=functools.partial(Q,directory=root)
srv=http.server.ThreadingHTTPServer(('127.0.0.1',0),H);port=srv.server_address[1]
threading.Thread(target=srv.serve_forever,daemon=True).start()
pages=[os.path.basename(p) for p in sorted(glob.glob(root+'/*.html'))]
bad=[]
JS='''()=>{const r=[];const vw=innerWidth,vh=innerHeight;
if(document.documentElement.scrollWidth>vw)r.push('debordement horizontal '+document.documentElement.scrollWidth);
document.querySelectorAll('p,li,a,span,small,label,h1,h2,h3,button,input,select,textarea').forEach(e=>{if(!e.offsetParent&&getComputedStyle(e).position!=='fixed')return;if(![...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim()))return;const f=parseFloat(getComputedStyle(e).fontSize);if(f<15.9)r.push('texte '+f.toFixed(1)+'px: '+e.textContent.trim().slice(0,25))});
document.querySelectorAll('a,button,input,select,textarea').forEach(e=>{if(!e.offsetParent)return;const b=e.getBoundingClientRect();if(e.closest('.foot nav,.skip'))return;if(b.width&&(b.height<43.5||(b.width<43.5)))r.push('cible '+Math.round(b.width)+'x'+Math.round(b.height)+': '+(e.textContent.trim().slice(0,20)||e.className))});
document.querySelectorAll('img').forEach(i=>{if(i.complete&&i.naturalWidth===0)r.push('image cassee '+i.alt.slice(0,20));const b=i.getBoundingClientRect();if(i.naturalWidth&&b.width>i.naturalWidth+1)r.push('image agrandie '+i.alt.slice(0,20))});
document.querySelectorAll('main > section').forEach(s=>{const h=s.getBoundingClientRect().height/vh;if(h>1.2)r.push('section haute '+s.className+' '+h.toFixed(2)+'vh')});
const f=document.querySelector('footer');if(f&&f.getBoundingClientRect().height>vh*.3)r.push('footer>30% '+Math.round(f.getBoundingClientRect().height));
const h1=document.querySelectorAll('h1').length;if(h1!==1)r.push('h1 x'+h1);
return r}'''
with sync_playwright() as p:
    br=p.chromium.launch()
    for w,hh in ((390,844),(768,1024),(981,800),(1280,800),(1920,1080)):
        pg=br.new_page(viewport={'width':w,'height':hh})
        for f in pages:
            pg.goto(f'http://127.0.0.1:{port}/{f}');pg.wait_for_timeout(300)
            for m in pg.evaluate(JS): bad.append(f'{f}@{w}: {m}')
        pg.close()
    # liens internes + poids
    for f in pages:
        t=open(os.path.join(root,f),encoding='utf-8').read()
        for l in re.findall(r'(?:href|src)="([^"#:]+)"',t):
            if not l.startswith('http') and not l.endswith('.html') and not os.path.exists(os.path.join(root,l)) and l not in pages: bad.append(f'{f}: lien/fichier absent {l}')
    for i in glob.glob(root+'/images/*'):
        if os.path.getsize(i)>250000: bad.append('image >250Ko '+os.path.basename(i))
    br.close()
print('\n'.join(sorted(set(bad))) if bad else 'tout est OK')
