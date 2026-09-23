# -*- coding: utf-8 -*-
"""Conteúdo do site em português do Brasil. Traduzido da versão em espanhol (content_es.py)."""

DATA = {
    "lang": "pt",
    "preview_banner": "Pré-visualização interna — não indexada — dados sujeitos a confirmação antes da publicação",
    "saltar": "Ir para o conteúdo",
    "relacionados": "Continue explorando",
    "textos_form": {
        "formOk": "Recebemos sua consulta e vamos responder no e-mail que você deixou. Se preferir falar agora, chame no WhatsApp.",
        "formWhatsapp": "Preparamos sua consulta e abrimos o WhatsApp em uma nova aba: confira a mensagem e toque em enviar. Se não abriu, use o botão abaixo.",
        "formIncompleto": "Preencha os campos obrigatórios antes de continuar."
    },
    "nav_aria": "Navegação principal",
    "menu_label": "Abrir menu",
    "lang_aria": "Mudar idioma",
    "cta_nav": "Fale com a gente",
    "logo_alt": "MCG Consultora Contable y Tributaria — escritório de contabilidade em Assunção, Paraguai, dirigido por Cristina Rolón",
    "org_description": (
        "MCG Consultora Contable y Tributaria é um escritório de contabilidade de Assunção, Paraguai, "
        "dirigido pela contadora Cristina Rolón. Oferece contabilidade empresarial, "
        "estratégia tributária perante a DNIT (autoridade tributária do Paraguai, antiga SET), abertura de empresas "
        "(EAS, SRL e SA) e acompanhamento a empresários e investidores estrangeiros que se instalam no Paraguai."
    ),
    "person_jobtitle": "Contadora Pública · Mestre em Impostos · Diretora da MCG Consultora Contable y Tributaria",
    "person_description": (
        "Cristina Rolón é contadora formada pela Universidad Nacional de Asunción (Universidade Nacional de Assunção, 2008), "
        "Mestre em Impostos e diretora da MCG Consultora Contable y Tributaria, em Assunção, Paraguai, "
        "com 18 anos de experiência profissional em contabilidade empresarial e estratégia tributária."
    ),
    "person_knows": [
        "Contabilidade empresarial no Paraguai", "Estratégia tributária", "Imposto de Renda Empresarial (IRE)",
        "Imposto sobre o Valor Agregado (IVA)", "DNIT", "Abertura de empresas no Paraguai",
        "Investimento estrangeiro no Paraguai", "Nota fiscal eletrônica (SIFEN)",
        "Implantação de ERP", "Módulo contábil de ERP", "Custeio e rentabilidade",
        "Conciliação bancária", "Rastreabilidade e auditabilidade contábil",
    ],
    "footer": {
        "tagline": ("Contabilidade empresarial e estratégia tributária no Paraguai, sob a direção de "
                    "Cristina Rolón, contadora pela Universidad Nacional de Asunción (UNA) e Mestre em Impostos."),
        "ciudad": "Assunção, Paraguai · Atendimento em espanhol, inglês e português",
        "col_servicios": "Serviços",
        "col_estudio": "Escritório",
        "col_contacto": "Contato",
        "wa_mensaje": "Olá MCG, vim pelo site e gostaria de fazer uma consulta",
        "copyright": "MCG Consultora Contable y Tributaria. Todos os direitos reservados.",
        "legal": ("Conteúdo informativo geral sobre a legislação paraguaia; não substitui uma avaliação "
                  "profissional de cada caso."),
    },
    "pages": {},
}

P = DATA["pages"]

