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
