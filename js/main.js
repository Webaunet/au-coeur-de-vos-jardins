(function(){
  var b=document.querySelector('.burger'),m=document.getElementById('menu');
  if(!b||!m)return;
  function set(o){b.setAttribute('aria-expanded',o);b.setAttribute('aria-label',o?'Fermer le menu':'Ouvrir le menu');m.classList.toggle('open',o)}
  b.addEventListener('click',function(){set(b.getAttribute('aria-expanded')!=='true')});
  m.addEventListener('click',function(e){if(e.target.closest('a'))set(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&m.classList.contains('open')){set(false);b.focus()}});
  window.matchMedia('(min-width:981px)').addEventListener('change',function(e){if(e.matches)set(false)});
  var y=document.getElementById('an');if(y)y.textContent=new Date().getFullYear();
})();
(function(){
  var f=document.getElementById('devis');if(!f)return;
  var recap=document.getElementById('recap'),txt=document.getElementById('recap-text'),ok=document.getElementById('r-ok');
  var TEL=/^(?:(?:\+|00)33|0)[1-9](?:[\s.-]?\d{2}){4}$/;
  function err(id,msg){var i=document.getElementById(id),e=document.getElementById('err-'+id);if(!e)return;e.textContent=msg||'';if(msg){i.setAttribute('aria-invalid','true')}else{i.removeAttribute('aria-invalid')}}
  function check(){
    var v={nom:f.nom.value.trim(),tel:f.tel.value.trim(),commune:f.commune.value.trim(),besoin:f.besoin.value,message:f.message.value.trim()},bad=null;
    function fail(id,m){err(id,m);if(!bad)bad=id}
    err('nom');err('tel');err('commune');err('besoin');
    if(v.nom.length<2)fail('nom','Indiquez votre nom et prénom.');
    if(!v.tel)fail('tel','Indiquez votre numéro de téléphone.');else if(!TEL.test(v.tel))fail('tel','Numéro non valide. Exemple : 06 12 34 56 78.');
    if(v.commune.length<2)fail('commune','Indiquez la commune du projet.');
    if(!v.besoin)fail('besoin','Choisissez votre besoin dans la liste.');
    if(bad){document.getElementById(bad).focus();return null}
    return v;
  }
  f.addEventListener('submit',function(e){
    e.preventDefault();var v=check();if(!v)return;
    var t='Bonjour, je souhaite un devis.\nBesoin : '+v.besoin+'\nCommune : '+v.commune+'\nNom : '+v.nom+'\nTéléphone : '+v.tel+(v.message?'\nMessage : '+v.message:'');
    txt.textContent=t;
    document.getElementById('r-sms').href='sms:+33683648818?body='+encodeURIComponent(t);
    document.getElementById('r-mail').href='mailto:contact@aucoeurdevosjardins.com?subject='+encodeURIComponent('Demande de devis - '+v.besoin)+'&body='+encodeURIComponent(t);
    ok.textContent='';recap.hidden=false;recap.scrollIntoView({behavior:'smooth',block:'center'});recap.focus({preventScroll:true});
  });
  ['nom','tel','commune','besoin'].forEach(function(id){document.getElementById(id).addEventListener('input',function(){err(id)})});
  document.getElementById('r-copy').addEventListener('click',function(){
    var t=txt.textContent;
    function done(m){ok.textContent=m}
    function fallback(){var r=document.createRange();r.selectNodeContents(txt);var s=getSelection();s.removeAllRanges();s.addRange(r);try{done(document.execCommand('copy')?'Message copié.':'Texte sélectionné : copiez-le avec Ctrl+C.')}catch(x){done('Texte sélectionné : copiez-le avec Ctrl+C.')}}
    if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(t).then(function(){done('Message copié.')},fallback)}else fallback();
  });
})();