# ---------------------------------------------------------------------- HOME
P["home"] = {
    "slug": "index.html",
    "nav": "Início",
    "nav_footer": "Início",
    "title": "Contabilidade no Paraguai | Impostos e abertura de empresa — MCG",
    "description": ("Escritório de contabilidade em Assunção. Contabilidade empresarial, impostos no Paraguai perante a DNIT "
                    "e abertura de empresa. Direção de Cristina Rolón, contadora."),
    "h1": "Contabilidade empresarial e estratégia tributária no Paraguai",
    "blocks": [
        {
            "type": "hero",
            "chip": "Consultoria contábil e tributária · Assunção, Paraguai",
            "h1_html": "Contabilidade empresarial e <span class=\"acento\">estratégia tributária</span> no Paraguai",
            "lead": ("Acompanhamos empresas e investidores nas suas decisões contábeis, tributárias e de instalação "
                     "no Paraguai, com informação confiável e critério profissional."),
            "firma_html": ("Sob a direção de <strong>Cristina Rolón</strong>, contadora pela Universidad Nacional de Asunción (UNA), "
                           "Mestre em Impostos e membro de conselhos de administração, com uma equipe estável por trás."),
            "cta1": "Fale com a gente",
            "cta2": "Conhecer nossos serviços",
            "cta2_href": "#servicios",
            "credenciales": [
                ("18 anos", "de experiência profissional"),
                ("Contadora Pública", "Universidad Nacional de Asunción"),
                ("Mestre", "em Impostos"),
                ("+30 empresas", "com ERP contábil implantado"),
            ],
            "figura_alt": ("Cristina Rolón, contadora e diretora da MCG Consultora Contable y Tributaria, "
                           "escritório de contabilidade em Assunção, Paraguai"),
            "figura_nombre": "Cristina Rolón",
            "figura_rol": "Diretora da MCG · Contadora Pública · Mestre em Impostos",
        },
        {
            "type": "franja",
            "items": [
                "Empresas que precisam organizar sua situação contábil e tributária no Paraguai",
                "Empresários e investidores estrangeiros que querem se instalar no Paraguai",
                "Empresas de qualquer porte e setor que buscam um escritório de contabilidade sério e caprichoso",
                "Sócios e gestores que precisam de informação confiável para decidir",
            ],
            "microcopy": ("Trabalhamos com todo tipo de empresa: o que definimos juntos é o escopo do serviço, "
                          "não um faturamento mínimo."),
        },
        {
            "type": "caminos",
            "items": [
                {"badge": "Já tenho uma empresa", "h3": "Já tenho uma empresa no Paraguai",
                 "p": ("Preciso de contabilidade confiável, previsibilidade tributária perante a DNIT (autoridade tributária do Paraguai, "
                       "antiga SET) e acompanhamento estratégico para tomar decisões melhores."),
                 "cta": "Ver contabilidade empresarial →", "target": "contabilidad"},
                {"badge": "Quero me instalar", "h3": "Quero mudar minha empresa para o Paraguai",
                 "p": ("Sou estrangeiro ou investidor e preciso de apoio local para abrir a empresa, "
                       "obter o RUC (cadastro fiscal paraguaio) e operar dentro da lei desde o primeiro dia."),
                 "cta": "Ver apoio a empresários estrangeiros →", "target": "extranjeros"},
            ],
        },
        {
            "type": "rich",
            "alt": True,
            "eyebrow": "Quem somos",
            "h2": "Um escritório de contabilidade de confiança em Assunção, Paraguai",
            "paragraphs": [
                ("A MCG Consultora Contable y Tributaria é um escritório de contabilidade sediado em Assunção que atende empresas "
                 "paraguaias e investidores estrangeiros que escolhem o Paraguai para instalar ou expandir seu negócio. "
                 "A direção está a cargo de <strong>Cristina Rolón</strong>, contadora formada pela "
                 "Universidad Nacional de Asunción (Universidade Nacional de Assunção) em 2008, Mestre em Impostos e com 18 anos "
                 "de experiência profissional em diferentes setores."),
                ("Nosso trabalho não termina quando as declarações são entregues no prazo. Uma contabilidade bem feita no Paraguai "
                 "deveria servir para mais do que isso: para saber quanto cada linha de negócio realmente dá de lucro, para antecipar o "
                 "impacto do IRE (Imposto de Renda Empresarial) e do IVA (Imposto sobre o Valor Agregado) antes do vencimento, para sustentar "
                 "uma conversa com o banco com números que fecham e para dormir tranquilo se amanhã a DNIT pedir explicações."),
                ("Por isso combinamos três coisas em cada empresa que atendemos: cumprimento caprichoso perante a DNIT, informação "
                 "organizada e no tempo certo para a direção, e um olhar tributário preventivo que evita surpresas. Esse é o "
                 "padrão com que trabalhamos, e é o que define a confiança que queremos construir com cada cliente."),
            ],
        },
        {
            "type": "problemas",
            "eyebrow": "Problemas que resolvemos",
            "h2": "Quando a contabilidade não ajuda você a decidir",
            "lead": "Estas são as situações mais frequentes que as empresas nos trazem antes de trabalharem conosco.",
            "items": [
                "Informação contábil que chega tarde ou que não permite tomar decisões.",
                "Falta de previsão sobre as obrigações tributárias do período e seus vencimentos perante a DNIT.",
                "Desorganização entre movimentações bancárias, nota fiscal eletrônica e registros contábeis.",
                "Crescimento acelerado sem controles internos nem documentação de respaldo suficiente.",
                "Períodos anteriores não entregues ou com declarações que precisam ser regularizadas.",
                "Insegurança de um estrangeiro sobre como abrir e operar legalmente um negócio no Paraguai.",
            ],
            "paragraphs": [
                ("Nenhum desses problemas se resolve com uma declaração entregue em cima da hora. Eles se resolvem "
                 "organizando o processo inteiro: que documentação entra, como é registrada, o que se revisa todo mês e que "
                 "informação chega à direção para decidir."),
            ],
        },
        {
            "type": "cards",
            "alt": True,
            "eyebrow": "Serviços",
            "h2": "O que fazemos na MCG",
            "lead": ("Cinco serviços pensados para o ciclo completo de uma empresa no Paraguai: da abertura "
                     "até a operação organizada, a estratégia tributária e os sistemas que sustentam a informação."),
            "columns": 2,
            "items": [
                ("Contabilidade empresarial",
                 "Gestão contábil mensal, cumprimento das obrigações perante a DNIT, fechamentos e relatórios periódicos para que a direção decida com informação confiável."),
                ("Estratégia tributária",
                 "Diagnóstico da situação tributária, identificação de contingências, planejamento das obrigações e um plano de ação com prioridades claras."),
                ("Abertura de empresas",
                 "Avaliação do tipo societário (EAS, SRL ou SA), coordenação do processo de constituição, obtenção do RUC perante a DNIT e início da operação contábil."),
                ("Empresários estrangeiros",
                 "Apoio local para instalar e operar uma empresa no Paraguai: sociedade, documentação, coordenação migratória e contabilidade desde o primeiro dia."),
                ("Implantação de ERP — módulo contábil",
                 "Parametrização do coração contábil do ERP e sua integração com tesouraria, logística, produção, compras e bancos, com custeio e rastreabilidade auditável."),
            ],
        },
        {
            "type": "pasos",
            "eyebrow": "Como trabalhamos",
            "h2": "Um processo claro desde a primeira conversa",
            "items": [
                ("Conversamos sobre a sua empresa", "Entendemos seu setor, sua operação atual, sua situação documental e o que você precisa resolver primeiro."),
                ("Revisamos a situação real", "Vemos em que estado estão os registros, as declarações perante a DNIT e a documentação de respaldo."),
                ("Apresentamos uma proposta", "Com escopo, honorários e condições por escrito, sem custos ocultos nem serviços que você não pediu."),
                ("Coordenamos a entrada", "Organizamos a transição a partir do seu contador anterior ou do zero, e começamos conforme o combinado."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Perguntas frequentes",
            "h2": "Antes de nos escrever",
            "ver_todas": "Ver as 28 perguntas frequentes sobre impostos e empresas no Paraguai →",
            "items": [
                ("Vocês atendem empresas de qualquer porte?",
                 "Sim. Trabalhamos com todo tipo de empresa no Paraguai: companhias que já faturam de forma significativa, negócios que estão começando e empresas que precisam regularizar períodos anteriores. O que definimos em cada caso é o escopo do serviço conforme a complexidade real da operação — setor, volume de notas fiscais, funcionários, filiais, importações e situação documental —, e não um faturamento mínimo."),
                ("Quanto custa trabalhar com a MCG?",
                 "Os honorários dependem do escopo e da complexidade da sua operação. Pesam o setor, o volume de documentos fiscais eletrônicos, a quantidade de funcionários, as filiais, se há importações ou exportações e o estado da documentação. Depois de conhecer sua empresa, apresentamos uma proposta concreta e por escrito, com o escopo detalhado antes de começar."),
                ("Vocês atendem empresários e investidores estrangeiros?",
                 "Sim, e essa é uma parte importante do nosso trabalho. Acompanhamos estrangeiros que querem instalar e operar uma empresa no Paraguai: escolha do tipo societário, constituição, obtenção do RUC perante a DNIT, preparação da documentação bancária, coordenação com profissionais da área migratória e contabilidade desde o primeiro dia. Atendemos em espanhol, inglês e português."),
                ("O que acontece se eu tiver períodos atrasados perante a DNIT?",
                 "É mais comum do que parece e tem solução. Começamos por um diagnóstico da situação real: que períodos faltam, que documentação existe e que declarações ficaram pendentes. Com isso montamos um plano de regularização, orçado à parte do serviço mensal porque é um trabalho pontual diferente. Quanto antes o assunto for enfrentado, menor o risco de acumular contingências."),
                ("A primeira conversa tem custo?",
                 "Não. O contato inicial nos permite entender sua situação e avaliar o encaixe e o escopo possível do trabalho. Se for necessária uma revisão técnica mais profunda ou um diagnóstico tributário completo, isso é orçado separadamente e combinado antes de começar."),
            ],
        },
        {
            "type": "opiniones",
            "eyebrow": "Avaliações",
            "h2": "O que dizem nossos clientes",
            "lead": "As avaliações das empresas que trabalham com a MCG estão publicadas no nosso perfil do Google Business, onde qualquer pessoa pode verificá-las e deixar a sua.",
            "cta": "Ver avaliações no Google",
            "reseñas": [],
        },
        {
            "type": "cta",
            "h2": "Vamos conversar sobre a sua empresa",
            "lead": "Conte sua situação e avaliamos juntos o escopo do trabalho.",
            "cta": "Fale com a gente",
        },
    ],
}

# -------------------------------------------------------------- CONTABILIDAD
P["contabilidad"] = {
    "slug": "contabilidade-empresarial-paraguai.html",
    "nav": "Contabilidade",
    "nav_footer": "Contabilidade empresarial",
    "service": "Contabilidade empresarial",
    "title": "Contabilidade no Paraguai | Serviço contábil mensal — MCG",
    "description": ("Contabilidade no Paraguai para empresas: registros contábeis, IVA e IRE perante a DNIT, fechamentos e relatórios. Escritório em Assunção."),
    "h1": "Contabilidade empresarial no Paraguai, feita para decidir",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Contabilidade empresarial",
         "h1": "Contabilidade empresarial no Paraguai, feita para decidir",
         "lead": ("Cumprimento organizado perante a DNIT (autoridade tributária do Paraguai, antiga SET) e informação melhor "
                  "para que a direção da sua empresa decida com números confiáveis."),
         "cta": "Fale com a gente"},
        {
            "type": "rich",
            "eyebrow": "O serviço",
            "h2": "O que significa cuidar bem da contabilidade de uma empresa no Paraguai",
            "paragraphs": [
                ("Cuidar da contabilidade de uma empresa no Paraguai envolve muito mais do que lançar documentos e entregar "
                 "declarações. Envolve manter registros consistentes com a Ley 6380/2019 (Lei 6380/2019), apurar corretamente o IVA "
                 "(Imposto sobre o Valor Agregado) e o IRE (Imposto de Renda Empresarial) conforme o regime que cabe à empresa, cumprir "
                 "as regras da nota fiscal eletrônica do sistema SIFEN, conciliar as movimentações bancárias com o que foi registrado e manter "
                 "a documentação de respaldo organizada caso a DNIT venha a solicitá-la."),
                ("Na MCG fazemos esse trabalho com um critério simples: a contabilidade tem que fechar para fora — perante a "
                 "administração tributária — e também para dentro — perante a direção da empresa. Se os números só "
                 "servem para cumprir o vencimento, mas não dizem ao dono qual é a margem de cada linha de negócio "
                 "ou por que o custo subiu neste trimestre, o trabalho está pela metade."),
                ("Trabalhamos com empresas de todos os setores: comércio, serviços, construção, importação, tecnologia, "
                 "saúde, gastronomia e projetos de investimento estrangeiro. Cada setor tem suas particularidades tributárias, "
                 "e isso faz parte do que avaliamos antes de definir o escopo."),
            ],
        },
        {
            "type": "cards",
            "alt": True,
            "eyebrow": "Escopo proposto",
            "h2": "O que inclui o serviço de contabilidade mensal",
            "lead": "Este é o escopo de referência. O escopo final de cada empresa é definido conforme a sua operação real.",
            "columns": 3,
            "items": [
                ("Gestão contábil mensal", "Registro e manutenção contábil de toda a operação, com critérios consistentes período a período."),
                ("Obrigações tributárias", "Preparação e entrega das obrigações aplicáveis perante a DNIT, com controle de vencimentos conforme o RUC."),
                ("Fechamentos e relatórios periódicos", "Fechamentos com relatórios que mostram resultados, margens e evolução, em um formato que a direção consiga ler."),
                ("Conciliações", "Conciliação de movimentações bancárias, notas fiscais eletrônicas e registros contábeis, conforme o plano contratado."),
                ("Acompanhamento documental", "Organização e controle da documentação de respaldo, que é a primeira coisa pedida em uma fiscalização."),
                ("Coordenação com a DNIT", "Condução de processos, consultas e comunicações com a administração tributária em nome da empresa."),
            ],
        },
        {
            "type": "checks",
            "eyebrow": "O que muda na sua empresa",
            "h2": "O que você deveria conseguir fazer quando a contabilidade está organizada",
            "items": [
                "Saber, sem esperar o fechamento do ano, como está o resultado do período.",
                "Antecipar quanto vai pagar de IVA e de IRE antes de chegar o vencimento.",
                "Responder rápido quando um banco pede demonstrações financeiras ou documentação de respaldo.",
                "Ter clareza sobre quais documentos faltam e quem precisa providenciá-los.",
                "Entrar em uma fiscalização da DNIT com a documentação em ordem e sem improviso.",
                "Discutir com seu contador decisões de negócio, e não apenas vencimentos.",
            ],
        },
        {
            "type": "planes",
            "eyebrow": "Níveis de serviço",
            "h2": "Duas formas de trabalhar conosco",
            "items": [
                {"badge": "Contabilidade empresarial", "valor": "Orçamento personalizado", "destacado": True,
                 "p": "Gestão contábil e tributária organizada, para empresas de qualquer porte e setor no Paraguai.",
                 "checks": ["Gestão contábil mensal e cumprimento perante a DNIT",
                            "Fechamentos e relatórios periódicos",
                            "Acompanhamento documental e coordenação com a administração tributária"],
                 "cta": "Consultar sobre este plano"},
                {"badge": "Contabilidade e acompanhamento estratégico", "valor": "Proposta personalizada",
                 "p": "Para operações de maior complexidade, com acompanhamento estratégico contínuo à direção.",
                 "checks": ["Tudo o que o serviço de contabilidade empresarial inclui",
                            "Reuniões de revisão estratégica com a direção",
                            "Análise tributária preventiva e apoio nas decisões"],
                 "cta": "Consultar sobre este plano"},
            ],
            "paragraphs": [
                ("Os honorários são definidos conforme o escopo e a complexidade operacional: setor, volume de documentos fiscais, "
                 "quantidade de funcionários, filiais e estado da documentação, entre outros fatores. A regularização de "
                 "períodos anteriores, as auditorias e os trabalhos extraordinários são orçados separadamente e sempre "
                 "acordados por escrito antes de serem faturados."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Perguntas frequentes",
            "h2": "Sobre o serviço contábil",
            "ver_todas": "Ver todas as perguntas frequentes sobre impostos e empresas no Paraguai →",
            "items": [
                ("De quanto em quanto tempo uma empresa entrega declarações no Paraguai?",
                 "Depende do imposto e do regime. O IVA é apurado e entregue mensalmente; o IRE tem apuração anual, com antecipações conforme o regime; e existem declarações informativas adicionais conforme a atividade. Os vencimentos seguem o calendário da DNIT de acordo com o último dígito do RUC, e parte do nosso serviço é manter um calendário próprio para cada empresa."),
                ("Dá para trocar de contador no meio do ano?",
                 "Sim, e é uma situação habitual. O importante é organizar a transição: levantar quais períodos já foram entregues, obter os arquivos e respaldos do contador anterior, verificar saldos de abertura e detectar se ficou algo pendente perante a DNIT antes de continuar. Esse levantamento inicial fazemos sempre, porque começar sem conhecer o ponto de partida gera problemas mais adiante."),
                ("O serviço inclui folha de pagamento?",
                 "A folha de pagamento e as obrigações trabalhistas são avaliadas conforme o caso e acordadas dentro do escopo quando cabe. Ao definir a proposta deixamos explícito o que fica incluído e o que é orçado à parte, para que não haja ambiguidade depois."),
                ("O que acontece se a DNIT fiscalizar minha empresa?",
                 "Acompanhamos a empresa durante o processo: organizamos e apresentamos a documentação exigida, respondemos às intimações formais dentro dos prazos e coordenamos com os profissionais necessários conforme o alcance da fiscalização. Nenhum escritório sério pode prometer que não haverá ajustes; o que se pode fazer é chegar com os registros e respaldos em condições, que é exatamente o que reduz o risco."),
            ],
        },
        {"type": "cta", "h2": "Vamos organizar a contabilidade da sua empresa",
         "lead": "Conte sua situação atual e avaliamos o escopo juntos.",
         "cta": "Fale com a gente"},
    ],
}

# ---------------------------------------------------------------- TRIBUTARIA
P["tributaria"] = {
    "slug": "estrategia-tributaria-paraguai.html",
    "nav": "Estratégia tributária",
    "nav_footer": "Estratégia tributária",
    "service": "Estratégia e planejamento tributário",
    "title": "Impostos no Paraguai | Estratégia tributária e DNIT — MCG",
    "description": ("Diagnóstico tributário, contingências e plano de ação para empresas no Paraguai. Planejamento de IRE, IVA e IDU perante a DNIT. MCG, Assunção."),
    "h1": "Estratégia tributária e prevenção de riscos no Paraguai",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Estratégia tributária",
         "h1": "Estratégia tributária e prevenção de riscos no Paraguai",
         "lead": ("Organizamos a situação tributária da sua empresa perante a DNIT (autoridade tributária do Paraguai, antiga SET), "
                  "identificamos contingências e montamos um plano de ação com prioridades claras."),
         "cta": "Fale com a gente"},
        {
            "type": "rich",
            "eyebrow": "A abordagem",
            "h2": "Planejar antes, não explicar depois",
            "paragraphs": [
                ("A maioria dos problemas tributários que vemos no Paraguai não nasce de uma decisão ousada: nasce da "
                 "falta de revisão. Documentos que não respaldam o que foi deduzido, regimes escolhidos anos atrás que já não "
                 "correspondem ao tamanho atual da empresa, saldos que nunca foram conciliados, retiradas de lucros sem "
                 "considerar o IDU (imposto sobre dividendos e lucros), ou pagamentos ao exterior sem analisar o imposto de renda de não residentes."),
                ("Uma estratégia tributária séria começa por saber exatamente onde a empresa está: quais impostos "
                 "cabem a ela conforme a Ley 6380/2019 (Lei 6380/2019), em que regime do IRE (Imposto de Renda Empresarial) está inscrita, "
                 "que contingências arrasta de períodos anteriores e quais decisões próximas — um investimento, uma distribuição de lucros, "
                 "a abertura de uma filial, a entrada de um sócio — terão impacto tributário."),
                ("Com esse mapa montamos um plano de ação com prioridades: o que precisa ser corrigido já, o que pode esperar o "
                 "próximo fechamento e o que exige uma decisão do dono. Não prometemos ausência de fiscalizações nem de "
                 "ajustes — isso ninguém pode prometer —: trabalhamos para que, se eles chegarem, a empresa esteja em condições "
                 "de responder com documentação e critério."),
            ],
        },
        {
            "type": "checks",
            "alt": True,
            "eyebrow": "O que avaliamos",
            "h2": "O que o diagnóstico tributário cobre",
            "items": [
                "Situação tributária atual da empresa e regime do IRE em que ela está inscrita.",
                "Contingências de períodos em aberto e consistência das declarações entregues à DNIT.",
                "Documentação de respaldo de custos, despesas e créditos fiscais de IVA.",
                "Coerência entre registros contábeis, movimentações bancárias e nota fiscal eletrônica (SIFEN).",
                "Tratamento de retiradas, dividendos e lucros (IDU) e de pagamentos ao exterior (INR).",
                "Planejamento das obrigações e vencimentos do exercício seguinte.",
                "Alternativas legais aplicáveis ao caso concreto, com o impacto estimado de cada uma.",
            ],
        },
        {
            "type": "cards",
            "eyebrow": "Entregáveis",
            "h2": "O que você recebe ao final do diagnóstico",
            "columns": 2,
            "items": [
                ("Relatório executivo", "Resumo claro da situação, escrito para que a direção entenda, e não apenas um contador."),
                ("Mapa de riscos e prioridades", "Quais contingências existem, qual a exposição estimada e em que ordem convém enfrentá-las."),
                ("Recomendações concretas", "Alternativas aplicáveis ao seu caso, com o que cada uma implica em termos de trabalho e de impacto."),
                ("Roteiro de implementação", "Passos, responsáveis e ordem de execução para colocar o plano em marcha sem travar a operação."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Perguntas frequentes",
            "h2": "Sobre estratégia e proteção tributária",
            "ver_todas": "Ver todas as perguntas frequentes sobre impostos e empresas no Paraguai →",
            "items": [
                ("O que se entende por blindagem fiscal ou tributária no Paraguai?",
                 "No uso cotidiano, blindagem se refere a organizar a estrutura societária, a documentação e o cumprimento tributário para reduzir riscos evitáveis: escolher bem o tipo societário e o regime do IRE, manter a contabilidade em dia, separar o patrimônio pessoal do da empresa, respaldar cada dedução e cumprir os prazos e as formas perante a DNIT. Nenhum escritório sério pode prometer imunidade a fiscalizações nem eliminar o risco por completo: o que se pode fazer é trabalhar de forma preventiva e caprichosa para minimizar exposições desnecessárias."),
                ("O diagnóstico substitui a contabilidade mensal?",
                 "Não. O diagnóstico é um trabalho pontual de revisão e planejamento, com entregáveis próprios. A gestão contábil mensal é um serviço contínuo e separado. Muitas empresas começam pelo diagnóstico para entender onde estão e depois decidem se também passam a contabilidade mensal para nós."),
                ("Quanto tempo leva um diagnóstico tributário?",
                 "Depende do volume de informação, da quantidade de períodos a revisar e de quão disponível está a documentação. Uma empresa com registros organizados e arquivos digitais completos avança muito mais rápido do que uma que precisa reconstruir respaldos. Ao avaliar seu caso, damos um prazo concreto antes de começar."),
                ("Serve para uma empresa que está começando agora?",
                 "Sim, e costuma ser o melhor momento. Definir desde o início o tipo societário, o regime tributário correto, como as despesas serão documentadas e como os lucros serão retirados evita ter que corrigir anos depois, quando corrigir custa muito mais."),
            ],
        },
        {"type": "cta", "h2": "Vamos organizar a situação tributária da sua empresa",
         "lead": "Começamos com uma conversa sobre a sua operação atual.",
         "cta": "Fale com a gente"},
    ],
}

# ---------------------------------------------------------------- SOCIEDADES
P["sociedades"] = {
    "slug": "abrir-empresa-no-paraguai.html",
    "nav": "Abrir empresa",
    "nav_footer": "Abertura de empresas",
    "service": "Abertura de empresas",
    "title": "Abrir empresa no Paraguai | EAS, SRL e SA passo a passo — MCG",
    "description": ("Abrir empresa no Paraguai: escolha entre EAS, SRL e SA, processo societário, RUC perante a DNIT e "
                    "início da operação contábil. Acompanhamento da MCG, em Assunção."),
    "h1": "Abrir empresa no Paraguai: EAS, SRL ou SA",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Abertura de empresas",
         "h1": "Abrir empresa no Paraguai: EAS, SRL ou SA",
         "lead": ("Avaliamos sua atividade, seus sócios e seus objetivos antes de recomendar uma estrutura, e acompanhamos "
                  "o processo até a empresa estar operando."),
         "cta": "Fale com a gente"},
        {
            "type": "rich",
            "eyebrow": "A decisão de fundo",
            "h2": "Qual tipo societário vale mais a pena no Paraguai",
            "paragraphs": [
                ("No Paraguai convivem vários tipos societários, e três concentram a maioria dos casos. A "
                 "<strong>EAS (Empresa por Acciones Simplificada, empresa por ações simplificada)</strong> foi pensada para simplificar a criação de "
                 "empresas: permite constituir com uma estrutura flexível e é o caminho mais ágil para novos negócios e "
                 "pequenas e médias empresas. A <strong>SRL (Sociedad de Responsabilidad Limitada, equivalente à Ltda. brasileira)</strong> é o tipo tradicional para "
                 "negócios com poucos sócios e gestão simples, com quotas sociais em vez de ações. A "
                 "<strong>SA (Sociedad Anónima, sociedade anônima)</strong> é a opção habitual para operações de maior porte: "
                 "permite emitir ações, receber investidores e sustentar uma governança mais formal, algo que costuma ser "
                 "exigido por bancos, sócios institucionais e projetos de investimento estrangeiro."),
                ("Não existe um tipo societário que seja sempre o melhor. A escolha correta depende de quantos sócios há e "
                 "de como eles entram ou saem, de se há planos de receber investidores, do tipo de atividade e do perfil das "
                 "contrapartes com quem a empresa vai trabalhar. Um projeto que vai participar de licitações públicas ou "
                 "pedir financiamento bancário relevante não se estrutura do mesmo jeito que um negócio familiar."),
                ("Essa análise fazemos antes de iniciar qualquer processo, porque mudar de tipo societário depois implica "
                 "custo, tempo e, em alguns casos, consequências tributárias que podem ser evitadas decidindo bem no "
                 "começo."),
            ],
        },
        {
            "type": "cards",
            "alt": True,
            "eyebrow": "O que inclui",
            "h2": "Acompanhamento em todo o processo",
            "columns": 3,
            "items": [
                ("Avaliação inicial", "Analisamos atividade, sócios, objetivos e planos de crescimento antes de sugerir uma estrutura."),
                ("Coordenação da constituição", "Acompanhamos o processo societário de ponta a ponta e coordenamos com o cartório quando cabe."),
                ("Organização documental", "Organizamos e revisamos a documentação de cada sócio, inclusive a de sócios estrangeiros."),
                ("Cadastro perante a DNIT", "Inscrição no RUC, definição do regime tributário aplicável e cadastro das obrigações."),
                ("Nota fiscal eletrônica", "Implantação do esquema de documentos fiscais eletrônicos para que a empresa possa faturar dentro da lei."),
                ("Início contábil", "A empresa começa a operar com a contabilidade organizada desde a primeira movimentação."),
            ],
        },
        {
            "type": "pasos",
            "eyebrow": "O processo",
            "h2": "Como é abrir uma empresa no Paraguai",
            "items": [
                ("Definição da estrutura", "Escolhemos o tipo societário, o objeto social, o capital e a distribuição entre os sócios."),
                ("Reunião da documentação", "Identificação de cada sócio, documentos societários e, havendo sócios estrangeiros, legalizações ou apostilamentos."),
                ("Constituição e registro", "Formaliza-se o ato constitutivo e são feitos os registros correspondentes."),
                ("RUC e obrigações", "Cadastro perante a DNIT, definição do regime do IRE e das obrigações que cabem à empresa."),
                ("Alvarás e faturamento", "Alvará municipal conforme o setor e implantação da nota fiscal eletrônica."),
                ("Início da operação contábil", "Abertura de registros, critérios contábeis e calendário de vencimentos próprio da empresa."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Perguntas frequentes",
            "h2": "Sobre abrir uma empresa no Paraguai",
            "ver_todas": "Ver todas as perguntas frequentes sobre impostos e empresas no Paraguai →",
            "items": [
                ("Quanto tempo leva para abrir uma empresa no Paraguai?",
                 "Depende do tipo societário escolhido, da carga de trabalho dos registros e cartórios envolvidos e, sobretudo, de quão completa está a documentação desde o início. Quando há sócios estrangeiros com documentos a legalizar ou apostilar no exterior, esse costuma ser o passo que mais condiciona o prazo. A EAS é, em geral, o tipo societário com o processo mais ágil, por seu desenho simplificado."),
                ("Um estrangeiro pode ser sócio ou acionista de uma empresa paraguaia?",
                 "Sim. A legislação paraguaia admite sócios e acionistas estrangeiros, tanto pessoas físicas quanto jurídicas. O que muda em relação a um sócio local é a documentação: são exigidos documentos legalizados ou apostilados no país de origem e, no caso de pessoas jurídicas estrangeiras, a documentação societária da empresa matriz devidamente traduzida e legalizada."),
                ("Quanto capital é necessário para abrir uma empresa no Paraguai?",
                 "O capital social é definido conforme o tipo societário escolhido e o tipo de atividade, e deve guardar relação com a operação que a empresa vai desenvolver. É uma das definições que revisamos na avaliação inicial, porque tem efeitos práticos: bancos, contrapartes e órgãos costumam olhar esse dado."),
                ("Dá para abrir a empresa sem viajar ao Paraguai?",
                 "Em muitos casos é possível avançar boa parte do processo à distância, por meio de procurações específicas outorgadas no país de origem e devidamente legalizadas ou apostiladas, que habilitam um representante local a assinar a documentação societária. Algumas providências pontuais, como a abertura de conta bancária ou certos trâmites migratórios, costumam exigir presença física ou ao menos uma atuação mais direta."),
            ],
        },
        {"type": "cta", "h2": "Vamos avaliar a estrutura da sua empresa",
         "lead": "Conte sua atividade e seus objetivos para orientarmos melhor.",
         "cta": "Fale com a gente"},
    ],
}

# --------------------------------------------------------------- EXTRANJEROS
P["extranjeros"] = {
    "slug": "empresarios-estrangeiros-paraguai.html",
    "nav": "Estrangeiros",
    "nav_footer": "Empresários estrangeiros",
    "service": "Acompanhamento a investidores estrangeiros",
    "title": "Mudar empresa para o Paraguai | Residência e contabilidade — MCG",
    "description": ("Apoio local a brasileiros que querem mudar a empresa para o Paraguai: abertura da sociedade, RUC "
                    "perante a DNIT, banco, residência paraguaia e contabilidade."),
    "h1": "Instale e opere sua empresa no Paraguai com apoio local",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Empresários e investidores estrangeiros",
         "h1": "Instale e opere sua empresa no Paraguai com apoio local",
         "lead": ("Trabalhamos com estrangeiros que querem realmente operar ou investir no Paraguai, e não apenas resolver "
                  "documentação pessoal."),
         "cta": "Fale com a gente"},
        {
            "type": "rich",
            "eyebrow": "Por que o Paraguai",
            "h2": "O que um investidor estrangeiro olha quando avalia o Paraguai",
            "paragraphs": [
                ("O Paraguai aparece com frequência nas avaliações de empresários do Brasil, da Argentina, dos Estados Unidos e "
                 "da Europa por um conjunto de razões concretas: alíquotas comparativamente baixas dentro da região "
                 "— 10% de IRE (Imposto de Renda Empresarial) e 10% de IVA (Imposto sobre o Valor Agregado) como alíquotas gerais, com IVA reduzido de 5% para determinados bens e "
                 "serviços —, um sistema tributário relativamente simples desde a Ley 6380/2019 (Lei 6380/2019), custos operacionais "
                 "competitivos e um regime de residência vinculado ao investimento."),
                ("Nada disso significa imposto zero nem benefícios automáticos, e desconfie de quem apresentar as coisas assim. "
                 "A carga tributária real de cada empresa depende do seu regime, do seu setor, da sua estrutura societária e de "
                 "como os lucros são retirados. Um projeto bem estruturado desde o início aproveita o marco legal; um "
                 "improvisado acaba corrigindo com custo."),
                ("Nosso trabalho é o lado paraguaio do projeto: que a sociedade esteja bem constituída, que a empresa "
                 "esteja corretamente inscrita perante a DNIT (autoridade tributária do Paraguai, antiga SET), que a contabilidade comece organizada e que a documentação "
                 "esteja em condições para bancos e contrapartes. As obrigações que o investidor mantenha no seu país "
                 "de origem exigem coordenação com especialistas daquela jurisdição."),
            ],
        },
        {
            "type": "pasos",
            "alt": True,
            "eyebrow": "O percurso",
            "h2": "Como acompanhamos a sua instalação no Paraguai",
            "items": [
                ("Avaliação do projeto", "Entendemos sua atividade, seus objetivos, sua estrutura atual no exterior e sua situação de partida."),
                ("Estrutura e constituição", "Definimos o tipo societário adequado e coordenamos o processo de abertura no Paraguai."),
                ("Cadastro perante a DNIT", "Inscrição no RUC, regime tributário aplicável e cadastro das obrigações que couberem."),
                ("Coordenação migratória", "Com profissionais competentes na matéria, conforme sua situação e o tipo de residência que você busca."),
                ("Documentação bancária", "Preparamos a documentação necessária para suas gestões de abertura de conta e financiamento."),
                ("Contabilidade e operação", "A empresa começa com a contabilidade organizada e seguimos acompanhando a operação mês a mês."),
            ],
        },
        {
            "type": "rich",
            "eyebrow": "Residência e investimento",
            "h2": "Residência por investimento, cédula paraguaia e RUC: três coisas diferentes",
            "paragraphs": [
                ("É a confusão mais frequente e vale esclarecer cedo. A <strong>residência</strong> é um status "
                 "migratório da pessoa física: habilita você a viver e permanecer legalmente no Paraguai. Existe um regime "
                 "de residência vinculado ao investimento, conduzido pelo SUACE (sistema unificado de abertura e fechamento de empresas), que exige uma certificação de "
                 "investimento emitida pelo Ministério da Indústria e Comércio, além de documentação pessoal e societária."),
                ("A <strong>cédula de identidade paraguaia</strong> é o documento que se tira depois de obtida a "
                 "residência e que simplifica enormemente a vida operacional: gestões bancárias, assinaturas em cartório e "
                 "trâmites perante órgãos públicos. O <strong>RUC</strong>, por sua vez, é a inscrição tributária perante a DNIT: "
                 "quem tem é a empresa, e também pode tê-lo uma pessoa física que desenvolva atividade tributada."),
                ("Uma empresa pode ser constituída e operar no Paraguai com sócios que não residem no país; o que precisa "
                 "ficar bem definido nesse caso é a representação legal local, as procurações outorgadas e quem fica responsável pela "
                 "assinatura do dia a dia. E obter residência no Paraguai não elimina, por si só, as obrigações que a pessoa "
                 "possa ter no seu país de origem: isso se analisa com um especialista daquela jurisdição."),
            ],
        },
        {
            "type": "checks",
            "alt": True,
            "eyebrow": "Pontos importantes",
            "h2": "O que convém deixar claro desde o início",
            "items": [
                "A residência migratória e a situação tributária são questões distintas, ainda que relacionadas.",
                "Obter residência ou abrir uma sociedade no Paraguai não elimina obrigações no seu país de origem.",
                "A aprovação de contas bancárias e de financiamentos está sujeita à avaliação de cada instituição.",
                "A distribuição de lucros ao exterior tem tratamento tributário próprio (IDU) e convém projetá-la desde o início.",
                "Cuidamos do lado paraguaio do projeto; o da sua jurisdição de origem é coordenado com especialistas de lá.",
                "Atendemos em espanhol, inglês e português, para que a operação não dependa de uma tradução improvisada.",
            ],
        },
        {
            "type": "faq",
            "eyebrow": "Perguntas frequentes",
            "h2": "Sobre investir e se instalar no Paraguai",
            "ver_todas": "Ver todas as perguntas frequentes sobre impostos e empresas no Paraguai →",
            "items": [
                ("Como faço para mudar minha empresa para o Paraguai?",
                 "Na prática não se transfere uma sociedade estrangeira tal como ela é: o habitual é constituir uma sociedade paraguaia (EAS, SRL ou SA) ou registrar uma filial da empresa do exterior, conforme o projeto. Depois vem o cadastro do RUC perante a DNIT, o alvará municipal se o setor exigir, a abertura de conta bancária e a implantação da contabilidade e da nota fiscal eletrônica. Em paralelo se resolve a situação migratória das pessoas envolvidas, caso elas vão residir no país."),
                ("Posso administrar minha empresa paraguaia do exterior?",
                 "Sim, é uma situação frequente. Dá para ser sócio ou acionista de uma empresa paraguaia sem residir no país, definindo bem a representação legal local e as procurações outorgadas. A contabilidade, a nota fiscal eletrônica e as entregas perante a DNIT são conduzidas remotamente com uma equipe local de confiança, que é justamente o papel que cumprimos para clientes que operam de fora."),
                ("Que impostos paga uma empresa estrangeira que opera no Paraguai?",
                 "Uma sociedade constituída no Paraguai é tributada como qualquer empresa local: IRE sobre seus lucros, IVA sobre suas operações e os impostos específicos que couberem à sua atividade. A isso se soma o IDU quando distribui lucros aos sócios, com alíquota maior quando o beneficiário não é residente, e o INR (Imposto de Renda de Não Residentes) sobre determinadas rendas de fonte paraguaia pagas ao exterior. A estrutura com que o projeto é montado influi diretamente nessa carga."),
                ("Vocês atendem em português e inglês?",
                 "Sim. Boa parte dos investidores que chegam ao Paraguai são brasileiros, e também trabalhamos com clientes de língua inglesa. O site está disponível em espanhol, inglês e português, e o atendimento é coordenado no idioma mais confortável para o cliente."),
            ],
        },
        {"type": "cta", "h2": "Vamos conversar sobre o seu projeto no Paraguai",
         "lead": "Conte em que etapa você está e o que precisa resolver primeiro.",
         "cta": "Fale com a gente"},
    ],
}

