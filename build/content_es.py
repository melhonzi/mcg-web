# -*- coding: utf-8 -*-
"""Contenido del sitio en español (Paraguay). Fuente para las versiones en inglés y portugués."""

DATA = {
    "lang": "es",
    "preview_banner": "Vista previa interna — no indexada — datos sujetos a confirmación antes de publicar",
    "saltar": "Ir al contenido",
    "relacionados": "Seguí explorando",
    "textos_form": {
        "formOk": "Recibimos tu consulta. Te vamos a responder al correo que dejaste. Si preferís que hablemos ahora, escribinos por WhatsApp.",
        "formWhatsapp": "Preparamos tu consulta y abrimos WhatsApp en una pestaña nueva: revisá el mensaje y presioná enviar allí. Si no se abrió, usá el botón de abajo.",
        "formIncompleto": "Completá los campos obligatorios antes de continuar."
    },
    "nav_aria": "Navegación principal",
    "menu_label": "Abrir menú",
    "lang_aria": "Cambiar idioma",
    "cta_nav": "Hablá con nosotros",
    "logo_alt": "MCG Consultora Contable y Tributaria — estudio contable en Asunción, Paraguay, dirigido por Cristina Rolón",
    "org_description": (
        "MCG Consultora Contable y Tributaria es un estudio contable de Asunción, Paraguay, "
        "dirigido por la Contadora Pública Cristina Rolón. Brinda contabilidad empresarial, "
        "estrategia tributaria ante la DNIT, constitución de sociedades (EAS, SRL y SA) y "
        "acompañamiento a empresarios e inversionistas extranjeros que se instalan en Paraguay."
    ),
    "person_jobtitle": "Contadora Pública · Magíster en Impuestos · Directora de MCG Consultora Contable y Tributaria",
    "person_description": (
        "Cristina Rolón es Contadora Pública egresada de la Universidad Nacional de Asunción (2008), "
        "Magíster en Impuestos y directora de MCG Consultora Contable y Tributaria en Asunción, Paraguay, "
        "con 18 años de experiencia profesional en contabilidad empresarial y estrategia tributaria."
    ),
    "person_knows": [
        "Contabilidad empresarial en Paraguay", "Estrategia tributaria", "Impuesto a la Renta Empresarial (IRE)",
        "Impuesto al Valor Agregado (IVA)", "DNIT", "Constitución de sociedades en Paraguay",
        "Inversión extranjera en Paraguay", "Facturación electrónica (SIFEN)",
    ],
    "footer": {
        "tagline": ("Contabilidad empresarial y estrategia tributaria en Paraguay, bajo la dirección de "
                    "Cristina Rolón, Contadora Pública (UNA) y Magíster en Impuestos."),
        "ciudad": "Asunción, Paraguay · Atención en español, inglés y portugués",
        "col_servicios": "Servicios",
        "col_estudio": "Estudio",
        "col_contacto": "Contacto",
        "wa_mensaje": "Hola MCG, vengo de la página web y quiero hacer una consulta",
        "copyright": "MCG Consultora Contable y Tributaria. Todos los derechos reservados.",
        "legal": ("Contenido informativo general sobre normativa paraguaya; no reemplaza una evaluación "
                  "profesional de cada caso."),
    },
    "pages": {},
}

P = DATA["pages"]

