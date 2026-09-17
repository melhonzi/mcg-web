# -*- coding: utf-8 -*-
"""English site content (localized for foreign investors researching Paraguay). Derived from content_es.py."""

DATA = {
    "lang": "en",
    "preview_banner": "Internal preview — not indexed — data subject to confirmation before publishing",
    "saltar": "Skip to content",
    "relacionados": "Keep exploring",
    "textos_form": {
        "formOk": "We received your enquiry and will reply to the email you left. If you would rather talk now, message us on WhatsApp.",
        "formWhatsapp": "We prepared your enquiry and opened WhatsApp in a new tab: check the message and press send there. If it did not open, use the button below.",
        "formIncompleto": "Please complete the required fields before continuing."
    },
    "nav_aria": "Main navigation",
    "menu_label": "Open menu",
    "lang_aria": "Change language",
    "cta_nav": "Talk to us",
    "logo_alt": "MCG Consultora Contable y Tributaria — accounting firm in Asunción, Paraguay, led by Cristina Rolón",
    "org_description": (
        "MCG Consultora Contable y Tributaria is an accounting firm based in Asunción, Paraguay, "
        "led by Certified Public Accountant Cristina Rolón. The firm provides business accounting, "
        "tax strategy before DNIT (Paraguay's tax authority), company formation (EAS, SRL and SA) and "
        "hands-on support for foreign business owners and investors setting up in Paraguay."
    ),
    "person_jobtitle": "Certified Public Accountant · Master's in Taxation · Director of MCG Consultora Contable y Tributaria",
    "person_description": (
        "Cristina Rolón is a Certified Public Accountant who graduated from the Universidad Nacional de Asunción "
        "(National University of Asunción) in 2008, holds a Master's in Taxation and directs MCG Consultora Contable "
        "y Tributaria in Asunción, Paraguay, with 18 years of professional experience in business accounting and tax strategy."
    ),
    "person_knows": [
        "Business accounting in Paraguay", "Tax strategy", "Corporate income tax (IRE)",
        "Value added tax (IVA)", "DNIT", "Company formation in Paraguay",
        "Foreign investment in Paraguay", "Electronic invoicing (SIFEN)",
        "ERP implementation", "ERP accounting module", "Costing and profitability analysis",
        "Bank reconciliation", "Accounting traceability and auditability",
    ],
    "footer": {
        "tagline": ("Business accounting and tax strategy in Paraguay, under the direction of "
                    "Cristina Rolón, Certified Public Accountant (UNA) and holder of a Master's in Taxation."),
        "ciudad": "Asunción, Paraguay · We work in Spanish, English and Portuguese",
        "col_servicios": "Services",
        "col_estudio": "The firm",
        "col_contacto": "Contact",
        "wa_mensaje": "Hi MCG, I'm visiting from your website and I'd like to ask a question",
        "copyright": "MCG Consultora Contable y Tributaria. All rights reserved.",
        "legal": ("General informational content about Paraguayan regulations; it does not replace a professional "
                  "assessment of each individual case."),
    },
    "pages": {},
}

P = DATA["pages"]

