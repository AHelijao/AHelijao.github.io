window.I18N = {
  fr: {
    "meta.desc":
      "Une histoire d’intérêts techniques — du desktop local aux agents et à la cybersécurité.",
    "rail.aria": "Portfolio — défilement horizontal",
    "nav.prev": "Précédent",
    "nav.next": "Suivant",
    "cover.line": "Engineer in Cybersecurity and Software AI",
    "cover.edgeHint": "Suivant",
    "who.chapter": "Qui",
    "who.title": "Engineer in Cybersecurity and Software AI",
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
    "thread.ronin": "Traducteur IA desktop, glossaire verrouillé.",
    "thread.centinel": "Modèle cyber spécialisé sur les référentiels.",
    "thread.voice": "GenAI sur callbot Connect+Lex, sans données perso.",
    "thread.mcp": "Livrables Office via MCP — SSO, IRSA, URL bornée.",
    "thread.analyzer": "Scan dépôt → Spec sheet, hors du modèle.",
    "thread.codium": "Assistant pentest IDE, Kali isolé, humain dans la boucle.",
    "ronin.chapter": "Chapitre I · Fondations",
    "ronin.lede": "Un traducteur IA qui reste dans le flux — sur le bureau, puis sur Android.",
    "ronin.body":
      "Quand on écrit en franglais ou en jargon technique, un traducteur classique a tendance à « améliorer » des termes qu’on voulait garder : noms de produits, acronymes, formulations figées. Ronin est né de ce frottement — un outil discret, clavier d’abord, qui s’appuie sur un glossaire pour protéger ce qui ne doit pas bouger.",
    "ronin.body2":
      "Je l’ai d’abord livré en application desktop (Python, interface légère, packaging type PyInstaller), branchée sur un modèle local ou une API. Puis le même contrat produit a suivi sur mobile : une version portable Android en Kotlin, toujours dans un esprit terminal, pour ne pas rester coincé au poste.",
    "ronin.hr":
      "Au fond, c’est la première marche du portfolio : prouver qu’on sait sortir un vrai petit produit, avec une règle métier simple mais non négociable, et le faire vivre sur plus d’une plateforme.",
    "ronin.tag": "Glossaire JSON",
    "arch.caption": "Architecture",
    "centinel.chapter": "Chapitre II · Modèle spécialisé",
    "centinel.lede": "Une IA cyber entraînée sur les référentiels — pas un chat générique sur des PDF.",
    "centinel.body":
      "Avant une mission, on a besoin d’interroger vite des référentiels denses — ISO, DORA, RGPD, NIST, OWASP, PTES — sans dépendre d’un LLM public qui n’a pas ces cadres en tête. Un mur de texte ne sert presque à rien sur le terrain : il faut quelque chose qu’on peut suivre.",
    "centinel.body2":
      "J’ai pris une base Abliterated Qwen3 sur Hugging Face, puis un notebook Google Colab avec Unsloth pour tout le pipeline d’entraînement — préparer le dataset, fine-tune (LoRA/SFT), éval / export — sur le corpus de refs cyber. En sortie : un modèle local spécialisé sur ces référentiels, avec des réponses orientées méthodo.",
    "centinel.hr":
      "C’est le moment où l’outil devient un vrai spécialiste : les refs sont le point, pas un add-on — utile au métier cyber, prêt mission.",
    "voice.chapter": "Chapitre III · Voix & GenAI",
    "voice.lede": "Quand le parcours téléphonique ne suffit plus, et que la GenAI doit s’y greffer sans tout casser.",
    "voice.body":
      "Un callbot à parcours figé marche tant que l’appelant suit le script. Dès qu’il digresse, le dialogue se brise. L’enjeu n’était pas d’ajouter de l’IA pour la forme, mais d’ouvrir la conversation tout en gardant un contact center solide — Connect, Lex, les parcours déjà en place.",
    "voice.body2":
      "J’ai travaillé une couche GenAI additive sur AWS (Lambda, mémoire courte de conversation, Bedrock), branchée sur le bot existant plutôt que de le remplacer d’un bloc. Terraform, environnements séparés, staging : on peut comparer, reculer, avancer sans brûler le canal.",
    "voice.hr":
      "Contrainte non négociable : aucun accès aux données personnelles — expliquer et guider seulement, isolé du bot scripté live. GenAI cloud, mais bornée, et livrée sans brûler le canal.",
    "mcp.chapter": "Chapitre IV · Agents qui livrent",
    "mcp.lede": "Faire produire un PPT, un Word, un Excel — avec une vraie chaîne d’identité.",
    "mcp.body":
      "Les équipes se lassent vite d’un agent qui explique sans jamais livrer. Elles veulent un support, un tableau, un deck. Les scripts jetables ne tiennent pas : il fallait des outils réutilisables, et un moyen propre de récupérer le fichier — sans clé partagée ni bucket ouvert.",
    "mcp.body2":
      "OpenWebUI tient la porte (session / SSO). Un serveur MCP (FastMCP) génère le livrable Office ; côté AWS, le worker tourne sous un rôle IAM via IRSA — moindre privilège, écriture S3 bornée, pas de secrets longue durée. Le fichier revient en URL présignée liée à l’utilisateur qui a demandé.",
    "mcp.hr":
      "Fil IAM : identité de session → IRSA → S3 → URL signée user-scoped. L’agent ne parle plus seulement — il livre, sous contrôle d’accès.",
    "analyzer.chapter": "Chapitre V · Scan & distance",
    "analyzer.lede": "Qualifier un dépôt — qualité et posture sécu — sans le verser entier dans le modèle.",
    "analyzer.body":
      "Dès qu’on parle dette, qualité ou posture de sécurité sur un code, la tentation est d’envoyer tout le dépôt à un LLM. C’est cher, bruyant, et risqué. Ce qu’il faut : un regard synthétique. L’utilisateur arrive depuis n’importe quel chat (OWUI, local, cloud) avec un lien GitHub, GitLab ou Bitbucket ; n8n + l’IA câblent le job.",
    "analyzer.body2":
      "Le MCP prend le relais : Tree-sitter lit l’arbre du code, puis descend niveau par niveau. On peut trancher dans le temps — début de projet, +2 mois, +1 an — et scorer la qualité via la complexité cyclomatique, avec des signaux sécurité. Seule une Spec sheet structurée revient au chat : ce qu’est le projet, utile pour un développeur.",
    "analyzer.hr":
      "L’idée à retenir : l’IA orchestre, le MCP exécute, le source reste hors du modèle. La Spec sheet est le contrat — pas un dump de dépôt.",
    "codium.chapter": "Chapitre VI · Plan & isolement",
    "codium.lede": "Un assistant pentest IA dans l’IDE — moteur Kali local, chaque action sous approbation humaine.",
    "codium.body":
      "L’idée : un IDE type Cursor, branché à une IA, pour engager une appli web. Derrière, un moteur conteneur isolé — Kali en CLI avec outils pentest, playground Python vide, serveur HTTP, VPN discret. L’IA s’en sert pour se connecter à la cible, lever un serveur, écrire son propre code Python, enchaîner l’engagement.",
    "codium.body2":
      "L’agent est borné : restrictions + dictionnaire méthodo nourri de PTES, MITRE ATT&CK et CVE. Chaque action attend l’approbation du pentester. En fin de run : un rapport de findings. Le moteur est local d’abord, intégrable en cloud. La vitrine reste méthodo et architecture — volontairement sans exploits.",
    "codium.hr":
      "Dernière marche : IDE + IA planifient, le conteneur exécute, l’humain garde la main — isolation, pas de spectacle offensif.",
    "close.chapter": "Contact",
    "close.title": "On en parle.",
    "close.p1":
      "Vous venez de parcourir six projets — du desktop local aux agents, du cloud GenAI au pentest assisté. Le fil commun : construire des systèmes utiles, et les border dès le design.",
    "close.p2":
      "Je cherche des missions et des équipes où software engineering et cybersécurité se croisent vraiment — AppSec, agents GenAI bornés, infra cloud, méthodo offensive avec un humain dans la boucle.",
    "close.p3":
      "Un poste, une collab, une question sur un projet : écrivez-moi. Les vitrines GitHub sont sanitizées ; le détail et le code, on en discute directement.",
    "soon.link": "Vitrine GitHub (sans code source) →",
    "soon.linkMethod": "Vitrine méthodo GitHub (sans exploits) →",
  },
  en: {
    "meta.desc":
      "A story of technical interests — from local desktop tools to agents and cybersecurity.",
    "rail.aria": "Portfolio — horizontal scroll",
    "nav.prev": "Previous",
    "nav.next": "Next",
    "cover.line": "Engineer in Cybersecurity and Software AI",
    "cover.edgeHint": "Next",
    "who.chapter": "Who",
    "who.title": "Engineer in Cybersecurity and Software AI",
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
    "thread.ronin": "Desktop AI translator with a locked glossary.",
    "thread.centinel": "Cyber model specialized on the frameworks.",
    "thread.voice": "GenAI on Connect+Lex callbot, no personal data.",
    "thread.mcp": "Office deliverables via MCP — SSO, IRSA, scoped URL.",
    "thread.analyzer": "Repo scan → Spec sheet, source stays out of the model.",
    "thread.codium": "IDE pentest assistant, isolated Kali, human in the loop.",
    "ronin.chapter": "Chapter I · Foundations",
    "ronin.lede": "An AI translator that stays in the flow — on the desktop, then on Android.",
    "ronin.body":
      "When you write in mixed language or technical jargon, a mainstream translator tends to “improve” terms you meant to keep: product names, acronyms, fixed phrasing. Ronin came from that friction — a quiet, keyboard-first tool that leans on a glossary so protected wording stays put.",
    "ronin.body2":
      "I shipped it first as a desktop app (Python, light UI, PyInstaller-style packaging), wired to a local model or an API. Then the same product contract moved to mobile: a portable Android build in Kotlin, still terminal in spirit, so it wasn’t stuck at the desk.",
    "ronin.hr":
      "In the end this is the first step of the portfolio: show that I can ship a real small product, with one simple non-negotiable rule, and carry it across more than one platform.",
    "ronin.tag": "JSON glossary",
    "arch.caption": "Architecture",
    "centinel.chapter": "Chapter II · Specialized model",
    "centinel.lede": "A cyber AI trained on the frameworks — not generic chat over PDFs.",
    "centinel.body":
      "Before a mission you need to query dense frameworks quickly — ISO, DORA, GDPR, NIST, OWASP, PTES — without depending on a public LLM that doesn’t really know those refs. A wall of text barely helps in the field: you need something you can follow.",
    "centinel.body2":
      "I pulled an Abliterated Qwen3 base from Hugging Face, then ran a Google Colab notebook with Unsloth for the full training pipeline — prepare dataset, fine-tune (LoRA/SFT), eval / export — on the cyber refs corpus. The output is a local model specialized on those frameworks, with methodology-aware answers.",
    "centinel.hr":
      "This is where the tool becomes a real specialist: the refs are the point, not an add-on — useful for cyber work, mission-ready.",
    "voice.chapter": "Chapter III · Voice & GenAI",
    "voice.lede": "When a phone journey isn’t enough, and GenAI has to plug in without breaking it.",
    "voice.body":
      "A path-locked callbot works until the caller leaves the script. The point wasn’t to sprinkle AI for show — it was to open the dialogue while keeping a solid contact-center base: Connect, Lex, journeys already in place.",
    "voice.body2":
      "I worked an additive GenAI layer on AWS (Lambda, short conversation memory, Bedrock), attached to the existing bot instead of replacing it overnight. Terraform, separated environments, staging: you can compare, roll back, move forward without burning the channel.",
    "voice.hr":
      "Non-negotiable constraint: no personal-data access — explain and guide only, isolated from the live scripted bot. Cloud GenAI, but bounded, shipped without burning the channel.",
    "mcp.chapter": "Chapter IV · Agents that deliver",
    "mcp.lede": "Make the chat produce a deck, a Word, an Excel — with a real identity chain.",
    "mcp.body":
      "Teams tire quickly of an agent that explains and never ships. They want a slide, a table, a document. Throwaway scripts don’t last: we needed reusable tools, and a clean way to get the file back — without shared keys or an open bucket.",
    "mcp.body2":
      "OpenWebUI holds the gate (session / SSO). An MCP server (FastMCP) builds the Office deliverable; in AWS the worker runs under an IAM role via IRSA — least privilege, scoped S3 write, no long-lived secrets. The file returns as a user-scoped presigned URL for the requester only.",
    "mcp.hr":
      "IAM thread: session identity → IRSA → S3 → user-scoped signed URL. The agent doesn’t only talk — it delivers under access control.",
    "analyzer.chapter": "Chapter V · Scan & distance",
    "analyzer.lede": "Qualify a repository — quality and security posture — without pouring it into the model.",
    "analyzer.body":
      "When the topic is debt, quality, or security posture on a codebase, the temptation is to dump the whole repo into an LLM. That’s costly, noisy, and risky. What you want is a synthetic view. The user comes from whatever chat they already use (OWUI, local, cloud) with a GitHub, GitLab, or Bitbucket link; n8n + AI wire the job.",
    "analyzer.body2":
      "MCP takes over: Tree-sitter reads the code tree first, then drills level by level. Scans can be sliced in time — project start, +2 months, +1 year — and quality scored with cyclomatic complexity plus security-relevant signals. Only a structured Spec sheet returns to the chat: what this project is, something a developer can use.",
    "analyzer.hr":
      "The takeaway: AI orchestrates, MCP executes, source stays out of the model. The Spec sheet is the contract — not a raw dump of the repo.",
    "codium.chapter": "Chapter VI · Plan & isolation",
    "codium.lede": "An AI pentest assistant in the IDE — local Kali engine, every action under human approval.",
    "codium.body":
      "The idea: a Cursor-like IDE wired to an AI, aimed at any web app. Behind it, an isolated container engine — Kali CLI with pentest tools, an empty Python playground, an HTTP server, a stealth VPN. The AI uses that engine to reach the target, stand up a server, write its own Python, and run the engagement.",
    "codium.body2":
      "The agent is bounded: restrictions plus a methodology dictionary fed with PTES, MITRE ATT&CK, and CVE docs. Every action waits for the pentester’s approval. When the run finishes: a findings report. The engine is local first, cloud-integrable. The public showcase stays methodology and architecture — on purpose, with no exploits.",
    "codium.hr":
      "Last step: IDE + AI plan, the container executes, the human keeps the keys — isolation, no offensive theatre.",
    "close.chapter": "Contact",
    "close.title": "Let’s talk.",
    "close.p1":
      "You’ve just walked six projects — from local desktop tools to agents, cloud GenAI to AI-assisted pentest. The common thread: build systems that are useful, and bound them in the design.",
    "close.p2":
      "I’m looking for missions and teams where software engineering and cybersecurity actually meet — AppSec, bounded GenAI agents, cloud infra, offensive methodology with a human in the loop.",
    "close.p3":
      "A role, a collab, a question on a project: write me. The GitHub showcases are sanitized; depth and source are a conversation, not a public dump.",
    "soon.link": "GitHub showcase (no source) →",
    "soon.linkMethod": "Method showcase on GitHub (no exploits) →",
  },
};