# ---------------------------------------------------------------------- HOME
P["home"] = {
    "slug": "index.html",
    "nav": "Inicio",
    "nav_footer": "Inicio",
    "title": "Estudio contable en Paraguay | MCG Consultora Contable",
    "description": ("Estudio contable en Asunción: contabilidad empresarial, estrategia tributaria ante la DNIT, sociedades y extranjeros. Dirige Cristina Rolón."),
    "h1": "Contabilidad empresarial y estrategia tributaria en Paraguay",
    "blocks": [
        {
            "type": "hero",
            "chip": "Consultora contable y tributaria · Asunción, Paraguay",
            "h1_html": "Contabilidad empresarial y <span class=\"acento\">estrategia tributaria</span> en Paraguay",
            "lead": ("Acompañamos a empresas e inversionistas en sus decisiones contables, tributarias y de instalación "
                     "en Paraguay, con información confiable y criterio profesional."),
            "firma_html": ("Bajo la dirección de <strong>Cristina Rolón</strong>, Contadora Pública (UNA), Magíster en "
                           "Impuestos y miembro de directorios empresariales, con un equipo estable detrás."),
            "cta1": "Hablá con nosotros",
            "cta2": "Conocer nuestros servicios",
            "cta2_href": "#servicios",
            "credenciales": [
                ("18 años", "de experiencia profesional"),
                ("Contadora Pública", "Universidad Nacional de Asunción"),
                ("Magíster", "en Impuestos"),
                ("+30 empresas", "con ERP contable implementado"),
            ],
            "figura_alt": ("Cristina Rolón, Contadora Pública y directora de MCG Consultora Contable y Tributaria, "
                           "estudio contable en Asunción, Paraguay"),
            "figura_nombre": "Cristina Rolón",
            "figura_rol": "Directora de MCG · Contadora Pública · Magíster en Impuestos",
        },
        {
            "type": "franja",
            "items": [
                "Empresas que necesitan ordenar su situación contable y tributaria en Paraguay",
                "Empresarios e inversionistas extranjeros que quieren instalarse en Paraguay",
                "Empresas de cualquier tamaño y rubro que buscan un estudio contable serio y prolijo",
                "Dueños y gerentes que necesitan información confiable para decidir",
            ],
            "microcopy": ("Trabajamos con todo tipo de empresas: lo que definimos juntos es el alcance del servicio, "
                          "no un piso de facturación."),
        },
        {
            "type": "caminos",
            "items": [
                {"badge": "Ya tengo una empresa", "h3": "Ya tengo una empresa en Paraguay",
                 "p": ("Necesito contabilidad confiable, previsión tributaria ante la DNIT y acompañamiento estratégico "
                       "para tomar mejores decisiones."),
                 "cta": "Ver contabilidad empresarial →", "target": "contabilidad"},
                {"badge": "Quiero instalarme", "h3": "Quiero instalar mi empresa en Paraguay",
                 "p": ("Soy extranjero o inversionista y necesito acompañamiento local para constituir la sociedad, "
                       "obtener el RUC y operar en regla desde el primer día."),
                 "cta": "Ver acompañamiento para extranjeros →", "target": "extranjeros"},
            ],
        },
        {
            "type": "rich",
            "alt": True,
            "eyebrow": "Quiénes somos",
            "h2": "Un estudio contable de confianza en Asunción, Paraguay",
            "paragraphs": [
                ("MCG Consultora Contable y Tributaria es un estudio contable con base en Asunción que trabaja con empresas "
                 "paraguayas y con inversionistas extranjeros que eligen Paraguay para instalar o expandir su negocio. "
                 "Nuestra dirección está a cargo de <strong>Cristina Rolón</strong>, Contadora Pública egresada de la "
                 "Universidad Nacional de Asunción en 2008, Magíster en Impuestos y con 18 años de experiencia profesional "
                 "en distintas industrias."),
                ("Nuestro trabajo no termina en presentar declaraciones a tiempo. Una contabilidad bien llevada en Paraguay "
                 "debería servir para algo más: para saber cuánto gana realmente cada línea de negocio, para anticipar el "
                 "impacto del IRE y del IVA antes de que llegue el vencimiento, para sostener una conversación con el banco "
                 "con números que cierran, y para dormir tranquilo si mañana la DNIT pide explicaciones."),
                ("Por eso combinamos tres cosas en cada empresa que atendemos: cumplimiento prolijo ante la DNIT, información "
                 "ordenada y a tiempo para la dirección, y una mirada tributaria preventiva que evita sorpresas. Ese es el "
                 "estándar con el que trabajamos, y es lo que define la confianza que buscamos construir con cada cliente."),
            ],
        },
        {
            "type": "problemas",
            "eyebrow": "Problemas que resolvemos",
            "h2": "Cuando la contabilidad no te ayuda a decidir",
            "lead": "Estas son las situaciones más frecuentes que nos traen las empresas antes de trabajar con nosotros.",
            "items": [
                "Información contable que llega tarde o que no permite tomar decisiones.",
                "Falta de previsión sobre las obligaciones tributarias del período y sus vencimientos ante la DNIT.",
                "Desorden entre movimientos bancarios, facturación electrónica y registros contables.",
                "Crecimiento acelerado sin controles internos ni respaldo documental suficiente.",
                "Períodos anteriores sin presentar o con presentaciones que hay que regularizar.",
                "Incertidumbre de un extranjero sobre cómo constituir y operar legalmente un negocio en Paraguay.",
            ],
            "paragraphs": [
                ("Ninguno de estos problemas se resuelve con una sola declaración presentada a último momento. Se resuelven "
                 "ordenando el proceso completo: qué documentación entra, cómo se registra, qué se revisa cada mes y qué "
                 "información llega a la dirección para decidir."),
            ],
        },
        {
            "type": "cards",
            "alt": True,
            "eyebrow": "Servicios",
            "h2": "Qué hacemos en MCG",
            "lead": ("Cinco servicios pensados para el ciclo completo de una empresa en Paraguay: desde su constitución "
                     "hasta su operación ordenada y su estrategia tributaria."),
            "columns": 2,
            "items": [
                ("Contabilidad empresarial",
                 "Gestión contable mensual, cumplimiento de obligaciones ante la DNIT, cierres e informes periódicos para que la dirección decida con información confiable."),
                ("Estrategia tributaria",
                 "Diagnóstico de la situación tributaria, identificación de contingencias, planificación de obligaciones y un plan de acción con prioridades claras."),
                ("Constitución de sociedades",
                 "Evaluación de la figura societaria (EAS, SRL o SA), coordinación del proceso de constitución, alta de RUC ante la DNIT y puesta en marcha contable."),
                ("Empresarios extranjeros",
                 "Acompañamiento local para instalar y operar una empresa en Paraguay: sociedad, documentación, coordinación migratoria y contabilidad desde el día uno."),
                ("Implementación de ERP — módulo contable",
                 "Parametrización del corazón contable del ERP y su integración con tesorería, logística, producción, compras y bancos, con costeo y trazabilidad auditable."),
            ],
        },
        {
            "type": "pasos",
            "eyebrow": "Cómo trabajamos",
            "h2": "Un proceso claro desde la primera conversación",
            "items": [
                ("Conversamos sobre tu empresa", "Entendemos tu rubro, tu operación actual, tu situación documental y qué necesitás resolver primero."),
                ("Revisamos la situación real", "Vemos en qué estado están los registros, las presentaciones ante la DNIT y la documentación de respaldo."),
                ("Presentamos una propuesta", "Con alcance, honorarios y condiciones por escrito, sin costos ocultos ni servicios que no pediste."),
                ("Coordinamos la incorporación", "Ordenamos la transición desde tu contador anterior o desde cero, y arrancamos según lo acordado."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Preguntas frecuentes",
            "h2": "Antes de escribirnos",
            "ver_todas": "Ver las 28 preguntas frecuentes sobre impuestos y empresas en Paraguay →",
            "items": [
                ("¿Trabajan con empresas de cualquier tamaño?",
                 "Sí. Trabajamos con todo tipo de empresas en Paraguay: compañías que ya facturan de forma significativa, negocios que recién arrancan y empresas que necesitan ordenar períodos anteriores. Lo que definimos en cada caso es el alcance del servicio según la complejidad real de la operación —rubro, volumen de comprobantes, empleados, sucursales, importaciones y situación documental—, no un piso de facturación."),
                ("¿Cuánto cuesta trabajar con MCG?",
                 "Los honorarios dependen del alcance y de la complejidad de tu operación. Pesan el rubro, el volumen de comprobantes electrónicos, la cantidad de empleados, las sucursales, si hay importaciones o exportaciones y el estado de la documentación. Después de conocer tu empresa presentamos una propuesta concreta y por escrito, con el alcance detallado antes de empezar."),
                ("¿Atienden a empresarios e inversionistas extranjeros?",
                 "Sí, y es una parte importante de nuestro trabajo. Acompañamos a extranjeros que quieren instalar y operar una empresa en Paraguay: elección de la figura societaria, constitución, obtención del RUC ante la DNIT, preparación de la documentación bancaria, coordinación con profesionales migratorios y contabilidad desde el primer día. Atendemos en español, inglés y portugués."),
                ("¿Qué pasa si tengo períodos atrasados ante la DNIT?",
                 "Es más común de lo que parece y tiene solución. Empezamos por un diagnóstico del estado real: qué períodos faltan, qué documentación existe y qué presentaciones quedaron pendientes. Con eso armamos un plan de regularización, que se cotiza aparte del servicio mensual porque es un trabajo puntual distinto. Cuanto antes se aborda, menor es el riesgo de acumular contingencias."),
                ("¿La primera conversación tiene costo?",
                 "No. La solicitud inicial nos permite entender tu situación y evaluar el encaje y el alcance posible del trabajo. Si hace falta una revisión técnica más profunda o un diagnóstico tributario completo, eso se cotiza por separado y se acuerda antes de empezar."),
            ],
        },
        {
            "type": "opiniones",
            "eyebrow": "Opiniones",
            "h2": "Lo que dicen nuestros clientes",
            "lead": "Las opiniones de las empresas que trabajan con MCG están publicadas en nuestro perfil de Google Business, donde cualquiera puede verificarlas y dejar la suya.",
            "cta": "Ver opiniones en Google",
            "reseñas": [],
        },
        {
            "type": "cta",
            "h2": "Conversemos sobre tu empresa",
            "lead": "Contanos tu situación y evaluamos juntos el alcance del trabajo.",
            "cta": "Hablá con nosotros",
        },
    ],
}

# -------------------------------------------------------------- CONTABILIDAD
P["contabilidad"] = {
    "slug": "contabilidad-empresarial.html",
    "nav": "Contabilidad",
    "nav_footer": "Contabilidad empresarial",
    "service": "Contabilidad empresarial",
    "title": "Contabilidad empresarial en Paraguay | MCG Consultora",
    "description": ("Contabilidad mensual para empresas en Paraguay: registros, IVA e IRE ante la DNIT, cierres e informes para la dirección. Estudio contable en Asunción."),
    "h1": "Contabilidad empresarial en Paraguay, pensada para decidir",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Contabilidad empresarial",
         "h1": "Contabilidad empresarial en Paraguay, pensada para decidir",
         "lead": ("Cumplimiento ordenado ante la DNIT y mejor información para que la dirección de tu empresa "
                  "tome decisiones con números confiables."),
         "cta": "Hablá con nosotros"},
        {
            "type": "rich",
            "eyebrow": "El servicio",
            "h2": "Qué significa llevar bien la contabilidad de una empresa en Paraguay",
            "paragraphs": [
                ("Llevar la contabilidad de una empresa en Paraguay implica mucho más que cargar comprobantes y presentar "
                 "declaraciones. Implica mantener registros consistentes con la Ley 6380/2019, liquidar correctamente el IVA "
                 "y el Impuesto a la Renta Empresarial (IRE) según el régimen que le corresponde a la empresa, cumplir con la "
                 "facturación electrónica del sistema SIFEN, conciliar los movimientos bancarios con lo registrado y tener "
                 "la documentación de respaldo ordenada por si la DNIT la solicita."),
                ("En MCG hacemos ese trabajo con un criterio simple: la contabilidad tiene que cerrar hacia afuera —ante la "
                 "administración tributaria— y también hacia adentro —ante la dirección de la empresa—. Si los números solo "
                 "sirven para cumplir con el vencimiento, pero no le dicen al dueño cuánto margen deja cada línea de negocio "
                 "o por qué subió el costo este trimestre, el trabajo está a medias."),
                ("Trabajamos con empresas de todos los rubros: comercio, servicios, construcción, importación, tecnología, "
                 "salud, gastronomía y proyectos de inversión extranjera. Cada rubro tiene sus particularidades tributarias, "
                 "y eso es parte de lo que evaluamos antes de definir el alcance."),
            ],
        },
        {
            "type": "cards",
            "alt": True,
            "eyebrow": "Alcance propuesto",
            "h2": "Qué incluye el servicio de contabilidad mensual",
            "lead": "Este es el alcance de referencia. El alcance final de cada empresa se define según su operación real.",
            "columns": 3,
            "items": [
                ("Gestión contable mensual", "Registro y mantenimiento contable de toda la operación, con criterios consistentes período a período."),
                ("Obligaciones tributarias", "Preparación y presentación de las obligaciones aplicables ante la DNIT, con control de vencimientos según el RUC."),
                ("Cierres e informes periódicos", "Cierres con informes que muestran resultados, márgenes y evolución, en un formato que la dirección pueda leer."),
                ("Conciliaciones", "Conciliación de movimientos bancarios, facturación electrónica y registros contables, según el plan contratado."),
                ("Seguimiento documental", "Orden y control de la documentación de respaldo, que es lo primero que se pide en una fiscalización."),
                ("Coordinación con la DNIT", "Gestión de trámites, consultas y comunicaciones con la administración tributaria en nombre de la empresa."),
            ],
        },
        {
            "type": "checks",
            "eyebrow": "Qué cambia en tu empresa",
            "h2": "Lo que deberías poder hacer cuando la contabilidad está ordenada",
            "items": [
                "Saber, sin esperar al cierre del año, cómo viene el resultado del período.",
                "Anticipar cuánto vas a pagar de IVA y de IRE antes de que llegue el vencimiento.",
                "Responder rápido cuando un banco pide estados financieros o respaldo documental.",
                "Tener claro qué comprobantes faltan y quién los tiene que conseguir.",
                "Entrar a una fiscalización de la DNIT con la documentación en orden y sin improvisar.",
                "Discutir con tu contador decisiones de negocio, no solo vencimientos.",
            ],
        },
        {
            "type": "planes",
            "eyebrow": "Niveles de servicio",
            "h2": "Dos formas de trabajar con nosotros",
            "items": [
                {"badge": "Contabilidad empresarial", "valor": "Cotización personalizada", "destacado": True,
                 "p": "Gestión contable y tributaria ordenada, para empresas de cualquier tamaño y rubro en Paraguay.",
                 "checks": ["Gestión contable mensual y cumplimiento ante la DNIT",
                            "Cierres e informes periódicos",
                            "Seguimiento documental y coordinación con la administración tributaria"],
                 "cta": "Consultar por este plan"},
                {"badge": "Contabilidad y acompañamiento estratégico", "valor": "Propuesta personalizada",
                 "p": "Para operaciones de mayor complejidad, con acompañamiento estratégico continuo a la dirección.",
                 "checks": ["Todo lo del servicio de contabilidad empresarial",
                            "Reuniones de revisión estratégica con la dirección",
                            "Análisis tributario preventivo y acompañamiento en decisiones"],
                 "cta": "Consultar por este plan"},
            ],
            "paragraphs": [
                ("Los honorarios se definen según el alcance y la complejidad operativa: rubro, volumen de comprobantes, "
                 "cantidad de empleados, sucursales y estado de la documentación, entre otros factores. La regularización de "
                 "períodos anteriores, las auditorías y los trabajos extraordinarios se cotizan por separado y siempre se "
                 "acuerdan por escrito antes de facturarse."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Preguntas frecuentes",
            "h2": "Sobre el servicio contable",
            "ver_todas": "Ver todas las preguntas frecuentes sobre impuestos y empresas en Paraguay →",
            "items": [
                ("¿Cada cuánto presenta declaraciones una empresa en Paraguay?",
                 "Depende del impuesto y del régimen. El IVA se liquida y presenta mensualmente; el IRE tiene una liquidación anual, con anticipos según el régimen; y existen presentaciones informativas adicionales según la actividad. Los vencimientos siguen el calendario de la DNIT según el último dígito del RUC, y parte de nuestro servicio es sostener un calendario propio para cada empresa."),
                ("¿Se puede cambiar de contador a mitad de año?",
                 "Sí, y es una situación habitual. Lo importante es ordenar la transición: relevar qué períodos están presentados, obtener los archivos y respaldos del contador anterior, verificar saldos de apertura y detectar si quedó algo pendiente ante la DNIT antes de continuar. Ese relevamiento inicial lo hacemos siempre, porque arrancar sin conocer el punto de partida genera problemas más adelante."),
                ("¿El servicio incluye liquidación de sueldos?",
                 "La liquidación de remuneraciones y las obligaciones laborales se evalúan según el caso y se acuerdan dentro del alcance cuando corresponde. Al definir la propuesta dejamos explícito qué queda incluido y qué se cotiza aparte, para que no haya ambigüedad después."),
                ("¿Qué pasa si la DNIT fiscaliza a mi empresa?",
                 "Acompañamos a la empresa durante el proceso: ordenamos y presentamos la documentación requerida, respondemos los requerimientos formales dentro de los plazos y coordinamos con los profesionales que hagan falta según el alcance de la fiscalización. Ningún estudio serio puede prometer que no habrá ajustes; lo que sí se puede hacer es llegar con los registros y respaldos en condiciones, que es exactamente lo que reduce el riesgo."),
            ],
        },
        {"type": "cta", "h2": "Ordenemos la contabilidad de tu empresa",
         "lead": "Contanos tu situación actual y evaluamos el alcance juntos.",
         "cta": "Hablá con nosotros"},
    ],
}

# ---------------------------------------------------------------- TRIBUTARIA
P["tributaria"] = {
    "slug": "estrategia-tributaria.html",
    "nav": "Estrategia tributaria",
    "nav_footer": "Estrategia tributaria",
    "service": "Estrategia y planificación tributaria",
    "title": "Estrategia tributaria en Paraguay ante la DNIT | MCG",
    "description": ("Diagnóstico tributario, contingencias y plan de acción para empresas en Paraguay. Planificación de IRE, IVA e IDU ante la DNIT, con criterio preventivo."),
    "h1": "Estrategia tributaria y prevención de riesgos en Paraguay",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Estrategia tributaria",
         "h1": "Estrategia tributaria y prevención de riesgos en Paraguay",
         "lead": ("Ordenamos la situación tributaria de tu empresa ante la DNIT, identificamos contingencias y armamos "
                  "un plan de acción con prioridades claras."),
         "cta": "Hablá con nosotros"},
        {
            "type": "rich",
            "eyebrow": "El enfoque",
            "h2": "Planificar antes, no explicar después",
            "paragraphs": [
                ("La mayoría de los problemas tributarios que vemos en Paraguay no nacen de una decisión audaz: nacen de la "
                 "falta de revisión. Comprobantes que no respaldan lo que se dedujo, regímenes elegidos hace años que ya no "
                 "corresponden al tamaño actual de la empresa, saldos que nunca se conciliaron, retiros de utilidades sin "
                 "considerar el IDU, o pagos al exterior sin analizar el impuesto a la renta de no residentes."),
                ("Una estrategia tributaria seria empieza por saber exactamente dónde está parada la empresa: qué impuestos "
                 "le corresponden según la Ley 6380/2019, en qué régimen del IRE está inscripta, qué contingencias arrastra "
                 "de períodos anteriores y qué decisiones próximas —una inversión, una distribución de utilidades, la apertura "
                 "de una sucursal, la incorporación de un socio— van a tener impacto tributario."),
                ("Con ese mapa armamos un plan de acción con prioridades: qué hay que corregir ya, qué puede esperar al "
                 "próximo cierre y qué requiere una decisión del dueño. No prometemos ausencia de fiscalizaciones ni de "
                 "ajustes —eso no lo puede prometer nadie—: trabajamos para que, si llegan, la empresa esté en condiciones "
                 "de responder con documentación y criterio."),
            ],
        },
        {
            "type": "checks",
            "alt": True,
            "eyebrow": "Qué evaluamos",
            "h2": "Qué cubre el diagnóstico tributario",
            "items": [
                "Situación tributaria actual de la empresa y régimen del IRE en el que está inscripta.",
                "Contingencias de períodos abiertos y consistencia de las declaraciones presentadas ante la DNIT.",
                "Documentación de respaldo de costos, gastos y créditos fiscales de IVA.",
                "Coherencia entre registros contables, movimientos bancarios y facturación electrónica (SIFEN).",
                "Tratamiento de retiros, dividendos y utilidades (IDU) y de pagos al exterior (INR).",
                "Planificación de obligaciones y vencimientos del ejercicio siguiente.",
                "Alternativas legales aplicables al caso concreto, con su impacto estimado.",
            ],
        },
        {
            "type": "cards",
            "eyebrow": "Entregables",
            "h2": "Qué recibís al terminar el diagnóstico",
            "columns": 2,
            "items": [
                ("Informe ejecutivo", "Resumen claro de la situación, escrito para que lo entienda la dirección y no solo un contador."),
                ("Mapa de riesgos y prioridades", "Qué contingencias existen, cuál es su exposición estimada y en qué orden conviene atenderlas."),
                ("Recomendaciones concretas", "Alternativas aplicables a tu caso, con lo que implica cada una en términos de trabajo y de impacto."),
                ("Hoja de ruta de implementación", "Pasos, responsables y orden de ejecución para poner el plan en marcha sin frenar la operación."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Preguntas frecuentes",
            "h2": "Sobre estrategia y blindaje tributario",
            "ver_todas": "Ver todas las preguntas frecuentes sobre impuestos y empresas en Paraguay →",
            "items": [
                ("¿Qué se entiende por blindaje fiscal o tributario en Paraguay?",
                 "En el uso cotidiano, blindaje se refiere a ordenar la estructura societaria, la documentación y el cumplimiento tributario para reducir riesgos evitables: elegir bien la figura societaria y el régimen del IRE, mantener la contabilidad al día, separar el patrimonio personal del de la empresa, respaldar cada deducción y cumplir en tiempo y forma ante la DNIT. Ningún estudio serio puede prometer inmunidad ante fiscalizaciones ni eliminar el riesgo por completo: lo que sí se puede hacer es trabajar de forma preventiva y prolija para minimizar exposiciones innecesarias."),
                ("¿El diagnóstico reemplaza la contabilidad mensual?",
                 "No. El diagnóstico es un trabajo puntual de revisión y planificación, con entregables propios. La gestión contable mensual es un servicio continuo y separado. Muchas empresas empiezan por el diagnóstico para entender dónde están paradas y después deciden si incorporan también la contabilidad mensual con nosotros."),
                ("¿Cuánto tarda un diagnóstico tributario?",
                 "Depende del volumen de información, de la cantidad de períodos a revisar y de qué tan disponible esté la documentación. Una empresa con registros ordenados y archivos digitales completos avanza mucho más rápido que una que tiene que reconstruir respaldos. Al evaluar tu caso te damos un plazo concreto antes de empezar."),
                ("¿Sirve para una empresa que recién arranca?",
                 "Sí, y suele ser el mejor momento. Definir desde el inicio la figura societaria, el régimen tributario correcto, cómo se van a documentar los gastos y cómo se van a retirar las utilidades evita tener que corregir años después, cuando corregir cuesta mucho más."),
            ],
        },
        {"type": "cta", "h2": "Ordenemos la situación tributaria de tu empresa",
         "lead": "Empezamos con una conversación sobre tu operación actual.",
         "cta": "Hablá con nosotros"},
    ],
}

# ---------------------------------------------------------------- SOCIEDADES
P["sociedades"] = {
    "slug": "constitucion-sociedades.html",
    "nav": "Sociedades",
    "nav_footer": "Constitución de sociedades",
    "service": "Constitución de sociedades",
    "title": "Constituir una empresa en Paraguay: EAS, SRL o SA | MCG",
    "description": ("Constituir una empresa en Paraguay: elegir entre EAS, SRL o SA, proceso societario, alta de RUC ante la DNIT y puesta en marcha contable. En Asunción."),
    "h1": "Constitución de sociedades en Paraguay: EAS, SRL o SA",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Constitución de sociedades",
         "h1": "Constitución de sociedades en Paraguay: EAS, SRL o SA",
         "lead": ("Evaluamos tu actividad, tus socios y tus objetivos antes de recomendar una estructura, y acompañamos "
                  "el proceso hasta que la empresa está operativa."),
         "cta": "Hablá con nosotros"},
        {
            "type": "rich",
            "eyebrow": "La decisión de fondo",
            "h2": "Qué figura societaria conviene en Paraguay",
            "paragraphs": [
                ("En Paraguay conviven varias figuras societarias, y tres concentran la mayoría de los casos. La "
                 "<strong>EAS (Empresa por Acciones Simplificada)</strong> fue pensada para simplificar la creación de "
                 "empresas: permite constituir con una estructura flexible y es la vía más ágil para emprendimientos y "
                 "pymes. La <strong>SRL (Sociedad de Responsabilidad Limitada)</strong> es la figura tradicional para "
                 "negocios con pocos socios y una gestión simple, con cuotas sociales en lugar de acciones. La "
                 "<strong>SA (Sociedad Anónima)</strong> es la opción habitual para operaciones de mayor envergadura: "
                 "permite emitir acciones, incorporar inversores y sostener una gobernanza más formal, algo que suelen "
                 "requerir bancos, socios institucionales y proyectos de inversión extranjera."),
                ("No existe una figura que sea siempre la mejor. La elección correcta depende de cuántos socios hay y "
                 "cómo entran o salen, de si se planea incorporar inversores, del tipo de actividad y del perfil de "
                 "contraparte con el que la empresa va a trabajar. Un proyecto que va a licitar con entes públicos o a "
                 "pedir financiamiento bancario importante no se estructura igual que un negocio familiar."),
                ("Ese análisis lo hacemos antes de iniciar cualquier trámite, porque cambiar de figura después implica "
                 "costo, tiempo y, en algunos casos, consecuencias tributarias que se pueden evitar decidiendo bien al "
                 "principio."),
            ],
        },
        {
            "type": "cards",
            "alt": True,
            "eyebrow": "Qué incluye",
            "h2": "Acompañamiento en todo el proceso",
            "columns": 3,
            "items": [
                ("Evaluación inicial", "Analizamos actividad, socios, objetivos y planes de crecimiento antes de sugerir una estructura."),
                ("Coordinación de la constitución", "Acompañamos el proceso societario de punta a punta y coordinamos con escribanía cuando corresponde."),
                ("Organización documental", "Ordenamos y revisamos la documentación de cada socio, incluida la de socios extranjeros."),
                ("Alta ante la DNIT", "Inscripción en el RUC, definición del régimen tributario aplicable y alta de obligaciones."),
                ("Facturación electrónica", "Puesta en marcha del esquema de comprobantes electrónicos para que la empresa pueda facturar en regla."),
                ("Arranque contable", "La empresa empieza a operar con la contabilidad ordenada desde el primer movimiento."),
            ],
        },
        {
            "type": "pasos",
            "eyebrow": "El proceso",
            "h2": "Cómo es constituir una empresa en Paraguay",
            "items": [
                ("Definición de la estructura", "Elegimos la figura societaria, el objeto social, el capital y la distribución entre socios."),
                ("Reunión de documentación", "Identificación de cada socio, documentos societarios y, si hay socios extranjeros, legalizaciones o apostillas."),
                ("Constitución e inscripción", "Se formaliza el acto constitutivo y se realizan las inscripciones registrales correspondientes."),
                ("RUC y obligaciones", "Alta ante la DNIT, definición del régimen del IRE y de las obligaciones que le corresponden a la empresa."),
                ("Habilitaciones y facturación", "Habilitación municipal según el rubro y puesta en marcha de la facturación electrónica."),
                ("Puesta en marcha contable", "Apertura de registros, criterios contables y calendario de vencimientos propio de la empresa."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Preguntas frecuentes",
            "h2": "Sobre constituir una empresa en Paraguay",
            "ver_todas": "Ver todas las preguntas frecuentes sobre impuestos y empresas en Paraguay →",
            "items": [
                ("¿Cuánto tiempo lleva constituir una empresa en Paraguay?",
                 "Depende del tipo societario elegido, de la carga de trabajo vigente en los registros y escribanías involucradas y, sobre todo, de qué tan completa esté la documentación desde el inicio. Cuando hay socios extranjeros con documentos a legalizar o apostillar en el exterior, ese suele ser el paso que más condiciona el plazo. La EAS es, en general, la figura con el trámite más ágil por su diseño simplificado."),
                ("¿Un extranjero puede ser socio o accionista de una empresa paraguaya?",
                 "Sí. La legislación paraguaya admite socios y accionistas extranjeros, tanto personas físicas como jurídicas. Lo que cambia respecto de un socio local es la documentación: se requieren documentos legalizados o apostillados en el país de origen y, en el caso de personas jurídicas extranjeras, la documentación societaria de la empresa matriz debidamente traducida y legalizada."),
                ("¿Cuánto capital hace falta para abrir una empresa en Paraguay?",
                 "El capital social se define según la figura societaria elegida y el tipo de actividad, y debe guardar relación con la operación que la empresa va a desarrollar. Es una de las definiciones que revisamos en la evaluación inicial, porque tiene efectos prácticos: bancos, contrapartes y organismos suelen mirar ese dato."),
                ("¿Se puede constituir sin viajar a Paraguay?",
                 "En muchos casos sí se puede avanzar buena parte del proceso a distancia, mediante poderes especiales otorgados en el país de origen y debidamente legalizados o apostillados, que habilitan a un representante local a firmar la documentación societaria. Algunas gestiones puntuales, como la apertura de cuenta bancaria o ciertos trámites migratorios, suelen requerir presencia física o al menos una gestión más directa."),
            ],
        },
        {"type": "cta", "h2": "Evaluemos la estructura de tu empresa",
         "lead": "Contanos tu actividad y tus objetivos para orientarte mejor.",
         "cta": "Hablá con nosotros"},
    ],
}

# --------------------------------------------------------------- EXTRANJEROS
P["extranjeros"] = {
    "slug": "empresarios-extranjeros.html",
    "nav": "Extranjeros",
    "nav_footer": "Empresarios extranjeros",
    "service": "Acompañamiento a inversionistas extranjeros",
    "title": "Instalar tu empresa en Paraguay siendo extranjero | MCG",
    "description": ("Acompañamiento local para extranjeros que instalan su empresa en Paraguay: sociedad, RUC, banco, migraciones y contabilidad. En tres idiomas."),
    "h1": "Instalá y operá tu empresa en Paraguay con acompañamiento local",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Empresarios e inversionistas extranjeros",
         "h1": "Instalá y operá tu empresa en Paraguay con acompañamiento local",
         "lead": ("Trabajamos con extranjeros que quieren operar o invertir en Paraguay de verdad, no solo tramitar "
                  "documentación personal."),
         "cta": "Hablá con nosotros"},
        {
            "type": "rich",
            "eyebrow": "Por qué Paraguay",
            "h2": "Qué mira un inversionista extranjero cuando evalúa Paraguay",
            "paragraphs": [
                ("Paraguay aparece con frecuencia en las evaluaciones de empresarios de Brasil, Argentina, Estados Unidos y "
                 "Europa por un conjunto de razones concretas: tasas impositivas comparativamente bajas dentro de la región "
                 "—10% de IRE y 10% de IVA como tasas generales, con IVA reducido del 5% para determinados bienes y "
                 "servicios—, un sistema tributario relativamente simple desde la Ley 6380/2019, costos operativos "
                 "competitivos y un régimen de residencia vinculado a la inversión."),
                ("Nada de esto significa cero impuestos ni beneficios automáticos, y desconfiá de quien lo plantee así. "
                 "La carga tributaria real de cada empresa depende de su régimen, su rubro, su estructura societaria y de "
                 "cómo retire sus utilidades. Un proyecto bien estructurado desde el inicio aprovecha el marco legal; uno "
                 "improvisado termina corrigiendo con costo."),
                ("Nuestro trabajo es el lado paraguayo del proyecto: que la sociedad esté bien constituida, que la empresa "
                 "esté correctamente inscripta ante la DNIT, que la contabilidad arranque ordenada y que la documentación "
                 "esté en condiciones para bancos y contrapartes. Las obligaciones que el inversionista mantenga en su país "
                 "de origen requieren coordinación con especialistas de esa jurisdicción."),
            ],
        },
        {
            "type": "pasos",
            "alt": True,
            "eyebrow": "El recorrido",
            "h2": "Cómo acompañamos tu instalación en Paraguay",
            "items": [
                ("Evaluación del proyecto", "Entendemos tu actividad, tus objetivos, tu estructura actual en el exterior y tu situación de partida."),
                ("Estructura y constitución", "Definimos la figura societaria conveniente y coordinamos el proceso de constitución en Paraguay."),
                ("Alta ante la DNIT", "Inscripción en el RUC, régimen tributario aplicable y alta de las obligaciones que correspondan."),
                ("Coordinación migratoria", "Con profesionales competentes en la materia, según tu situación y el tipo de residencia que buscás."),
                ("Documentación bancaria", "Preparamos la documentación necesaria para tus gestiones de apertura de cuenta y financiamiento."),
                ("Contabilidad y operación", "La empresa arranca con la contabilidad ordenada y seguimos acompañando la operación mes a mes."),
            ],
        },
        {
            "type": "rich",
            "eyebrow": "Residencia e inversión",
            "h2": "Residencia por inversión, cédula paraguaya y RUC: tres cosas distintas",
            "paragraphs": [
                ("Es la confusión más frecuente y conviene despejarla temprano. La <strong>residencia</strong> es un estatus "
                 "migratorio de la persona física: te habilita a vivir y permanecer legalmente en Paraguay. Existe un régimen "
                 "de residencia vinculado a la inversión, que se gestiona a través del SUACE y requiere una certificación de "
                 "inversión emitida por el Ministerio de Industria y Comercio, además de documentación personal y societaria."),
                ("La <strong>cédula de identidad paraguaya</strong> es el documento que se tramita una vez obtenida la "
                 "residencia y que simplifica enormemente la vida operativa: gestiones bancarias, firmas ante escribanía y "
                 "trámites ante organismos. El <strong>RUC</strong>, en cambio, es la inscripción tributaria ante la DNIT: lo "
                 "tiene la empresa, y también puede tenerlo una persona física que desarrolle actividad gravada."),
                ("Una empresa puede constituirse y operar en Paraguay con socios que no residen en el país; lo que se necesita "
                 "definir bien en ese caso es la representación legal local, los poderes otorgados y quién queda a cargo de la "
                 "firma del día a día. Y obtener residencia en Paraguay no elimina por sí solo las obligaciones que la persona "
                 "pueda tener en su país de origen: eso se analiza con un especialista de esa jurisdicción."),
            ],
        },
        {
            "type": "checks",
            "alt": True,
            "eyebrow": "Puntos importantes",
            "h2": "Lo que conviene tener claro desde el inicio",
            "items": [
                "La residencia migratoria y la situación tributaria son cuestiones distintas, aunque estén relacionadas.",
                "Obtener residencia o constituir una sociedad en Paraguay no elimina obligaciones en tu país de origen.",
                "La aprobación de cuentas bancarias y financiamientos está sujeta a la evaluación de cada entidad.",
                "La distribución de utilidades al exterior tiene tratamiento tributario propio (IDU) y conviene proyectarla desde el inicio.",
                "Trabajamos el lado paraguayo del proyecto; lo de tu jurisdicción de origen se coordina con especialistas de allá.",
                "Atendemos en español, inglés y portugués, para que la operación no dependa de una traducción improvisada.",
            ],
        },
        {
            "type": "faq",
            "eyebrow": "Preguntas frecuentes",
            "h2": "Sobre invertir e instalarse en Paraguay",
            "ver_todas": "Ver todas las preguntas frecuentes sobre impuestos y empresas en Paraguay →",
            "items": [
                ("¿Cómo migro mi empresa a Paraguay?",
                 "En términos prácticos no se traslada una sociedad extranjera tal cual: lo habitual es constituir una sociedad paraguaya (EAS, SRL o SA) o inscribir una sucursal de la empresa del exterior, según el proyecto. Después viene el alta de RUC ante la DNIT, la habilitación municipal si el rubro lo requiere, la apertura de cuenta bancaria y la puesta en marcha contable y de facturación electrónica. En paralelo se resuelve la situación migratoria de las personas involucradas si van a residir en el país."),
                ("¿Puedo administrar mi empresa paraguaya desde el exterior?",
                 "Sí, es una situación frecuente. Se puede ser socio o accionista de una empresa paraguaya sin residir en el país, definiendo bien la representación legal local y los poderes otorgados. La contabilidad, la facturación electrónica y las presentaciones ante la DNIT se gestionan de forma remota con un equipo local de confianza, que es justamente el rol que cumplimos para clientes que operan desde afuera."),
                ("¿Qué impuestos paga una empresa extranjera que opera en Paraguay?",
                 "Una sociedad constituida en Paraguay tributa como cualquier empresa local: IRE sobre sus utilidades, IVA sobre sus operaciones y los impuestos específicos que correspondan a su actividad. A eso se suma el IDU cuando distribuye utilidades a sus socios, con una tasa mayor cuando el beneficiario no es residente, y el INR sobre determinadas rentas de fuente paraguaya pagadas al exterior. La estructura con la que se arma el proyecto influye directamente en esa carga."),
                ("¿Atienden en portugués e inglés?",
                 "Sí. Buena parte de los inversionistas que llegan a Paraguay son brasileños, y también trabajamos con clientes de habla inglesa. El sitio está disponible en español, inglés y portugués, y la atención se coordina en el idioma que le resulte más cómodo al cliente."),
            ],
        },
        {"type": "cta", "h2": "Conversemos sobre tu proyecto en Paraguay",
         "lead": "Contanos en qué etapa estás y qué necesitás resolver primero.",
         "cta": "Hablá con nosotros"},
    ],
}