# ---------------------------------------------------------------------- HOME
P["home"] = {
    "slug": "index.html",
    "nav": "Home",
    "nav_footer": "Home",
    "title": "Accounting Firm in Paraguay | Business Accounting & Tax Strategy",
    "description": ("Accounting firm in Asunción, Paraguay: business accounting, tax strategy before DNIT, company "
                    "formation and support for foreign investors. Led by CPA Cristina Rolón."),
    "h1": "Business accounting and tax strategy in Paraguay",
    "blocks": [
        {
            "type": "hero",
            "chip": "Accounting and tax consultancy · Asunción, Paraguay",
            "h1_html": "Business accounting and <span class=\"acento\">tax strategy</span> in Paraguay",
            "lead": ("We guide companies and investors through their accounting, tax and market-entry decisions in "
                     "Paraguay, with reliable information and professional judgment."),
            "firma_html": ("Under the direction of <strong>Cristina Rolón</strong>, Certified Public Accountant "
                           "(Universidad Nacional de Asunción), holder of a Master's in Taxation and a member of "
                           "corporate boards, backed by a stable team."),
            "cta1": "Talk to us",
            "cta2": "See our services",
            "cta2_href": "#servicios",
            "credenciales": [
                ("18 years", "of professional experience"),
                ("Certified Public Accountant", "Universidad Nacional de Asunción"),
                ("Master's degree", "in Taxation"),
                ("30+ companies", "with the ERP accounting module implemented"),
            ],
            "figura_alt": ("Cristina Rolón, Certified Public Accountant and director of MCG Consultora Contable y "
                           "Tributaria, an accounting firm in Asunción, Paraguay"),
            "figura_nombre": "Cristina Rolón",
            "figura_rol": "Director of MCG · Certified Public Accountant · Master's in Taxation",
        },
        {
            "type": "franja",
            "items": [
                "Companies that need to get their accounting and tax position in Paraguay in order",
                "Foreign business owners and investors who want to set up operations in Paraguay",
                "Companies of any size and any industry looking for a serious, meticulous accounting firm",
                "Owners and managers who need reliable information to make decisions",
            ],
            "microcopy": ("We work with companies of every size: what we define together is the scope of the service, "
                          "not a minimum revenue threshold."),
        },
        {
            "type": "caminos",
            "items": [
                {"badge": "I already have a company", "h3": "I already have a company in Paraguay",
                 "p": ("I need reliable accounting, tax planning before DNIT (Paraguay's tax authority) and strategic "
                       "support so I can make better decisions."),
                 "cta": "See business accounting →", "target": "contabilidad"},
                {"badge": "I want to set up here", "h3": "I want to set up my company in Paraguay",
                 "p": ("I am a foreigner or an investor and I need local support to form the company, obtain the RUC "
                       "(tax ID) and operate in full compliance from day one."),
                 "cta": "See support for foreign investors →", "target": "extranjeros"},
            ],
        },
        {
            "type": "rich",
            "alt": True,
            "eyebrow": "Who we are",
            "h2": "A trusted accounting firm in Asunción, Paraguay",
            "paragraphs": [
                ("MCG Consultora Contable y Tributaria is an accounting firm based in Asunción that works with "
                 "Paraguayan companies and with foreign investors who choose Paraguay to launch or expand their "
                 "business. The firm is led by <strong>Cristina Rolón</strong>, a Certified Public Accountant who "
                 "graduated from the Universidad Nacional de Asunción (National University of Asunción) in 2008, "
                 "holds a Master's in Taxation and brings 18 years of professional experience across a range of "
                 "industries."),
                ("Our work does not end with filing returns on time. Accounting done properly in Paraguay should do "
                 "more than that: it should tell you how much each business line actually earns, let you anticipate "
                 "the impact of IRE (corporate income tax) and IVA (VAT) before the filing deadline arrives, support "
                 "a conversation with your bank using numbers that hold up, and let you sleep at night if DNIT asks "
                 "for explanations tomorrow."),
                ("That is why we combine three things for every company we serve: meticulous compliance before DNIT, "
                 "organized and timely information for management, and a preventive tax perspective that avoids "
                 "surprises. That is the standard we work to, and it defines the kind of trust we aim to build with "
                 "every client."),
            ],
        },
        {
            "type": "problemas",
            "eyebrow": "Problems we solve",
            "h2": "When your accounting does not help you decide",
            "lead": "These are the situations companies most often bring to us before they start working with us.",
            "items": [
                "Accounting information that arrives late, or that does not support real decisions.",
                "No visibility into the period's tax liabilities or their filing deadlines before DNIT.",
                "Disconnect between bank transactions, electronic invoicing and accounting records.",
                "Fast growth with no internal controls and insufficient supporting documentation.",
                "Prior periods never filed, or filings that now need to be corrected.",
                "A foreigner's uncertainty about how to legally form and operate a business in Paraguay.",
            ],
            "paragraphs": [
                ("None of these problems is solved by a single return filed at the last minute. They are solved by "
                 "organizing the whole process: what documentation comes in, how it is recorded, what gets reviewed "
                 "each month and what information reaches management so decisions can be made."),
            ],
        },
        {
            "type": "cards",
            "alt": True,
            "eyebrow": "Services",
            "h2": "What we do at MCG",
            "lead": ("Five services designed to cover a company's full life cycle in Paraguay: from formation through "
                     "orderly day-to-day operations, systems and tax strategy."),
            "columns": 2,
            "items": [
                ("Business accounting",
                 "Monthly bookkeeping, compliance with DNIT obligations, period closings and regular reports so management can decide with reliable information."),
                ("Tax strategy",
                 "A diagnostic review of your tax position, identification of contingencies, planning of obligations and an action plan with clear priorities."),
                ("Company formation",
                 "Choosing the right legal structure (EAS, SRL or SA), coordinating the incorporation process, obtaining the RUC (tax ID) from DNIT and setting up the accounting."),
                ("Foreign business owners",
                 "Local support to establish and run a company in Paraguay: the entity, documentation, immigration coordination and accounting from day one."),
                ("ERP implementation — accounting module",
                 "Setting up the accounting core of the ERP and its integration with treasury, logistics, production, purchasing and banking, with costing and an auditable trail."),
            ],
        },
        {
            "type": "pasos",
            "eyebrow": "How we work",
            "h2": "A clear process from the very first conversation",
            "items": [
                ("We talk about your company", "We get to know your industry, your current operation, the state of your documentation and what you need to solve first."),
                ("We review the real situation", "We look at the condition of your records, your filings before DNIT and your supporting documentation."),
                ("We present a proposal", "With scope, fees and terms in writing — no hidden costs and no services you did not ask for."),
                ("We coordinate onboarding", "We organize the handover from your previous accountant, or start from scratch, and begin as agreed."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Frequently asked questions",
            "h2": "Before you write to us",
            "ver_todas": "See all 28 frequently asked questions about taxes and companies in Paraguay →",
            "items": [
                ("Do you work with companies of any size?",
                 "Yes. We work with all kinds of companies in Paraguay: businesses already billing significant volumes, ventures that are just getting started, and companies that need to clean up prior periods. What we define in each case is the scope of the service, based on the real complexity of the operation — industry, volume of invoices, employees, branches, imports and the state of the documentation — not a minimum revenue threshold."),
                ("How much does it cost to work with MCG?",
                 "Fees depend on the scope and the complexity of your operation. The factors that matter are your industry, the volume of electronic invoices, the number of employees, branch locations, whether there are imports or exports, and the condition of your documentation. Once we understand your company, we present a concrete written proposal with the scope spelled out before any work begins."),
                ("Do you work with foreign business owners and investors?",
                 "Yes, and it is a significant part of our practice. We support foreigners who want to establish and operate a company in Paraguay: choosing the legal structure, incorporation, obtaining the RUC (tax ID) from DNIT, preparing banking documentation, coordinating with immigration professionals, and handling the accounting from day one. We work in Spanish, English and Portuguese."),
                ("What if I have overdue filings with DNIT?",
                 "It is more common than you would think, and it can be fixed. We start with a diagnostic review of the real situation: which periods are missing, what documentation exists and which filings were left pending. From there we build a remediation plan, quoted separately from the monthly service because it is a distinct one-off engagement. The sooner it is addressed, the lower the risk of accumulating contingencies."),
                ("Is the first conversation free?",
                 "Yes. The initial inquiry lets us understand your situation and assess fit and the possible scope of the work. If a deeper technical review or a full tax diagnostic is needed, that is quoted separately and agreed before any work starts."),
            ],
        },
        {
            "type": "opiniones",
            "eyebrow": "Reviews",
            "h2": "What our clients say",
            "lead": "Reviews from the companies that work with MCG are published on our Google Business profile, where anyone can verify them and leave their own.",
            "cta": "Read our Google reviews",
            "reseñas": [],
        },
        {
            "type": "cta",
            "h2": "Let's talk about your company",
            "lead": "Tell us about your situation and we will assess the scope of the work together.",
            "cta": "Talk to us",
        },
    ],
}

# -------------------------------------------------------------- CONTABILIDAD
P["contabilidad"] = {
    "slug": "business-accounting-paraguay.html",
    "nav": "Accounting",
    "nav_footer": "Business accounting",
    "service": "Business accounting",
    "title": "Business Accounting in Paraguay | Monthly Accounting Services",
    "description": ("Business accounting in Paraguay: bookkeeping, IVA and IRE filings before DNIT, closings and "
                    "management reports. Accounting firm in Asunción led by a CPA."),
    "h1": "Business accounting in Paraguay, built for decision-making",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Business accounting",
         "h1": "Business accounting in Paraguay, built for decision-making",
         "lead": ("Orderly compliance before DNIT (Paraguay's tax authority) and better information, so your "
                  "management team can decide with numbers it can trust."),
         "cta": "Talk to us"},
        {
            "type": "rich",
            "eyebrow": "The service",
            "h2": "What it really means to keep a company's books properly in Paraguay",
            "paragraphs": [
                ("Keeping a company's books in Paraguay involves far more than entering invoices and filing returns. "
                 "It means maintaining records consistent with Law 6380/2019 (Ley 6380/2019), correctly calculating "
                 "IVA (VAT) and IRE (corporate income tax) under the regime that applies to the company, complying "
                 "with electronic invoicing through the SIFEN system, reconciling bank transactions against the "
                 "records, and keeping supporting documentation organized in case DNIT requests it."),
                ("At MCG we do that work with a simple standard: the accounting has to hold up externally — before "
                 "the tax authority — and internally — before the company's management. If the numbers only serve to "
                 "meet a filing deadline but never tell the owner what margin each business line generates or why "
                 "costs rose this quarter, the job is only half done."),
                ("We work with companies across every industry: retail and wholesale, services, construction, import, "
                 "technology, healthcare, food service and foreign investment projects. Each industry has its own tax "
                 "particularities, and that is part of what we assess before defining the scope."),
            ],
        },
        {
            "type": "cards",
            "alt": True,
            "eyebrow": "Proposed scope",
            "h2": "What the monthly accounting service includes",
            "lead": "This is the reference scope. The final scope for each company is defined by its actual operation.",
            "columns": 3,
            "items": [
                ("Monthly bookkeeping", "Recording and maintaining the accounting for the entire operation, with consistent criteria period after period."),
                ("Tax obligations", "Preparation and filing of the applicable obligations before DNIT, with deadline control based on your RUC (tax ID)."),
                ("Closings and periodic reports", "Period closings with reports showing results, margins and trends, in a format management can actually read."),
                ("Reconciliations", "Reconciliation of bank transactions, electronic invoicing and accounting records, according to the plan contracted."),
                ("Documentation follow-up", "Organizing and controlling supporting documentation — the first thing requested in a tax audit."),
                ("DNIT coordination", "Handling filings, queries and communications with the tax authority on the company's behalf."),
            ],
        },
        {
            "type": "checks",
            "eyebrow": "What changes in your company",
            "h2": "What you should be able to do once the accounting is in order",
            "items": [
                "Know how the period's result is shaping up, without waiting for the year-end close.",
                "Anticipate how much IVA (VAT) and IRE (corporate income tax) you will owe before the deadline arrives.",
                "Respond quickly when a bank asks for financial statements or supporting documentation.",
                "Know exactly which invoices are missing and who needs to obtain them.",
                "Enter a DNIT tax audit with your documentation in order, without improvising.",
                "Discuss business decisions with your accountant, not just filing deadlines.",
            ],
        },
        {
            "type": "planes",
            "eyebrow": "Service levels",
            "h2": "Two ways to work with us",
            "items": [
                {"badge": "Business accounting", "valor": "Custom quote", "destacado": True,
                 "p": "Orderly accounting and tax management, for companies of any size and any industry in Paraguay.",
                 "checks": ["Monthly bookkeeping and compliance before DNIT",
                            "Period closings and regular reports",
                            "Documentation follow-up and coordination with the tax authority"],
                 "cta": "Ask about this plan"},
                {"badge": "Accounting with strategic advisory", "valor": "Custom proposal",
                 "p": "For more complex operations, with continuous strategic support for the management team.",
                 "checks": ["Everything included in the business accounting service",
                            "Strategic review meetings with management",
                            "Preventive tax analysis and support on key decisions"],
                 "cta": "Ask about this plan"},
            ],
            "paragraphs": [
                ("Fees are set according to scope and operational complexity: industry, volume of invoices, number of "
                 "employees, branch locations and the condition of the documentation, among other factors. Remediation "
                 "of prior periods, audits and extraordinary engagements are quoted separately and are always agreed "
                 "in writing before they are invoiced."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Frequently asked questions",
            "h2": "About the accounting service",
            "ver_todas": "See all frequently asked questions about taxes and companies in Paraguay →",
            "items": [
                ("How often does a company in Paraguay have to file tax returns?",
                 "It depends on the tax and the regime. IVA (VAT) is calculated and filed monthly; IRE (corporate income tax) has an annual return, with advance payments depending on the regime; and there are additional informational filings depending on the activity. Deadlines follow DNIT's calendar based on the last digit of your RUC (tax ID), and part of our service is maintaining a dedicated deadline calendar for each company."),
                ("Can I change accountants in the middle of the year?",
                 "Yes, and it happens often. What matters is organizing the handover: establishing which periods have been filed, obtaining the files and supporting records from the previous accountant, verifying opening balances and identifying anything left pending before DNIT before moving forward. We always perform that initial review, because starting without knowing the true starting point creates problems later on."),
                ("Does the service include payroll?",
                 "Payroll processing and labor obligations are assessed case by case and included in the scope where appropriate. When we define the proposal we state explicitly what is included and what is quoted separately, so there is no ambiguity afterwards."),
                ("What happens if DNIT audits my company?",
                 "We support the company throughout the process: we organize and submit the required documentation, respond to formal requests within the deadlines, and coordinate with any other professionals needed depending on the scope of the audit. No serious firm can promise there will be no adjustments; what can be done is to arrive with records and supporting documentation in proper condition, which is exactly what reduces the risk."),
            ],
        },
        {"type": "cta", "h2": "Let's get your company's accounting in order",
         "lead": "Tell us about your current situation and we will assess the scope together.",
         "cta": "Talk to us"},
    ],
}

# ---------------------------------------------------------------- TRIBUTARIA
P["tributaria"] = {
    "slug": "tax-strategy-paraguay.html",
    "nav": "Tax strategy",
    "nav_footer": "Tax strategy",
    "service": "Tax strategy and planning",
    "title": "Tax Strategy in Paraguay | Tax Advisor & DNIT Risk Review — MCG",
    "description": ("Paraguay tax advisor: tax diagnostic, contingency review and action plan for companies. IRE, "
                    "IVA and IDU planning before DNIT, from an accounting firm in Asunción."),
    "h1": "Tax strategy and risk prevention in Paraguay",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Tax strategy",
         "h1": "Tax strategy and risk prevention in Paraguay",
         "lead": ("We organize your company's tax position before DNIT (Paraguay's tax authority), identify "
                  "contingencies and build an action plan with clear priorities."),
         "cta": "Talk to us"},
        {
            "type": "rich",
            "eyebrow": "The approach",
            "h2": "Plan in advance instead of explaining afterwards",
            "paragraphs": [
                ("Most of the tax problems we see in Paraguay do not come from an aggressive decision: they come from "
                 "a lack of review. Invoices that do not support what was deducted, a tax regime chosen years ago "
                 "that no longer matches the company's current size, balances that were never reconciled, profit "
                 "withdrawals made without considering IDU (the tax on dividends and profits), or payments abroad "
                 "made without analyzing INR (non-resident income tax)."),
                ("A serious tax strategy starts by knowing exactly where the company stands: which taxes apply to it "
                 "under Law 6380/2019 (Ley 6380/2019), which IRE (corporate income tax) regime it is registered "
                 "under, which contingencies it carries over from prior periods, and which upcoming decisions — an "
                 "investment, a profit distribution, opening a branch, bringing in a new partner — will have a tax "
                 "impact."),
                ("With that map we build an action plan with priorities: what must be corrected now, what can wait "
                 "until the next closing and what requires a decision from the owner. We do not promise the absence "
                 "of audits or adjustments — nobody can promise that. We work so that, if they come, the company is "
                 "in a position to respond with documentation and sound reasoning."),
            ],
        },
        {
            "type": "checks",
            "alt": True,
            "eyebrow": "What we review",
            "h2": "What the tax diagnostic covers",
            "items": [
                "The company's current tax position and the IRE (corporate income tax) regime it is registered under.",
                "Contingencies in open periods and the consistency of returns already filed with DNIT.",
                "Supporting documentation for costs, expenses and IVA (VAT) input credits.",
                "Consistency between accounting records, bank transactions and electronic invoicing (SIFEN).",
                "Treatment of withdrawals, dividends and profits (IDU) and of payments abroad (INR).",
                "Planning of obligations and filing deadlines for the following fiscal year.",
                "Legal alternatives applicable to your specific case, with their estimated impact.",
            ],
        },
        {
            "type": "cards",
            "eyebrow": "Deliverables",
            "h2": "What you receive when the diagnostic is complete",
            "columns": 2,
            "items": [
                ("Executive report", "A clear summary of the situation, written so management can understand it — not just an accountant."),
                ("Risk and priority map", "Which contingencies exist, what their estimated exposure is and in what order they should be addressed."),
                ("Concrete recommendations", "Alternatives that apply to your case, with what each one implies in terms of work and impact."),
                ("Implementation roadmap", "Steps, owners and sequence to put the plan into action without disrupting the operation."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Frequently asked questions",
            "h2": "About tax strategy and risk protection",
            "ver_todas": "See all frequently asked questions about taxes and companies in Paraguay →",
            "items": [
                ("What does \"tax shielding\" mean in Paraguay?",
                 "In everyday use, \"shielding\" refers to organizing the corporate structure, the documentation and tax compliance in order to reduce avoidable risks: choosing the right legal structure and IRE (corporate income tax) regime, keeping the books up to date, separating personal assets from company assets, supporting every deduction and filing correctly and on time before DNIT (Paraguay's tax authority). No serious firm can promise immunity from tax audits or eliminate risk entirely: what can be done is to work preventively and meticulously to minimize unnecessary exposure."),
                ("Does the diagnostic replace monthly accounting?",
                 "No. The diagnostic is a one-off review and planning engagement with its own deliverables. Monthly accounting is a separate, ongoing service. Many companies start with the diagnostic to understand where they stand and then decide whether to also move their monthly accounting to us."),
                ("How long does a tax diagnostic take?",
                 "It depends on the volume of information, the number of periods to review and how readily available the documentation is. A company with organized records and complete digital files moves much faster than one that has to rebuild its supporting documentation. When we assess your case we give you a concrete timeline before starting."),
                ("Is it worth it for a company that is just starting out?",
                 "Yes, and that is usually the best moment. Defining the legal structure, the correct tax regime, how expenses will be documented and how profits will be withdrawn — all from the outset — avoids having to correct things years later, when correcting costs far more."),
            ],
        },
        {"type": "cta", "h2": "Let's get your company's tax position in order",
         "lead": "We start with a conversation about your current operation.",
         "cta": "Talk to us"},
    ],
}

# ---------------------------------------------------------------- SOCIEDADES
P["sociedades"] = {
    "slug": "company-formation-paraguay.html",
    "nav": "Company formation",
    "nav_footer": "Company formation",
    "service": "Company formation",
    "title": "Company Formation in Paraguay | Open a Company: EAS, SRL or SA",
    "description": ("Open a company in Paraguay: choosing between EAS, SRL and SA, the incorporation process, RUC "
                    "registration with DNIT and accounting setup. Guided from Asunción."),
    "h1": "Company formation in Paraguay: EAS, SRL or SA",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Company formation",
         "h1": "Company formation in Paraguay: EAS, SRL or SA",
         "lead": ("We assess your activity, your partners and your objectives before recommending a structure, and "
                  "we guide the process until the company is fully operational."),
         "cta": "Talk to us"},
        {
            "type": "rich",
            "eyebrow": "The underlying decision",
            "h2": "Which legal structure makes sense in Paraguay",
            "paragraphs": [
                ("Several legal structures coexist in Paraguay, and three account for most cases. The "
                 "<strong>EAS (Empresa por Acciones Simplificada, or simplified stock company)</strong> was designed "
                 "to simplify company creation: it allows incorporation with a flexible structure and is the fastest "
                 "route for startups and small and mid-sized businesses. The <strong>SRL (Sociedad de "
                 "Responsabilidad Limitada, or limited liability company)</strong> is the traditional vehicle for "
                 "businesses with few partners and simple governance, where ownership is represented by membership "
                 "quotas rather than shares. The <strong>SA (Sociedad Anónima, or corporation)</strong> is the usual "
                 "choice for larger operations: it allows shares to be issued, investors to be brought in and a more "
                 "formal governance structure to be maintained — something banks, institutional partners and foreign "
                 "investment projects often require."),
                ("There is no structure that is always the best one. The right choice depends on how many partners "
                 "there are and how they join or exit, on whether investors are planned, on the type of activity and "
                 "on the kind of counterparties the company will work with. A project that will bid on public tenders "
                 "or seek significant bank financing is not structured the same way as a family business."),
                ("We carry out that analysis before starting any filing, because changing structures later means "
                 "cost, time and, in some cases, tax consequences that can be avoided by deciding well at the "
                 "beginning."),
            ],
        },
        {
            "type": "cards",
            "alt": True,
            "eyebrow": "What is included",
            "h2": "Support through the entire process",
            "columns": 3,
            "items": [
                ("Initial assessment", "We analyze the activity, the partners, the objectives and the growth plans before suggesting a structure."),
                ("Incorporation coordination", "We guide the corporate process end to end and coordinate with a notary public where required."),
                ("Document organization", "We organize and review each partner's documentation, including that of foreign partners."),
                ("Registration with DNIT", "RUC (tax ID) registration, definition of the applicable tax regime and registration of obligations."),
                ("Electronic invoicing", "Setting up the electronic invoicing scheme so the company can issue compliant invoices."),
                ("Accounting kickoff", "The company begins operating with its accounting in order from the very first transaction."),
            ],
        },
        {
            "type": "pasos",
            "eyebrow": "The process",
            "h2": "What it takes to open a company in Paraguay",
            "items": [
                ("Defining the structure", "We choose the legal structure, the corporate purpose, the capital and how it is distributed among partners."),
                ("Gathering documentation", "Identification for each partner, corporate documents and, where there are foreign partners, legalizations or apostilles."),
                ("Incorporation and registration", "The incorporation deed is formalized and the corresponding registry filings are completed."),
                ("RUC and tax obligations", "Registration with DNIT, definition of the IRE (corporate income tax) regime and the obligations that apply to the company."),
                ("Permits and invoicing", "Municipal business license depending on the activity, and launch of electronic invoicing."),
                ("Accounting setup", "Opening the books, setting accounting criteria and building the company's own deadline calendar."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Frequently asked questions",
            "h2": "About opening a company in Paraguay",
            "ver_todas": "See all frequently asked questions about taxes and companies in Paraguay →",
            "items": [
                ("How long does it take to form a company in Paraguay?",
                 "It depends on the legal structure chosen, on the current workload at the registries and notary offices involved and, above all, on how complete the documentation is from the outset. When there are foreign partners whose documents must be legalized or apostilled abroad, that is usually the step that drives the timeline. The EAS is generally the fastest structure to set up, thanks to its simplified design."),
                ("Can a foreigner be a partner or shareholder in a Paraguayan company?",
                 "Yes. Paraguayan law permits foreign partners and shareholders, both individuals and legal entities. What differs from a local partner is the documentation: documents legalized or apostilled in the country of origin are required and, for foreign legal entities, the corporate documentation of the parent company must be duly translated and legalized."),
                ("How much capital do I need to open a company in Paraguay?",
                 "Share capital is defined according to the legal structure chosen and the type of activity, and it must be proportionate to the operation the company will actually carry out. This is one of the items we review in the initial assessment, because it has practical consequences: banks, counterparties and public agencies tend to look at that figure."),
                ("Can I incorporate without traveling to Paraguay?",
                 "In many cases a large part of the process can be advanced remotely, using special powers of attorney granted in your country of origin and duly legalized or apostilled, which authorize a local representative to sign the corporate documentation. Certain specific steps, such as opening a bank account or some immigration procedures, usually require physical presence or at least more direct involvement."),
            ],
        },
        {"type": "cta", "h2": "Let's assess the right structure for your company",
         "lead": "Tell us about your activity and your objectives so we can guide you properly.",
         "cta": "Talk to us"},
    ],
}

# --------------------------------------------------------------- EXTRANJEROS
P["extranjeros"] = {
    "slug": "foreign-investors-paraguay.html",
    "nav": "Foreign investors",
    "nav_footer": "Foreign business owners",
    "service": "Support for foreign investors",
    "title": "Move My Business to Paraguay | Taxes & Residency for Foreigners",
    "description": ("Move your business to Paraguay with local support: incorporation, RUC with DNIT, banking "
                    "documents, residency by investment coordination and accounting. In English."),
    "h1": "Set up and run your company in Paraguay with local support",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Foreign business owners and investors",
         "h1": "Set up and run your company in Paraguay with local support",
         "lead": ("We work with foreigners who genuinely want to operate or invest in Paraguay — not just process "
                  "personal paperwork."),
         "cta": "Talk to us"},
        {
            "type": "rich",
            "eyebrow": "Why Paraguay",
            "h2": "What a foreign investor looks at when evaluating Paraguay",
            "paragraphs": [
                ("Paraguay comes up frequently in the evaluations of business owners from Brazil, Argentina, the "
                 "United States and Europe, for a set of concrete reasons: comparatively low tax rates within the "
                 "region — 10% IRE (corporate income tax) and 10% IVA (VAT) as general rates, with a reduced 5% IVA "
                 "for certain goods and services — a relatively simple tax system since Law 6380/2019 (Ley "
                 "6380/2019), competitive operating costs, and a residency regime linked to investment."),
                ("None of this means zero taxes or automatic benefits, and you should be skeptical of anyone who "
                 "frames it that way. Each company's real tax burden depends on its regime, its industry, its "
                 "corporate structure and how it withdraws profits. A project that is well structured from the start "
                 "makes good use of the legal framework; an improvised one ends up paying to fix it later."),
                ("Our work is the Paraguayan side of the project: making sure the company is properly incorporated, "
                 "correctly registered with DNIT (Paraguay's tax authority), that the accounting starts out organized "
                 "and that the documentation is in order for banks and counterparties. Any obligations the investor "
                 "retains in their home country require coordination with specialists in that jurisdiction."),
            ],
        },
        {
            "type": "pasos",
            "alt": True,
            "eyebrow": "The path",
            "h2": "How we support your setup in Paraguay",
            "items": [
                ("Project assessment", "We get to know your activity, your objectives, your existing structure abroad and your starting point."),
                ("Structure and incorporation", "We define the appropriate legal structure and coordinate the incorporation process in Paraguay."),
                ("Registration with DNIT", "RUC (tax ID) registration, the applicable tax regime and registration of the obligations that apply."),
                ("Immigration coordination", "With qualified professionals in that field, based on your situation and the type of residency you are seeking."),
                ("Banking documentation", "We prepare the documentation you need for account opening and financing applications."),
                ("Accounting and operations", "The company starts with its accounting in order, and we keep supporting the operation month after month."),
            ],
        },
        {
            "type": "rich",
            "eyebrow": "Residency and investment",
            "h2": "Residency by investment, Paraguayan ID card and RUC: three different things",
            "paragraphs": [
                ("This is the most common confusion and it is worth clearing up early. <strong>Residency</strong> is "
                 "an immigration status held by an individual: it allows you to live and remain legally in Paraguay. "
                 "There is a residency regime linked to investment, processed through SUACE, which requires an "
                 "investment certificate issued by the Ministry of Industry and Commerce, along with personal and "
                 "corporate documentation."),
                ("The <strong>Paraguayan identity card (cédula)</strong> is the document obtained once residency has "
                 "been granted, and it makes day-to-day life vastly simpler: banking, signing before a notary and "
                 "dealings with government agencies. The <strong>RUC (tax ID)</strong>, by contrast, is the tax "
                 "registration with DNIT: the company holds one, and an individual carrying out taxable activity can "
                 "hold one too."),
                ("A company can be formed and operated in Paraguay with partners who do not reside in the country; "
                 "what needs to be clearly defined in that case is local legal representation, the powers of attorney "
                 "granted and who handles day-to-day signing authority. And obtaining residency in Paraguay does not "
                 "by itself eliminate obligations a person may have in their country of origin: that has to be "
                 "analyzed with a specialist in that jurisdiction."),
            ],
        },
        {
            "type": "checks",
            "alt": True,
            "eyebrow": "Important points",
            "h2": "What you should be clear about from the start",
            "items": [
                "Immigration residency and tax position are distinct matters, even though they are related.",
                "Obtaining residency or forming a company in Paraguay does not eliminate obligations in your home country.",
                "Approval of bank accounts and financing is subject to each institution's own assessment.",
                "Distributing profits abroad has its own tax treatment (IDU) and should be projected from the outset.",
                "We handle the Paraguayan side of the project; your home jurisdiction is coordinated with specialists there.",
                "We work in Spanish, English and Portuguese, so the operation never depends on improvised translation.",
            ],
        },
        {
            "type": "faq",
            "eyebrow": "Frequently asked questions",
            "h2": "About investing and setting up in Paraguay",
            "ver_todas": "See all frequently asked questions about taxes and companies in Paraguay →",
            "items": [
                ("How do I move my business to Paraguay?",
                 "In practical terms a foreign company is not relocated as such: the usual route is to form a Paraguayan company (EAS, SRL or SA) or register a branch of the foreign entity, depending on the project. Next comes RUC (tax ID) registration with DNIT, the municipal business license if the activity requires it, opening a bank account, and setting up the accounting and electronic invoicing. In parallel, the immigration status of the people involved is resolved if they will be living in the country."),
                ("Can I manage my Paraguayan company from abroad?",
                 "Yes, it is a common arrangement. You can be a partner or shareholder in a Paraguayan company without residing in the country, as long as local legal representation and the powers of attorney granted are properly defined. Accounting, electronic invoicing and filings before DNIT are handled remotely with a trusted local team — which is precisely the role we play for clients operating from abroad."),
                ("What taxes does a foreign-owned company operating in Paraguay pay?",
                 "A company incorporated in Paraguay is taxed like any local company: IRE (corporate income tax) on its profits, IVA (VAT) on its transactions and any specific taxes that apply to its activity. On top of that comes IDU when it distributes profits to its partners, at a higher rate when the beneficiary is not a resident, and INR (non-resident income tax) on certain Paraguayan-source income paid abroad. The structure used to set up the project directly influences that burden."),
                ("Do you work in Portuguese and English?",
                 "Yes. A significant share of the investors arriving in Paraguay are Brazilian, and we also work with English-speaking clients. This site is available in Spanish, English and Portuguese, and we coordinate service in whichever language the client finds most comfortable."),
            ],
        },
        {"type": "cta", "h2": "Let's talk about your project in Paraguay",
         "lead": "Tell us what stage you are at and what you need to solve first.",
         "cta": "Talk to us"},
    ],
}

