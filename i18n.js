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
    "ronin.lede": "Un traducteur IA qui reste dans le flux — sur le bureau, puis sur Android.",
    "ronin.body":
      "Quand on écrit en franglais ou en jargon technique, un traducteur classique a tendance à « améliorer » des termes qu’on voulait garder : noms de produits, acronymes, formulations figées. Ronin est né de ce frottement — un outil discret, clavier d’abord, qui s’appuie sur un glossaire pour protéger ce qui ne doit pas bouger.",
    "ronin.body2":
      "Je l’ai d’abord livré en application desktop (Python, interface légère, packaging type PyInstaller), branchée sur un modèle local ou une API. Puis le même contrat produit a suivi sur mobile : une version portable Android en Kotlin, toujours dans un esprit terminal, pour ne pas rester coincé au poste.",
    "ronin.hr":
      "Au fond, c’est la première marche du portfolio : prouver qu’on sait sortir un vrai petit produit, avec une règle métier simple mais non négociable, et le faire vivre sur plus d’une plateforme.",
    "ronin.tag": "Glossaire JSON",
    "centinel.chapter": "Chapitre II · Mémoire locale",
    "centinel.lede": "Une mémoire cyber qui reste sur la machine — pour préparer sans exposer.",
    "centinel.body":
      "Avant une mission, on a besoin d’interroger vite des référentiels denses — ISO, DORA, RGPD, NIST, OWASP, PTES — sans envoyer des documents sensibles dans un LLM public. Et une réponse en mur de texte ne sert presque à rien sur le terrain : il faut quelque chose qu’on peut suivre.",
    "centinel.body2":
      "Centinel indexe ces PDF en local, les interroge en langage naturel via un modèle offline, et structure les réponses méthodo en phases. Les règles de conformité et les guides d’exécution restent distingués pour que la restitution reste lisible.",
    "centinel.hr":
      "C’est le moment où l’outil devient un système de connaissance : utile au métier cyber, avec la contrainte offline comme point de départ, pas comme détail après coup.",
    "voice.chapter": "Chapitre III · Voix & GenAI",
    "voice.lede": "Quand le parcours téléphonique ne suffit plus, et que la GenAI doit s’y greffer sans tout casser.",
    "voice.body":
      "Un callbot à parcours figé marche tant que l’appelant suit le script. Dès qu’il digresse, le dialogue se brise. L’enjeu n’était pas d’ajouter de l’IA pour la forme, mais d’ouvrir la conversation tout en gardant un contact center solide — Connect, Lex, les parcours déjà en place.",
    "voice.body2":
      "J’ai travaillé une couche GenAI additive sur AWS (Lambda, mémoire courte de conversation, Bedrock), branchée sur le bot existant plutôt que de le remplacer d’un bloc. Terraform, environnements séparés, staging : on peut comparer, reculer, avancer sans brûler le canal.",
    "voice.hr":
      "Ce chapitre montre surtout une modernisation raisonnable d’un canal client vocal — GenAI cloud, mais respect de l’existant et de la livraison industrialisée.",
    "mcp.chapter": "Chapitre IV · Agents qui livrent",
    "mcp.lede": "Faire produire un PPT, un Word, un Excel — pas seulement une belle phrase.",
    "mcp.body":
      "Les équipes se lassent vite d’un agent qui explique sans jamais livrer. Elles veulent un support, un tableau, un deck. Les scripts jetables ne tiennent pas la distance : il fallait des outils réutilisables, et un moyen propre de récupérer le fichier.",
    "mcp.body2":
      "Un serveur MCP (FastMCP) expose la génération Office ; l’agent choisit l’outil, le document est construit, déposé en stockage objet, renvoyé via une URL signée. Le service se déploie en conteneur, à côté de la plateforme d’agents, sans coller tout le monde sur une machine unique.",
    "mcp.hr":
      "C’est le basculement net : l’agent ne se contente plus de parler, il produit quelque chose qu’on peut envoyer à un client ou à un manager.",
    "analyzer.chapter": "Chapitre V · Scan & distance",
    "analyzer.lede": "Lire un dépôt pour la qualité et la sécu — sans le verser entier dans le modèle.",
    "analyzer.body":
      "Dès qu’on parle de dette, de qualité ou de posture de sécurité sur un code, la tentation est d’envoyer tout le dépôt à un LLM. C’est cher, bruyant, et risqué. Ce qu’il faut, c’est un regard synthétique : un rapport sur lequel un humain — ou un agent — peut raisonner.",
    "analyzer.body2":
      "Un worker clone et parse le dépôt (Tree-sitter), expose une API, écrit un rapport structuré. L’orchestrateur IA ne voit que ce rapport, pas le source brut. Le tout se conteneurise et se déploie comme un service (Docker / EKS).",
    "analyzer.hr":
      "L’idée à retenir : faire travailler l’IA là où elle orchestre, et garder l’exécution bornée — surtout quand le sujet, c’est le code de l’entreprise.",
    "codium.chapter": "Chapitre VI · Plan & isolement",
    "codium.lede": "Accélérer la structure d’un pentest sans lâcher la main à un agent offensif.",
    "codium.body":
      "En cybersécurité offensive, on gagne du temps sur le plan, les notes, la forme des findings — mais on ne délègue pas le jugement. Personne ne veut d’un agent qui « pirate tout seul » sur le poste du quotidien.",
    "codium.body2":
      "L’architecture sépare volontairement deux plans : l’intelligence (l’agent qui aide à structurer) et l’exécution (outils en conteneurs, scanners type ZAP), reliés par un pont contrôlé, dans une logique OWASP. Ici, la vitrine reste méthodo et architecture — volontairement sans exploits.",
    "codium.hr":
      "Dernière marche du fil : montrer que l’IA et la cyber peuvent se croiser avec discipline — isolation, humain dans la boucle, pas de spectacle offensif.",
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
    "ronin.lede": "An AI translator that stays in the flow — on the desktop, then on Android.",
    "ronin.body":
      "When you write in mixed language or technical jargon, a mainstream translator tends to “improve” terms you meant to keep: product names, acronyms, fixed phrasing. Ronin came from that friction — a quiet, keyboard-first tool that leans on a glossary so protected wording stays put.",
    "ronin.body2":
      "I shipped it first as a desktop app (Python, light UI, PyInstaller-style packaging), wired to a local model or an API. Then the same product contract moved to mobile: a portable Android build in Kotlin, still terminal in spirit, so it wasn’t stuck at the desk.",
    "ronin.hr":
      "In the end this is the first step of the portfolio: show that I can ship a real small product, with one simple non-negotiable rule, and carry it across more than one platform.",
    "ronin.tag": "JSON glossary",
    "centinel.chapter": "Chapter II · Local memory",
    "centinel.lede": "Cyber memory that stays on the machine — prepare without exposing.",
    "centinel.body":
      "Before a mission you need to query dense frameworks quickly — ISO, DORA, GDPR, NIST, OWASP, PTES — without pushing sensitive documents into a public LLM. And a wall of text barely helps in the field: you need something you can follow.",
    "centinel.body2":
      "Centinel indexes those PDFs locally, answers in natural language through an offline model, and shapes methodology answers into phases. Compliance rules and execution guides stay distinct so the output stays readable.",
    "centinel.hr":
      "This is where a tool becomes a knowledge system: useful for cyber work, with offline as the starting constraint, not a late add-on.",
    "voice.chapter": "Chapter III · Voice & GenAI",
    "voice.lede": "When a phone journey isn’t enough, and GenAI has to plug in without breaking it.",
    "voice.body":
      "A path-locked callbot works until the caller leaves the script. The point wasn’t to sprinkle AI for show — it was to open the dialogue while keeping a solid contact-center base: Connect, Lex, journeys already in place.",
    "voice.body2":
      "I worked an additive GenAI layer on AWS (Lambda, short conversation memory, Bedrock), attached to the existing bot instead of replacing it overnight. Terraform, separated environments, staging: you can compare, roll back, move forward without burning the channel.",
    "voice.hr":
      "This chapter is mainly about a reasonable modernization of a voice customer channel — cloud GenAI, but respect for what already runs and how you ship it.",
    "mcp.chapter": "Chapter IV · Agents that deliver",
    "mcp.lede": "Make the chat produce a deck, a Word file, a spreadsheet — not only a nice sentence.",
    "mcp.body":
      "Teams tire quickly of an agent that explains and never ships. They want a slide, a table, a document. Throwaway scripts don’t last: we needed reusable tools, and a clean way to get the file back.",
    "mcp.body2":
      "An MCP server (FastMCP) exposes Office generation; the agent picks the tool, the document is built, stored in object storage, returned as a signed URL. The service deploys in a container next to the agent platform, instead of living on one laptop.",
    "mcp.hr":
      "That’s the clear shift: the agent doesn’t only talk — it produces something you can send to a client or a manager.",
    "analyzer.chapter": "Chapter V · Scan & distance",
    "analyzer.lede": "Read a repository for quality and security — without pouring it all into the model.",
    "analyzer.body":
      "When the topic is debt, quality, or security posture on a codebase, the temptation is to dump the whole repo into an LLM. That’s costly, noisy, and risky. What you want is a synthetic view: a report a human — or an agent — can reason over.",
    "analyzer.body2":
      "A worker clones and parses the repo (Tree-sitter), exposes an API, writes a structured report. The AI orchestrator only sees that report, not raw source. It containerizes and deploys like a service (Docker / EKS).",
    "analyzer.hr":
      "The takeaway: let AI orchestrate, keep execution bounded — especially when the subject is the company’s own code.",
    "codium.chapter": "Chapter VI · Plan & isolation",
    "codium.lede": "Speed up pentest structure without handing the keys to an offensive agent.",
    "codium.body":
      "In offensive security you can save time on the plan, the notes, the shape of findings — but you don’t outsource judgment. Nobody wants an agent that “hacks alone” on the daily workstation.",
    "codium.body2":
      "The architecture deliberately splits two planes: intelligence (the agent that helps structure) and execution (tools in containers, scanners such as ZAP), linked by a controlled bridge, in an OWASP mindset. The public showcase stays methodology and architecture — on purpose, with no exploits.",
    "codium.hr":
      "Last step in the thread: show that AI and cyber can meet with discipline — isolation, human in the loop, no offensive theatre.",
    "close.chapter": "End",
    "close.title": "EOF — your move.",
    "close.body":
      "Agents act. Humans decide. If this build × cyber thread lands, write me.",
    "soon.link": "GitHub showcase (no source) →",
    "soon.linkMethod": "Method showcase on GitHub (no exploits) →",
  },
};
