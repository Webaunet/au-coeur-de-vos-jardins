# Génère prestations.html, a-propos.html, contact.html (index.html est écrit à part) : python3 outils/gen_pages.py
import os,re
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
leaf='<svg viewBox="0 0 64 64" aria-hidden="true"><path d="M32 54V32M32 32C32 19 41 13 53 13c0 12-8 19-21 19ZM32 41C32 31 25 27 14 27c0 10 7 14 18 14Z" fill="none" stroke="#3f7a46" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/></svg>'
S='fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"'
phone=f'<svg viewBox="0 0 24 24" {S}><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/></svg>'
mail=f'<svg viewBox="0 0 24 24" {S}><rect x="3" y="5" width="18" height="14" rx="3"/><path d="m3 8 9 6 9-6"/></svg>'
pin=f'<svg viewBox="0 0 24 24" {S}><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/></svg>'
def ic(d,c='#1d2b22'):return f'<svg viewBox="0 0 64 64" fill="none" stroke="{c}" stroke-width="3.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{d}</svg>'
def nav(cur):
    it=[('index.html','Accueil'),('prestations.html','Prestations'),('a-propos.html','À propos'),('contact.html','Contact')]
    return ''.join(f'<a href="{h}"'+(' aria-current="page"' if h==cur else '')+f'>{t}</a>' for h,t in it)
def page(cur,title,desc,main):
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="noindex, nofollow">
<link rel="icon" href="images/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,700;12..96,800&family=Figtree:wght@400;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
</head>
<body>
<a class="skip" href="#contenu">Aller au contenu</a>
<header class="top">
  <div class="wrap">
    <a class="logo" href="https://webaunet.github.io/au-coeur-de-vos-jardins/" aria-label="Au Cœur de vos Jardins, accueil">{leaf}<span>Au Cœur de vos Jardins<small>Paysagiste · Beynes</small></span></a>
    <nav class="nav" aria-label="Navigation principale">{nav(cur)}</nav>
    <div class="top-actions">
      <a class="btn btn-apricot call" href="tel:+33683648818">{phone}<span>06 83 64 88 18</span></a>
      <button class="burger" type="button" aria-expanded="false" aria-controls="menu" aria-label="Ouvrir le menu"><svg class="b" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg><svg class="x" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"><path d="m6 6 12 12M18 6 6 18"/></svg></button>
    </div>
  </div>
  <nav class="menu" id="menu" aria-label="Menu mobile">{nav(cur)}</nav>
</header>
<main id="contenu">
{main}
</main>
<footer class="foot">
  <div class="wrap">
    <span>© <span id="an">2026</span> Au Cœur de vos Jardins · Beynes (78) · Maquette de démonstration</span>
    <nav aria-label="Pied de page"><a href="index.html">Accueil</a><a href="prestations.html">Prestations</a><a href="a-propos.html">À propos</a><a href="contact.html">Contact</a></nav>
  </div>
</footer>
<script src="js/main.js"></script>
</body>
</html>
'''
def im(n,alt,w=1000,h=545,lazy=True,extra=''):
    return f'<img src="images/{n}.jpg" width="{w}" height="{h}" alt="{alt}"'+(' loading="lazy"' if lazy else ' fetchpriority="high"')+f'{extra}>'

# ---------- PRESTATIONS ----------
presta=f'''<section class="page-head">
  <div class="wrap ph-grid">
    <div>
      <span class="eyebrow">Prestations</span>
      <h1 style="margin-top:18px">Aménager, planter, <em>entretenir</em>.</h1>
      <p class="lead">Un jardin réussi tient à la cohérence de l'ensemble. Voici les domaines dans lesquels Au Cœur de vos Jardins intervient autour de Beynes.</p>
      <div class="cta"><a class="btn btn-apricot" href="contact.html">Demander un devis</a><a class="btn btn-line" href="tel:+33683648818">{phone}Appeler</a></div>
    </div>
    <div class="mosaic">
      {im('allee-dallee',"Allée dallée éclairée le soir devant une maison en pierre, en cours d'aménagement",1000,545,False,' class="m1"')}
      {im('nivellement',"Jardinier ratissant une terre fraîchement nivelée au pied d'un massif",1000,545,False,' class="m2"')}
      {im('robot-tonte',"Robot tondeuse sur une pelouse bordée d'un muret en pierre et de massifs",1000,545,False,' class="m3"')}
    </div>
  </div>
</section>