# -------------------------------------------------------------------- EQUIPO
P["equipo"] = {
    "slug": "cristina-rolon-contadora-paraguai.html",
    "nav": "Equipe",
    "nav_footer": "Direção e equipe",
    "title": "Cristina Rolón, contadora no Paraguai | Diretora da MCG",
    "description": ("Cristina Rolón, contadora pela Universidad Nacional de Asunción (2008) e Mestre em Impostos, dirige a "
                    "MCG em Assunção, Paraguai, com 18 anos de experiência."),
    "h1": "Cristina Rolón, contadora e diretora da MCG",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Direção e equipe",
         "h1": "Cristina Rolón, contadora e diretora da MCG",
         "lead": ("Uma direção técnica que entende como as empresas decidem: formação tributária, prática "
                  "profissional e experiência em conselhos de administração no Paraguai.")},
        {
            "type": "bio",
            "h2": "Trajetória",
            "nombre": "Cristina Rolón",
            "cargo": "Diretora da MCG · Contadora Pública · Mestre em Impostos",
            "foto_alt": ("Cristina Rolón, contadora e diretora da MCG Consultora Contable y Tributaria, "
                         "nos escritórios da consultoria contábil em Assunção, Paraguai"),
            "trayectoria": [
                "Contadora Pública, formada pela Universidad Nacional de Asunción (Universidade Nacional de Assunção, 2008)",
                "Mestre em Impostos e especializações na área tributária",
                "18 anos de experiência profissional em diferentes setores",
                "Especialista na implantação do módulo contábil de ERP, com mais de 30 empresas implantadas",
                "Experiência em organizações de 10 até mais de 700 funcionários",
                "Integrante de conselhos de administração de empresas",
                "Diretora da MCG Consultora Contable y Tributaria, em Assunção, Paraguai",
            ],
            "paragraphs": [
                ("Essa experiência em conselhos dá a Cristina uma leitura direta de como as empresas avaliam "
                 "informação, priorizam riscos e tomam decisões, algo que ela transfere ao critério com que dirige a MCG "
                 "e ao tipo de relatórios que o escritório entrega a seus clientes."),
            ],
        },
        {
            "type": "rich",
            "alt": True,
            "eyebrow": "A história dela",
            "h2": "De onde vem a disciplina com que ela trabalha",
            "paragraphs": [
                ("Cristina é contadora, formada pela Universidad Nacional de Asunción (Universidade Nacional de Assunção) em 2008. Antes de fundar "
                 "a MCG, passou por diferentes setores que marcaram seu jeito de trabalhar: cada um lhe ensinou a olhar os "
                 "números com contexto, entendendo o negócio que existe por trás de cada cifra. Mais adiante concluiu "
                 "especializações e um Mestrado em Impostos, buscando sempre aprofundar e estar à altura dos "
                 "desafios de seus clientes."),
                ("Essa mesma exigência a levou, durante um período da vida, a competir em fisiculturismo. Preparar-se "
                 "para subir num palco não é um esforço de um dia: é treinar durante anos para um resultado que se "
                 "mede em minutos, sustentar uma rotina quando ninguém está olhando e ajustar o método quando algo não "
                 "funciona. Cristina aplica essa mesma lógica — constância, método e revisão constante — à contabilidade e "
                 "à estratégia tributária de cada empresa que atende."),
                ("Ela se define pela perseverança, pela solidez dos seus conhecimentos e pela vontade genuína de colaborar com "
                 "cada empresa em que trabalha. Seu lema é simples: deixar algo construído no lugar onde presta "
                 "serviço e impactar significativamente no resultado."),
            ],
        },
        {
            "type": "equipo",
            "eyebrow": "A equipe",
            "h2": "Uma equipe estável como respaldo operacional",
            "foto_alt": ("Equipe da MCG Consultora Contable y Tributaria junto a Cristina Rolón nos escritórios da "
                         "consultoria contábil em Assunção, Paraguai"),
            "paragraphs": [
                ("Por trás da direção de Cristina, a MCG conta com uma equipe estável que executa o trabalho contábil e "
                 "tributário do dia a dia: registros, conciliações, entregas perante a DNIT, acompanhamento documental "
                 "e atendimento às dúvidas de cada empresa."),
                ("Essa estabilidade faz parte do serviço. Que as mesmas pessoas acompanhem sua empresa mês a mês significa que não é "
                 "preciso explicar o negócio de novo a cada vez, e que os critérios contábeis se mantêm consistentes ao "
                 "longo do tempo."),
            ],
        },
        {"type": "cta", "h2": "Veja como podemos ajudar a sua empresa",
         "lead": "Conte sua situação e avaliamos juntos o escopo do trabalho.",
         "cta": "Fale com a gente"},
    ],
}

