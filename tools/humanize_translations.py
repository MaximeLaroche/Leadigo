from pathlib import Path

DOCS = Path(__file__).resolve().parents[1] / "docs"


def rep(text, old, new, count=1):
    found = text.count(old)
    if found != count:
        raise SystemExit(f"Humanize replacement mismatch for {old[:90]!r}: found {found}, expected {count}")
    return text.replace(old, new)


def apply(text, pairs):
    for item in pairs:
        old, new = item[0], item[1]
        count = item[2] if len(item) > 2 else None
        text = text.replace(old, new) if count is None else rep(text, old, new, count)
    return text


FR_GLOBAL = [
    ("Prospection par courriel basée sur la performance", "Courriel à froid payé aux résultats"),
    ("Le calcul", "Les chiffres"),
    ("Aucuns frais fixes", "Aucun forfait mensuel"),
]
FR_INDEX = [
    ("Le moteur de croissance B2B ultime", "Le moteur de croissance B2B le plus simple"),
    ("""Et si vous pouviez ajouter un <span class="grad-text text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-blue-300">flux prévisible d’appels de vente qualifiés</span> à votre calendrier chaque mois&nbsp;?""", """Et si vous ajoutiez un <span class="grad-text text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-blue-300">flux prévisible d’appels de vente qualifiés</span> à votre calendrier chaque mois&nbsp;?"""),
    ("— Sans dépenser un sou à moins qu’ils se présentent réellement.", "— Sans dépenser un sou tant qu’ils ne se présentent pas."),
    ("Aucun risque. Vous payez seulement lorsqu’un acheteur qualifié réserve un appel avec vous — chaque facture signifie qu’une vraie conversation de vente est déjà à votre calendrier.", "Zéro risque : vous ne payez que lorsqu’un acheteur qualifié réserve un appel. Chaque facture correspond à une vraie conversation de vente, déjà dans votre calendrier."),
    ("Vous préférez lire&nbsp;? Tout ce qui est dans la vidéo est couvert ci-dessous, section par section — le problème, le système, les preuves, les chiffres et la garantie.", "Vous préférez lire&nbsp;? Tout ce qui est dans la vidéo est repris ci-dessous, section par section : le problème, le système, les preuves, les chiffres et la garantie."),
    ("Un système de courriel à froid basé sur la performance", "Un système de courriel à froid payé aux résultats"),
    ("Qui remplit votre calendrier, sans risque.", "Qui remplit votre calendrier sans vous faire prendre de risque."),
    ("Voici exactement ce que je vous offre :", "Voici exactement ce que je propose :"),
    ("""Je bâtis et gère toute votre infrastructure de prospection par courriel — de la configuration des domaines aux appels réservés — et <strong class="text-brand-400 font-bold">vous payez seulement lorsqu’un acheteur qualifié réserve un appel avec vous.</strong>""", """Je m’occupe de toute votre prospection par courriel — des domaines aux appels réservés — et <strong class="text-brand-400 font-bold">vous ne payez que lorsqu’un acheteur qualifié réserve un appel avec vous.</strong>"""),
    ("Paiement par appel tenu", "Payé par appel présenté"),
    ("Ça ne remplace pas. Ça multiplie.", "Ça ne remplace rien. Ça multiplie."),
    ("Laissez-moi le répéter : vous payez seulement lorsqu’un acheteur qualifié est à votre calendrier, prêt à vous parler.", "Je le répète : vous ne payez que lorsqu’un acheteur qualifié est déjà dans votre calendrier, prêt à vous parler."),
    ("Voici ce que des entreprises obtiennent avec une prospection par courriel bien gérée — des exemples indépendants, avec la source pour les vérifier vous-même.", "Voici ce que des entreprises obtiennent avec une prospection par courriel bien gérée — des exemples indépendants, avec la source pour les vérifier vous-même."),
    ("Sachez exactement combien de courriels partent et combien d’appels se réservent. Prévoyez votre pipeline avec beaucoup plus de confiance que les recommandations ou la publicité ne le permettent.", "Vous savez combien de courriels partent et combien d’appels se réservent. Le pipeline devient beaucoup plus prévisible qu’avec les recommandations ou la pub."),
    ("En supposant un service de 15 000 $ et un taux de conclusion de 20 % pour l’exemple — mettez vos vrais chiffres dans le calculateur ci-dessous.", "En prenant un service à 15 000 $ et un taux de conclusion de 20 % pour l’exemple — mettez vos vrais chiffres dans le calculateur ci-dessous."),
    ("Il s’agit d’une infrastructure complète, clé en main. La voiture au complet. Pas seulement les pneus.", "C’est une installation complète, clé en main. La voiture entière, pas juste les pneus."),
    ("Réservez un appel de 15 minutes avec moi. Pas un vendeur. Moi. Zéro obligation. Zéro pression.", "Réservez 15 minutes avec moi. Pas un vendeur. Moi. Zéro obligation, zéro pression."),
]
FR_ROI = [("Le calcul", "Les chiffres")]
FR_STRATEGY = [
    ("Cet appel sert à voir si notre prospection à froid convient à votre entreprise — et à en apprendre davantage sur nos services de prospection à froid. Zéro obligation. Zéro pression.", "Cet appel sert à voir si notre prospection à froid peut vraiment aider votre entreprise — et à vous montrer comment on travaille. Zéro obligation, zéro pression."),
]