<section class="band band-cream" id="amenager">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Aménager</span><h2>Donner une structure à votre extérieur.</h2><p>Avant de planter, on dessine : les circulations, les niveaux, les matériaux. C'est là que se joue la tenue du jardin dans le temps.</p></div>
    <div class="trio">
      <article class="panel">{im('conception-chantier',"Plan de jardin consulté sur une tablette avec le jardin aménagé en arrière-plan")}<div class="in"><h3>Conception du jardin</h3><ul class="ticks"><li>Plan de l'espace et des zones de vie</li><li>Choix des matériaux et des végétaux</li><li>Cohérence avec la maison existante</li></ul></div></article>
      <article class="panel">{im('terrasse-bois',"Pose d'une terrasse en bois devant une maison en pierre")}<div class="in"><h3>Terrasses et allées</h3><ul class="ticks"><li>Terrasses en bois ou en dalles</li><li>Allées en pavés, dalles ou stabilisé</li><li>Préparation et nivellement du sol</li></ul></div></article>
      <article class="panel">{im('maconnerie',"Muret en pierre sèche monté autour d'un escalier de jardin")}<div class="in"><h3>Murets et maçonnerie paysagère</h3><ul class="ticks"><li>Murets et soutènements en pierre</li><li>Marches et changements de niveau</li><li>Bordures de massifs</li></ul></div></article>
    </div>
  </div>
</section>

<section class="band band-sage" id="planter">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Planter</span><h2>Des végétaux choisis pour votre terre.</h2></div>
    <article class="row">
      <div class="row-img">{im('plantation',"Jardinier mettant en terre un végétal dans un massif")}</div>
      <div class="row-txt"><h3>Plantations et massifs</h3><p>Arbustes, vivaces et couvre-sols choisis selon l'exposition, le sol et l'entretien que vous souhaitez y consacrer.</p><a class="btn btn-dark" href="contact.html">Parler de mon projet</a></div>
    </article>
  </div>
</section>

<section class="band band-cream" id="entretenir">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Entretenir</span><h2>Garder le jardin net, toute l'année.</h2></div>
    <article class="row rev">
      <div class="row-img duo">{im('tonte',"Tonte d'une pelouse devant une maison en pierre et ses massifs")}{im('taille-haies',"Taille d'une haie de laurier au taille-haie")}</div>
      <div class="row-txt"><h3>Pelouse, haies et entretien</h3><p>Tonte, taille des haies et suivi des espaces verts : un entretien régulier qui préserve le travail d'aménagement.</p><a class="btn btn-dark" href="contact.html">Demander un devis</a></div>
    </article>
  </div>
</section>

<section class="band band-moss" id="etapes">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Étapes d'un projet</span><h2>De l'idée au premier été dans le jardin.</h2><p>Un projet d'aménagement suit en général quatre temps. Le détail s'ajuste à chaque chantier.</p></div>
    <div class="seasons">
      <div class="season s1">{ic('<path d="M10 14h44v26H30l-12 10V40H10Z"/>')}<h3>Échange</h3><p>On parle de votre jardin, de vos envies et de vos usages.</p></div>
      <div class="season s2">{ic('<path d="M12 52l6-18 26-26 12 12-26 26ZM38 14l12 12"/>')}<h3>Plan</h3><p>Le projet est dessiné et les choix de matériaux sont arrêtés.</p></div>
      <div class="season s3">{ic('<path d="M32 8v28M24 36h16l-3 20H27ZM20 14l12-6 12 6"/>')}<h3>Chantier</h3><p>Terrassement, ouvrages en dur puis plantations, dans l'ordre.</p></div>
      <div class="season s4">{ic('<rect x="10" y="14" width="44" height="40" rx="6"/><path d="M10 26h44M22 8v10M42 8v10"/>')}<h3>Suivi</h3><p>Le jardin s'installe ; l'entretien peut prendre le relais.</p></div>
    </div>
  </div>
</section>

<section class="band band-leaf" id="devis">
  <div class="wrap cta-band">
    <div><span class="eyebrow">Un projet précis</span><h2 style="margin-top:14px">Dites-nous ce que vous avez en tête.</h2><p>Terrasse à créer, massif à reprendre, pelouse à remettre en état : décrivez la situation et nous vous répondrons.</p><div class="cta" style="margin-top:28px"><a class="btn btn-apricot" href="contact.html">Demander un devis</a></div></div>
    <div class="cta-card"><a class="line" href="tel:+33683648818">{phone}06 83 64 88 18</a><a class="line" href="mailto:contact@aucoeurdevosjardins.com">{mail}contact@aucoeurdevosjardins.com</a></div>
  </div>
