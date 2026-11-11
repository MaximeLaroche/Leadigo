from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs"


def rep(text, old, new, count=1):
    found = text.count(old)
    if found != count:
        raise SystemExit(f"Replacement count mismatch for {old[:90]!r}: found {found}, expected {count}")
    return text.replace(old, new)


def common_es(text):
    text = text.replace('<html lang="en"', '<html lang="es"')
    text = text.replace("label: 'System'", "label: 'Sistema'")
    text = text.replace("label: 'Light'", "label: 'Claro'")
    text = text.replace("label: 'Dark'", "label: 'Oscuro'")
    text = text.replace("themeTip.textContent = 'Theme: ' + themeMeta[theme].label;", "themeTip.textContent = 'Tema: ' + themeMeta[theme].label;")
    text = text.replace('aria-label="Theme: system, light, or dark"', 'aria-label="Tema: sistema, claro u oscuro"')
    text = text.replace('>Theme: System</span>', '>Tema: Sistema</span>')
    text = text.replace("themeToggle.setAttribute('aria-label', 'Theme: ' + themeMeta[theme].label + ' (click to switch)');", "themeToggle.setAttribute('aria-label', 'Tema: ' + themeMeta[theme].label + ' (haz clic para cambiar)');")
    text = rep(text, ">Connect</span>", ">Conectar</span>")
    text = rep(text, "Let's Stay In Touch", "Mantengamos el contacto")
    text = rep(text, "Follow along, see the work, or reach out directly — whichever works best for you.", "Sigue el trabajo, mira los resultados o contáctanos directamente — como prefieras.")
    text = rep(text, ">Email</span>", ">Correo</span>")
    text = rep(text, "Leadigo — Performance-Based Cold Email", "Leadigo — Prospección por correo basada en resultados")
    return text