# ----------------------------------------------------------------------- FAQ
P["faq"] = {
    "slug": "perguntas-frequentes-impostos-paraguai.html",
    "nav": "Perguntas frequentes",
    "nav_footer": "Perguntas frequentes",
    "title": "Impostos no Paraguai para brasileiros | Perguntas | MCG",
    "description": ("DNIT, IRE, IVA, IRP, IDU, nota fiscal eletrônica, residência por investimento, cédula paraguaia e "
                    "abertura de empresa no Paraguai: 28 respostas detalhadas da MCG."),
    "h1": "Perguntas frequentes sobre impostos e empresas no Paraguai",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Perguntas frequentes",
         "h1": "Perguntas frequentes sobre impostos e empresas no Paraguai",
         "lead": ("As dúvidas mais habituais de empresas já instaladas no Paraguai e de investidores estrangeiros que "
                  "avaliam o país: DNIT, impostos, residência, cédula paraguaia, mudança de empresa e abertura "
                  "de sociedades.")},
        {
            "type": "faq",
            "eyebrow": "Impostos e regime tributário",
            "h2": "DNIT, IRE, IVA e o sistema tributário paraguaio",
            "items": [
                ("O que é a DNIT e qual é a relação dela com a antiga SET?",
                 "A DNIT (Dirección Nacional de Ingresos Tributarios), autoridade tributária do Paraguai, é o órgão que administra os impostos internos e aduaneiros do país. Ela foi formada a partir da fusão da SET (Subsecretaría de Estado de Tributación) com a Dirección Nacional de Aduanas, de modo que hoje uma única instituição concentra o que antes estava repartido. Se a sua empresa foi constituída antes dessa fusão, todos os seus antecedentes, seu RUC e suas obrigações continuam válidos sob a DNIT: não é preciso reconstituir a empresa nem obter um número novo. Os canais de entrega e as senhas de acesso se mantêm, embora a transição tenha trazido ajustes administrativos pontuais que convém verificar antes de cada entrega. Na prática, quando você ler SET em documentação antiga, entenda DNIT."),
                ("Quais são os principais impostos que uma empresa paga no Paraguai?",
                 "Sob a Ley 6380/2019 (Lei 6380/2019), uma empresa no Paraguai se relaciona principalmente com quatro impostos. O IRE (Imposto de Renda Empresarial) incide sobre os lucros. O IVA (Imposto sobre o Valor Agregado) incide sobre as vendas de bens e as prestações de serviços, e é apurado mensalmente descontando o crédito fiscal das compras. O IDU alcança a distribuição de dividendos e lucros aos sócios. E o ISC (Imposto Seletivo ao Consumo) se aplica apenas a determinados produtos, como combustíveis, bebidas ou tabaco. A isso se somam as obrigações formais: nota fiscal eletrônica, declarações informativas e retenções quando cabe. A combinação exata depende do setor e do regime, e essa é uma das primeiras coisas que revisamos ao conhecer uma empresa."),
                ("O que é o IRE e quais são seus regimes: RESIMPLE, IRE SIMPLE e IRE GENERAL?",
                 "O IRE é o Imposto de Renda Empresarial e sua alíquota geral é de 10% sobre o lucro. A Ley 6380/2019 (Lei 6380/2019) prevê três regimes conforme o nível de receita da empresa. O RESIMPLE foi pensado para negócios muito pequenos, com um esquema simplificado de parcela fixa. O IRE SIMPLE se aplica a empresas dentro do limite de receita fixado pela norma e permite uma apuração com menos exigências documentais. O IRE GENERAL corresponde às empresas que superam esse limite: exige contabilidade completa e apuração sobre o lucro líquido real. Escolher mal o regime ou permanecer em um que já não cabe tem consequências concretas: mais carga administrativa do que o necessário, ou diretamente um descumprimento. Por isso convém revisar o enquadramento ao se inscrever e sempre que o volume da empresa mudar de escala."),
                ("Qual é a alíquota do IVA no Paraguai e como ele é apurado?",
                 "O Paraguai tem uma alíquota geral de IVA de 10%, com alíquota reduzida de 5% para determinados bens e serviços definidos pela norma, entre eles certos produtos da cesta básica familiar e algumas operações imobiliárias. O IVA é apurado mensalmente: calcula-se o débito fiscal das vendas, subtrai-se o crédito fiscal das compras respaldadas por documentos válidos, e a diferença é o que se paga. Por isso o respaldo documental não é um detalhe burocrático: um crédito fiscal sem documento válido simplesmente não pode ser usado. Uma mesma empresa pode ter operações a 10% e a 5% no mesmo período, e essa classificação precisa estar bem feita já na emissão da nota."),
                ("O que é o IRP e quem ele alcança no Paraguai?",
                 "O IRP (Imposto de Renda Pessoal) incide sobre os rendimentos das pessoas físicas residentes no Paraguai, com alíquotas escalonadas de 8%, 9% e 10% conforme o nível de renda e as deduções admitidas. Alcança, entre outros, quem presta serviços pessoais, recebe honorários profissionais, obtém ganhos de capital ou recebe determinados rendimentos por sua atividade independente. É um imposto distinto do IRE, que incide sobre a empresa em si. Essa diferença importa na prática: um dono de empresa pode ter que considerar o IRE da sua sociedade e, separadamente, a sua própria situação frente ao IRP, conforme a forma como retira rendimentos."),
                ("O que é o IDU, o imposto sobre dividendos e lucros?",
                 "O IDU incide sobre a distribuição de dividendos e lucros que uma empresa paraguaia faz a seus sócios ou acionistas. A alíquota é de 8% quando quem recebe é residente no Paraguai e de 15% quando o beneficiário é uma pessoa ou empresa não residente. É um ponto especialmente relevante para investidores estrangeiros que planejam remeter lucros ao seu país de origem, porque impacta diretamente o retorno líquido do investimento. Também importa para sócios locais na hora de decidir entre reinvestir na empresa ou distribuir. Convém projetá-lo já no desenho societário inicial, e não descobri-lo quando a decisão já foi tomada."),
                ("O que é o INR e quando ele se aplica a pagamentos ao exterior?",
                 "O INR é o Imposto de Renda de Não Residentes e alcança as rendas de fonte paraguaia obtidas por pessoas ou empresas do exterior sem residência fiscal no Paraguai, com alíquota geral de 15% sobre a base de cálculo determinada pela lei. Aplica-se, por exemplo, quando uma empresa paraguaia paga serviços, juros, royalties ou assistência técnica a um fornecedor do exterior. Nesses casos a empresa local costuma atuar como agente de retenção, de modo que o descumprimento não é um problema do fornecedor estrangeiro, e sim da empresa paraguaia que pagou. Convém analisar isso antes de assinar contratos com fornecedores do exterior."),
                ("O que é a nota fiscal eletrônica SIFEN e ela é obrigatória?",
                 "O SIFEN (Sistema Integrado de Facturación Electrónica Nacional) é o esquema da DNIT para emitir documentos fiscais eletrônicos com validade fiscal. Sua obrigatoriedade foi implementada de forma escalonada, por grupos de contribuintes definidos pela administração tributária, e a esta altura já alcança a grande maioria das empresas ativas, com os últimos grupos entrando conforme o calendário oficial. Se a sua empresa ainda emite em bloco de notas ou com autoimpressor, convém confirmar em que grupo ela está e planejar a migração com antecedência, porque a mudança não é apenas tecnológica: implica ajustar processos internos de faturamento, cobrança e arquivamento de documentos."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Estrangeiros e investimento",
            "h2": "Mudar empresa para o Paraguai, residência e cédula paraguaia",
            "items": [
                ("Como faço a mudança da minha empresa para o Paraguai?",
                 "O que normalmente se chama de mudar a empresa para o Paraguai consiste, na prática, em constituir uma sociedade paraguaia — EAS, SRL ou SA — ou registrar uma filial da sociedade estrangeira, e transferir para ela a operação que se quer desenvolver no país. O percurso inclui definir o tipo societário, reunir a documentação dos sócios legalizada ou apostilada, constituir e registrar a sociedade, obter o RUC perante a DNIT, tirar o alvará municipal do setor se couber, abrir conta bancária e colocar em marcha a contabilidade e a nota fiscal eletrônica. Em paralelo se resolve a situação migratória das pessoas que vão morar no Paraguai. A ordem e a duração dependem do projeto: não é a mesma coisa uma consultoria de serviços e uma operação com depósito e importações."),
                ("O que é a residência por investimento no Paraguai e quais são os requisitos?",
                 "O Paraguai conta com um regime de residência vinculado ao investimento, conduzido pelo SUACE (Sistema Unificado de Apertura y Cierre de Empresas). Ele exige uma certificação de investimento emitida pelo Ministério da Indústria e Comércio e a apresentação de um conjunto de documentos pessoais e societários: antecedentes, atestado de saúde, comprovante do valor efetivamente investido e documentação da empresa, entre outros. O processo tem uma taxa estabelecida pela norma vigente e a residência obtida é renovada periodicamente. Como a regulamentação pode ser atualizada, convém confirmar valores e requisitos exatos no momento de iniciar o processo e não se basear em informação de anos anteriores."),
                ("A residência no Paraguai me dá a nacionalidade paraguaia?",
                 "Não. A residência, seja temporária, permanente ou por investimento, é um status migratório que habilita a viver e operar legalmente no país. A nacionalidade se obtém por naturalização, que é um processo distinto, posterior, com seus próprios requisitos e prazos perante as autoridades competentes. Muitos investidores estrangeiros operam sua empresa paraguaia durante anos mantendo apenas a residência, sem buscar a nacionalidade, e isso não afeta em nada a validade da sua empresa nem das suas operações."),
                ("Preciso de cédula paraguaia para ter uma empresa no Paraguai?",
                 "Depende da etapa. Para constituir a sociedade e obter o RUC é possível avançar com passaporte e a documentação migratória correspondente. Agora, uma vez que o estrangeiro obtém sua residência, tirar a cédula de identidade paraguaia costuma ser o passo natural seguinte, porque simplifica muito a operação cotidiana: abertura e manejo de contas bancárias, assinaturas em cartório, trâmites perante órgãos públicos e gestões junto à própria DNIT. Na prática, ter cédula acelera tudo, ainda que nem sempre seja um requisito legal prévio indispensável para que a empresa exista."),
                ("O que significa blindagem patrimonial ou tributária para um investidor estrangeiro?",
                 "No uso cotidiano, blindagem se refere a organizar a estrutura societária, a documentação e o cumprimento tributário para reduzir riscos legais, patrimoniais e fiscais evitáveis: escolher o tipo societário adequado, manter a contabilidade em dia, separar com clareza o patrimônio pessoal do da empresa, respaldar documentalmente cada operação e cumprir prazos e formas perante a DNIT. Nenhum escritório de contabilidade sério pode prometer imunidade a fiscalizações, nem garantir que nunca haverá um ajuste, nem oferecer estruturas para ocultar patrimônio. O que se pode fazer, e é o que fazemos, é trabalhar de forma preventiva e caprichosa para minimizar exposições desnecessárias."),
                ("Posso administrar minha empresa paraguaia morando no exterior?",
                 "Sim, é uma situação muito frequente entre investidores estrangeiros. É possível constituir e ser sócio ou acionista de uma empresa paraguaia sem residir no país. O que precisa ficar bem definido é a representação legal local, o alcance das procurações outorgadas e quem fica responsável pela assinatura e pelas decisões do dia a dia. A contabilidade, a nota fiscal eletrônica e as entregas perante a DNIT são conduzidas perfeitamente de forma remota quando há uma equipe local de confiança à frente, que é justamente o papel que um escritório de contabilidade como a MCG cumpre para clientes que operam de fora."),
                ("Quais são as vantagens tributárias reais do Paraguai para um investidor estrangeiro?",
                 "O Paraguai se caracteriza por alíquotas comparativamente baixas dentro da região: IRE de 10% sobre os lucros e IVA geral de 10%, com alíquota reduzida de 5% para determinados bens e serviços. A isso se soma um sistema relativamente simples desde a Ley 6380/2019 (Lei 6380/2019), regimes simplificados para negócios pequenos e um regime de residência vinculado ao investimento. Nenhuma dessas características implica imposto zero nem benefícios automáticos, e convém desconfiar de quem apresentar as coisas assim. A carga tributária real depende do regime em que a empresa se inscreve, do seu setor, da sua estrutura societária e de como os lucros são retirados, onde entra o IDU. Por isso a avaliação séria é feita sobre o caso concreto, com números."),
                ("Uma empresa estrangeira pode abrir conta bancária no Paraguai?",
                 "Sim, e é um dos passos que mais vale a pena preparar com antecedência. Os bancos paraguaios aplicam procedimentos de conhecimento do cliente que exigem documentação societária completa, identificação dos beneficiários finais, comprovação da origem dos recursos e, em muitos casos, presença dos signatários. Nosso trabalho nesta etapa é preparar e organizar a documentação e coordenar com a instituição, mas a aprovação sempre depende da avaliação de cada banco: não existe, e desconfie de quem oferecer, um contato que garanta aprovações."),
            ],
        },
        {
            "type": "faq",
            "eyebrow": "Abertura de empresas",
            "h2": "EAS, SRL, SA e o processo de constituição no Paraguai",
            "items": [
                ("Que tipo de sociedade vale mais a pena no Paraguai: EAS, SRL ou SA?",
                 "Os três tipos mais usados são a EAS (Empresa por Acciones Simplificada, empresa por ações simplificada), a SRL (Sociedad de Responsabilidad Limitada, equivalente à Ltda. brasileira) e a SA (Sociedad Anónima, sociedade anônima). A EAS foi criada como caminho ágil e flexível para novos negócios e pequenas e médias empresas, com um processo de constituição mais simples. A SRL é o tipo tradicional para negócios com poucos sócios e gestão simples, onde a participação é representada em quotas sociais. A SA é a opção habitual para operações de maior porte: permite emitir ações, receber investidores e sustentar uma governança mais formal, algo que costuma ser exigido por bancos, fundos e sócios institucionais. A escolha correta depende do número de sócios, do plano de crescimento, de se haverá entrada de investidores e do tipo de contraparte com quem a empresa vai trabalhar."),
                ("Quanto tempo leva para abrir uma empresa no Paraguai?",
                 "O prazo depende do tipo societário escolhido, da carga de trabalho dos registros e cartórios envolvidos e, sobretudo, de quão completa está a documentação desde o início. Quando há sócios estrangeiros com documentos que precisam ser legalizados ou apostilados no exterior, esse costuma ser o passo que mais condiciona o calendário, porque não depende do Paraguai. A EAS é, em geral, o tipo societário com o processo mais ágil, por seu desenho simplificado. Mais do que prometer um número fixo de dias, o útil é montar o dossiê completo desde o começo: é isso que realmente encurta os prazos."),
                ("Quais documentos preciso para constituir uma sociedade no Paraguai?",
                 "Em termos gerais é necessária a identificação de cada sócio — cédula se for paraguaio, passaporte e documentação migratória se for estrangeiro —, o estatuto ou contrato social com o objeto e a estrutura societária, a definição do capital social e sua integralização, e a designação de administradores ou representantes legais. Quando há sócios estrangeiros, pessoas físicas ou jurídicas, soma-se documentação legalizada ou apostilada no país de origem, com tradução oficial quando cabe. Se uma pessoa jurídica estrangeira for sócia, exige-se também a documentação societária da matriz. Convém revisar a lista exata antes de iniciar legalizações, para não pagar duas vezes por trâmites mal encaminhados."),
                ("Posso abrir uma empresa no Paraguai sem viajar ao país?",
                 "Em muitos casos é possível avançar boa parte do processo à distância, por meio de procurações específicas outorgadas em cartório no país de origem e devidamente legalizadas ou apostiladas, que habilitam um representante local a assinar a documentação societária. No entanto, algumas providências pontuais, sobretudo a abertura de conta bancária e certos trâmites migratórios, costumam exigir presença física ou ao menos uma atuação mais direta do interessado. O recomendável é planejar desde o início o que se resolve à distância e o que convém concentrar em uma única viagem ao Paraguai."),
                ("De quanto capital social preciso para abrir uma empresa no Paraguai?",
                 "O capital social é definido conforme o tipo societário escolhido e o tipo de atividade, e deve guardar uma relação razoável com a operação que a empresa vai desenvolver. Não é um dado meramente formal: bancos, contrapartes comerciais e órgãos olham esse número ao avaliar a empresa, e um capital inconsistente com o volume de operações gera perguntas. Essa é uma das definições que revisamos na avaliação inicial, junto com a estrutura de sócios e o objeto social."),
                ("Que obrigações tem uma empresa recém-constituída no Paraguai?",
                 "A partir do momento em que obtém seu RUC, a empresa passa a estar sujeita às obrigações do regime em que se inscreveu, mesmo que ainda não tenha faturado. Isso inclui entregar as declarações cabíveis em cada vencimento, emitir documentos com validade fiscal por meio do esquema de nota fiscal eletrônica, manter registros contábeis e conservar a documentação de respaldo. Entregar declaração zerada quando não houve movimento também é cumprir: a omissão, ainda que sem atividade, gera descumprimentos formais que depois precisam ser regularizados."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Contabilidade e trabalho com a MCG",
            "h2": "Cumprimento, regularização e como começar",
            "items": [
                ("De quanto em quanto tempo devo entregar declarações à DNIT?",
                 "A periodicidade depende do imposto e do regime. O IVA é apurado e entregue mensalmente; o IRE tem apuração anual, com antecipações conforme o regime em que a empresa está; e existem declarações informativas específicas conforme a atividade, além das retenções quando cabe atuar como agente. Os vencimentos seguem o calendário da DNIT de acordo com o último dígito do RUC. Manter um calendário próprio por empresa, e não só olhar o calendário geral, é uma das funções básicas do nosso serviço de contabilidade empresarial."),
                ("O que acontece se eu estiver com a contabilidade atrasada ou desorganizada?",
                 "É uma situação mais comum do que parece, sobretudo em empresas que cresceram rápido ou que trocaram de contador várias vezes. A primeira coisa é fazer um diagnóstico do estado real: que períodos faltam, que documentação existe, que entregas ficaram pendentes perante a DNIT e que saldos não fecham. A partir daí se monta um plano de regularização com prioridades, orçado à parte do serviço mensal porque é um trabalho pontual diferente. Quanto antes o assunto for enfrentado, menor o risco de acumular contingências e de um problema pequeno virar um caro."),
                ("A MCG atende empresas de qualquer setor e porte?",
                 "Sim. Trabalhamos com todo tipo de empresa: companhias que já faturam de forma significativa, negócios que estão começando, empresas familiares que precisam se organizar e projetos de investidores estrangeiros que se instalam no Paraguai. Os setores são variados: comércio, serviços, construção, importação, tecnologia, saúde e gastronomia, entre outros. O que definimos em cada caso é o escopo do serviço conforme a complexidade real da operação, e não um faturamento mínimo para podermos trabalhar juntos."),
                ("Como começo a trabalhar com a MCG?",
                 "O primeiro passo é preencher o formulário de contato ou nos escrever pelo WhatsApp contando sua situação: se você já tem uma empresa no Paraguai, se está prestes a se instalar como estrangeiro ou se tem outra dúvida pontual. Com essa informação avaliamos o encaixe e o escopo possível e marcamos uma conversa para entender melhor o caso. Se for necessário um diagnóstico ou uma revisão técnica mais profunda, isso é orçado como um passo à parte antes de definir a proposta final. Tudo fica por escrito antes de começar."),
                ("Os honorários incluem tudo ou há custos à parte?",
                 "Os honorários são definidos conforme o escopo acordado — gestão contábil, obrigações tributárias, fechamentos, acompanhamento estratégico — e esse escopo fica explícito na proposta antes de começarmos a trabalhar. Os serviços que ficam de fora, como a regularização de períodos anteriores, auditorias pontuais, trabalhos extraordinários ou providências que exigem profissionais de outras especialidades, são orçados separadamente. Além disso, as taxas e emolumentos de órgãos e cartórios são despesas de terceiros e são sempre informados como tais, separados dos nossos honorários."),
                ("Vocês atendem empresas do interior do país ou apenas em Assunção?",
                 "Nosso escritório fica em Assunção, mas o trabalho contábil e tributário é feito em grande medida de forma digital: recebimento de documentação, registros, entregas perante a DNIT e reuniões de revisão. Isso nos permite atender empresas de diferentes pontos do Paraguai e também clientes que operam do exterior. Quando alguma providência exige presença física, ela é combinada conforme o caso."),
            ],
        },
        {"type": "cta", "h2": "Sua pergunta não está na lista?",
         "lead": "Conte sua situação específica e respondemos diretamente.",
         "cta": "Fale com a gente"},
    ],
}

# ------------------------------------------------------------------ CONTACTO
P["contacto"] = {
    "slug": "contato.html",
    "nav": "Contato",
    "nav_footer": "Contato",
    "title": "Contato | Contador no Paraguai — MCG Consultora, Assunção",
    "description": ("Fale com a MCG Consultora Contable y Tributaria, contador no Paraguai. Conte sobre sua empresa ou "
                    "projeto. Atendimento em espanhol, inglês e português."),
    "h1": "Solicite uma avaliação empresarial",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Contato",
         "h1": "Solicite uma avaliação empresarial",
         "lead": ("Conte sobre a sua empresa ou o seu projeto no Paraguai. O contato inicial permite avaliar o encaixe e o "
                  "escopo; uma revisão técnica ou diagnóstico é orçado separadamente.")},
        {
            "type": "form",
            "form": {
                "situacion": "Qual é a sua situação?",
                "seleccione": "Selecione uma opção",
                "situacion_opciones": [("empresa", "Já tenho uma empresa no Paraguai"),
                                       ("extranjero", "Quero mudar minha empresa para o Paraguai"),
                                       ("otro", "Outra dúvida")],
                "nombre": "Nome",
                "empresa": "Empresa ou projeto",
                "correo": "E-mail",
                "whatsapp": "WhatsApp",
                "whatsapp_ph": "Ex.: +55 11 91234 5678",
                "servicio": "Serviço de interesse",
                "seleccione_servicio": "Selecione um serviço",
                "servicio_opciones": [("Contabilidad empresarial", "Contabilidade empresarial"),
                                      ("Estrategia tributaria", "Estratégia tributária"),
                                      ("Constitución de sociedades", "Abertura de empresas"),
                                      ("Instalación para extranjeros", "Instalação para estrangeiros"),
                                      ("No estoy seguro todavía", "Ainda não tenho certeza")],
                "legend_empresa": "Sobre a sua empresa",
                "rubro": "Setor",
                "facturacion": "Faturamento mensal aproximado",
                "facturacion_opciones": ["Estamos começando agora", "Menos de G. 400 milhões",
                                         "G. 400–1.000 milhões", "Mais de G. 1.000 milhões",
                                         "Prefiro informar em uma conversa"],
                "necesidad": "Principal necessidade",
                "legend_extranjero": "Sobre o seu projeto no Paraguai",
                "pais": "País de residência",
                "tipo_proyecto": "Tipo de projeto",
                "tipo_ph": "Ex.: comércio, serviços, investimento",
                "etapa": "Etapa do projeto",
                "seleccione_etapa": "Selecione uma etapa",
                "etapa_opciones": [("Recién estoy evaluando la idea", "Ainda estou avaliando a ideia"),
                                   ("Ya decidí instalarme y quiero avanzar", "Já decidi me instalar e quero avançar"),
                                   ("Ya tengo una empresa constituida en Paraguay", "Já tenho uma empresa constituída no Paraguai")],
                "aviso": ("Não é necessário enviar documentos financeiros nem informações bancárias sensíveis neste "
                          "formulário. Se for preciso, vamos pedi-los de forma segura mais adiante."),
                "enviar": "Enviar mensagem",
                "abrir_wa": "Abrir o WhatsApp manualmente",
            },
        },
        {
            "type": "contacto_extra",
            "eyebrow": "Outra forma de falar com a gente",
            "h2": "Você também pode nos escrever direto",
            "p": ("Se preferir, escreva direto pelo WhatsApp ou siga a gente no Instagram. Atendemos em espanhol, "
                  "inglês e português, a partir de Assunção, Paraguai."),
            "wa_mensaje": "Olá MCG, vim pelo site e gostaria de fazer uma consulta",
            "wa_cta": "Falar pelo WhatsApp",
            "ig_cta": "Ver Instagram",
        },
    ],
}

