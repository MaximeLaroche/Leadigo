from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs"


def rep(text, old, new, count=1):
    found = text.count(old)
    if found != count:
        raise SystemExit(f"Replacement count mismatch for {old[:90]!r}: found {found}, expected {count}")
    return text.replace(old, new)


def common_fr(text):
    text = text.replace('<html lang="en"', '<html lang="fr"')
    text = text.replace("label: 'System'", "label: 'Système'")
    text = text.replace("label: 'Light'", "label: 'Clair'")
    text = text.replace("label: 'Dark'", "label: 'Sombre'")
    text = text.replace("themeTip.textContent = 'Theme: ' + themeMeta[theme].label;", "themeTip.textContent = 'Thème : ' + themeMeta[theme].label;")
    text = text.replace('aria-label="Theme: system, light, or dark"', 'aria-label="Thème : système, clair ou sombre"')
    text = text.replace('>Theme: System</span>', '>Thème : Système</span>')
    text = text.replace("themeToggle.setAttribute('aria-label', 'Theme: ' + themeMeta[theme].label + ' (click to switch)');", "themeToggle.setAttribute('aria-label', 'Thème : ' + themeMeta[theme].label + ' (cliquez pour changer)');")
    text = rep(text, ">Connect</span>", ">Suivez-nous</span>")
    text = rep(text, "Let's Stay In Touch", "Restons en contact")
    text = rep(text, "Follow along, see the work, or reach out directly — whichever works best for you.", "Suivez le travail, voyez les résultats ou contactez-nous directement — comme vous préférez.")
    text = rep(text, ">Email</span>", ">Courriel</span>")
    text = rep(text, "Leadigo — Performance-Based Cold Email", "Leadigo — Prospection par courriel basée sur la performance")
    return text