# -------------------------------------------------------------------- EQUIPO
P["equipo"] = {
    "slug": "cristina-rolon-accountant-paraguay.html",
    "nav": "Team",
    "nav_footer": "Leadership and team",
    "title": "Cristina Rolón, Accountant in Asunción | Director of MCG Consultora",
    "description": ("Cristina Rolón, CPA (National University of Asunción, 2008) and Master's in Taxation, is the "
                    "accountant in Asunción who leads MCG, with 18 years of experience."),
    "h1": "Cristina Rolón, Certified Public Accountant and director of MCG",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Leadership and team",
         "h1": "Cristina Rolón, Certified Public Accountant and director of MCG",
         "lead": ("Technical leadership that understands how companies actually decide: tax training, professional "
                  "practice and experience on corporate boards in Paraguay.")},
        {
            "type": "bio",
            "h2": "Background",
            "nombre": "Cristina Rolón",
            "cargo": "Director of MCG · Certified Public Accountant · Master's in Taxation",
            "foto_alt": ("Cristina Rolón, Certified Public Accountant and director of MCG Consultora Contable y "
                         "Tributaria, at the firm's offices in Asunción, Paraguay"),
            "trayectoria": [
                "Certified Public Accountant, graduated from the Universidad Nacional de Asunción (National University of Asunción), 2008",
                "Master's in Taxation, with additional specializations in tax matters",
                "18 years of professional experience across a range of industries",
                "Specialist in implementing the accounting module of ERP systems, with more than 30 companies implemented",
                "Experience in organizations ranging from 10 to more than 700 employees",
                "Member of corporate boards",
                "Director of MCG Consultora Contable y Tributaria, in Asunción, Paraguay",
            ],
            "paragraphs": [
                ("That board-level experience gives Cristina a direct read on how companies evaluate information, "
                 "prioritize risks and make decisions — something she carries into the judgment with which she leads "
                 "MCG and into the kind of reports the firm delivers to its clients."),
            ],
        },
        {
            "type": "rich",
            "alt": True,
            "eyebrow": "Her story",
            "h2": "Where the discipline behind her work comes from",
            "paragraphs": [
                ("Cristina is a Certified Public Accountant, a 2008 graduate of the Universidad Nacional de Asunción "
                 "(National University of Asunción). Before founding MCG she worked across several industries that "
                 "shaped how she works: each one taught her to look at numbers in context, understanding the business "
                 "behind every figure. She later completed additional specializations and a Master's in Taxation, "
                 "always seeking to go deeper and to meet the challenges her clients bring."),
                ("That same demanding standard led her, for a stretch of her life, to compete in bodybuilding. "
                 "Preparing to step on stage is not a one-day effort: it means training for years for a result "
                 "measured in minutes, holding a routine when nobody is watching, and adjusting the method when "
                 "something is not working. Cristina applies that same logic — consistency, method and constant "
                 "review — to the accounting and tax strategy of every company she serves."),
                ("She defines herself by perseverance, the depth of her technical knowledge and a genuine desire to "
                 "contribute to every company she works with. Her motto is simple: leave something built where you "
                 "provide your services, and make a meaningful impact on the result."),
            ],
        },
        {
            "type": "equipo",
            "eyebrow": "The team",
            "h2": "A stable team as operational backing",
            "foto_alt": ("The team at MCG Consultora Contable y Tributaria with Cristina Rolón at the firm's offices "
                         "in Asunción, Paraguay"),
            "paragraphs": [
                ("Behind Cristina's leadership, MCG has a stable team that carries out the day-to-day accounting and "
                 "tax work: records, reconciliations, filings before DNIT (Paraguay's tax authority), documentation "
                 "follow-up and answering each company's questions."),
                ("That stability is part of the service. Having the same people follow your company month after month "
                 "means you never have to explain the business from scratch again, and that accounting criteria stay "
                 "consistent over time."),
            ],
        },
        {"type": "cta", "h2": "See how we can help your company",
         "lead": "Tell us about your situation and we will assess the scope of the work together.",
         "cta": "Talk to us"},
    ],
}

