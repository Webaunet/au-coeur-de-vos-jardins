# Génère un index.html autonome (CSS, JS et images intégrés) pour l'artefact : python3 outils/build_artifact.py <sortie>
import re,base64,sys,os
r=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
h=open(r+'/index.html',encoding='utf-8').read()
css=open(r+'/css/style.css',encoding='utf-8').read();js=open(r+'/js/main.js',encoding='utf-8').read()
def b(path,mime):return f'data:{mime};base64,'+base64.b64encode(open(r+'/'+path,'rb').read()).decode()
h=h.replace('<link rel="stylesheet" href="css/style.css">','<style>'+css+'</style>').replace('<script src="js/main.js"></script>','<script>'+js+'</script>')
h=h.replace('images/favicon.svg',b('images/favicon.svg','image/svg+xml'))
h=re.sub(r'images/([a-z\-]+\.jpg)',lambda m:b('images/'+m.group(1),'image/jpeg'),h)
os.makedirs(os.path.dirname(sys.argv[1]),exist_ok=True);open(sys.argv[1],'w',encoding='utf-8').write(h)