# -------------------------------------------------------------------- EQUIPO
P["equipo"] = {
    "slug": "direccion-equipo.html",
    "nav": "Equipo",
    "nav_footer": "Dirección y equipo",
    "title": "Cristina Rolón, Contadora Pública en Asunción | MCG",
    "description": ("Cristina Rolón, Contadora Pública (UNA, 2008) y Magíster en Impuestos, dirige MCG Consultora en Asunción, Paraguay, con 18 años de experiencia."),
    "h1": "Cristina Rolón, Contadora Pública y directora de MCG",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Dirección y equipo",
         "h1": "Cristina Rolón, Contadora Pública y directora de MCG",
         "lead": ("Una dirección técnica que entiende cómo deciden las empresas: formación tributaria, práctica "
                  "profesional y experiencia en directorios empresariales en Paraguay.")},
        {
            "type": "bio",
            "h2": "Trayectoria",
            "nombre": "Cristina Rolón",
            "cargo": "Directora de MCG · Contadora Pública · Magíster en Impuestos",
            "foto_alt": ("Cristina Rolón, Contadora Pública y directora de MCG Consultora Contable y Tributaria, "
                         "en las oficinas del estudio contable en Asunción, Paraguay"),
            "trayectoria": [
                "Contadora Pública, egresada de la Universidad Nacional de Asunción (2008)",
                "Magíster en Impuestos y especializaciones en materia tributaria",
                "18 años de experiencia profesional en distintas industrias",
                "Especialista en implementación del módulo contable de ERP, con más de 30 empresas implementadas",
                "Experiencia en organizaciones desde 10 hasta más de 700 funcionarios",
                "Integrante de directorios empresariales",
                "Directora de MCG Consultora Contable y Tributaria, en Asunción, Paraguay",
            ],
            "paragraphs": [
                ("Esa experiencia en directorios le da a Cristina una lectura directa de cómo las empresas evalúan "
                 "información, priorizan riesgos y toman decisiones, algo que traslada al criterio con el que dirige MCG "
                 "y al tipo de informes que el estudio entrega a sus clientes."),
            ],
        },
        {
            "type": "rich",
            "alt": True,
            "eyebrow": "Su historia",
            "h2": "De dónde viene la disciplina con la que trabaja",
            "paragraphs": [
                ("Cristina es Contadora Pública, egresada de la Universidad Nacional de Asunción en 2008. Antes de fundar "
                 "MCG pasó por distintas industrias que marcaron su forma de trabajar: cada una le enseñó a mirar los "
                 "números con contexto, entendiendo el negocio que hay detrás de cada cifra. Más adelante completó "
                 "especializaciones y una Maestría en Impuestos, buscando siempre profundizar y estar a la altura de los "
                 "desafíos de sus clientes."),
                ("Esa misma exigencia la llevó, durante un tramo de su vida, a competir en fisicoculturismo. Prepararse "
                 "para subir a un escenario no es un esfuerzo de un día: es entrenar durante años para un resultado que se "
                 "mide en minutos, sostener una rutina cuando nadie está mirando y ajustar el método cuando algo no "
                 "funciona. Cristina aplica esa misma lógica —constancia, método y revisión constante— a la contabilidad y "
                 "a la estrategia tributaria de cada empresa que atiende."),
                ("Se define por la perseverancia, la solidez de sus conocimientos y las ganas genuinas de colaborar con "
                 "cada empresa en la que trabaja. Su lema es simple: dejar algo construido en el lugar donde presta "
                 "servicio e impactar significativamente en el resultado."),
            ],
        },
        {
            "type": "equipo",
            "eyebrow": "El equipo",
            "h2": "Un equipo estable como respaldo operativo",
            "foto_alt": ("Equipo de MCG Consultora Contable y Tributaria junto a Cristina Rolón en las oficinas del "
                         "estudio contable en Asunción, Paraguay"),
            "paragraphs": [
                ("Detrás de la dirección de Cristina, MCG cuenta con un equipo estable que ejecuta el trabajo contable y "
                 "tributario del día a día: registros, conciliaciones, presentaciones ante la DNIT, seguimiento documental "
                 "y atención a las consultas de cada empresa."),
                ("Esa estabilidad es parte del servicio. Que la misma gente siga tu empresa mes a mes significa que no hay "
                 "que volver a explicar el negocio cada vez, y que los criterios contables se mantienen consistentes a lo "
                 "largo del tiempo."),
            ],
        },
        {"type": "cta", "h2": "Conocé cómo podemos ayudar a tu empresa",
         "lead": "Contanos tu situación y evaluamos juntos el alcance del trabajo.",
         "cta": "Hablá con nosotros"},
    ],
}