def index_es():
    text = (ROOT / "index.html").read_text(encoding="utf-8")
    text = common_es(text)
    text = rep(text, "<title>Leadigo VSL | Performance-Based Cold Email</title>", "<title>Leadigo VSL | Prospección por correo basada en resultados</title>")
    text = rep(text, 'href="roi_calculator.html"', 'href="roi_calculator-es.html"', 2)
    text = rep(text, 'src="roi_calculator.html"', 'src="roi_calculator-es.html"', 1)

    pairs = [
        (">Proof</a>", ">Pruebas</a>"),
        (">The Math</a>", ">Los números</a>"),
        (">FAQ</a>", ">FAQ</a>"),
        (">Book a Call</a>", ">Reservar una llamada</a>"),
        ("The Ultimate B2B Growth Engine", "El motor de crecimiento B2B definitivo"),
        ("""What If You Could Add a <span class="grad-text text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-blue-300">Predictable Flow of Qualified Sales Calls</span> to Your Calendar Every Month?""", """¿Y si pudieras agregar un <span class="grad-text text-transparent bg-clip-text bg-gradient-to-r from-brand-400 to-blue-300">flujo predecible de llamadas de ventas calificadas</span> a tu calendario cada mes?"""),
        ("— Without Spending a Dime Unless They Actually Show Up.", "— Sin gastar un centavo a menos que realmente se presenten."),
        ("Book Your Free Strategy Call", "Reserva tu llamada estratégica gratuita", 2),
        ("No risk. You only pay when a qualified buyer books a call with you — every invoice means a real sales conversation is already on your calendar.", "Sin riesgo. Solo pagas cuando un comprador calificado agenda una llamada contigo — cada factura significa que una conversación de ventas real ya está en tu calendario."),
        ("Prefer reading? Everything in the video is covered below, section by section — the problem, the system, the evidence, the math, and the guarantee.", "¿Prefieres leer? Todo lo del video está cubierto abajo, sección por sección — el problema, el sistema, la evidencia, los números y la garantía."),
        ("What We're Covering Today", "Lo que cubriremos hoy"),
        ("The Problem: Unpredictable Pipeline", "El problema: un pipeline impredecible"),
        ("The Solution: Performance Cold Email", "La solución: correo frío basado en resultados"),
        ("Industry Evidence: Cold Email at Scale", "Evidencia del sector: correo frío a gran escala"),
        ("The Math: What You're Leaving Behind", "Los números: lo que estás dejando atrás"),
        ("How It Works: The 4-Step System", "Cómo funciona: el sistema en 4 pasos"),
        ("What You Get: The Full Build-Out", "Lo que obtienes: la implementación completa"),
        ("Your Questions, Answered", "Tus preguntas, respondidas", 2),
        ("Next Steps: Strategy Call", "Próximos pasos: llamada estratégica"),
        (">The Problem</span>", ">El problema</span>"),
        ("Let Me Ask You Something...", "Déjame preguntarte algo..."),
        ('"How many <strong class="text-white font-bold">qualified sales calls</strong> did you have on your calendar last month?"', """« ¿Cuántas <strong class="text-white font-bold">llamadas de ventas calificadas</strong> tenías en tu calendario el mes pasado? »"""),
        ("""If the answer is less than 20, <span class="text-white font-bold">the math further down this page will show you exactly what that's costing you.</span>""", """Si la respuesta es menos de 20, <span class="text-white font-bold">los números más abajo en esta página te mostrarán exactamente lo que eso te cuesta.</span>"""),
        ("Running Ads", "Publicidad pagada"),
        ("Expensive and constantly changing algorithms.", "Cara y con algoritmos que cambian constantemente."),
        ("Posting on LinkedIn", "Publicar en LinkedIn"),
        ("Great for brand, but unpredictable lead flow.", "Excelente para la marca, pero un flujo de leads impredecible."),
        ("Networking & Referrals", "Networking y referidos"),
        ("High quality, but entirely out of your control.", "Alta calidad, pero completamente fuera de tu control."),
        ("The Truth About Unpredictable Channels", "La verdad sobre los canales impredecibles"),
        ("Some of that is working. You're getting some calls. You're closing deals.", "Parte de eso funciona. Obtienes algunas llamadas. Cierras ventas."),
        ("But none of those channels are predictable.", "Pero ninguno de esos canales es predecible."),
        ("You can't control when a referral comes in.", "No puedes controlar cuándo llega un referido."),
        ("You can't control when someone sees your post.", "No puedes controlar cuándo alguien ve tu publicación."),
        ("You can't control when an ad converts.", "No puedes controlar cuándo convierte un anuncio."),
        ("One month you book 15 calls. The next month you book 3. One quarter you hit your goals. The next quarter you're scrambling. It's exhausting.", "Un mes agendan 15 llamadas. Al siguiente, 3. Un trimestre cumples tus metas. Al siguiente, estás corriendo. Es agotador."),
        ("Your Competitors Are Already Solving This.", "Tus competidores ya están resolviendo esto."),
        ("""While you're waiting for referrals, they're booking calls with your ideal buyers every week using a system that <span class="text-white font-bold border-b-2 border-brand-500">costs them nothing unless it works.</span>""", """Mientras esperas referidos, ellos agendan llamadas con tus compradores ideales cada semana usando un sistema que <span class="text-white font-bold border-b-2 border-brand-500">no les cuesta nada a menos que funcione.</span>"""),
        (">The Solution</span>", ">La solución</span>"),
        ("A Performance-Based Cold Email System", "Un sistema de correo frío basado en resultados"),
        ("That fills your calendar with zero risk.", "Que llena tu calendario sin riesgo."),
        ("Here's exactly what I'm offering:", "Esto es exactamente lo que te ofrezco:"),
        ("""I'll build and run your entire cold email infrastructure — from domain setup to booked calls — and <strong class="text-brand-400 font-bold">you only pay when a qualified buyer books a call with you.</strong>""", """Construyo y opero toda tu infraestructura de prospección por correo — desde la configuración de dominios hasta las llamadas agendadas — y <strong class="text-brand-400 font-bold">solo pagas cuando un comprador calificado agenda una llamada contigo.</strong>"""),
        ("No Retainers", "Sin retainers"),
        ("Zero Risk", "Cero riesgo"),
        ("Pay Per Show", "Pago por llamada realizada"),
        ("It Doesn't Replace. It Multiplies.", "No reemplaza. Multiplica."),
        ("Let me say that again: You only pay when a qualified buyer is sitting on your calendar, ready to talk to you.", "Déjame repetirlo: solo pagas cuando un comprador calificado está en tu calendario, listo para hablar contigo."),
        ("Not for opens.", "No por aperturas."),
        ("Not for replies.", "No por respuestas."),
        ("""Not for "interested" responses.""", """No por respuestas "interesadas"."""),
        ("Only for confirmed calls with your ICP.", "Solo por llamadas confirmadas con tu cliente ideal (ICP)."),
        ("Keep doing what works:", "Sigue haciendo lo que funciona:"),
        ("Facebook Ads", "Anuncios de Facebook"),
        ("LinkedIn Content", "Contenido de LinkedIn"),
        ("Keep doing that.", "Sigue haciéndolo.", 3),
        (">Referrals</span>", ">Referidos</span>"),
        ("Add a channel that costs nothing unless it works. If it works, you make money. If it doesn't, you pay nothing.", "Agrega un canal que no cuesta nada a menos que funcione. Si funciona, ganas dinero. Si no, no pagas nada."),
        (">Industry Evidence</span>", ">Evidencia del sector</span>"),
        ("Why This Works At Scale", "Por qué funciona a gran escala"),
        ("Here's what companies achieve with professionally run cold email — independent examples, each linked to its source so you can verify them yourself.", "Esto es lo que las empresas logran con correo frío gestionado profesionalmente — ejemplos independientes, cada uno enlazado a su fuente para que puedas verificarlos."),
        ('alt="Phil Kirkeiner Case Study"', 'alt="Caso de estudio de Phil Kirkeiner"'),
        ('alt="Sunny Stuart Case Study"', 'alt="Caso de estudio de Sunny Stuart"'),
        ("""B2B SaaS Founder closed <strong class="text-white">50 meetings in the first month</strong> of hiring cold email services.""", """Un fundador de SaaS B2B obtuvo <strong class="text-white">50 reuniones en el primer mes</strong> después de contratar servicios de correo frío."""),
        ("Independent example — watch the source interview", "Ejemplo independiente — mira la entrevista fuente", 2),
        ("""Management tool for fitness studios got <strong class="text-white">26 booked demos</strong> with gym owners within the first 3 weeks.""", """Una herramienta de gestión para estudios de fitness obtuvo <strong class="text-white">26 demos agendadas</strong> con dueños de gimnasios en las primeras 3 semanas."""),
        ("The Logic: Why Cold Email Works", "La lógica: por qué funciona el correo frío"),
        (">Reach</h3>", ">Alcance</h3>"),
        ("Reach thousands of your exact ideal buyers every week. Decision-makers with budget and authority.", "Llega cada semana a miles de tus compradores ideales exactos. Decisores con presupuesto y autoridad."),
        (">Targeting</h3>", ">Segmentación</h3>"),
        ("Control exactly who you reach. Specific titles, company sizes, industries. No wasted impressions.", "Controla exactamente a quién llegas. Cargos específicos, tamaños de empresa, industrias. Sin impresiones desperdiciadas."),
        (">Predictability</h3>", ">Previsibilidad</h3>"),
        ("Know exactly how many emails go out and calls book. Forecast pipeline with far more confidence than referrals or ads allow.", "Sabrás exactamente cuántos correos salen y cuántas llamadas se agendan. Pronostica tu pipeline con mucha más confianza de la que permiten los referidos o los anuncios."),
        (">Scalability</h3>", ">Escalabilidad</h3>"),
        ("Runs 24/7. You're not dependent on algorithms, ad platforms, or social media trends.", "Funciona 24/7. No dependes de algoritmos, plataformas publicitarias ni tendencias de redes sociales."),
        (">The Math</span>", ">Los números</span>"),
        ("What You're Leaving On The Table", "Lo que estás dejando sobre la mesa"),
        ("Assuming a $15,000 service and an illustrative 20% close rate — plug in your own numbers in the calculator below.", "Asumiendo un servicio de $15,000 y una tasa de cierre ilustrativa del 20% — ingresa tus propios números en la calculadora de abajo."),
        ("Scenario 1: 10 Calls/Mo", "Escenario 1: 10 llamadas/mes"),
        ("10 calls &times; 20% close rate = 2 new clients", "10 llamadas &times; 20% de cierre = 2 nuevos clientes"),
        ("Scenario 2: 25 Calls/Mo", "Escenario 2: 25 llamadas/mes"),
        ("25 calls &times; 20% close rate = 5 new clients", "25 llamadas &times; 20% de cierre = 5 nuevos clientes"),
        ("Scenario 3: 50 Calls/Mo", "Escenario 3: 50 llamadas/mes"),
        ("50 calls &times; 20% close rate = 10 new clients", "50 llamadas &times; 20% de cierre = 10 nuevos clientes"),
        (">/mo</span>", ">/mes</span>", 3),
        ("The Cost of Inaction", "El costo de la inacción"),
        ("If you could be booking 25 calls per month and closing 5 new clients at $15K each, that's $75,000 in revenue per month.", "Si pudieras agendar 25 llamadas por mes y cerrar 5 nuevos clientes a $15K cada uno, eso son $75,000 en ingresos por mes."),
        ("Wait 30 days:", "Esperar 30 días:"),
        ("Up to $75,000 in pipeline never created", "Hasta $75,000 en pipeline nunca creado"),
        ("Wait 90 days:", "Esperar 90 días:"),
        ("Up to $225,000 in pipeline never created", "Hasta $225,000 en pipeline nunca creado"),
        ("This doesn't account for lifetime value, referrals, case studies, or compounding growth. Every day you wait is pipeline you'll never get back.", "Esto no cuenta el valor de por vida, referidos, casos de estudio ni crecimiento compuesto. Cada día que esperas es pipeline que nunca recuperarás."),
        ("><i class=\"fa-solid fa-calculator text-brand-400\"></i> ROI Calculator</h3>", "><i class=\"fa-solid fa-calculator text-brand-400\"></i> Calculadora de ROI</h3>"),
        ("Open in new tab", "Abrir en una pestaña nueva"),
        ("Interactive ROI Calculator", "Calculadora de ROI interactiva"),
        ("Due to browser security, this app opens in a new window.", "Por seguridad del navegador, esta app se abre en una ventana nueva."),
        ("Calculate Your ROI", "Calcula tu ROI"),
        (">How It Works</span>", ">Cómo funciona</span>"),
        ("The 4-Step System That Books Calls on Autopilot", "El sistema en 4 pasos que agenda llamadas en piloto automático"),
        ("Step 1: Domain & Inbox Setup", "Paso 1: configuración de dominios e inbox"),
        ("Dedicated sending domains separate from your main. We warm them up over 2-3 weeks to build trust and ensure maximum deliverability.", "Dominios de envío dedicados, separados de tu principal. Los calentamos durante 2-3 semanas para generar confianza y asegurar máxima entregabilidad."),
        ("Step 2: Precision Data Mining", "Paso 2: minería de datos de precisión"),
        ("We target decision-makers based on specific job titles, company sizes, and industries. Every contact is verified before sending, keeping bounce rates near zero.", "Apuntamos a decisores según cargos, tamaños de empresa e industrias específicas. Cada contacto se verifica antes de enviar, manteniendo las tasas de rebote cerca de cero."),
        ("Step 3: High-Converting Copy", "Paso 3: copy de alta conversión"),
        ("Short, direct, conversational emails personalized to pain points. We continuously A/B test and optimize based on booked call rates.", "Correos cortos, directos y conversacionales, personalizados según puntos de dolor. Probamos y optimizamos continuamente según las tasas de llamadas agendadas."),
        ("Step 4: Qualified Calls Booked", "Paso 4: llamadas calificadas agendadas"),
        ("Interested prospects book directly onto your calendar.", "Los prospectos interesados agendan directamente en tu calendario."),
        (">What You Get</span>", ">Lo que obtienes</span>"),
        ("The Full Build-Out", "La implementación completa"),
        ("This is a full done-for-you infrastructure build. The entire car. Not just the tires.", "Es una infraestructura completa hecha para ti. El auto completo. No solo las llantas."),
        ("Infrastructure Setup", "Configuración de infraestructura"),
        ("Dedicated domain registration & DNS", "Registro de dominios dedicados y DNS"),
        ("Inbox setup & auth (SPF, DKIM, DMARC)", "Configuración de inbox y autenticación (SPF, DKIM, DMARC)"),
        ("Automated 2-3 week inbox warming", "Calentamiento automatizado de inbox durante 2-3 semanas"),
        ("Data & Targeting", "Datos y segmentación"),
        ("ICP definition & buyer mapping", "Definición del cliente ideal (ICP) y mapeo de compradores"),
        ("Building verified lists of thousands of leads matching the ICP", "Creación de listas verificadas de miles de leads que coinciden con el ICP"),
        ("Ongoing list refresh & hygiene", "Actualización e higiene continua de listas"),
        ("Copywriting & Management", "Copywriting y gestión"),
        ("Writing copy", "Redacción de copy"),
        ("Multi-touchpoint sequence creation", "Creación de secuencias multipunto"),
        ("Continuous A/B testing & iteration", "Pruebas A/B e iteración continuas"),
        ("Daily sending & deliverability management", "Envío diario y gestión de entregabilidad"),
        ("Lead qualification & calendar routing", "Calificación de leads y enrutamiento al calendario"),
        ("The Guarantee", "La garantía"),
        ("You only pay when a qualified buyer books a call.", "Solo pagas cuando un comprador calificado agenda una llamada."),
        ("If a booked call doesn't fit your ICP, you don't pay for it.", "Si una llamada agendada no encaja con tu ICP, no la pagas."),
        ("No retainers. No risk.", "Sin retainers. Sin riesgo."),
        ("We handle everything. You just close deals.", "Nosotros nos encargamos de todo. Tú solo cierras ventas."),
        ("""<h4 class="text-lg font-bold mb-2 text-brand-300">"How much does this cost?"</h4>""", """<h4 class="text-lg font-bold mb-2 text-brand-300">"¿Cuánto cuesta esto?"</h4>"""),
        ("You only pay per qualified call that shows. Pricing is a flat per-show fee, set on the strategy call based on your industry and deal size. And if a booked call doesn't fit your ICP, you don't pay for it.", "Solo pagas por llamada calificada que se presente. El precio es una tarifa fija por llamada realizada, definida en la llamada estratégica según tu industria y el tamaño de tus ventas. Y si una llamada agendada no encaja con tu ICP, no la pagas."),
        ("""<h4 class="text-lg font-bold mb-2 text-brand-300">"How long to see results?"</h4>""", """<h4 class="text-lg font-bold mb-2 text-brand-300">"¿Cuánto tardan los resultados?"</h4>"""),
        ("Setup takes 2-3 weeks (domain warming, list building, copy). After that, you'll start seeing booked calls within the first 30 days. Consistent flow by month 2.", "La configuración tarda 2-3 semanas (calentamiento de dominios, creación de listas, copy). Después, empezarás a ver llamadas agendadas dentro de los primeros 30 días. Flujo constante para el segundo mes."),
        ("""<h4 class="text-lg font-bold mb-2 text-brand-300">"What if the leads aren't qualified?"</h4>""", """<h4 class="text-lg font-bold mb-2 text-brand-300">"¿Y si los leads no están calificados?"</h4>"""),
        ("""We vet every lead before they book. If someone books who doesn't fit your ICP, <strong class="text-white">we don't charge you.</strong> Simple as that.""", """Revisamos cada lead antes de que agende. Si alguien agenda sin encajar con tu ICP, <strong class="text-white">no te cobramos.</strong> Así de simple."""),
        ("""<h4 class="text-lg font-bold mb-2 text-brand-300">"Can I cancel anytime?"</h4>""", """<h4 class="text-lg font-bold mb-2 text-brand-300">"¿Puedo cancelar en cualquier momento?"</h4>"""),
        ("Yes. No long-term contracts. If you want to stop, you stop. No penalties. Our incentives are 100% aligned with yours.", "Sí. Sin contratos a largo plazo. Si quieres parar, paras. Sin penalidades. Nuestros incentivos están 100% alineados con los tuyos."),
        (">Next Steps</span>", ">Próximos pasos</span>"),
        ("Book a 15-minute call with me. Not a salesperson. Me. Zero obligation. Zero pressure.", "Agenda una llamada de 15 minutos conmigo. No un vendedor. Conmigo. Cero obligación. Cero presión."),
        ("Meet The Founder", "Conoce al fundador"),
        ('alt="Maxime - Founder of Leadigo"', 'alt="Maxime — fundador de Leadigo"'),
        ('"I founded Leadigo with one mission: to eliminate the guesswork in customer acquisition."', """« Fundé Leadigo con una sola misión: eliminar las conjeturas en la adquisición de clientes. »"""),
        ('"After working in software for 2 years at an investment bank, I saw firsthand how critical predictable revenue systems were to massive organizations. I wanted to bring my own creation into the world to solve this exact problem for high-ticket B2B companies—and this is it!"', """« Después de trabajar 2 años en software en un banco de inversión, vi de primera mano lo críticos que eran los sistemas de ingresos predecibles para las grandes organizaciones. Quería lanzar mi propia creación para resolver exactamente este problema para empresas B2B de ticket alto — ¡y aquí está! »"""),
    ]
    for old, new, *rest in pairs:
        count = rest[0] if rest else 1
        text = rep(text, old, new, count)
    (ROOT / "index-es.html").write_text(text, encoding="utf-8")