# ----------------------------------------------------------------------- ERP
P["erp"] = {
    "slug": "implementacao-erp-contabil-paraguai.html",
    "nav": "ERP",
    "nav_footer": "Implantação de ERP",
    "service": "Implantação de ERP — módulo contábil",
    "title": "ERP contábil no Paraguai | Implantação do módulo contábil — MCG",
    "description": ("Implantação do módulo contábil de ERP no Paraguai: plano de contas, integração com estoque, "
                    "produção, compras e bancos, custeio e rastreabilidade auditável."),
    "h1": "Implantação de ERP: o módulo contábil como coração do sistema",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Implantação de ERP",
         "h1": "Implantação de ERP: o módulo contábil como coração do sistema",
         "lead": ("Especialidade de Cristina Rolón: deixar o módulo contábil bem parametrizado para que todo o resto "
                  "do ERP — tesouraria, logística, produção, compras, bancos — feche, seja rastreável e auditável."),
         "cta": "Fale com a gente"},
        {
            "type": "rich",
            "eyebrow": "O ponto de partida",
            "h2": "Por que o módulo contábil é a mãe de todos os outros módulos",
            "paragraphs": [
                ("Num ERP, tudo acaba impactando a contabilidade. Uma venda gera um lançamento; uma compra, um passivo "
                 "e um crédito fiscal de IVA (Imposto sobre o Valor Agregado); uma movimentação de estoque altera a "
                 "valorização do inventário; uma ordem de produção consome matéria-prima e gera custo; um recebimento "
                 "mexe na tesouraria e nos bancos. Se o <strong>módulo contábil</strong> estiver mal parametrizado, "
                 "todas essas movimentações são registradas de forma errada — ou simplesmente não são registradas — e o "
                 "resto do sistema passa a mostrar informação que não fecha."),
                ("Por isso uma implantação de ERP não se decide na tela bonita de cada módulo: ela se decide no plano de "
                 "contas, nas regras de contabilização automática, na valorização de estoque, nos centros de custo e na "
                 "forma como os livros auxiliares se integram ao razão geral. Quando isso é bem feito, a empresa obtém "
                 "demonstrações financeiras confiáveis sem trabalho manual paralelo; quando é mal feito, a equipe acaba "
                 "reconstruindo tudo em planilhas."),
                ("Cristina Rolón trabalha exatamente nesse ponto: entra no projeto de ERP pelo olhar contábil e "
                 "tributário, define como cada operação do negócio precisa ser registrada no Paraguai — incluindo as "
                 "exigências da DNIT (autoridade tributária do Paraguai, antiga SET) e da nota fiscal eletrônica — e "
                 "acompanha até que os fechamentos saiam do sistema, e não de um Excel."),
            ],
        },
        {
            "type": "cards",
            "alt": True,
            "eyebrow": "Integração",
            "h2": "Os módulos que dependem do coração contábil",
            "lead": ("Cada um destes módulos gera ou consome informação contábil. A implantação define como isso é "
                     "registrado, como é conciliado e como é auditado."),
            "columns": 3,
            "items": [
                ("Tesouraria e caixa", "Recebimentos, pagamentos, fundo fixo e conferência de caixa, com contabilização automática e conciliação contra os saldos contábeis."),
                ("Bancos e conciliação", "Extratos, cheques, transferências e conciliação bancária periódica, com as partidas pendentes identificadas."),
                ("Compras e contas a pagar", "Pedidos de compra, recebimento, nota do fornecedor e pagamento, com conferência de três vias e crédito fiscal de IVA corretamente apropriado."),
                ("Vendas e contas a receber", "Nota fiscal eletrônica, notas de crédito, recebimentos e idade dos saldos, integrados ao livro de vendas."),
                ("Estoque e logística", "Entradas, saídas, transferências entre depósitos e valorização de estoque, com impacto direto no custo das mercadorias vendidas."),
                ("Produção", "Ordens de produção, consumo de matéria-prima, mão de obra e gastos gerais de fabricação aplicados ao custo do produto acabado."),
                ("Expedição e remessas", "Notas de remessa e entregas vinculadas à nota fiscal e à movimentação de estoque, para que nada saia sem respaldo."),
                ("Ativo imobilizado", "Aquisições, baixas, depreciação e reavaliações, com seu impacto no resultado e nas demonstrações financeiras."),
                ("Custeio e rentabilidade", "Centros de custo, custeio por produto, linha ou projeto, e margem real por unidade de negócio."),
            ],
        },
        {
            "type": "checks",
            "eyebrow": "O resultado",
            "h2": "O que a empresa precisa conseguir fazer quando o ERP está bem implantado",
            "items": [
                "Emitir demonstração de resultado e balanço direto do sistema, sem montá-los à mão em planilhas.",
                "Ver a rentabilidade real por produto, linha de negócio, filial ou projeto, com os custos aplicados.",
                "Rastrear qualquer número para trás: do resultado ao lançamento, e do lançamento ao documento de origem.",
                "Conciliar bancos, estoque e contas correntes sem discussão sobre qual sistema tem razão.",
                "Fazer o fechamento mensal no prazo, com os livros auxiliares batendo contra o razão geral.",
                "Responder a uma fiscalização da DNIT mostrando a rastreabilidade completa a partir do sistema.",
                "Controlar acessos e manter registro de quem lançou, alterou ou aprovou cada movimentação.",
            ],
            "paragraphs": [
                ("Rastreabilidade e auditabilidade não são luxo: são o que permite que a direção confie nos números e "
                 "que uma auditoria externa, um banco ou a administração tributária consigam verificar o que a empresa "
                 "declara."),
            ],
        },
        {
            "type": "rich",
            "alt": True,
            "eyebrow": "Experiência",
            "h2": "Mais de 30 empresas implantadas, de 10 a mais de 700 funcionários",
            "paragraphs": [
                ("Cristina Rolón participou da implantação do módulo contábil de ERP em <strong>mais de 30 "
                 "empresas</strong> de portes e setores diferentes: de companhias pequenas, com cerca de 10 "
                 "funcionários, até organizações com <strong>mais de 700 funcionários</strong>, com várias filiais, "
                 "produção própria e estruturas de custo complexas."),
                ("Essa diferença de escala importa. Uma empresa de dez pessoas precisa de um sistema simples, com um "
                 "plano de contas administrável e processos que não a sufoquem; uma de setecentas precisa de centros de "
                 "custo, perfis de acesso por área, alçadas de aprovação e fechamentos coordenados entre várias equipes. "
                 "A implantação tem que ser do tamanho real da operação, não do tamanho do folheto do software."),
                ("Esse percurso também deixou uma leitura clara de onde os projetos costumam falhar: planos de contas "
                 "copiados de outra empresa, saldos iniciais migrados sem conciliação, módulos que são ativados sem "
                 "definir a contrapartida contábil, e treinamentos que ensinam a apertar botões, mas não a entender o "
                 "que cada botão registra."),
            ],
        },
        {
            "type": "pasos",
            "eyebrow": "Metodologia",
            "h2": "Como conduzimos uma implantação",
            "items": [
                ("Levantamento do negócio", "Entendemos o circuito real: o que acontece desde que entra um pedido até ele ser recebido e registrado."),
                ("Desenho do plano de contas", "Montagem ou redesenho do plano de contas e dos centros de custo conforme a direção precisa ler a informação."),
                ("Parametrização contábil", "Regras de contabilização automática, livros auxiliares, tratamento de IVA e retenções, valorização de estoque e critérios de custeio."),
                ("Migração e conciliação de saldos", "Carga dos saldos iniciais já conciliados, para que o sistema comece batendo e não arraste diferenças."),
                ("Testes integrados", "Simulação de operações reais de ponta a ponta, verificando o impacto contábil de cada módulo antes de entrar no ar."),
                ("Treinamento da equipe", "Capacitação por papel, para que cada área entenda o que o sistema registra quando ela opera e quais são as consequências."),
                ("Entrada em operação e acompanhamento", "Go-live, primeiro fechamento assistido e ajustes finos até as demonstrações financeiras saírem do ERP sem retoques."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Perguntas frequentes",
            "h2": "Sobre implantação de ERP no Paraguai",
            "items": [
                ("Vocês trabalham com um ERP específico ou com qualquer sistema?",
                 "O trabalho da MCG é o conteúdo contábil da implantação, não a venda de uma licença: plano de contas, regras de contabilização, critérios de valorização e custeio, tratamento de IVA e retenções, conciliações e fechamentos. Esse conteúdo se aplica ao ERP que a empresa já escolheu ou está avaliando, e é coordenado com o fornecedor do sistema e com a equipe de tecnologia."),
                ("Por que o módulo contábil precisa ser definido antes dos demais?",
                 "Porque todos os outros módulos acabam impactando nele. Se logística, produção ou tesouraria forem ativadas sem se ter definido como cada movimentação é contabilizada, o sistema passa a gerar registros incompletos ou mal classificados, e corrigi-los depois significa reprocessar meses de informação. Definir primeiro o coração contábil economiza exatamente esse retrabalho."),
                ("Dá para consertar uma implantação que já saiu errada?",
                 "Sim, e essa é uma parte importante do que fazemos. Começa por um diagnóstico: revisar o plano de contas, verificar se os livros auxiliares batem com o razão geral, revisar a valorização de estoque e os saldos migrados, e identificar quais movimentações estão sendo registradas de forma errada. Com isso se monta um plano de correção por prioridade, sem parar a operação."),
                ("O que é preciso para que o ERP seja auditável?",
                 "Que cada cifra possa ser rastreada até o documento de origem, que os acessos estejam definidos por perfil, que fique registro de quem lançou e aprovou cada operação, que os livros auxiliares batam contra o razão geral e que a documentação de respaldo esteja disponível. É isso que permite responder com solidez a uma auditoria externa, a um banco ou a uma fiscalização da DNIT."),
                ("Serve para uma empresa pequena ou só para empresas grandes?",
                 "Serve para as duas, com escopos diferentes. Uma empresa de dez pessoas precisa de um plano de contas simples e de processos leves que ainda assim deixem rastreabilidade; uma empresa de centenas de funcionários precisa de centros de custo, perfis de acesso, alçadas de aprovação e fechamentos coordenados. Já trabalhamos nos dois extremos, e o erro mais comum é aplicar o esquema de uma na outra."),
            ],
        },
        {"type": "cta", "h2": "Você está prestes a implantar ou corrigir um ERP?",
         "lead": "Conte em que etapa está o projeto e revisamos juntos.",
         "cta": "Fale com a gente"},
    ],
}