ES_GLOBAL = [
    ("Prospección por correo basada en resultados", "Correo frío pagado por resultados"),
    ("Sin retainers", "Sin mensualidades fijas"),
]
ES_INDEX = [
    ("El motor de crecimiento B2B definitivo", "El motor de crecimiento B2B más simple"),
    ("""¿Y si pudieras agregar un <span class="grad-text text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-blue-300">flujo predecible de llamadas de ventas calificadas</span> a tu calendario cada mes?""", """¿Y si agregaras un <span class="grad-text text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-blue-300">flujo predecible de llamadas de ventas calificadas</span> a tu calendario cada mes?"""),
    ("— Sin gastar un centavo a menos que realmente se presenten.", "— Sin gastar un centavo hasta que realmente se presenten."),
    ("Sin riesgo. Solo pagas cuando un comprador calificado agenda una llamada contigo — cada factura significa que una conversación de ventas real ya está en tu calendario.", "Cero riesgo: solo pagas cuando un comprador calificado agenda una llamada. Cada factura significa una conversación de ventas real, ya en tu calendario."),
    ("¿Prefieres leer? Todo lo del video está cubierto abajo, sección por sección — el problema, el sistema, la evidencia, los números y la garantía.", "¿Prefieres leer? Todo lo del video está retomado abajo, sección por sección: el problema, el sistema, la evidencia, los números y la garantía."),
    ("La solución: correo frío basado en resultados", "La solución: correo frío pagado por resultados"),
    ("Un sistema de correo frío basado en resultados", "Un sistema de correo frío pagado por resultados"),
    ("Que llena tu calendario sin riesgo.", "Que llena tu calendario sin hacerte correr riesgos."),
    ("Esto es exactamente lo que te ofrezco:", "Esto es exactamente lo que te propongo:"),
    ("""Construyo y opero toda tu infraestructura de prospección por correo — desde la configuración de dominios hasta las llamadas agendadas — y <strong class="text-brand-400 font-bold">solo pagas cuando un comprador calificado agenda una llamada contigo.</strong>""", """Me encargo de toda tu prospección por correo — de los dominios a las llamadas agendadas — y <strong class="text-brand-400 font-bold">solo pagas cuando un comprador calificado agenda una llamada contigo.</strong>"""),
    ("No reemplaza. Multiplica.", "No reemplaza nada. Multiplica."),
    ("Déjame repetirlo: solo pagas cuando un comprador calificado está en tu calendario, listo para hablar contigo.", "Te lo repito: solo pagas cuando un comprador calificado ya está en tu calendario, listo para hablar contigo."),
    ("Esto es lo que las empresas logran con correo frío gestionado profesionalmente — ejemplos independientes, cada uno enlazado a su fuente para que puedas verificarlos.", "Esto es lo que logran las empresas con correo frío bien gestionado — ejemplos independientes, cada uno con su fuente para que lo verifiques."),
    ("Sabrás exactamente cuántos correos salen y cuántas llamadas se agendan. Pronostica tu pipeline con mucha más confianza de la que permiten los referidos o los anuncios.", "Sabes cuántos correos salen y cuántas llamadas se agendan. El pipeline se vuelve mucho más previsible que con referidos o anuncios."),
    ("Asumiendo un servicio de $15,000 y una tasa de cierre ilustrativa del 20% — ingresa tus propios números en la calculadora de abajo.", "Tomando un servicio de $15,000 y una tasa de cierre del 20% como ejemplo — pon tus números reales en la calculadora de abajo."),
    ("Es una infraestructura completa hecha para ti. El auto completo. No solo las llantas.", "Es una implementación completa, llave en mano. El auto entero, no solo las llantas."),
    ("Agenda una llamada de 15 minutos conmigo. No un vendedor. Conmigo. Cero obligación. Cero presión.", "Agenda 15 minutos conmigo. No un vendedor. Conmigo. Cero obligación, cero presión."),
]
ES_STRATEGY = [
    ("Esta llamada es para ver si nuestra prospección en frío encaja con tu empresa — y para conocer más sobre nuestros servicios de prospección en frío. Cero obligación. Cero presión.", "Esta llamada es para ver si nuestra prospección en frío puede ayudar de verdad a tu empresa — y para mostrarte cómo trabajamos. Cero obligación, cero presión."),
]


def run(path, globals_, specifics):
    p = DOCS / path
    text = p.read_text(encoding="utf-8")
    text = apply(text, globals_)
    text = apply(text, specifics)
    p.write_text(text, encoding="utf-8")


run("index-fr.html", FR_GLOBAL, FR_INDEX)
run("roi_calculator-fr.html", FR_GLOBAL, FR_ROI)
run("strategy_call-fr.html", FR_GLOBAL, FR_STRATEGY)
run("index-es.html", ES_GLOBAL, ES_INDEX)
run("roi_calculator-es.html", ES_GLOBAL, [])
run("strategy_call-es.html", ES_GLOBAL, ES_STRATEGY)
print("Humanized French and Spanish copy")