# ----------------------------------------------------------------------- FAQ
P["faq"] = {
    "slug": "faq-taxes-companies-paraguay.html",
    "nav": "FAQ",
    "nav_footer": "Frequently asked questions",
    "title": "Paraguay Taxes for Foreigners: FAQ | DNIT, IRE, IVA & Residency",
    "description": ("Paraguay taxes for foreigners: DNIT, IRE, IVA, IRP, IDU, e-invoicing, residency by investment "
                    "and company formation — 28 detailed answers from an Asunción firm."),
    "h1": "Frequently asked questions about taxes and companies in Paraguay",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Frequently asked questions",
         "h1": "Frequently asked questions about taxes and companies in Paraguay",
         "lead": ("The questions we hear most often from companies already operating in Paraguay and from foreign "
                  "investors evaluating the country: DNIT, taxes, residency, the Paraguayan ID card, moving a "
                  "business and company formation.")},
        {
            "type": "faq",
            "eyebrow": "Taxes and tax regimes",
            "h2": "DNIT, IRE, IVA and the Paraguayan tax system",
            "items": [
                ("What is DNIT and how does it relate to the former SET?",
                 "DNIT (Dirección Nacional de Ingresos Tributarios) is Paraguay's tax authority, responsible for administering both domestic and customs taxes. It was created by merging SET (the former tax office, Subsecretaría de Estado de Tributación) with the National Customs Directorate, so a single institution now handles what used to be split between two. If your company was formed before that merger, all of its history, its RUC (tax ID) and its obligations remain valid under DNIT: there is no need to re-incorporate the company or obtain a new number. Filing channels and access credentials carry over, although the transition brought some specific administrative adjustments that are worth verifying before each filing. In practice, whenever you see SET in older documentation, read it as DNIT."),
                ("What are the main taxes a company pays in Paraguay?",
                 "Under Law 6380/2019 (Ley 6380/2019), a company in Paraguay deals primarily with four taxes. IRE (Impuesto a la Renta Empresarial, corporate income tax) applies to profits. IVA (Impuesto al Valor Agregado, VAT) applies to sales of goods and to services, and is settled monthly by deducting input credits from purchases. IDU applies to the distribution of dividends and profits to partners. And ISC (Impuesto Selectivo al Consumo, excise tax) applies only to specific products such as fuel, beverages or tobacco. On top of these come formal obligations: electronic invoicing, informational filings and withholdings where applicable. The exact combination depends on the industry and the regime, and that is one of the first things we review when we get to know a company."),
                ("What is IRE, and what are the RESIMPLE, IRE SIMPLE and IRE GENERAL regimes?",
                 "IRE is Paraguay's corporate income tax, with a general rate of 10% on profits. Law 6380/2019 (Ley 6380/2019) provides for three regimes based on the company's revenue level. RESIMPLE is designed for very small businesses, with a simplified flat-fee scheme. IRE SIMPLE applies to companies within the revenue threshold set by the regulations and allows a filing with fewer documentation requirements. IRE GENERAL applies to companies above that threshold: it requires full accounting records and a return based on actual net income. Choosing the wrong regime, or staying in one that no longer fits, has concrete consequences: more administrative burden than necessary, or outright non-compliance. That is why the classification should be reviewed at registration and every time the company's volume changes scale."),
                ("What is the IVA (VAT) rate in Paraguay and how is it filed?",
                 "Paraguay has a general IVA (VAT) rate of 10%, with a reduced 5% rate for certain goods and services defined by regulation, including some basic food-basket products and certain real estate transactions. IVA is settled monthly: output tax on sales is calculated, input tax on purchases backed by valid invoices is deducted, and the difference is what you pay. That is why supporting documentation is not a bureaucratic detail: an input credit without a valid invoice simply cannot be used. The same company can have both 10% and 5% transactions in the same period, and that classification has to be done correctly at the invoicing stage."),
                ("What is IRP and who does it apply to in Paraguay?",
                 "IRP (Impuesto a la Renta Personal, personal income tax) applies to the income of individuals resident in Paraguay, with graduated rates of 8%, 9% and 10% depending on the income level and the deductions allowed. It reaches, among others, people who provide personal services, earn professional fees, realize capital gains or receive certain income from independent activity. It is a different tax from IRE, which applies to the company itself. That distinction matters in practice: a business owner may have to consider their company's IRE and, separately, their own IRP position, depending on how they take income out."),
                ("What is IDU, the tax on dividends and profits?",
                 "IDU applies to the distribution of dividends and profits by a Paraguayan company to its partners or shareholders. The rate is 8% when the recipient is a resident of Paraguay and 15% when the beneficiary is a non-resident individual or company. This is especially relevant for foreign investors planning to remit profits to their home country, because it directly affects the net return on the investment. It also matters for local partners deciding between reinvesting in the company and distributing. It should be projected from the initial corporate design, not discovered after the decision has already been made."),
                ("What is INR and when does it apply to payments abroad?",
                 "INR (Impuesto a la Renta de No Residentes) is Paraguay's non-resident income tax, and it applies to Paraguayan-source income earned by individuals or companies abroad without tax residency in Paraguay, at a general rate of 15% on the taxable base established by law. It applies, for example, when a Paraguayan company pays for services, interest, royalties or technical assistance from a supplier abroad. In those cases the local company usually acts as withholding agent, so non-compliance is not the foreign supplier's problem but the Paraguayan company's. It is worth analyzing before signing contracts with foreign suppliers."),
                ("What is SIFEN electronic invoicing and is it mandatory?",
                 "SIFEN (Sistema Integrado de Facturación Electrónica Nacional) is DNIT's system for issuing electronic invoices with full tax validity. It was rolled out in stages, by groups of taxpayers defined by the tax authority, and by now it covers the great majority of active companies, with the final groups joining according to the official calendar. If your company still invoices from a paper booklet or with a self-printing system, it is worth confirming which group it belongs to and planning the migration with time to spare, because the change is not only technological: it means adjusting internal invoicing, collections and document-archiving processes."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Foreigners and investment",
            "h2": "Moving a business, residency and the Paraguayan ID card",
            "items": [
                ("How do I move my business to Paraguay?",
                 "What people usually call \"moving the business to Paraguay\" means, in practice, forming a Paraguayan company — EAS, SRL or SA — or registering a branch of the foreign entity, and shifting into it the operation you want to run in the country. The path includes choosing the legal structure, gathering the partners' documentation legalized or apostilled, incorporating and registering the company, obtaining the RUC (tax ID) from DNIT (Paraguay's tax authority), securing the municipal business license if applicable, opening a bank account and setting up the accounting and electronic invoicing. In parallel, the immigration status of the people who will live in Paraguay is resolved. The order and the duration depend on the project: a services consultancy is not the same as an operation with a warehouse and imports."),
                ("What is residency by investment in Paraguay and what does it require?",
                 "Paraguay has a residency regime linked to investment, processed through SUACE (Sistema Unificado de Apertura y Cierre de Empresas, the unified business opening and closing system). It requires an investment certificate issued by the Ministry of Industry and Commerce and the submission of a set of personal and corporate documents: police record, health certificate, proof of the amount actually invested and company documentation, among others. The process carries a fee set by current regulations, and the residency granted is renewed periodically. Since the rules can be updated, it is best to confirm exact amounts and requirements at the time you start the process rather than relying on information from previous years."),
                ("Does residency in Paraguay give me Paraguayan citizenship?",
                 "No. Residency — whether temporary, permanent or investment-based — is an immigration status that allows you to live and operate legally in the country. Citizenship is obtained through naturalization, which is a separate, later process with its own requirements and timelines before the competent authorities. Many foreign investors run their Paraguayan company for years holding only residency, without pursuing citizenship, and that has no effect whatsoever on the validity of their company or its operations."),
                ("Do I need a Paraguayan ID card to own a company in Paraguay?",
                 "It depends on the stage. To incorporate the company and obtain the RUC (tax ID), you can proceed with a passport and the corresponding immigration documentation. That said, once a foreigner obtains residency, applying for the Paraguayan identity card (cédula) is usually the natural next step, because it greatly simplifies everyday operations: opening and managing bank accounts, signing before a notary, dealings with public agencies and procedures before DNIT itself. In practice, having the cédula speeds everything up, even though it is not always a strict legal prerequisite for the company to exist."),
                ("What does asset or tax \"shielding\" mean for a foreign investor?",
                 "In everyday use, \"shielding\" refers to organizing the corporate structure, the documentation and tax compliance in order to reduce avoidable legal, asset and tax risks: choosing the appropriate legal structure, keeping the accounting up to date, clearly separating personal assets from company assets, documenting every transaction and filing correctly and on time before DNIT (Paraguay's tax authority). No serious accounting firm can promise immunity from tax audits, guarantee that there will never be an adjustment, or offer structures to hide assets. What can be done, and what we do, is work preventively and meticulously to minimize unnecessary exposure."),
                ("Can I run my Paraguayan company while living abroad?",
                 "Yes, and it is very common among foreign investors. You can incorporate and be a partner or shareholder in a Paraguayan company without residing in the country. What needs to be clearly defined is local legal representation, the scope of the powers of attorney granted and who is responsible for signing and for day-to-day decisions. Accounting, electronic invoicing and filings before DNIT are handled perfectly well remotely when a trusted local team is in charge — which is exactly the role an accounting firm like MCG plays for clients operating from abroad."),
                ("What real tax advantages does Paraguay offer a foreign investor?",
                 "Paraguay is characterized by comparatively low rates within the region: 10% IRE (corporate income tax) on profits and a general 10% IVA (VAT), with a reduced 5% rate for certain goods and services. Add to that a relatively simple system since Law 6380/2019 (Ley 6380/2019), simplified regimes for small businesses, and a residency regime linked to investment. None of these features implies zero taxes or automatic benefits, and you should be skeptical of anyone who presents it that way. The real tax burden depends on the regime the company registers under, its industry, its corporate structure and how profits are withdrawn — which is where IDU comes in. That is why a serious evaluation is done on the specific case, with actual numbers."),
                ("Can a foreign company open a bank account in Paraguay?",
                 "Yes, and it is one of the steps most worth preparing well in advance. Paraguayan banks apply know-your-customer procedures that require complete corporate documentation, identification of ultimate beneficial owners, evidence of the source of funds and, in many cases, the presence of the authorized signatories. Our role at this stage is to prepare and organize the documentation and coordinate with the institution, but approval always depends on each bank's own assessment: there is no contact who can guarantee approvals — and be skeptical of anyone who offers one."),
            ],
        },
        {
            "type": "faq",
            "eyebrow": "Company formation",
            "h2": "EAS, SRL, SA and the incorporation process in Paraguay",
            "items": [
                ("Which type of company suits me in Paraguay: EAS, SRL or SA?",
                 "The three most commonly used structures are the EAS (Empresa por Acciones Simplificada, simplified stock company), the SRL (Sociedad de Responsabilidad Limitada, limited liability company) and the SA (Sociedad Anónima, corporation). The EAS was designed as a fast, flexible route for startups and small and mid-sized businesses, with a simpler incorporation process. The SRL is the traditional vehicle for businesses with few partners and simple governance, where ownership is represented by membership quotas. The SA is the usual choice for larger operations: it allows shares to be issued, investors to be brought in and a more formal governance structure to be maintained, something banks, funds and institutional partners often require. The right choice depends on the number of partners, the growth plan, whether investors will be brought in, and the type of counterparties the company will work with."),
                ("How long does it take to form a company in Paraguay?",
                 "The timeline depends on the legal structure chosen, on the current workload at the registries and notary offices involved and, above all, on how complete the documentation is from the outset. When there are foreign partners whose documents must be legalized or apostilled abroad, that is usually the step that drives the calendar, because it does not depend on Paraguay. The EAS is generally the fastest structure to set up, thanks to its simplified design. Rather than promising a fixed number of days, the useful thing is to assemble the complete file from the start: that is what actually shortens the timeline."),
                ("What documents do I need to incorporate a company in Paraguay?",
                 "Generally speaking, you need identification for each partner — a Paraguayan ID card for nationals, a passport and immigration documentation for foreigners — the bylaws or articles of association with the corporate purpose and ownership structure, the definition of share capital and how it is paid in, and the appointment of directors or legal representatives. Where there are foreign partners, whether individuals or legal entities, you also need documentation legalized or apostilled in the country of origin, with official translation where required. If a foreign legal entity will be a partner, the parent company's corporate documentation is required as well. It is worth reviewing the exact list before starting legalizations, so you do not pay twice for procedures handled incorrectly."),
                ("Can I form a company in Paraguay without traveling to the country?",
                 "In many cases it is possible to advance much of the process remotely, using special powers of attorney granted before a notary in your country of origin and duly legalized or apostilled, which authorize a local representative to sign the corporate documentation. That said, certain specific steps, above all opening a bank account and some immigration procedures, usually require physical presence or at least more direct involvement from the interested party. The recommended approach is to plan from the outset what can be resolved remotely and what is best concentrated into a single trip to Paraguay."),
                ("How much share capital do I need to open a company in Paraguay?",
                 "Share capital is defined according to the legal structure chosen and the type of activity, and it must bear a reasonable relationship to the operation the company will carry out. It is not a merely formal figure: banks, commercial counterparties and public agencies look at it when assessing the company, and capital that is inconsistent with the volume of operations raises questions. This is one of the items we review in the initial assessment, along with the ownership structure and the corporate purpose."),
                ("What obligations does a newly formed company have in Paraguay?",
                 "From the moment it obtains its RUC (tax ID), the company is subject to the obligations of the regime it registered under, even if it has not yet issued a single invoice. That includes filing the applicable returns by each deadline, issuing tax-valid invoices through the electronic invoicing system, keeping accounting records and preserving supporting documentation. Filing a zero return when there was no activity also counts as compliance: failing to file, even with no activity, creates formal breaches that have to be remediated later."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Accounting and working with MCG",
            "h2": "Compliance, remediation and how to get started",
            "items": [
                ("How often do I have to file returns with DNIT?",
                 "The frequency depends on the tax and the regime. IVA (VAT) is calculated and filed monthly; IRE (corporate income tax) has an annual return, with advance payments depending on the regime the company is in; and there are specific informational filings depending on the activity, plus withholdings when the company has to act as a withholding agent. Deadlines follow DNIT's calendar based on the last digit of your RUC (tax ID). Maintaining a dedicated calendar per company, rather than just looking at the general calendar, is one of the basic functions of our business accounting service."),
                ("What if my accounting is behind or disorganized?",
                 "It is a more common situation than it seems, especially in companies that grew fast or that changed accountants several times. The first step is a diagnostic review of the real situation: which periods are missing, what documentation exists, which filings were left pending before DNIT and which balances do not reconcile. From there we build a remediation plan with priorities, quoted separately from the monthly service because it is a distinct one-off engagement. The sooner it is addressed, the lower the risk of accumulating contingencies and of a small problem turning into an expensive one."),
                ("Does MCG work with companies in any industry and of any size?",
                 "Yes. We work with all kinds of companies: businesses already billing significant volumes, ventures that are just getting started, family businesses that need to get organized, and projects from foreign investors setting up in Paraguay. The industries vary: retail and wholesale, services, construction, import, technology, healthcare and food service, among others. What we define in each case is the scope of the service based on the real complexity of the operation, not a minimum revenue threshold to be able to work together."),
                ("How do I start working with MCG?",
                 "The first step is to complete the contact form or write to us on WhatsApp describing your situation: whether you already have a company in Paraguay, whether you are about to set up as a foreigner, or whether you have another specific question. With that information we assess fit and the possible scope, and we arrange a conversation to understand the case better. If a diagnostic or a deeper technical review is needed, it is quoted as a separate step before the final proposal is defined. Everything is put in writing before any work begins."),
                ("Do the fees cover everything, or are there separate costs?",
                 "Fees are set according to the agreed scope — bookkeeping, tax obligations, closings, strategic advisory — and that scope is stated explicitly in the proposal before work begins. Services outside that scope, such as remediation of prior periods, specific audits, extraordinary engagements or procedures requiring professionals from other specialties, are quoted separately. In addition, government agency and notary fees are third-party costs and are always reported as such, separate from our own fees."),
                ("Do you work with companies outside Asunción, or only in the capital?",
                 "Our office is in Asunción, but accounting and tax work is largely done digitally: receiving documentation, keeping records, filing before DNIT and holding review meetings. That allows us to serve companies from different parts of Paraguay as well as clients operating from abroad. When a procedure requires physical presence, we coordinate it case by case."),
            ],
        },
        {"type": "cta", "h2": "Is your question not on the list?",
         "lead": "Tell us about your specific situation and we will answer you directly.",
         "cta": "Talk to us"},
    ],
}

# ------------------------------------------------------------------ CONTACTO
P["contacto"] = {
    "slug": "contact.html",
    "nav": "Contact",
    "nav_footer": "Contact",
    "title": "Contact | Accountant in Asunción, Paraguay — MCG Consultora",
    "description": ("Contact MCG Consultora, an accounting firm in Asunción, Paraguay. Tell us about your company or "
                    "investment project and we will coordinate next steps."),
    "h1": "Talk to us",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "Contact",
         "h1": "Talk to us",
         "lead": ("Tell us about your company or your project in Paraguay. The initial inquiry lets us assess fit and "
                  "scope; a technical review or diagnostic is quoted separately.")},
        {
            "type": "form",
            "form": {
                "situacion": "What is your situation?",
                "seleccione": "Select an option",
                "situacion_opciones": [("empresa", "I already have a company in Paraguay"),
                                       ("extranjero", "I want to set up my company in Paraguay"),
                                       ("otro", "Another question")],
                "nombre": "Name",
                "empresa": "Company or project",
                "correo": "Email address",
                "whatsapp": "WhatsApp",
                "whatsapp_ph": "E.g.: +595 981 234 567",
                "servicio": "Service of interest",
                "seleccione_servicio": "Select a service",
                "servicio_opciones": [("Business accounting", "Business accounting"),
                                      ("Tax strategy", "Tax strategy"),
                                      ("Company formation", "Company formation"),
                                      ("Setting up for foreigners", "Setting up for foreigners"),
                                      ("I am not sure yet", "I am not sure yet")],
                "legend_empresa": "About your company",
                "rubro": "Industry",
                "facturacion": "Approximate monthly revenue",
                "facturacion_opciones": ["We are just getting started", "Less than PYG 400 million",
                                         "PYG 400–1,000 million", "More than PYG 1,000 million",
                                         "I would rather discuss it in a conversation"],
                "necesidad": "Main need",
                "legend_extranjero": "About your project in Paraguay",
                "pais": "Country of residence",
                "tipo_proyecto": "Type of project",
                "tipo_ph": "E.g.: trade, services, investment",
                "etapa": "Project stage",
                "seleccione_etapa": "Select a stage",
                "etapa_opciones": [("I am still evaluating the idea", "I am still evaluating the idea"),
                                   ("I have decided to set up and want to move forward", "I have decided to set up and want to move forward"),
                                   ("I already have a company formed in Paraguay", "I already have a company formed in Paraguay")],
                "aviso": ("There is no need to send financial documents or sensitive banking information through this "
                          "form. If we need it, we will request it securely at a later stage."),
                "enviar": "Send inquiry",
                "abrir_wa": "Open WhatsApp manually",
            },
        },
        {
            "type": "contacto_extra",
            "eyebrow": "Another way to reach us",
            "h2": "You can also write to us directly",
            "p": ("If you prefer, write to us directly on WhatsApp or follow us on Instagram. We work in Spanish, "
                  "English and Portuguese, from Asunción, Paraguay."),
            "wa_mensaje": "Hi MCG, I'm visiting from your website and I'd like to ask a question",
            "wa_cta": "Message us on WhatsApp",
            "ig_cta": "See our Instagram",
        },
    ],
}