def index_fr():
    text = (ROOT / "index.html").read_text(encoding="utf-8")
    text = common_fr(text)
    text = rep(text, "<title>Leadigo VSL | Performance-Based Cold Email</title>", "<title>Leadigo VSL | Prospection par courriel basée sur la performance</title>")
    text = rep(text, 'href="roi_calculator.html"', 'href="roi_calculator-fr.html"', 2)
    text = rep(text, 'src="roi_calculator.html"', 'src="roi_calculator-fr.html"', 1)

    pairs = [
        (">Proof</a>", ">Preuves</a>"),
        (">The Math</a>", ">Le calcul</a>"),
        (">FAQ</a>", ">FAQ</a>"),
        (">Book a Call</a>", ">Réserver un appel</a>"),
        ("The Ultimate B2B Growth Engine", "Le moteur de croissance B2B ultime"),
        ("""What If You Could Add a <span class="grad-text text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-blue-300">Predictable Flow of Qualified Sales Calls</span> to Your Calendar Every Month?""", """Et si vous pouviez ajouter un <span class="grad-text text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-blue-300">flux prévisible d’appels de vente qualifiés</span> à votre calendrier chaque mois&nbsp;?"""),
        ("— Without Spending a Dime Unless They Actually Show Up.", "— Sans dépenser un sou à moins qu’ils se présentent réellement."),
        ("Book Your Free Strategy Call", "Réservez votre appel stratégique gratuit", 2),
        ("No risk. You only pay when a qualified buyer books a call with you — every invoice means a real sales conversation is already on your calendar.", "Aucun risque. Vous payez seulement lorsqu’un acheteur qualifié réserve un appel avec vous — chaque facture signifie qu’une vraie conversation de vente est déjà à votre calendrier."),
        ("Prefer reading? Everything in the video is covered below, section by section — the problem, the system, the evidence, the math, and the guarantee.", "Vous préférez lire&nbsp;? Tout ce qui est dans la vidéo est couvert ci-dessous, section par section — le problème, le système, les preuves, le calcul et la garantie."),
        ("What We're Covering Today", "Ce que nous couvrons aujourd’hui"),
        ("The Problem: Unpredictable Pipeline", "Le problème : un pipeline imprévisible"),
        ("The Solution: Performance Cold Email", "La solution : le courriel à froid basé sur la performance"),
        ("Industry Evidence: Cold Email at Scale", "Preuves du secteur : le courriel à froid à grande échelle"),
        ("The Math: What You're Leaving Behind", "Le calcul : ce que vous laissez derrière"),
        ("How It Works: The 4-Step System", "Comment ça fonctionne : le système en 4 étapes"),
        ("What You Get: The Full Build-Out", "Ce que vous obtenez : l’installation complète"),
        ("Your Questions, Answered", "Vos questions, nos réponses", 2),
        ("Next Steps: Strategy Call", "Prochaines étapes : appel stratégique"),
        (">The Problem</span>", ">Le problème</span>"),
        ("Let Me Ask You Something...", "Laissez-moi vous demander quelque chose..."),
        ('"How many <strong class="text-white font-bold">qualified sales calls</strong> did you have on your calendar last month?"', """« Combien d’<strong class="text-white font-bold">appels de vente qualifiés</strong> aviez-vous à votre calendrier le mois dernier&nbsp;? »"""),
        ("""If the answer is less than 20, <span class="text-white font-bold">the math further down this page will show you exactly what that's costing you.</span>""", """Si la réponse est moins de 20, <span class="text-white font-bold">le calcul plus bas sur cette page vous montrera exactement ce que cela vous coûte.</span>"""),
        ("Running Ads", "La publicité payante"),
        ("Expensive and constantly changing algorithms.", "Coûteuse, avec des algorithmes qui changent constamment."),
        ("Posting on LinkedIn", "Publier sur LinkedIn"),
        ("Great for brand, but unpredictable lead flow.", "Excellent pour la marque, mais un flux de prospects imprévisible."),
        ("Networking & Referrals", "Réseautage et recommandations"),
        ("High quality, but entirely out of your control.", "De grande qualité, mais entièrement hors de votre contrôle."),
        ("The Truth About Unpredictable Channels", "La vérité sur les canaux imprévisibles"),
        ("Some of that is working. You're getting some calls. You're closing deals.", "Une partie de cela fonctionne. Vous obtenez des appels. Vous concluez des ventes."),
        ("But none of those channels are predictable.", "Mais aucun de ces canaux n’est prévisible."),
        ("You can't control when a referral comes in.", "Vous ne contrôlez pas quand une recommandation arrive."),
        ("You can't control when someone sees your post.", "Vous ne contrôlez pas quand quelqu’un voit votre publication."),
        ("You can't control when an ad converts.", "Vous ne contrôlez pas quand une publicité convertit."),
        ("One month you book 15 calls. The next month you book 3. One quarter you hit your goals. The next quarter you're scrambling. It's exhausting.", "Un mois, vous réservez 15 appels. Le mois suivant, vous en réservez 3. Un trimestre, vous atteignez vos objectifs. Le trimestre suivant, vous courez après. C’est épuisant."),
        ("Your Competitors Are Already Solving This.", "Vos concurrents règlent déjà ce problème."),
        ("""While you're waiting for referrals, they're booking calls with your ideal buyers every week using a system that <span class="text-white font-bold border-b-2 border-brand-500">costs them nothing unless it works.</span>""", """Pendant que vous attendez des recommandations, ils réservent chaque semaine des appels avec vos acheteurs idéaux grâce à un système qui <span class="text-white font-bold border-b-2 border-brand-500">ne leur coûte rien à moins qu’il fonctionne.</span>"""),
        (">The Solution</span>", ">La solution</span>"),
        ("A Performance-Based Cold Email System", "Un système de courriel à froid basé sur la performance"),
        ("That fills your calendar with zero risk.", "Qui remplit votre calendrier, sans risque."),
        ("Here's exactly what I'm offering:", "Voici exactement ce que je vous offre :"),
        ("""I'll build and run your entire cold email infrastructure — from domain setup to booked calls — and <strong class="text-brand-400 font-bold">you only pay when a qualified buyer books a call with you.</strong>""", """Je bâtis et gère toute votre infrastructure de prospection par courriel — de la configuration des domaines aux appels réservés — et <strong class="text-brand-400 font-bold">vous payez seulement lorsqu’un acheteur qualifié réserve un appel avec vous.</strong>"""),
        ("No Retainers", "Aucuns frais fixes"),
        ("Zero Risk", "Zéro risque"),
        ("Pay Per Show", "Paiement par appel tenu"),
        ("It Doesn't Replace. It Multiplies.", "Ça ne remplace pas. Ça multiplie."),
        ("Let me say that again: You only pay when a qualified buyer is sitting on your calendar, ready to talk to you.", "Laissez-moi le répéter : vous payez seulement lorsqu’un acheteur qualifié est à votre calendrier, prêt à vous parler."),
        ("Not for opens.", "Pas pour les ouvertures."),
        ("Not for replies.", "Pas pour les réponses."),
        ("""Not for "interested" responses.""", """Pas pour les réponses « intéressées »."""),
        ("Only for confirmed calls with your ICP.", "Seulement pour des appels confirmés avec votre client idéal (ICP)."),
        ("Keep doing what works:", "Continuez ce qui fonctionne :"),
        ("Facebook Ads", "Publicités Facebook"),
        ("LinkedIn Content", "Contenu LinkedIn"),
        ("Keep doing that.", "Continuez.", 3),
        (">Referrals</span>", ">Recommandations</span>"),
        ("Add a channel that costs nothing unless it works. If it works, you make money. If it doesn't, you pay nothing.", "Ajoutez un canal qui ne coûte rien à moins qu’il fonctionne. S’il fonctionne, vous faites de l’argent. Sinon, vous ne payez rien."),
        (">Industry Evidence</span>", ">Preuves du secteur</span>"),
        ("Why This Works At Scale", "Pourquoi ça fonctionne à grande échelle"),
        ("Here's what companies achieve with professionally run cold email — independent examples, each linked to its source so you can verify them yourself.", "Voici ce que des entreprises réussissent avec une prospection par courriel gérée professionnellement — des exemples indépendants, chacun lié à sa source pour que vous puissiez les vérifier vous-même."),
        ('alt="Phil Kirkeiner Case Study"', 'alt="Étude de cas Phil Kirkeiner"'),
        ('alt="Sunny Stuart Case Study"', 'alt="Étude de cas Sunny Stuart"'),
        ("""B2B SaaS Founder closed <strong class="text-white">50 meetings in the first month</strong> of hiring cold email services.""", """Un fondateur de SaaS B2B a obtenu <strong class="text-white">50 rendez-vous dès le premier mois</strong> après avoir embauché un service de prospection par courriel."""),
        ("Independent example — watch the source interview", "Exemple indépendant — regardez l’entrevue source", 2),
        ("""Management tool for fitness studios got <strong class="text-white">26 booked demos</strong> with gym owners within the first 3 weeks.""", """Un outil de gestion pour studios de conditionnement physique a obtenu <strong class="text-white">26 démos réservées</strong> avec des propriétaires de gyms en moins de 3 semaines."""),
        ("The Logic: Why Cold Email Works", "La logique : pourquoi le courriel à froid fonctionne"),
        (">Reach</h3>", ">Portée</h3>"),
        ("Reach thousands of your exact ideal buyers every week. Decision-makers with budget and authority.", "Rejoignez chaque semaine des milliers de vos acheteurs idéaux exacts. Des décideurs avec budget et autorité."),
        (">Targeting</h3>", ">Ciblage</h3>"),
        ("Control exactly who you reach. Specific titles, company sizes, industries. No wasted impressions.", "Contrôlez exactement qui vous rejoignez. Titres précis, tailles d’entreprise, industries. Aucune impression gaspillée."),
        (">Predictability</h3>", ">Prévisibilité</h3>"),
        ("Know exactly how many emails go out and calls book. Forecast pipeline with far more confidence than referrals or ads allow.", "Sachez exactement combien de courriels partent et combien d’appels se réservent. Prévoyez votre pipeline avec beaucoup plus de confiance que les recommandations ou la publicité ne le permettent."),
        (">Scalability</h3>", ">Évolutivité</h3>"),
        ("Runs 24/7. You're not dependent on algorithms, ad platforms, or social media trends.", "Fonctionne 24/7. Vous ne dépendez ni des algorithmes, ni des plateformes publicitaires, ni des tendances des réseaux sociaux."),
        (">The Math</span>", ">Le calcul</span>"),
        ("What You're Leaving On The Table", "Ce que vous laissez sur la table"),
        ("Assuming a $15,000 service and an illustrative 20% close rate — plug in your own numbers in the calculator below.", "En supposant un service de 15 000 $ et un taux de conclusion illustratif de 20 % — entrez vos propres chiffres dans le calculateur ci-dessous."),
        ("Scenario 1: 10 Calls/Mo", "Scénario 1 : 10 appels/mois"),
        ("10 calls &times; 20% close rate = 2 new clients", "10 appels &times; 20 % de conclusion = 2 nouveaux clients"),
        ("Scenario 2: 25 Calls/Mo", "Scénario 2 : 25 appels/mois"),
        ("25 calls &times; 20% close rate = 5 new clients", "25 appels &times; 20 % de conclusion = 5 nouveaux clients"),
        ("Scenario 3: 50 Calls/Mo", "Scénario 3 : 50 appels/mois"),
        ("50 calls &times; 20% close rate = 10 new clients", "50 appels &times; 20 % de conclusion = 10 nouveaux clients"),
        (">/mo</span>", ">/mois</span>", 3),
        ("The Cost of Inaction", "Le coût de l’inaction"),
        ("If you could be booking 25 calls per month and closing 5 new clients at $15K each, that's $75,000 in revenue per month.", "Si vous pouviez réserver 25 appels par mois et conclure 5 nouveaux clients à 15 000 $ chacun, cela fait 75 000 $ de revenus par mois."),
        ("Wait 30 days:", "Attendre 30 jours :"),
        ("Up to $75,000 in pipeline never created", "Jusqu’à 75 000 $ de pipeline jamais créé"),
        ("Wait 90 days:", "Attendre 90 jours :"),
        ("Up to $225,000 in pipeline never created", "Jusqu’à 225 000 $ de pipeline jamais créé"),
        ("This doesn't account for lifetime value, referrals, case studies, or compounding growth. Every day you wait is pipeline you'll never get back.", "Cela ne tient pas compte de la valeur à vie, des recommandations, des études de cas ni de la croissance composée. Chaque jour d’attente est du pipeline que vous ne récupérerez jamais."),
        ("><i class=\"fa-solid fa-calculator text-brand-400\"></i> ROI Calculator</h3>", "><i class=\"fa-solid fa-calculator text-brand-400\"></i> Calculateur de ROI</h3>"),
        ("Open in new tab", "Ouvrir dans un nouvel onglet"),
        ("Interactive ROI Calculator", "Calculateur de ROI interactif"),
        ("Due to browser security, this app opens in a new window.", "Pour des raisons de sécurité du navigateur, cette application s’ouvre dans une nouvelle fenêtre."),
        ("Calculate Your ROI", "Calculez votre ROI"),
        (">How It Works</span>", ">Comment ça fonctionne</span>"),
        ("The 4-Step System That Books Calls on Autopilot", "Le système en 4 étapes qui réserve des appels en pilote automatique"),
        ("Step 1: Domain & Inbox Setup", "Étape 1 : configuration des domaines et des boîtes courriel"),
        ("Dedicated sending domains separate from your main. We warm them up over 2-3 weeks to build trust and ensure maximum deliverability.", "Des domaines d’envoi dédiés, séparés de votre domaine principal. Nous les réchauffons pendant 2 à 3 semaines pour bâtir la confiance et assurer une délivrabilité maximale."),
        ("Step 2: Precision Data Mining", "Étape 2 : extraction de données de précision"),
        ("We target decision-makers based on specific job titles, company sizes, and industries. Every contact is verified before sending, keeping bounce rates near zero.", "Nous ciblons les décideurs selon des titres de poste, des tailles d’entreprise et des industries précis. Chaque contact est vérifié avant l’envoi, ce qui garde les taux de rebond près de zéro."),
        ("Step 3: High-Converting Copy", "Étape 3 : des textes qui convertissent"),
        ("Short, direct, conversational emails personalized to pain points. We continuously A/B test and optimize based on booked call rates.", "Des courriels courts, directs et conversationnels, personnalisés selon les points de douleur. Nous testons et optimisons continuellement en fonction des taux d’appels réservés."),
        ("Step 4: Qualified Calls Booked", "Étape 4 : appels qualifiés réservés"),
        ("Interested prospects book directly onto your calendar.", "Les prospects intéressés réservent directement dans votre calendrier."),
        (">What You Get</span>", ">Ce que vous obtenez</span>"),
        ("The Full Build-Out", "L’installation complète"),
        ("This is a full done-for-you infrastructure build. The entire car. Not just the tires.", "Il s’agit d’une infrastructure complète, clé en main. La voiture au complet. Pas seulement les pneus."),
        ("Infrastructure Setup", "Configuration de l’infrastructure"),
        ("Dedicated domain registration & DNS", "Enregistrement de domaines dédiés et DNS"),
        ("Inbox setup & auth (SPF, DKIM, DMARC)", "Configuration des boîtes courriel et authentification (SPF, DKIM, DMARC)"),
        ("Automated 2-3 week inbox warming", "Réchauffement automatisé des boîtes courriel pendant 2 à 3 semaines"),
        ("Data & Targeting", "Données et ciblage"),
        ("ICP definition & buyer mapping", "Définition du client idéal (ICP) et cartographie des acheteurs"),
        ("Building verified lists of thousands of leads matching the ICP", "Création de listes vérifiées de milliers de prospects correspondant au client idéal"),
        ("Ongoing list refresh & hygiene", "Rafraîchissement et hygiène continus des listes"),
        ("Copywriting & Management", "Rédaction et gestion"),
        ("Writing copy", "Rédaction des textes"),
        ("Multi-touchpoint sequence creation", "Création de séquences multipoints"),
        ("Continuous A/B testing & iteration", "Tests A/B et itérations continus"),
        ("Daily sending & deliverability management", "Envoi quotidien et gestion de la délivrabilité"),
        ("Lead qualification & calendar routing", "Qualification des prospects et acheminement au calendrier"),
        ("The Guarantee", "La garantie"),
        ("You only pay when a qualified buyer books a call.", "Vous payez seulement lorsqu’un acheteur qualifié réserve un appel."),
        ("If a booked call doesn't fit your ICP, you don't pay for it.", "Si un appel réservé ne correspond pas à votre client idéal, vous ne le payez pas."),
        ("No retainers. No risk.", "Aucuns frais fixes. Aucun risque."),
        ("We handle everything. You just close deals.", "Nous nous occupons de tout. Vous n’avez qu’à conclure les ventes."),
        ("""<h4 class="text-lg font-bold mb-2 text-brand-300">"How much does this cost?"</h4>""", """<h4 class="text-lg font-bold mb-2 text-brand-300">« Combien ça coûte ? »</h4>"""),
        ("You only pay per qualified call that shows. Pricing is a flat per-show fee, set on the strategy call based on your industry and deal size. And if a booked call doesn't fit your ICP, you don't pay for it.", "Vous payez seulement par appel qualifié qui se présente. Le prix est un frais fixe par appel tenu, établi pendant l’appel stratégique selon votre industrie et la taille de vos ventes. Et si un appel réservé ne correspond pas à votre client idéal, vous ne le payez pas."),
        ("""<h4 class="text-lg font-bold mb-2 text-brand-300">"How long to see results?"</h4>""", """<h4 class="text-lg font-bold mb-2 text-brand-300">« Combien de temps avant de voir des résultats ? »</h4>"""),
        ("Setup takes 2-3 weeks (domain warming, list building, copy). After that, you'll start seeing booked calls within the first 30 days. Consistent flow by month 2.", "L’installation prend 2 à 3 semaines (réchauffement des domaines, création des listes, rédaction). Ensuite, vous commencerez à voir des appels réservés dans les 30 premiers jours. Un flux constant dès le deuxième mois."),
        ("""<h4 class="text-lg font-bold mb-2 text-brand-300">"What if the leads aren't qualified?"</h4>""", """<h4 class="text-lg font-bold mb-2 text-brand-300">« Et si les prospects ne sont pas qualifiés ? »</h4>"""),
        ("""We vet every lead before they book. If someone books who doesn't fit your ICP, <strong class="text-white">we don't charge you.</strong> Simple as that.""", """Nous vérifions chaque prospect avant qu’il réserve. Si quelqu’un réserve sans correspondre à votre client idéal, <strong class="text-white">nous ne vous facturons pas.</strong> C’est aussi simple que ça."""),
        ("""<h4 class="text-lg font-bold mb-2 text-brand-300">"Can I cancel anytime?"</h4>""", """<h4 class="text-lg font-bold mb-2 text-brand-300">« Puis-je annuler en tout temps ? »</h4>"""),
        ("Yes. No long-term contracts. If you want to stop, you stop. No penalties. Our incentives are 100% aligned with yours.", "Oui. Aucun contrat à long terme. Si vous voulez arrêter, vous arrêtez. Aucune pénalité. Nos incitatifs sont alignés à 100 % avec les vôtres."),
        (">Next Steps</span>", ">Prochaines étapes</span>"),
        # CTA heading is covered by the shared replacement above.
        ("Book a 15-minute call with me. Not a salesperson. Me. Zero obligation. Zero pressure.", "Réservez un appel de 15 minutes avec moi. Pas un vendeur. Moi. Zéro obligation. Zéro pression."),
        ("Meet The Founder", "Rencontrez le fondateur"),
        ('alt="Maxime - Founder of Leadigo"', 'alt="Maxime — fondateur de Leadigo"'),
        ('"I founded Leadigo with one mission: to eliminate the guesswork in customer acquisition."', """« J’ai fondé Leadigo avec une seule mission : éliminer les devinettes dans l’acquisition de clients. »"""),
        ('"After working in software for 2 years at an investment bank, I saw firsthand how critical predictable revenue systems were to massive organizations. I wanted to bring my own creation into the world to solve this exact problem for high-ticket B2B companies—and this is it!"', """« Après avoir travaillé 2 ans en logiciels dans une banque d’investissement, j’ai vu à quel point des systèmes de revenus prévisibles étaient essentiels aux grandes organisations. Je voulais lancer ma propre création pour régler exactement ce problème pour les entreprises B2B à panier élevé — et la voici ! »"""),
    ]
    for old, new, *rest in pairs:
        count = rest[0] if rest else 1
        text = rep(text, old, new, count)
    (ROOT / "index-fr.html").write_text(text, encoding="utf-8")