def roi_es():
    text = (ROOT / "roi_calculator.html").read_text(encoding="utf-8")
    text = common_es(text)
    text = rep(text, "<title>ROI Calculator | Leadigo</title>", "<title>Calculadora de ROI | Leadigo</title>")
    pairs = [
        (">The Math</span>", ">Los números</span>"),
        (">ROI Calculator</h1>", ">Calculadora de ROI</h1>"),
        ("Customer Value / LTV ($)", "Valor del cliente / LTV ($)"),
        ("Sales Calls Booked", "Llamadas de ventas agendadas"),
        ("Sales Call Close Rate", "Tasa de cierre de llamadas"),
        ("Gross Margin (%)", "Margen bruto (%)"),
        ("Advertising Rate ($)", "Tarifa publicitaria ($)"),
        (">Per Call</div>", ">Por llamada</div>"),
        (">Per Closed Client</div>", ">Por cliente cerrado</div>"),
        ("Added Revenue", "Ingresos agregados"),
        ("Price of Email Campaign", "Precio de la campaña de correos"),
        ("(Advertising Rate × Closed Clients)", "(Tarifa publicitaria × Clientes cerrados)", 2),
        ("(Advertising Rate × Calls Booked)", "(Tarifa publicitaria × Llamadas agendadas)"),
        ("""For every $1 spent on the email campaign, your business makes back $<span id="roiSubtext">0.00</span> in profit.""", """Por cada $1 gastado en la campaña de correos, tu negocio recupera $<span id="roiSubtext">0.00</span> en ganancia."""),
        ("new Intl.NumberFormat('en-US'", "new Intl.NumberFormat('es-MX'"),
        ('roiSubtext.textContent = "Infinite";', 'roiSubtext.textContent = "Infinito";'),
    ]
    for old, new, *rest in pairs:
        count = rest[0] if rest else 1
        text = rep(text, old, new, count)
    (ROOT / "roi_calculator-es.html").write_text(text, encoding="utf-8")


def strategy_es():
    text = (ROOT / "strategy_call.html").read_text(encoding="utf-8")
    text = common_es(text)
    text = rep(text, "<title>Strategy Call | Leadigo</title>", "<title>Llamada estratégica | Leadigo</title>")
    text = rep(text, 'href="index.html"', 'href="index-es.html"', 2)
    pairs = [
        ("Back to the VSL", "Volver a la VSL"),
        (">Next Steps</span>", ">Próximos pasos</span>"),
        ("Book Your Free Strategy Call", "Reserva tu llamada estratégica gratuita"),
        ("This call is to see if our cold outreach is a good fit for your company — and to get to know more about our cold outreach services. Zero obligation. Zero pressure.", "Esta llamada es para ver si nuestra prospección en frío encaja con tu empresa — y para conocer más sobre nuestros servicios de prospección en frío. Cero obligación. Cero presión."),
    ]
    for old, new in pairs:
        text = rep(text, old, new)
    (ROOT / "strategy_call-es.html").write_text(text, encoding="utf-8")


index_es()
roi_es()
strategy_es()
print("Spanish pages generated: index-es.html, roi_calculator-es.html, strategy_call-es.html")