</section>'''

# ---------- A PROPOS ----------
apropos=f'''<section class="page-head">
  <div class="wrap ph-grid">
    <div>
      <span class="eyebrow">À propos</span>
      <h1 style="margin-top:18px">Un paysagiste de <em>Beynes</em>.</h1>
      <p class="lead">Au Cœur de vos Jardins est une société d'aménagement paysager créée en 2017 et dirigée par David Duarte.</p>
      <div class="cta"><a class="btn btn-apricot" href="contact.html">Nous contacter</a><a class="btn btn-line" href="prestations.html">Voir les prestations</a></div>
    </div>
    <div class="arch">{im('conception-chantier',"Deux personnes consultant le plan d'un jardin sur une tablette",1000,545,False,'')}</div>
  </div>
</section>

<section class="band band-cream" id="en-bref">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">L'entreprise en bref</span><h2>Une structure à taille humaine.</h2><p>Les informations ci-dessous proviennent de l'annuaire officiel des entreprises.</p></div>
    <div class="idcards">
      <div class="idc"><span>Forme</span><b>SARL</b></div>
      <div class="idc"><span>Création</span><b>Septembre 2017</b></div>
      <div class="idc"><span>Siège</span><b>Beynes (78650)</b></div>
      <div class="idc"><span>Activité</span><b>Aménagement paysager</b></div>
      <div class="idc"><span>Dirigeant</span><b>David Duarte</b></div>
      <div class="idc"><span>Équipe</span><b>Petite structure</b></div>
    </div>
  </div>
</section>

<section class="band band-moss" id="regard">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Notre regard</span><h2>Un jardin se pense avec son terrain.</h2></div>
    <div class="trio principles">
      <div class="pr">{ic('<path d="M8 50c8-12 16-18 24-18s16 6 24 18M32 32V12M22 20l10-8 10 8"/>','#f0a64b')}<h3>Partir du sol</h3><p>Exposition, pente, nature de la terre : le terrain dicte ce qui peut pousser et ce qui tiendra.</p></div>
      <div class="pr">{ic('<path d="M8 30 32 10l24 20v24H8Z"/><path d="M26 54V38h12v16"/>','#f0a64b')}<h3>Penser avec la maison</h3><p>Terrasse, allée et massifs prolongent l'habitation. Les matériaux dialoguent avec la façade.</p></div>
      <div class="pr">{ic('<circle cx="32" cy="32" r="22"/><path d="M32 18v14l9 6"/>','#f0a64b')}<h3>Voir dans la durée</h3><p>Un aménagement doit bien vieillir et rester simple à entretenir une fois les végétaux installés.</p></div>
    </div>
  </div>
</section>

<section class="band band-sage" id="beynes">
  <div class="wrap about">
    <div class="about-photo">{im('allee-paves',"Allée dallée bordée d'un muret en pierre et de massifs devant une maison")}</div>
    <div class="about-card">
      <span class="eyebrow">Autour de Beynes</span>
      <h2>Basés à Beynes, dans les Yvelines.</h2>
      <p>L'entreprise est installée à Beynes (78650). Pour savoir si votre commune peut être desservie, un appel suffit.</p>
      <a class="line-link" href="tel:+33683648818">{phone}06 83 64 88 18</a>
      <a class="btn btn-dark" href="contact.html" style="justify-self:start">Écrire à l'entreprise</a>
    </div>
  </div>
</section>

<section class="band band-leaf" id="rencontre">
  <div class="wrap cta-band">
    <div><span class="eyebrow">Faisons connaissance</span><h2 style="margin-top:14px">Le plus simple : en parler.</h2><p>Un appel ou un message, et nous prenons le temps de comprendre votre jardin.</p></div>
    <div class="cta-card"><a class="line" href="tel:+33683648818">{phone}06 83 64 88 18</a><a class="line" href="mailto:contact@aucoeurdevosjardins.com">{mail}contact@aucoeurdevosjardins.com</a><a class="btn btn-dark" href="contact.html">Ouvrir le formulaire</a></div>
  </div>
</section>'''

# ---------- CONTACT ----------
contact=f'''<section class="page-head compact">
  <div class="wrap">
    <span class="eyebrow">Contact</span>
    <h1 style="margin-top:18px">Parlons de votre <em>jardin</em>.</h1>
    <p class="lead">Appelez, écrivez ou remplissez le formulaire plus bas : un récapitulatif est préparé, prêt à être envoyé par SMS ou par e-mail.</p>
    <div class="tiles">
      <a class="tile" href="tel:+33683648818">{phone}<span><small>Téléphone</small>06 83 64 88 18</span></a>
      <a class="tile" href="mailto:contact@aucoeurdevosjardins.com">{mail}<span><small>E-mail</small>contact@aucoeurdevosjardins.com</span></a>
      <div class="tile">{pin}<span><small>Commune</small>Beynes (78650)</span></div>
    </div>
  </div>
</section>