# ----------------------------------------------------------------------- FAQ
P["faq"] = {
    "slug": "preguntas-frecuentes.html",
    "nav": "Preguntas frecuentes",
    "nav_footer": "Preguntas frecuentes",
    "title": "Preguntas frecuentes: impuestos y empresas en Paraguay",
    "description": ("DNIT, IRE, IVA, IRP, IDU, facturación electrónica, residencia por inversión y constitución de sociedades: 28 respuestas de un estudio de Asunción."),
    "h1": "Preguntas frecuentes sobre impuestos y empresas en Paraguay",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Preguntas frecuentes",
         "h1": "Preguntas frecuentes sobre impuestos y empresas en Paraguay",
         "lead": ("Las dudas más habituales de empresas ya instaladas en Paraguay y de inversionistas extranjeros que "
                  "evalúan el país: DNIT, impuestos, residencia, cédula paraguaya, migración de empresa y constitución "
                  "de sociedades.")},
        {
            "type": "faq",
            "eyebrow": "Impuestos y régimen tributario",
            "h2": "DNIT, IRE, IVA y el sistema tributario paraguayo",
            "items": [
                ("¿Qué es la DNIT y qué relación tiene con la ex SET?",
                 "La DNIT (Dirección Nacional de Ingresos Tributarios) es el organismo que administra los impuestos internos y aduaneros de Paraguay. Se formó a partir de la fusión de la SET (Subsecretaría de Estado de Tributación) con la Dirección Nacional de Aduanas, de modo que hoy una sola institución concentra lo que antes estaba repartido. Si tu empresa fue constituida antes de esa fusión, todos sus antecedentes, su RUC y sus obligaciones continúan vigentes bajo la DNIT: no hay que reconstituir la empresa ni obtener un número nuevo. Los canales de presentación y las claves de acceso se mantienen, aunque la transición trajo ajustes administrativos puntuales que conviene verificar antes de cada presentación. En la práctica, cuando leas SET en documentación antigua, referite a la DNIT."),
                ("¿Cuáles son los principales impuestos que paga una empresa en Paraguay?",
                 "Bajo la Ley 6380/2019, una empresa en Paraguay se relaciona principalmente con cuatro impuestos. El IRE (Impuesto a la Renta Empresarial) grava las utilidades. El IVA (Impuesto al Valor Agregado) grava las ventas de bienes y las prestaciones de servicios, y se liquida mensualmente descontando el crédito fiscal de las compras. El IDU alcanza la distribución de dividendos y utilidades a los socios. Y el ISC (Impuesto Selectivo al Consumo) aplica solo a determinados productos, como combustibles, bebidas o tabaco. A esto se suman las obligaciones formales: facturación electrónica, presentaciones informativas y retenciones cuando corresponde. La combinación exacta depende del rubro y del régimen, y esa es una de las primeras cosas que revisamos al conocer una empresa."),
                ("¿Qué es el IRE y cuáles son sus regímenes: RESIMPLE, IRE SIMPLE e IRE GENERAL?",
                 "El IRE es el Impuesto a la Renta Empresarial y su tasa general es del 10% sobre la utilidad. La Ley 6380/2019 prevé tres regímenes según el nivel de ingresos de la empresa. RESIMPLE está pensado para negocios muy pequeños, con un esquema simplificado de cuota. IRE SIMPLE aplica a empresas dentro del límite de ingresos que fija la normativa y permite una liquidación con menos exigencias documentales. IRE GENERAL corresponde a las empresas que superan ese límite: exige contabilidad completa y liquidación sobre renta neta real. Elegir mal el régimen o quedarse en uno que ya no corresponde tiene consecuencias concretas: más carga administrativa de la necesaria, o directamente un incumplimiento. Por eso conviene revisar el encuadre al inscribirse y cada vez que el volumen de la empresa cambia de escala."),
                ("¿Cuál es la tasa de IVA en Paraguay y cómo se liquida?",
                 "Paraguay tiene una tasa general de IVA del 10%, con una tasa reducida del 5% para determinados bienes y servicios definidos por la normativa, entre ellos ciertos productos de la canasta básica familiar y algunas operaciones inmobiliarias. El IVA se liquida mensualmente: se calcula el débito fiscal de las ventas, se le resta el crédito fiscal de las compras respaldadas con comprobantes válidos, y la diferencia es lo que se paga. Por eso el respaldo documental no es un detalle burocrático: un crédito fiscal sin comprobante válido simplemente no se puede usar. Una misma empresa puede tener operaciones al 10% y al 5% en el mismo período, y esa clasificación tiene que estar bien hecha desde la facturación."),
                ("¿Qué es el IRP y a quién alcanza en Paraguay?",
                 "El IRP (Impuesto a la Renta Personal) grava los ingresos de las personas físicas residentes en Paraguay, con tasas escalonadas del 8%, 9% y 10% según el nivel de renta y las deducciones admitidas. Alcanza, entre otros, a quienes prestan servicios personales, perciben honorarios profesionales, obtienen ganancias de capital o reciben determinados ingresos por su actividad independiente. Es un impuesto distinto del IRE, que grava a la empresa como tal. Esa diferencia importa en la práctica: un dueño de empresa puede tener que considerar el IRE de su sociedad y, por separado, su propia situación frente al IRP, según cómo retire ingresos."),
                ("¿Qué es el IDU, el impuesto a los dividendos y utilidades?",
                 "El IDU grava la distribución de dividendos y utilidades que hace una empresa paraguaya a sus socios o accionistas. La tasa es del 8% cuando quien recibe es residente en Paraguay y del 15% cuando el beneficiario es una persona o empresa no residente. Es un punto especialmente relevante para inversionistas extranjeros que planean girar utilidades a su país de origen, porque impacta directamente en el retorno neto de la inversión. También importa para socios locales al momento de decidir entre reinvertir en la empresa o distribuir. Conviene proyectarlo desde el diseño societario inicial y no descubrirlo cuando ya se tomó la decisión."),
                ("¿Qué es el INR y cuándo se aplica a pagos al exterior?",
                 "El INR es el Impuesto a la Renta de No Residentes y alcanza las rentas de fuente paraguaya obtenidas por personas o empresas del exterior sin residencia fiscal en Paraguay, con una tasa general del 15% sobre la base imponible que determina la ley. Se aplica, por ejemplo, cuando una empresa paraguaya paga servicios, intereses, regalías o asistencia técnica a un proveedor del exterior. En esos casos la empresa local suele actuar como agente de retención, de modo que el incumplimiento no es un problema del proveedor extranjero sino de la empresa paraguaya que pagó. Conviene analizarlo antes de firmar contratos con proveedores del exterior."),
                ("¿Qué es la facturación electrónica SIFEN y es obligatoria?",
                 "El SIFEN (Sistema Integrado de Facturación Electrónica Nacional) es el esquema de la DNIT para emitir comprobantes electrónicos con validez fiscal. Su obligatoriedad se implementó de forma escalonada por grupos de contribuyentes definidos por la administración tributaria, y a esta altura ya alcanza a la gran mayoría de las empresas activas, con los últimos grupos incorporándose según el calendario oficial. Si tu empresa todavía factura en talonario o con autoimpresor, conviene confirmar en qué grupo está y planificar la migración con tiempo, porque el cambio no es solo tecnológico: implica ajustar procesos internos de facturación, cobranza y archivo de comprobantes."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Extranjeros e inversión",
            "h2": "Migración de empresa, residencia y cédula paraguaya",
            "items": [
                ("¿Cómo hago la migración de mi empresa a Paraguay?",
                 "Lo que normalmente se llama migrar la empresa a Paraguay consiste, en la práctica, en constituir una sociedad paraguaya —EAS, SRL o SA— o inscribir una sucursal de la sociedad extranjera, y trasladar hacia ella la operación que se quiere desarrollar en el país. El recorrido incluye definir la figura societaria, reunir la documentación de los socios legalizada o apostillada, constituir e inscribir la sociedad, obtener el RUC ante la DNIT, habilitar el rubro ante la municipalidad si corresponde, abrir cuenta bancaria y poner en marcha la contabilidad y la facturación electrónica. En paralelo se resuelve la situación migratoria de las personas que van a vivir en Paraguay. El orden y la duración dependen del proyecto: no es lo mismo una consultora de servicios que una operación con depósito e importaciones."),
                ("¿Qué es la residencia por inversión en Paraguay y qué requisitos tiene?",
                 "Paraguay cuenta con un régimen de residencia vinculado a la inversión que se gestiona a través del SUACE (Sistema Unificado de Apertura y Cierre de Empresas). Requiere una certificación de inversión emitida por el Ministerio de Industria y Comercio y la presentación de un conjunto de documentos personales y societarios: antecedentes, certificado de salud, comprobante del monto efectivamente invertido y documentación de la empresa, entre otros. El trámite tiene un arancel establecido por la normativa vigente y la residencia obtenida se renueva periódicamente. Como la reglamentación puede actualizarse, conviene confirmar montos y requisitos exactos al momento de iniciar el trámite y no basarse en información de años anteriores."),
                ("¿La residencia en Paraguay me da la nacionalidad paraguaya?",
                 "No. La residencia, sea temporaria, permanente o por inversión, es un estatus migratorio que habilita a vivir y operar legalmente en el país. La nacionalidad se obtiene por naturalización, que es un proceso distinto, posterior, con sus propios requisitos y plazos ante las autoridades competentes. Muchos inversionistas extranjeros operan su empresa paraguaya durante años manteniendo únicamente su residencia, sin buscar la nacionalidad, y eso no afecta en nada la validez de su empresa ni de sus operaciones."),
                ("¿Necesito cédula paraguaya para tener una empresa en Paraguay?",
                 "Depende de la etapa. Para constituir la sociedad y obtener el RUC se puede avanzar con pasaporte y la documentación migratoria correspondiente. Ahora bien, una vez que el extranjero obtiene su residencia, tramitar la cédula de identidad paraguaya suele ser el paso natural siguiente, porque simplifica mucho la operación cotidiana: apertura y manejo de cuentas bancarias, firmas ante escribanía, trámites ante organismos públicos y gestiones ante la propia DNIT. En la práctica, tener cédula acelera todo, aunque no siempre sea un requisito legal previo indispensable para que la empresa exista."),
                ("¿Qué significa blindaje patrimonial o tributario para un inversionista extranjero?",
                 "En el uso cotidiano, blindaje se refiere a ordenar la estructura societaria, la documentación y el cumplimiento tributario para reducir riesgos legales, patrimoniales y fiscales evitables: elegir la figura societaria adecuada, mantener la contabilidad al día, separar con claridad el patrimonio personal del de la empresa, respaldar documentalmente cada operación y cumplir en tiempo y forma ante la DNIT. Ningún estudio contable serio puede prometer inmunidad ante fiscalizaciones, ni garantizar que nunca habrá un ajuste, ni ofrecer estructuras para ocultar patrimonio. Lo que sí se puede hacer, y es lo que hacemos, es trabajar de forma preventiva y prolija para minimizar exposiciones innecesarias."),
                ("¿Puedo administrar mi empresa paraguaya viviendo en el exterior?",
                 "Sí, es una situación muy frecuente entre inversionistas extranjeros. Se puede constituir y ser socio o accionista de una empresa paraguaya sin residir en el país. Lo que hay que definir bien es la representación legal local, el alcance de los poderes otorgados y quién queda a cargo de la firma y de las decisiones del día a día. La contabilidad, la facturación electrónica y las presentaciones ante la DNIT se gestionan perfectamente de forma remota cuando hay un equipo local de confianza a cargo, que es justamente el rol que cumple un estudio contable como MCG para clientes que operan desde afuera."),
                ("¿Qué ventajas tributarias reales tiene Paraguay para un inversionista extranjero?",
                 "Paraguay se caracteriza por tasas comparativamente bajas dentro de la región: IRE del 10% sobre utilidades e IVA general del 10%, con tasa reducida del 5% para determinados bienes y servicios. A eso se suma un sistema relativamente simple desde la Ley 6380/2019, regímenes simplificados para negocios pequeños y un régimen de residencia vinculado a la inversión. Ninguna de estas características implica cero impuestos ni beneficios automáticos, y conviene desconfiar de quien lo presente así. La carga tributaria real depende del régimen en que se inscribe la empresa, de su rubro, de su estructura societaria y de cómo se retiren las utilidades, donde entra el IDU. Por eso la evaluación seria se hace sobre el caso concreto, con números."),
                ("¿Puede una empresa extranjera abrir una cuenta bancaria en Paraguay?",
                 "Sí, y es uno de los pasos que más conviene preparar con anticipación. Los bancos paraguayos aplican procedimientos de conocimiento del cliente que exigen documentación societaria completa, identificación de los beneficiarios finales, respaldo del origen de los fondos y, en muchos casos, presencia de los firmantes. Nuestro trabajo en esta etapa es preparar y ordenar la documentación y coordinar con la entidad, pero la aprobación siempre depende de la evaluación de cada banco: no existe, y desconfiá de quien lo ofrezca, un contacto que garantice aprobaciones."),
            ],
        },
        {
            "type": "faq",
            "eyebrow": "Constitución de sociedades",
            "h2": "EAS, SRL, SA y el proceso de constitución en Paraguay",
            "items": [
                ("¿Qué tipo de sociedad me conviene en Paraguay: EAS, SRL o SA?",
                 "Las tres figuras más usadas son la EAS (Empresa por Acciones Simplificada), la SRL (Sociedad de Responsabilidad Limitada) y la SA (Sociedad Anónima). La EAS se eligió como vía ágil y flexible para emprendimientos y pymes, con un proceso de constitución más simple. La SRL es la figura tradicional para negocios con pocos socios y gestión simple, donde la participación se representa en cuotas sociales. La SA es la opción habitual para operaciones de mayor envergadura: permite emitir acciones, incorporar inversores y sostener una gobernanza más formal, algo que suelen requerir bancos, fondos y socios institucionales. La elección correcta depende del número de socios, del plan de crecimiento, de si se van a incorporar inversores y del tipo de contraparte con la que la empresa va a trabajar."),
                ("¿Cuánto tiempo lleva constituir una empresa en Paraguay?",
                 "El plazo depende del tipo societario elegido, de la carga de trabajo vigente en los registros y escribanías involucradas y, sobre todo, de qué tan completa esté la documentación desde el inicio. Cuando hay socios extranjeros con documentos que deben legalizarse o apostillarse en el exterior, ese suele ser el paso que más condiciona el calendario, porque no depende de Paraguay. La EAS es, en general, la figura con el trámite más ágil por su diseño simplificado. Más que prometer un número fijo de días, lo útil es armar el expediente completo desde el principio: eso es lo que realmente acorta los tiempos."),
                ("¿Qué documentos necesito para constituir una sociedad en Paraguay?",
                 "En términos generales se necesita la identificación de cada socio —cédula si es paraguayo, pasaporte y documentación migratoria si es extranjero—, el estatuto o contrato social con el objeto y la estructura societaria, la definición del capital social y su integración, y la designación de administradores o representantes legales. Cuando hay socios extranjeros, personas físicas o jurídicas, se suma documentación legalizada o apostillada en el país de origen, con traducción oficial cuando corresponde. Si una persona jurídica extranjera va a ser socia, se requiere además la documentación societaria de la matriz. Conviene revisar la lista exacta antes de iniciar legalizaciones, para no pagar dos veces por trámites mal encarados."),
                ("¿Puedo constituir una empresa en Paraguay sin viajar al país?",
                 "En muchos casos sí es posible avanzar buena parte del proceso a distancia, mediante poderes especiales otorgados ante notario en el país de origen y debidamente legalizados o apostillados, que habilitan a un representante local a firmar la documentación societaria. Sin embargo, algunas gestiones puntuales, sobre todo la apertura de cuenta bancaria y ciertos trámites migratorios, suelen requerir presencia física o al menos una gestión más directa del interesado. Lo recomendable es planificar desde el inicio qué se resuelve a distancia y qué conviene concentrar en un único viaje a Paraguay."),
                ("¿Cuánto capital social necesito para abrir una empresa en Paraguay?",
                 "El capital social se define según la figura societaria elegida y el tipo de actividad, y debe guardar una relación razonable con la operación que la empresa va a desarrollar. No es un dato meramente formal: bancos, contrapartes comerciales y organismos lo miran al evaluar a la empresa, y un capital inconsistente con el volumen de operaciones genera preguntas. Esta es una de las definiciones que revisamos en la evaluación inicial, junto con la estructura de socios y el objeto social."),
                ("¿Qué obligaciones tiene una empresa recién constituida en Paraguay?",
                 "Desde el momento en que obtiene su RUC, la empresa queda alcanzada por las obligaciones del régimen en el que se inscribió, aunque todavía no haya facturado. Eso incluye presentar las declaraciones que correspondan en cada vencimiento, emitir comprobantes con validez fiscal a través del esquema de facturación electrónica, llevar registros contables y conservar la documentación de respaldo. Presentar en cero cuando no hubo movimiento también es cumplir: la omisión, aun sin actividad, genera incumplimientos formales que después hay que regularizar."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Contabilidad y trabajo con MCG",
            "h2": "Cumplimiento, regularización y cómo empezar",
            "items": [
                ("¿Cada cuánto debo presentar declaraciones ante la DNIT?",
                 "La periodicidad depende del impuesto y del régimen. El IVA se liquida y presenta mensualmente; el IRE tiene liquidación anual, con anticipos según el régimen en que esté la empresa; y existen presentaciones informativas específicas según la actividad, además de las retenciones cuando corresponde actuar como agente. Los vencimientos siguen el calendario de la DNIT según el último dígito del RUC. Mantener un calendario propio por empresa, y no solo mirar el calendario general, es una de las funciones básicas de nuestro servicio de contabilidad empresarial."),
                ("¿Qué pasa si tengo la contabilidad atrasada o desordenada?",
                 "Es una situación más común de lo que parece, sobre todo en empresas que crecieron rápido o que cambiaron de contador varias veces. Lo primero es hacer un diagnóstico del estado real: qué períodos faltan, qué documentación existe, qué presentaciones quedaron pendientes ante la DNIT y qué saldos no cierran. A partir de ahí se arma un plan de regularización con prioridades, que se cotiza aparte del servicio mensual porque es un trabajo puntual distinto. Cuanto antes se aborda, menor es el riesgo de acumular contingencias y de que un problema chico se convierta en uno caro."),
                ("¿MCG atiende empresas de cualquier rubro y tamaño?",
                 "Sí. Trabajamos con todo tipo de empresas: compañías que ya facturan de forma significativa, negocios que recién están empezando, empresas familiares que necesitan ordenarse y proyectos de inversionistas extranjeros que se instalan en Paraguay. Los rubros son variados: comercio, servicios, construcción, importación, tecnología, salud y gastronomía, entre otros. Lo que definimos en cada caso es el alcance del servicio según la complejidad real de la operación, no un piso de facturación para poder trabajar juntos."),
                ("¿Cómo empiezo a trabajar con MCG?",
                 "El primer paso es completar el formulario de contacto o escribirnos por WhatsApp contando tu situación: si ya tenés una empresa en Paraguay, si estás por instalarte como extranjero o si tenés otra consulta puntual. Con esa información evaluamos el encaje y el alcance posible y coordinamos una conversación para entender mejor el caso. Si hace falta un diagnóstico o una revisión técnica más profunda, se cotiza como un paso aparte antes de definir la propuesta final. Todo queda por escrito antes de empezar."),
                ("¿Los honorarios incluyen todo o hay costos aparte?",
                 "Los honorarios se definen según el alcance acordado —gestión contable, obligaciones tributarias, cierres, acompañamiento estratégico— y ese alcance queda explícito en la propuesta antes de empezar a trabajar. Los servicios que quedan fuera, como la regularización de períodos anteriores, auditorías puntuales, trabajos extraordinarios o gestiones que requieren profesionales de otras especialidades, se cotizan por separado. Además, las tasas y aranceles de organismos y escribanías son gastos de terceros y se informan siempre como tales, separados de nuestros honorarios."),
                ("¿Trabajan con empresas del interior del país o solo en Asunción?",
                 "Nuestra oficina está en Asunción, pero el trabajo contable y tributario se realiza en gran medida de forma digital: recepción de documentación, registros, presentaciones ante la DNIT y reuniones de revisión. Eso nos permite atender empresas de distintos puntos de Paraguay y también clientes que operan desde el exterior. Cuando una gestión requiere presencia física, se coordina según el caso."),
            ],
        },
        {"type": "cta", "h2": "¿Tu pregunta no está en la lista?",
         "lead": "Contanos tu situación puntual y te respondemos directamente.",
         "cta": "Hablá con nosotros"},
    ],
}

# ------------------------------------------------------------------ CONTACTO
P["contacto"] = {
    "slug": "contacto.html",
    "nav": "Contacto",
    "nav_footer": "Contacto",
    "title": "Contacto | Estudio contable en Asunción, Paraguay — MCG",
    "description": ("Contactá a MCG Consultora en Asunción, Paraguay. Contanos sobre tu empresa o tu proyecto de inversión y coordinamos los siguientes pasos."),
    "h1": "Hablemos de tu empresa",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Contacto",
         "h1": "Hablemos de tu empresa",
         "lead": ("Contanos sobre tu empresa o tu proyecto en Paraguay. La solicitud inicial permite evaluar encaje y "
                  "alcance; una revisión técnica o diagnóstico se cotiza por separado.")},
        {
            "type": "form",
            "form": {
                "situacion": "¿Cuál es tu situación?",
                "seleccione": "Seleccioná una opción",
                "situacion_opciones": [("empresa", "Ya tengo una empresa en Paraguay"),
                                       ("extranjero", "Quiero instalar mi empresa en Paraguay"),
                                       ("otro", "Otra consulta")],
                "nombre": "Nombre",
                "empresa": "Empresa o proyecto",
                "correo": "Correo electrónico",
                "whatsapp": "WhatsApp",
                "whatsapp_ph": "Ej: 0981 234 567",
                "servicio": "Servicio de interés",
                "seleccione_servicio": "Seleccioná un servicio",
                "servicio_opciones": [("Contabilidad empresarial", "Contabilidad empresarial"),
                                      ("Estrategia tributaria", "Estrategia tributaria"),
                                      ("Constitución de sociedades", "Constitución de sociedades"),
                                      ("Instalación para extranjeros", "Instalación para extranjeros"),
                                      ("No estoy seguro todavía", "No estoy seguro todavía")],
                "legend_empresa": "Sobre tu empresa",
                "rubro": "Rubro",
                "facturacion": "Facturación mensual aproximada",
                "facturacion_opciones": ["Recién estamos empezando", "Menos de G. 400 millones",
                                         "G. 400–1.000 millones", "Más de G. 1.000 millones",
                                         "Prefiero indicarlo en una conversación"],
                "necesidad": "Principal necesidad",
                "legend_extranjero": "Sobre tu proyecto en Paraguay",
                "pais": "País de residencia",
                "tipo_proyecto": "Tipo de proyecto",
                "tipo_ph": "Ej: comercio, servicios, inversión",
                "etapa": "Etapa del proyecto",
                "seleccione_etapa": "Seleccioná una etapa",
                "etapa_opciones": [("Recién estoy evaluando la idea", "Recién estoy evaluando la idea"),
                                   ("Ya decidí instalarme y quiero avanzar", "Ya decidí instalarme y quiero avanzar"),
                                   ("Ya tengo una empresa constituida en Paraguay", "Ya tengo una empresa constituida en Paraguay")],
                "aviso": ("No es necesario enviar documentos financieros ni información bancaria sensible en este "
                          "formulario. Si hace falta, te la vamos a pedir de forma segura más adelante."),
                "enviar": "Enviar consulta",
                "abrir_wa": "Abrir WhatsApp manualmente",
            },
        },
        {
            "type": "contacto_extra",
            "eyebrow": "Otra forma de escribirnos",
            "h2": "También podés escribirnos directo",
            "p": ("Si preferís, escribinos directamente por WhatsApp o seguinos en Instagram. Atendemos en español, "
                  "inglés y portugués, desde Asunción, Paraguay."),
            "wa_mensaje": "Hola MCG, vengo de la página web y quiero hacer una consulta",
            "wa_cta": "Escribir por WhatsApp",
            "ig_cta": "Ver Instagram",
        },
    ],
}