# -------------------------------------------------------------------- ERP
P["erp"] = {
    "slug": "erp-accounting-implementation-paraguay.html",
    "nav": "ERP",
    "nav_footer": "ERP implementation",
    "service": "ERP implementation — accounting module",
    "title": "ERP Accounting Implementation in Paraguay | MCG Consultora",
    "description": ("ERP accounting module implementation in Paraguay: chart of accounts, subledgers, costing and an "
                    "auditable trail. Over 30 companies implemented by Cristina Rolón."),
    "h1": "ERP implementation: the accounting module as the core of the system",
    "blocks": [
        {"type": "hero_simple", "eyebrow": "ERP implementation",
         "h1": "ERP implementation: the accounting module as the core of the system",
         "lead": ("Cristina Rolón's specialty: getting the accounting module configured properly so that everything "
                  "else in the ERP — treasury, logistics, production, purchasing, banking — reconciles, and stays "
                  "traceable and auditable."),
         "cta": "Talk to us"},
        {
            "type": "rich",
            "eyebrow": "The starting point",
            "h2": "Why the accounting module is the parent of every other module",
            "paragraphs": [
                ("In an ERP, everything eventually lands in the accounting records. A sale generates a journal entry; a "
                 "purchase creates a liability and an IVA (value added tax) input credit; a warehouse movement changes "
                 "inventory valuation; a work order consumes raw materials and generates cost; a collection moves "
                 "treasury and the bank accounts. If the <strong>accounting module</strong> is configured badly, all of "
                 "those movements are recorded incorrectly — or not recorded at all — and the rest of the system starts "
                 "producing information that does not add up."),
                ("That is why an ERP implementation is not won on the attractive screens of each module: it is won in "
                 "the chart of accounts, in the automatic posting rules, in inventory valuation, in the cost centers "
                 "and in how the subledgers integrate with the general ledger. When that groundwork is done properly, "
                 "the company gets reliable financial statements without a parallel manual effort; when it is done "
                 "badly, the team ends up rebuilding everything in spreadsheets."),
                ("Cristina Rolón works at exactly that point: she joins the ERP project from the accounting and tax "
                 "perspective, defines how each business transaction has to be recorded in Paraguay — including the "
                 "requirements of DNIT (Paraguay's tax authority) and electronic invoicing — and stays with the project "
                 "until the closings come out of the system rather than out of a spreadsheet."),
            ],
        },
        {
            "type": "cards",
            "alt": True,
            "eyebrow": "Integration",
            "h2": "The modules that depend on the accounting core",
            "lead": ("Each of these modules either generates or consumes accounting information. The implementation "
                     "defines how it is recorded, how it is reconciled and how it is audited."),
            "columns": 3,
            "items": [
                ("Treasury and cash", "Collections, payments, petty cash funds and cash counts, with automatic posting and reconciliation against the accounting balances."),
                ("Banking and reconciliation", "Statements, checks, transfers and periodic bank reconciliation, with outstanding items clearly identified."),
                ("Purchasing and accounts payable", "Purchase orders, goods receipt, supplier invoice and payment, with three-way match control and IVA input credit correctly claimed."),
                ("Sales and accounts receivable", "Electronic invoicing, credit notes, collections and aging of balances, integrated into the sales ledger."),
                ("Inventory and logistics", "Receipts, issues, transfers between warehouses and inventory valuation, with a direct impact on cost of goods sold."),
                ("Production", "Work orders, raw material consumption, labor and manufacturing overhead applied to the cost of finished goods."),
                ("Dispatch and delivery notes", "Delivery notes and shipments linked to the invoice and to the stock movement, so nothing leaves without supporting documentation."),
                ("Fixed assets", "Additions, disposals, depreciation and revaluations, with their impact on results and on the financial statements."),
                ("Costing and profitability", "Cost centers, costing by product, line or project, and the real margin of each business unit."),
            ],
        },
        {
            "type": "checks",
            "eyebrow": "The outcome",
            "h2": "What a company should be able to do once the ERP is properly implemented",
            "items": [
                "Produce the income statement and balance sheet straight out of the system, without assembling them by hand in spreadsheets.",
                "See real profitability by product, business line, branch or project, with costs properly applied.",
                "Trace any number backwards: from the income statement to the journal entry, and from the entry to the source document.",
                "Reconcile banks, inventory and customer accounts without arguments over which system is right.",
                "Close the month on time, with the subledgers tied out against the general ledger.",
                "Respond to a DNIT tax audit by showing the full audit trail from within the system.",
                "Control access and keep a record of who entered, modified or approved each transaction.",
            ],
            "paragraphs": [
                ("Traceability and auditability are not a luxury: they are what allows management to trust the numbers, "
                 "and what allows an external auditor, a bank or the tax authority to verify what the company "
                 "reports."),
            ],
        },
        {
            "type": "rich",
            "alt": True,
            "eyebrow": "Experience",
            "h2": "More than 30 companies implemented, from 10 to over 700 employees",
            "paragraphs": [
                ("Cristina Rolón has taken part in the implementation of the ERP accounting module at <strong>more than "
                 "30 companies</strong> of different sizes and industries: from small companies of around 10 employees "
                 "to organizations with <strong>more than 700 employees</strong>, several branches, in-house production "
                 "and complex cost structures."),
                ("That difference in scale matters. A ten-person company needs a simple system, a manageable chart of "
                 "accounts and processes that do not suffocate it; a company of seven hundred needs cost centers, "
                 "access profiles by area, approval controls and closings coordinated across several teams. The "
                 "implementation has to fit the real size of the operation, not the software brochure."),
                ("That track record also produced a clear reading of where these projects usually fail: charts of "
                 "accounts copied from another company, opening balances migrated without being reconciled, modules "
                 "switched on before the accounting counterpart of each transaction has been defined, and training "
                 "that teaches people which buttons to press but not what each button actually records."),
            ],
        },
        {
            "type": "pasos",
            "eyebrow": "Methodology",
            "h2": "How we run an implementation",
            "items": [
                ("Business review", "We map the real cycle: what happens from the moment an order comes in until it is collected and recorded."),
                ("Chart of accounts design", "Building or redesigning the chart of accounts and the cost centers around the way management needs to read the information."),
                ("Accounting configuration", "Automatic posting rules, subledgers, treatment of IVA and withholdings, inventory valuation and costing criteria."),
                ("Balance migration and reconciliation", "Loading reconciled opening balances, so the system starts out tied and does not carry differences forward."),
                ("End-to-end testing", "Simulating real transactions from start to finish, verifying the accounting impact of each module before going live."),
                ("Team training", "Role-based training, so that every area understands what the system records when it operates and what the consequences are."),
                ("Go-live and support", "Launch, an assisted first month-end close and fine-tuning until the financial statements come out of the ERP without rework."),
            ],
        },
        {
            "type": "faq",
            "alt": True,
            "eyebrow": "Frequently asked questions",
            "h2": "About ERP implementation in Paraguay",
            "items": [
                ("Do you work with one particular ERP or with any system?",
                 "MCG's work is the accounting content of the implementation, not the sale of a license: chart of accounts, posting rules, valuation and costing criteria, treatment of IVA and withholdings, reconciliations and closings. That content is applied to whichever ERP the company has chosen or is evaluating, and it is coordinated with the software vendor and with the company's IT team."),
                ("Why does the accounting module have to be defined before the others?",
                 "Because every other module ultimately posts into it. If logistics, production or treasury are switched on before it has been defined how each movement is posted, the system starts generating incomplete or misclassified records, and correcting them later means reprocessing months of information. Defining the accounting core first is what saves exactly that rework."),
                ("Can an implementation that already went wrong be fixed?",
                 "Yes, and it is an important part of what we do. It starts with a diagnostic: reviewing the chart of accounts, checking whether the subledgers tie out to the general ledger, reviewing inventory valuation and the migrated balances, and identifying which transactions are being recorded incorrectly. From there we build a remediation plan by priority, without bringing the operation to a halt."),
                ("What does it take for an ERP to be auditable?",
                 "Every figure has to be traceable back to its source document, access has to be defined by role, there has to be a record of who entered and approved each transaction, the subledgers have to tie out to the general ledger, and the supporting documentation has to be available. That is what makes it possible to respond confidently to an external auditor, a bank or a DNIT tax audit."),
                ("Is this useful for a small company or only for large ones?",
                 "It is useful for both, with different scopes. A ten-person company needs a simple chart of accounts and light processes that still leave a traceable record; a company with hundreds of employees needs cost centers, access profiles, approval controls and coordinated closings. We have worked at both ends, and the most common mistake is applying the model of one to the other."),
            ],
        },
        {"type": "cta", "h2": "About to implement — or fix — an ERP?",
         "lead": "Tell us what stage the project is at and we will review it together.",
         "cta": "Talk to us"},
    ],
}
