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
    "ronin.lede": "Un traducteur IA sur le bureau — discret, fidèle au glossaire.",
    "ronin.body":
      "L’idée est simple : rester dans le flux quand on écrit en franglais ou en jargon métier. Ronin traduit avec un modèle, mais protège les termes qu’on ne doit pas « améliorer ». Interface minimale, packaging desktop — la première marche : un produit local qui tient dans la main.",
    "ronin.tag": "Glossaire JSON",
    "centinel.chapter": "Chapitre II · Mémoire locale",
    "centinel.lede": "Une base de connaissance cyber qui ne quitte pas la machine.",
    "centinel.body":
      "ISO, DORA, RGPD, NIST, OWASP — ingérés en PDF, indexés en local, interrogés en langage naturel via un LLM offline. Quand la question touche à la méthodo, la réponse se structure en phases. C’est le passage du « petit outil » au « système qui sait lire et restituer » sans exposer les docs au cloud.",
    "voice.chapter": "Chapitre III · Voix & GenAI",
    "voice.lede":
      "D’un callbot à parcours figé vers une conversation GenAI sur AWS.",
    "voice.body":
      "Le passage intéressant n’est pas « ajouter un LLM ». C’est faire évoluer un bot téléphonique scripté / à parcours vers une couche GenAI : compréhension plus naturelle, branches moins rigides, tout en restant sur un socle cloud (contact center, NLU, serverless, IaC). Architecture et staging sur AWS — le détail métier reste hors scope ici.",
    "mcp.chapter": "Chapitre IV · Agents qui livrent",
    "mcp.lede": "Du chat qui parle au chat qui produit un PPT, un Word, un Excel.",
    "mcp.body":
      "Un serveur MCP expose des outils de génération documentaire ; l’agent choisit, construit, dépose le fichier, renvoie une URL signée. Conteneurisé, déployable à côté d’une plateforme d’agents. C’est la suite logique de Voice Assist : même famille GenAI, mais l’output n’est plus une phrase — c’est un livrable.",
    "analyzer.chapter": "Chapitre V · Scan & distance",
    "analyzer.lede":
      "Un code analyzer : n’importe quel dépôt comme cible — qualité et sécurité.",
    "analyzer.body":
      "Le worker clone et parse le repo (Tree-sitter), produit un rapport structuré ; l’agent ne voit que ce rapport, pas le source brut. Objectif : signaux de qualité de code et de posture sécu sur une base quelconque. Même idée que plus haut — l’IA orchestre, l’exécution reste bornée.",
    "codium.chapter": "Chapitre VI · Plan & isolement",
    "codium.lede":
      "Pentest assisté par IA — intelligence d’un côté, exécution isolée de l’autre.",
    "codium.body":
      "Le fil s’arrête (pour l’instant) sur une idée d’architecture : un agent qui planifie et rédige, un environnement conteneurisé qui exécute l’outillage offensif, un humain qui valide. Assez pour montrer la discipline ; volontairement trop peu pour exposer lab ou exploits. La cybersécurité, ici, c’est d’abord la séparation des plans.",
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
    "ronin.lede": "A desktop AI translator — quiet, glossary-true.",
    "ronin.body":
      "The idea is simple: stay in flow when writing in mixed language or domain jargon. Ronin translates with a model, but protects terms that must not be “improved”. Minimal UI, desktop packaging — the first step: a local product you can hold.",
    "ronin.tag": "JSON glossary",
    "centinel.chapter": "Chapter II · Local memory",
    "centinel.lede": "A cyber knowledge base that never leaves the machine.",
    "centinel.body":
      "ISO, DORA, GDPR, NIST, OWASP — ingested as PDFs, indexed locally, queried in natural language via an offline LLM. Methodology questions get phased answers. The jump from “small tool” to “a system that can read and restate” without exposing docs to the cloud.",
    "voice.chapter": "Chapter III · Voice & GenAI",
    "voice.lede":
      "From a path-based callbot to GenAI conversation on AWS.",
    "voice.body":
      "The interesting move isn’t “drop in an LLM”. It’s evolving a scripted / journey-based phone bot toward a GenAI layer: more natural understanding, less rigid branching, still on a cloud foundation (contact center, NLU, serverless, IaC). Architecture and staging on AWS — business-domain detail stays out of scope here.",
    "mcp.chapter": "Chapter IV · Agents that deliver",
    "mcp.lede": "From a chat that talks to a chat that ships PPT, Word, Excel.",
    "mcp.body":
      "An MCP server exposes document-generation tools; the agent picks, builds, stores the file, returns a signed URL. Containerized, deployable next to an agent platform. The logical follow-up to Voice Assist: same GenAI family, but the output is no longer a sentence — it’s a deliverable.",
    "analyzer.chapter": "Chapter V · Scan & distance",
    "analyzer.lede":
      "A code analyzer: any repo as the scan target — quality and security.",
    "analyzer.body":
      "The worker clones and parses the repo (Tree-sitter), emits a structured report; the agent only sees that report, not raw source. Goal: code-quality and security-posture signals on whatever codebase you point at. Same idea as above — AI orchestrates, execution stays bounded.",
    "codium.chapter": "Chapter VI · Plan & isolation",
    "codium.lede":
      "AI-assisted pentest — intelligence on one side, isolated execution on the other.",
    "codium.body":
      "The thread stops (for now) on an architecture idea: an agent that plans and writes, a containerized environment that runs offensive tooling, a human who validates. Enough to show discipline; deliberately too little to expose labs or exploits. Cybersecurity here is first about separating the planes.",
    "close.chapter": "End",
    "close.title": "EOF — your move.",
    "close.body":
      "Agents act. Humans decide. If this build × cyber thread lands, write me.",
    "soon.link": "GitHub showcase (no source) →",
    "soon.linkMethod": "Method showcase on GitHub (no exploits) →",
  },
};
