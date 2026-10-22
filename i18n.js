window.I18N = {
  fr: {
    "meta.desc":
      "Une histoire d’intérêts techniques — du desktop local aux agents et à la cybersécurité.",
    "rail.aria": "Portfolio — défilement horizontal",
    "nav.prev": "Précédent",
    "nav.next": "Suivant",
    "cover.line": "Engineer in cyber and software.",
    "cover.nudge": "Glisser vers la droite →",
    "cover.nudgeMobile": "Glisser vers le bas ↓",
    "who.chapter": "Qui",
    "who.title": "Ingénieur logiciel et cybersécurité.",
    "who.p1":
      "Je m’appelle Helijao Andriamandranto. Master <strong>Software Engineering</strong> (EPITA) et Master <strong>Cybersécurité</strong> (ECPI, USA). Je construis des systèmes logiciels — du desktop au cloud — et je les pense dès le départ sous l’angle sécurité.",
    "who.p2":
      "En pratique, je travaille sur des APIs et des apps, de l’infra (Terraform, Docker, Kubernetes), et surtout des <strong>agents GenAI</strong> qui ne se limitent pas au chat : outils MCP, génération de documents, workers qui exécutent hors du modèle. Autre fil : la GenAI métier avec des contraintes dures (privacy, offline, isolation d’exécution).",
    "who.p3":
      "Côté cyber, mon réflexe c’est AppSec, moindre privilège, et méthodo (OWASP, GRC de base). Quand j’explore le pentest assisté par IA, l’humain reste dans la boucle — l’agent aide à structurer, il ne remplace pas le jugement.",
    "who.p4":
      "Les projets qui suivent montrent cette progression — vues sanitizées, besoin et stack visibles, IP privée. Pour aller plus loin, contactez-moi.",
    "interests.chapter": "Intérêts",
    "interests.title": "L’IA évolue — la sécurité doit suivre.",
    "interests.p1":
      "On est passé du modèle qui répond à des <em>agents qui agissent</em> : outils, fichiers, APIs, workers hors du LLM. Plus l’IA touche la prod et les données métier, plus elle devient une surface d’attaque — prompt injection, fuite de contexte, droits trop larges, supply chain des modèles et des plugins.",
    "interests.p2":
      "Ce qui m’intéresse, c’est exactement ce croisement : construire des agents utiles <em>et</em> les border — privacy by design, moindre privilège (IRSA, SSO), exécution isolée, RAG local quand le cloud n’est pas acceptable, humain dans la boucle sur le offensif. La cyber n’est pas une couche à côté de l’IA ; c’est le design de l’IA en production.",
    "interests.p3":
      "Stack du quotidien : Python, TypeScript, AWS, Terraform, Kubernetes — avec AppSec / OWASP comme réflexe, pas comme option.",
    "thread.chapter": "Le fil",
    "thread.title": "Six projets, une progression.",
    "thread.p1":
      "Chaque app ici marque une étape de mon évolution technique — de l’outil local au système agentique. La complexité monte, et la sécurité monte avec : ce n’est pas un add-on en fin de parcours, c’est le fil qui relie desktop, RAG, GenAI cloud, workers et cyber offensive assistée.",
    "ronin.chapter": "Chapitre I · Fondations",
    "ronin.lede": "Traducteur IA — desktop, puis app Android portable.",
    "ronin.body":
      "Besoin métier : écrire vite en franglais / jargon technique sans perdre le sens des termes protégés (noms de produits, acronymes, formulations figées). Un traducteur « grand public » réécrit trop ; il fallait un outil discret qui respecte un glossaire.",
    "ronin.body2":
      "Côté technique : app desktop Python (UI légère, packaging PyInstaller), modèle local ou API, glossaire JSON. Puis version portable Android (Kotlin), même logique produit — pour l’avoir aussi hors du poste de travail.",
    "ronin.hr":
      "Pourquoi c’est là : prouver qu’on peut livrer un vrai produit local (pas seulement un notebook), avec une règle métier simple mais dure — le glossaire — et le porter sur mobile.",
    "ronin.tag": "Glossaire JSON",
    "centinel.chapter": "Chapitre II · Mémoire locale",
    "centinel.lede": "Base de connaissance cyber offline — pour préparer une mission sans fuite cloud.",
    "centinel.body":
      "Besoin métier : un auditeur / pentester doit interroger ISO, DORA, RGPD, NIST, OWASP, PTES rapidement, sans uploader des docs sensibles vers un LLM public. Les réponses « mur de texte » ne servent pas ; il faut une structure utilisable en mission.",
    "centinel.body2":
      "Technique : RAG local (PDF → embeddings → Chroma), LLM offline type Ollama, et réponses en phases quand la question est méthodo. Séparation volontaire règles de conformité vs guides d’exécution.",
    "centinel.hr":
      "Pourquoi c’est là : montrer qu’on sait construire un système de connaissance utile au métier cyber, avec la contrainte privacy / offline comme exigence de design — pas un gadget chat.",
    "voice.chapter": "Chapitre III · Voix & GenAI",
    "voice.lede":
      "Faire évoluer un callbot à parcours vers une conversation GenAI sur AWS.",
    "voice.body":
      "Besoin métier : les bots téléphoniques à parcours figé cassent dès que l’appelant ne suit pas le script. L’objectif n’était pas « mettre de l’IA partout », mais rendre le dialogue plus naturel tout en gardant un socle contact-center fiable (Connect, Lex, parcours existants).",
    "voice.body2":
      "Technique : couche GenAI additive (Lambda, mémoire courte, Bedrock) branchée sur le bot — sans réécrire tout le parcours d’un coup. Terraform, envs séparés, staging. Le détail du domaine métier reste hors vitrine publique.",
    "voice.hr":
      "Pourquoi c’est là : prouver qu’on sait moderniser un canal client vocal avec GenAI cloud, en respectant l’existant et l’IaC — pas un POC console jetable.",
    "mcp.chapter": "Chapitre IV · Agents qui livrent",
    "mcp.lede": "Quand le chat doit produire un livrable Office, pas seulement une réponse.",
    "mcp.body":
      "Besoin métier : les équipes veulent que l’agent « fasse » — un PPT, un Word, un Excel — plutôt que de copier-coller. Les scripts one-shot ne scalent pas ; il fallait des outils réutilisables, avec fichiers récupérables de façon contrôlée.",
    "mcp.body2":
      "Technique : serveur MCP (FastMCP) pour générer pptx/docx/xlsx, dépôt objet (S3), URL signée, déploiement conteneur / Kubernetes à côté de la plateforme d’agents.",
    "mcp.hr":
      "Pourquoi c’est là : montrer le passage agents conversationnels → agents actionnables, avec une vraie intégration cloud et une idée claire de livrable métier.",
    "analyzer.chapter": "Chapitre V · Scan & distance",
    "analyzer.lede":
      "Scanner n’importe quel dépôt — qualité de code + posture sécu — sans tout verser dans le LLM.",
    "analyzer.body":
      "Besoin métier : piloter la qualité / la dette / des signaux de sécurité sur un repo, sans exposer tout le code source à un modèle (coût, fuite, bruit). L’humain ou l’agent doit raisonner sur un rapport, pas sur 50 000 fichiers bruts.",
    "analyzer.body2":
      "Technique : worker qui clone et parse (Tree-sitter), API (FastAPI), rapport structuré ; l’orchestrateur IA ne voit que ce rapport. Déploiement type Docker / EKS.",
    "analyzer.hr":
      "Pourquoi c’est là : architecture de confiance — l’IA orchestre, l’exécution reste bornée. Compétence utile dès qu’on parle GenAI + code en entreprise.",
    "codium.chapter": "Chapitre VI · Plan & isolement",
    "codium.lede":
      "Structurer un pentest avec l’IA — sans fusionner cerveau et outillage offensif.",
    "codium.body":
      "Besoin métier : accélérer la phase de structuration (plan, notes, findings) tout en gardant un humain responsable. On ne veut pas un « agent qui pirate tout seul » sur le poste du quotidien.",
    "codium.body2":
      "Technique : plan intelligence (agent) séparé du plan d’exécution (conteneurs / scanners type ZAP), pont de commandes contrôlé, méthodo OWASP. Vitrine architecture uniquement — pas d’exploits.",
    "codium.hr":
      "Pourquoi c’est là : montrer la cyber « sérieuse » appliquée à l’IA — isolation, supervision humaine, méthodo — pas du theatre offensive.",
    "close.chapter": "Fin",
    "close.title": "EOF — à vous.",
    "close.body":
      "Les agents agissent. Les humains décident. Si ce fil build × cyber vous parle, écrivez-moi.",
    "soon.link": "Vitrine GitHub (sans code source) →",
    "soon.linkMethod": "Vitrine méthodo GitHub (sans exploits) →",
  },
  en: {
    "meta.desc":
      "A story of technical interests — from local desktop tools to agents and cybersecurity.",
    "rail.aria": "Portfolio — horizontal scroll",
    "nav.prev": "Previous",
    "nav.next": "Next",
    "cover.line": "Engineer in cyber and software.",
    "cover.nudge": "Swipe right →",
    "cover.nudgeMobile": "Swipe down ↓",
    "who.chapter": "Who",
    "who.title": "Software and cybersecurity engineer.",
    "who.p1":
      "I’m Helijao Andriamandranto. Master’s in <strong>Software Engineering</strong> (EPITA) and <strong>Cybersecurity</strong> (ECPI, USA). I build software systems — from desktop to cloud — and I design them with security in from the start.",
    "who.p2":
      "Day to day that means APIs and apps, infra (Terraform, Docker, Kubernetes), and especially <strong>GenAI agents</strong> that do more than chat: MCP tools, document generation, workers that run outside the model. Parallel track: business GenAI under hard constraints (privacy, offline, isolated execution).",
    "who.p3":
      "On the cyber side, my default is AppSec, least privilege, and solid methodology (OWASP, basic GRC). When I explore AI-assisted pentest, a human stays in the loop — the agent helps structure the work; it doesn’t replace judgment.",
    "who.p4":
      "The projects ahead show that progression — sanitized views, need and stack clear, IP kept private. Want more depth? Reach out.",
    "interests.chapter": "Interests",
    "interests.title": "AI is evolving — security has to keep up.",
    "interests.p1":
      "We’ve moved from models that answer to <em>agents that act</em>: tools, files, APIs, workers outside the LLM. The more AI touches production and business data, the more it becomes an attack surface — prompt injection, context leakage, over-privileged tools, model and plugin supply chain.",
    "interests.p2":
      "That’s the intersection I care about: build agents that are useful <em>and</em> bounded — privacy by design, least privilege (IRSA, SSO), isolated execution, local RAG when the cloud isn’t acceptable, human-in-the-loop on offensive work. Cyber isn’t a side quest next to AI; it’s how you design AI for production.",
    "interests.p3":
      "Day-to-day stack: Python, TypeScript, AWS, Terraform, Kubernetes — with AppSec / OWASP as a reflex, not an optional add-on.",
    "thread.chapter": "The thread",
    "thread.title": "Six projects, one progression.",
    "thread.p1":
      "Each app here marks a step in my technical evolution — from a local tool to an agentic system. Complexity rises, and security rises with it: not a bolt-on at the end, but the thread that ties desktop, RAG, cloud GenAI, workers, and assisted offensive cyber together.",
    "ronin.chapter": "Chapter I · Foundations",
    "ronin.lede": "AI translator — desktop, then a portable Android app.",
    "ronin.body":
      "Business need: write fast in mixed language / technical jargon without losing protected terms (product names, acronyms, fixed phrasing). Consumer translators rewrite too much — we needed a quiet tool that respects a glossary.",
    "ronin.body2":
      "Technical: Python desktop app (light UI, PyInstaller), local or API model, JSON glossary. Then a portable Android twin (Kotlin) with the same product rules — so it leaves the desk too.",
    "ronin.hr":
      "Why it’s here: prove I can ship a real local product (not just a notebook), with one hard business rule — the glossary — and port it to mobile.",
    "ronin.tag": "JSON glossary",
    "centinel.chapter": "Chapter II · Local memory",
    "centinel.lede": "Offline cyber knowledge base — prepare a mission without cloud leakage.",
    "centinel.body":
      "Business need: an auditor / pentester must query ISO, DORA, GDPR, NIST, OWASP, PTES quickly without uploading sensitive docs to a public LLM. Wall-of-text answers don’t help; mission-ready structure does.",
    "centinel.body2":
      "Technical: local RAG (PDF → embeddings → Chroma), offline LLM (Ollama-class), phased answers for methodology questions. Deliberate split between compliance rules and execution guides.",
    "centinel.hr":
      "Why it’s here: show I can build a knowledge system that serves a cyber workflow, with privacy / offline as a design requirement — not a chat gadget.",
    "voice.chapter": "Chapter III · Voice & GenAI",
    "voice.lede":
      "Evolve a path-based callbot into GenAI conversation on AWS.",
    "voice.body":
      "Business need: rigid phone journeys break as soon as callers leave the script. The goal wasn’t “sprinkle AI everywhere”, but freer dialogue while keeping a reliable contact-center base (Connect, Lex, existing paths).",
    "voice.body2":
      "Technical: additive GenAI layer (Lambda, short memory, Bedrock) on top of the bot — without rewriting the whole journey at once. Terraform, separated envs, staging. Domain-specific detail stays out of the public showcase.",
    "voice.hr":
      "Why it’s here: prove I can modernize a voice customer channel with cloud GenAI while respecting legacy paths and IaC — not a throwaway console POC.",
    "mcp.chapter": "Chapter IV · Agents that deliver",
    "mcp.lede": "When chat must produce an Office deliverable, not only an answer.",
    "mcp.body":
      "Business need: teams want the agent to *do* something — a deck, a Word doc, a spreadsheet — not copy-paste forever. One-off scripts don’t scale; we needed reusable tools with controlled file delivery.",
    "mcp.body2":
      "Technical: MCP server (FastMCP) for pptx/docx/xlsx, object storage (S3), signed URL, container / Kubernetes deploy next to the agent platform.",
    "mcp.hr":
      "Why it’s here: show the jump from conversational agents to actionable ones, with real cloud integration and a clear business deliverable.",
    "analyzer.chapter": "Chapter V · Scan & distance",
    "analyzer.lede":
      "Scan any repo — code quality + security posture — without pouring source into the LLM.",
    "analyzer.body":
      "Business need: steer quality / debt / security signals on a codebase without exposing every file to a model (cost, leakage, noise). People and agents should reason over a report, not 50k raw files.",
    "analyzer.body2":
      "Technical: worker clones and parses (Tree-sitter), FastAPI, structured report; the AI orchestrator only sees that report. Docker / EKS-style deploy.",
    "analyzer.hr":
      "Why it’s here: trust architecture — AI orchestrates, execution stays bounded. Useful as soon as GenAI meets enterprise code.",
    "codium.chapter": "Chapter VI · Plan & isolation",
    "codium.lede":
      "Structure a pentest with AI — without merging brain and offensive tooling.",
    "codium.body":
      "Business need: speed up structuring (plan, notes, findings) while keeping a human accountable. Nobody wants an “agent that hacks alone” on the daily workstation.",
    "codium.body2":
      "Technical: intelligence plane (agent) separated from execution plane (containers / scanners e.g. ZAP), controlled bridge, OWASP methodology. Architecture showcase only — no exploits.",
    "codium.hr":
      "Why it’s here: serious cyber applied to AI — isolation, human oversight, methodology — not offensive theatre.",
    "close.chapter": "End",
    "close.title": "EOF — your move.",
    "close.body":
      "Agents act. Humans decide. If this build × cyber thread lands, write me.",
    "soon.link": "GitHub showcase (no source) →",
    "soon.linkMethod": "Method showcase on GitHub (no exploits) →",
  },
};