<section class="band band-cream" id="formulaire">
  <div class="wrap contact-grid">
    <div class="form-card">
      <h2>Votre demande</h2>
      <form id="devis" novalidate>
        <div class="field"><label for="nom">Nom et prénom</label><input id="nom" name="nom" type="text" autocomplete="name" required aria-describedby="err-nom"><p class="err" id="err-nom" role="alert"></p></div>
        <div class="field"><label for="tel">Téléphone</label><input id="tel" name="tel" type="tel" autocomplete="tel" inputmode="tel" required aria-describedby="err-tel" placeholder="06 12 34 56 78"><p class="err" id="err-tel" role="alert"></p></div>
        <div class="field"><label for="commune">Commune du projet</label><input id="commune" name="commune" type="text" autocomplete="address-level2" required aria-describedby="err-commune"><p class="err" id="err-commune" role="alert"></p></div>
        <div class="field"><label for="besoin">Votre besoin</label><select id="besoin" name="besoin" required aria-describedby="err-besoin"><option value="">Choisir…</option><option>Conception de jardin</option><option>Terrasse ou allée</option><option>Muret ou maçonnerie paysagère</option><option>Plantations et massifs</option><option>Pelouse, haies et entretien</option><option>Autre projet</option></select><p class="err" id="err-besoin" role="alert"></p></div>
        <div class="field"><label for="message">Message <span class="opt">(facultatif)</span></label><textarea id="message" name="message" rows="4"></textarea></div>
        <button class="btn btn-apricot full" type="submit">Préparer mon message</button>
      </form>
      <div class="recap" id="recap" hidden tabindex="-1">
        <h3>Votre message est prêt</h3>
        <p>Choisissez comment l'envoyer. Rien n'est transmis tant que vous n'avez pas envoyé le message vous-même.</p>
        <pre id="recap-text"></pre>
        <div class="cta">
          <a class="btn btn-dark" id="r-sms" href="sms:+33683648818">Envoyer par SMS</a>
          <a class="btn btn-dark" id="r-mail" href="mailto:contact@aucoeurdevosjardins.com">Envoyer par e-mail</a>
          <button class="btn btn-line dark" id="r-copy" type="button">Copier</button>
          <a class="btn btn-line dark" href="tel:+33683648818">Appeler</a>
        </div>
        <p class="ok" id="r-ok" role="status"></p>
      </div>
    </div>
    <aside class="side">
      <h2>Votre projet, notre métier.</h2>
      <p>Plus la description est précise, plus la réponse sera utile. Une surface approximative, une envie ou une contrainte suffisent pour commencer.</p>
      <div class="side-photo">{im('creation',"Jardinier au travail dans un massif devant une maison contemporaine")}</div>
    </aside>
  </div>
</section>

<section class="band band-sage" id="preparer">
  <div class="wrap">
    <div class="sec-head"><span class="eyebrow">Pour un échange efficace</span><h2>Trois choses utiles à nous dire.</h2></div>
    <div class="seasons three">
      <div class="season s1">{ic('<rect x="8" y="8" width="48" height="48" rx="6"/><path d="M8 24h48M24 8v48"/>')}<h3>La surface</h3><p>Une idée approximative de la taille de l'espace concerné suffit.</p></div>
      <div class="season s2">{ic('<path d="M32 54 12 34a12 12 0 0 1 20-14 12 12 0 0 1 20 14Z"/>')}<h3>Vos envies</h3><p>Usages, ambiance, contraintes : ce que vous voulez faire de ce jardin.</p></div>
      <div class="season s4">{ic('<rect x="8" y="16" width="48" height="36" rx="6"/><circle cx="32" cy="34" r="9"/><path d="M22 16l4-6h12l4 6"/>')}<h3>Des photos</h3><p>Quelques vues du lieu aident à comprendre le terrain avant tout déplacement.</p></div>
    </div>
  </div>
</section>'''

for f,t,d,m in (('prestations.html','Prestations d\'aménagement paysager à Beynes (78) | Au Cœur de vos Jardins','Conception, terrasses, allées, murets, plantations et entretien : les prestations d\'Au Cœur de vos Jardins, paysagiste à Beynes (78).',presta),
 ('a-propos.html','À propos | Au Cœur de vos Jardins, paysagiste à Beynes (78)','Au Cœur de vos Jardins, société d\'aménagement paysager créée en 2017 à Beynes (78), dirigée par David Duarte.',apropos),
 ('contact.html','Contact et devis | Au Cœur de vos Jardins, Beynes (78)','Contactez Au Cœur de vos Jardins à Beynes (78) : formulaire de demande, téléphone et e-mail pour votre projet de jardin.',contact)):
    open(os.path.join(R,f),'w',encoding='utf-8').write(page(f,t,d,m))