# -------------------------------------------------------------------- ERP
P["erp"] = {
    "slug": "implementacion-erp-contable.html",
    "nav": "ERP",
    "nav_footer": "Implementación de ERP",
    "service": "Implementación de ERP — módulo contable",
    "title": "Implementación de ERP contable en Paraguay | MCG",
    "description": ("Implementación del módulo contable de un ERP en Paraguay: plan de cuentas, integración con tesorería, compras y bancos, costeo y trazabilidad."),
    "h1": "Implementación de ERP: el módulo contable como corazón del sistema",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Implementación de ERP",
         "h1": "Implementación de ERP: el módulo contable como corazón del sistema",
         "lead": ("Especialidad de Cristina Rolón: dejar el módulo contable bien parametrizado para que todo el resto "
                  "del ERP —tesorería, logística, producción, compras, bancos— cierre, sea trazable y auditable."),
         "cta": "Hablá con nosotros"},
        {
            "type": "rich",
            "eyebrow": "El punto de partida",
            "h2": "Por qué el módulo contable es la madre de todos los demás módulos",
            "paragraphs": [
                ("En un ERP todo termina impactando en la contabilidad. Una venta genera un asiento; una compra, un "
                 "pasivo y un crédito fiscal de IVA; un movimiento de depósito cambia la valuación del inventario; una "
                 "orden de producción consume materia prima y genera costo; una cobranza mueve tesorería y bancos. Si el "
                 "<strong>módulo contable</strong> está mal parametrizado, todos esos movimientos se registran mal —o no "
                 "se registran— y el resto del sistema empieza a mostrar información que no cierra."),
                ("Por eso una implementación de ERP no se juega en la pantalla bonita de cada módulo: se juega en el plan "
                 "de cuentas, en las reglas de imputación automática, en la valuación de inventarios, en los centros de "
                 "costo y en cómo se integran los subdiarios. Cuando eso está bien hecho, la empresa obtiene estados "
                 "financieros confiables sin trabajo manual paralelo; cuando está mal hecho, el equipo termina "
                 "reconstruyendo todo en planillas."),
                ("Cristina Rolón trabaja exactamente en ese punto: entra en el proyecto de ERP desde la mirada contable y "
                 "tributaria, define cómo tiene que registrarse cada operación del negocio en Paraguay —incluidas las "
                 "exigencias de la DNIT y la facturación electrónica— y acompaña hasta que los cierres salen del sistema, "
                 "no de un Excel."),
            ],
        },
        {
            "type": "cards",
            "alt": True,
            "eyebrow": "Integración",
            "h2": "Los módulos que dependen del corazón contable",
            "lead": ("Cada uno de estos módulos genera o consume información contable. La implementación define cómo "
                     "se registra, cómo se concilia y cómo se audita."),
            "columns": 3,
            "items": [
                ("Tesorería y caja", "Cobranzas, pagos, fondos fijos y arqueos, con imputación automática y conciliación contra los saldos contables."),
                ("Bancos y conciliación", "Extractos, cheques, transferencias y conciliación bancaria periódica, con partidas pendientes identificadas."),
                ("Compras y cuentas a pagar", "Órdenes de compra, recepción, factura del proveedor y pago, con control de tres vías y crédito fiscal de IVA bien tomado."),
                ("Ventas y cuentas a cobrar", "Facturación electrónica, notas de crédito, cobranzas y antigüedad de saldos, integradas al libro de ventas."),
                ("Inventario y logística", "Entradas, salidas, transferencias entre depósitos y valuación de existencias, con impacto directo en el costo de ventas."),
                ("Producción", "Órdenes de producción, consumo de materia prima, mano de obra y gastos de fabricación aplicados al costo del producto terminado."),
                ("Despacho y remisiones", "Notas de remisión y entregas vinculadas a la factura y al movimiento de stock, para que nada salga sin respaldo."),
                ("Activos fijos", "Altas, bajas, depreciaciones y revalúos, con su impacto en el resultado y en los estados financieros."),
                ("Costos y rentabilidad", "Centros de costo, costeo por producto, línea o proyecto, y margen real por unidad de negocio."),
            ],
        },
        {
            "type": "checks",
            "eyebrow": "El resultado",
            "h2": "Qué tiene que poder hacer la empresa cuando el ERP está bien implementado",
            "items": [
                "Emitir estados de resultados y balance directamente del sistema, sin armarlos a mano en planillas.",
                "Ver la rentabilidad real por producto, línea de negocio, sucursal o proyecto, con costos aplicados.",
                "Rastrear cualquier número hacia atrás: del estado de resultados al asiento, del asiento al comprobante.",
                "Conciliar bancos, inventario y cuentas corrientes sin discusiones sobre cuál sistema tiene razón.",
                "Cerrar el mes en tiempo y forma, con los subdiarios cuadrados contra la contabilidad general.",
                "Responder una fiscalización de la DNIT mostrando la trazabilidad completa desde el sistema.",
                "Controlar accesos y dejar registro de quién cargó, modificó o aprobó cada movimiento.",
            ],
            "paragraphs": [
                ("Trazabilidad y auditabilidad no son un lujo: son lo que permite que la dirección confíe en los números "
                 "y que una auditoría externa, un banco o la administración tributaria puedan verificar lo que la empresa "
                 "declara."),
            ],
        },
        {
            "type": "rich",
            "alt": True,
            "eyebrow": "Experiencia",
            "h2": "Más de 30 empresas implementadas, de 10 a más de 700 funcionarios",
            "paragraphs": [
                ("Cristina Rolón participó en la implementación del módulo contable de ERP en <strong>más de 30 "
                 "empresas</strong> de distintos tamaños y rubros: desde compañías pequeñas de alrededor de 10 "
                 "funcionarios hasta organizaciones de <strong>más de 700 funcionarios</strong>, con varias sucursales, "
                 "producción propia y estructuras de costos complejas."),
                ("Esa diferencia de escala importa. Una empresa de diez personas necesita un sistema simple, con un plan "
                 "de cuentas manejable y procesos que no la ahoguen; una de setecientos necesita centros de costo, "
                 "perfiles de acceso por área, controles de aprobación y cierres coordinados entre varios equipos. La "
                 "implementación tiene que estar a la medida del tamaño real de la operación, no del folleto del "
                 "software."),
                ("Ese recorrido también dejó una lectura clara de dónde suelen fallar los proyectos: planes de cuentas "
                 "copiados de otra empresa, saldos iniciales migrados sin conciliar, módulos que se activan sin definir "
                 "la contrapartida contable, y capacitaciones que enseñan a apretar botones pero no a entender qué "
                 "registra cada botón."),
            ],
        },
        {
            "type": "pasos",
            "eyebrow": "Metodología",
            "h2": "Cómo trabajamos una implementación",
            "items": [
                ("Relevamiento del negocio", "Entendemos el circuito real: qué pasa desde que entra un pedido hasta que se cobra y se registra."),
                ("Diseño del plan de cuentas", "Armado o rediseño del plan de cuentas y de los centros de costo según cómo la dirección necesita leer la información."),
                ("Parametrización contable", "Reglas de imputación automática, subdiarios, tratamiento de IVA y retenciones, valuación de inventarios y criterios de costeo."),
                ("Migración y conciliación de saldos", "Carga de saldos iniciales conciliados, para que el sistema arranque cuadrado y no arrastre diferencias."),
                ("Pruebas integrales", "Simulación de operaciones reales de punta a punta, verificando el impacto contable de cada módulo antes de salir en vivo."),
                ("Capacitación del equipo", "Formación por rol, para que cada área entienda qué registra el sistema cuando ella opera y qué consecuencias tiene."),
                ("Salida en vivo y acompañamiento", "Puesta en marcha, primer cierre asistido y ajustes finos hasta que los estados financieros salen del ERP sin retoques."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Preguntas frecuentes",
            "h2": "Sobre implementación de ERP en Paraguay",
            "items": [
                ("¿Trabajan con un ERP en particular o con cualquier sistema?",
                 "El trabajo de MCG es el contenido contable de la implementación, no la venta de una licencia: plan de cuentas, reglas de imputación, criterios de valuación y costeo, tratamiento de IVA y retenciones, conciliaciones y cierres. Ese contenido se aplica al ERP que la empresa haya elegido o esté evaluando, y se coordina con el proveedor del sistema y con el equipo de tecnología."),
                ("¿Por qué el módulo contable tiene que definirse antes que los demás?",
                 "Porque todos los demás módulos terminan impactando en él. Si se activa logística, producción o tesorería sin haber definido cómo se imputa contablemente cada movimiento, el sistema empieza a generar registros incompletos o mal clasificados, y corregirlos después implica reprocesar meses de información. Definir primero el corazón contable ahorra exactamente ese retrabajo."),
                ("¿Se puede arreglar una implementación que ya salió mal?",
                 "Sí, y es una parte importante de lo que hacemos. Se empieza por un diagnóstico: revisar el plan de cuentas, verificar si los subdiarios cuadran con la contabilidad general, revisar la valuación de inventarios y los saldos migrados, y detectar qué movimientos se están registrando mal. Con eso se arma un plan de corrección por prioridad, sin frenar la operación."),
                ("¿Qué se necesita para que el ERP sea auditable?",
                 "Que cada cifra se pueda rastrear hasta su comprobante de origen, que los accesos estén definidos por rol, que quede registro de quién cargó y aprobó cada operación, que los subdiarios cuadren contra la contabilidad general y que la documentación de respaldo esté disponible. Eso es lo que permite responder con solvencia ante una auditoría externa, un banco o una fiscalización de la DNIT."),
                ("¿Sirve para una empresa chica o solo para empresas grandes?",
                 "Sirve para las dos, con alcances distintos. Una empresa de diez personas necesita un plan de cuentas simple y procesos livianos que igual dejen trazabilidad; una empresa de cientos de funcionarios necesita centros de costo, perfiles de acceso, controles de aprobación y cierres coordinados. Hemos trabajado en los dos extremos y el error más común es aplicar el esquema de una a la otra."),
            ],
        },
        {"type": "cta", "h2": "¿Estás por implementar o corregir un ERP?",
         "lead": "Contanos en qué etapa está el proyecto y lo revisamos juntos.",
         "cta": "Hablá con nosotros"},
    ],
}