def roi_fr():
    text = (ROOT / "roi_calculator.html").read_text(encoding="utf-8")
    text = common_fr(text)
    text = rep(text, "<title>ROI Calculator | Leadigo</title>", "<title>Calculateur de ROI | Leadigo</title>")
    pairs = [
        (">The Math</span>", ">Le calcul</span>"),
        (">ROI Calculator</h1>", ">Calculateur de ROI</h1>"),
        ("Customer Value / LTV ($)", "Valeur client / LTV ($)"),
        ("Sales Calls Booked", "Appels de vente réservés"),
        ("Sales Call Close Rate", "Taux de conclusion des appels"),
        ("Gross Margin (%)", "Marge brute (%)"),
        ("Advertising Rate ($)", "Tarif publicitaire ($)"),
        (">Per Call</div>", ">Par appel</div>"),
        (">Per Closed Client</div>", ">Par client conclu</div>"),
        ("Added Revenue", "Revenus ajoutés"),
        ("Price of Email Campaign", "Prix de la campagne de courriels"),
        ("(Advertising Rate × Closed Clients)", "(Tarif publicitaire × Clients conclus)", 2),
        ("(Advertising Rate × Calls Booked)", "(Tarif publicitaire × Appels réservés)"),
        ("""For every $1 spent on the email campaign, your business makes back $<span id="roiSubtext">0.00</span> in profit.""", """Pour chaque 1 $ dépensé dans la campagne de courriels, votre entreprise récupère <span id="roiSubtext">0,00</span> $ de profit."""),
        ("new Intl.NumberFormat('en-US'", "new Intl.NumberFormat('fr-CA'"),
        ('roiSubtext.textContent = "Infinite";', 'roiSubtext.textContent = "Infini";'),
        ('roiDisplay.textContent = roi.toFixed(1) + "x";', 'roiDisplay.textContent = roi.toFixed(1).replace(".", ",") + "x";'),
        ('roiSubtext.textContent = roi.toFixed(2);', 'roiSubtext.textContent = roi.toFixed(2).replace(".", ",");'),
    ]
    for old, new, *rest in pairs:
        count = rest[0] if rest else 1
        text = rep(text, old, new, count)
    (ROOT / "roi_calculator-fr.html").write_text(text, encoding="utf-8")


def strategy_fr():
    text = (ROOT / "strategy_call.html").read_text(encoding="utf-8")
    text = common_fr(text)
    text = rep(text, "<title>Strategy Call | Leadigo</title>", "<title>Appel stratégique | Leadigo</title>")
    text = rep(text, 'href="index.html"', 'href="index-fr.html"', 2)
    pairs = [
        ("Back to the VSL", "Retour à la VSL"),
        (">Next Steps</span>", ">Prochaines étapes</span>"),
        ("Book Your Free Strategy Call", "Réservez votre appel stratégique gratuit"),
        ("This call is to see if our cold outreach is a good fit for your company — and to get to know more about our cold outreach services. Zero obligation. Zero pressure.", "Cet appel sert à voir si notre prospection à froid convient à votre entreprise — et à en apprendre davantage sur nos services de prospection à froid. Zéro obligation. Zéro pression."),
    ]
    for old, new in pairs:
        text = rep(text, old, new)
    (ROOT / "strategy_call-fr.html").write_text(text, encoding="utf-8")


index_fr()
roi_fr()
strategy_fr()
print("French pages generated: index-fr.html, roi_calculator-fr.html, strategy_call-fr.html")
