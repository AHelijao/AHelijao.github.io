"""Build EN/FR architecture SVGs with stronger type + arrows."""
from pathlib import Path

OUT = Path(__file__).resolve().parent / "assets"
OUT.mkdir(exist_ok=True)

DEFS = """
  <defs>
    <marker id="a" viewBox="0 0 12 12" refX="10" refY="6" markerWidth="10" markerHeight="10" orient="auto-start-reverse">
      <path d="M1 1 L11 6 L1 11 Z" fill="#111"/>
    </marker>
    <style>
      .bg { fill:#fffcf6; }
      .b { fill:#f4f0e6; stroke:#111; stroke-width:2; }
      .hi { fill:#fff; stroke:#111; stroke-width:2.4; }
      .out { fill:none; stroke:#111; stroke-width:1.6; stroke-dasharray:6 5; }
      .plane { fill:none; stroke:#111; stroke-width:1.8; stroke-dasharray:7 5; }
      .cloud { fill:none; stroke:#111; stroke-width:1.6; stroke-dasharray:6 5; }
      .title { font-family:Segoe UI,system-ui,sans-serif; font-size:15px; font-weight:800; letter-spacing:0.08em; fill:#111; }
      .lab { font-family:Segoe UI,system-ui,sans-serif; font-size:14.5px; font-weight:800; fill:#111; }
      .sub { font-family:Segoe UI,system-ui,sans-serif; font-size:11.5px; font-weight:500; fill:#3a3a3a; }
      .cap { font-family:Segoe UI,system-ui,sans-serif; font-size:11px; font-weight:800; letter-spacing:0.12em; fill:#111; }
      .line {
        stroke:#111; stroke-width:2.2; fill:none; marker-end:url(#a);
        stroke-linecap:round; stroke-linejoin:round;
        stroke-dasharray:9 11;
        animation: flow 1.05s linear infinite;
      }
      /* RAG / corpus / ingest: slower packets */
      .line.ingest {
        stroke-dasharray: 4 16;
        animation: flow 1.7s linear infinite;
      }
      /* Return / report path: slightly quicker */
      .line.return {
        stroke-dasharray: 10 8;
        animation: flow 0.85s linear infinite;
      }
      .line.stem {
        marker-end: none;
        stroke-dasharray: 9 11;
        animation: flow 1.05s linear infinite;
      }
      .hi.pulse {
        animation: node-pulse 2.6s ease-in-out infinite;
      }
      .lbl.flow-lbl {
        animation: lbl-pulse 2.2s ease-in-out infinite;
      }
      .lbl { font-family:Segoe UI,system-ui,sans-serif; font-size:11px; font-weight:700; fill:#111; }
      .foot { font-family:Segoe UI,system-ui,sans-serif; font-size:11.5px; font-weight:600; fill:#3a3a3a; }
      @keyframes flow {
        to { stroke-dashoffset: -20; }
      }
      @keyframes node-pulse {
        0%, 100% { stroke-width: 2.4; }
        50% { stroke-width: 3.4; }
      }
      @keyframes lbl-pulse {
        0%, 100% { opacity: 0.55; }
        50% { opacity: 1; }
      }
      @media (prefers-reduced-motion: reduce) {
        .line, .line.ingest, .line.return, .line.stem, .hi.pulse, .lbl.flow-lbl { animation: none; }
        .line, .line.ingest, .line.return, .line.stem { stroke-dasharray: none; }
      }
    </style>
  </defs>
""".strip()


def save(stem: str, lang: str, body: str, title: str, desc: str) -> None:
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 560 360" role="img" aria-labelledby="t d">
  <title id="t">{title}</title>
  <desc id="d">{desc}</desc>
{DEFS}
  <rect class="bg" width="560" height="360"/>
{body}
</svg>
"""
    path = OUT / f"arch-{stem}.{lang}.svg"
    path.write_text(svg, encoding="utf-8", newline="\n")
    print("ok", path.name)


# --- RONIN ---
save(
    "ronin",
    "en",
    """
  <text x="24" y="30" class="title">TWO SHELLS / SHARED GLOSSARY</text>

  <rect class="out" x="24" y="48" width="248" height="236" rx="14"/>
  <text x="40" y="74" class="cap">DESKTOP - LOCAL AI</text>
  <rect class="b" x="48" y="90" width="200" height="48" rx="10"/>
  <text x="148" y="112" text-anchor="middle" class="lab">Desktop UI</text>
  <text x="148" y="128" text-anchor="middle" class="sub">Python / light UI</text>
  <line class="line" x1="148" y1="138" x2="148" y2="164"/>
  <rect class="b" x="48" y="164" width="200" height="48" rx="10"/>
  <text x="148" y="186" text-anchor="middle" class="lab">Glossary filter</text>
  <text x="148" y="202" text-anchor="middle" class="sub">terms kept untouched</text>
  <line class="line" x1="148" y1="212" x2="148" y2="238"/>
  <rect class="hi" x="48" y="238" width="200" height="36" rx="10"/>
  <text x="148" y="261" text-anchor="middle" class="lab">Local LLM</text>

  <rect class="out" x="288" y="48" width="248" height="236" rx="14"/>
  <text x="304" y="74" class="cap">ANDROID - CLOUD LLM</text>
  <rect class="b" x="312" y="90" width="200" height="48" rx="10"/>
  <text x="412" y="112" text-anchor="middle" class="lab">Android UI</text>
  <text x="412" y="128" text-anchor="middle" class="sub">Kotlin / portable</text>
  <line class="line" x1="412" y1="138" x2="412" y2="164"/>
  <rect class="b" x="312" y="164" width="200" height="48" rx="10"/>
  <text x="412" y="186" text-anchor="middle" class="lab">Glossary filter</text>
  <text x="412" y="202" text-anchor="middle" class="sub">same protected terms</text>
  <line class="line" x1="412" y1="212" x2="412" y2="238"/>
  <rect class="hi" x="312" y="238" width="200" height="36" rx="10"/>
  <text x="412" y="261" text-anchor="middle" class="lab">Cloud LLM API</text>

  <rect class="b" x="80" y="308" width="400" height="34" rx="8"/>
  <text x="280" y="330" text-anchor="middle" class="foot">Glossary = list of terms that must stay unchanged</text>
""",
    "Ronin architecture",
    "Desktop uses local AI; Android calls a cloud LLM API. Shared glossary of protected terms.",
)

save(
    "ronin",
    "fr",
    """
  <text x="24" y="30" class="title">DEUX COQUES / GLOSSAIRE PARTAGÉ</text>

  <rect class="out" x="24" y="48" width="248" height="236" rx="14"/>
  <text x="40" y="74" class="cap">DESKTOP - IA LOCALE</text>
  <rect class="b" x="48" y="90" width="200" height="48" rx="10"/>
  <text x="148" y="112" text-anchor="middle" class="lab">Interface desktop</text>
  <text x="148" y="128" text-anchor="middle" class="sub">Python / UI légère</text>
  <line class="line" x1="148" y1="138" x2="148" y2="164"/>
  <rect class="b" x="48" y="164" width="200" height="48" rx="10"/>
  <text x="148" y="186" text-anchor="middle" class="lab">Filtre glossaire</text>
  <text x="148" y="202" text-anchor="middle" class="sub">termes à préserver</text>
  <line class="line" x1="148" y1="212" x2="148" y2="238"/>
  <rect class="hi" x="48" y="238" width="200" height="36" rx="10"/>
  <text x="148" y="261" text-anchor="middle" class="lab">LLM local</text>

  <rect class="out" x="288" y="48" width="248" height="236" rx="14"/>
  <text x="304" y="74" class="cap">ANDROID - LLM CLOUD</text>
  <rect class="b" x="312" y="90" width="200" height="48" rx="10"/>
  <text x="412" y="112" text-anchor="middle" class="lab">Interface Android</text>
  <text x="412" y="128" text-anchor="middle" class="sub">Kotlin / portable</text>
  <line class="line" x1="412" y1="138" x2="412" y2="164"/>
  <rect class="b" x="312" y="164" width="200" height="48" rx="10"/>
  <text x="412" y="186" text-anchor="middle" class="lab">Filtre glossaire</text>
  <text x="412" y="202" text-anchor="middle" class="sub">mêmes termes protégés</text>
  <line class="line" x1="412" y1="212" x2="412" y2="238"/>
  <rect class="hi" x="312" y="238" width="200" height="36" rx="10"/>
  <text x="412" y="261" text-anchor="middle" class="lab">API LLM cloud</text>

  <rect class="b" x="80" y="308" width="400" height="34" rx="8"/>
  <text x="280" y="330" text-anchor="middle" class="foot">Glossaire = liste de termes qui ne doivent pas changer</text>
""",
    "Architecture Ronin",
    "Le desktop utilise une IA locale ; Android appelle une API LLM cloud. Glossaire partagé de termes protégés.",
)

# --- CENTINEL ---
save(
    "centinel",
    "en",
    """
  <text x="24" y="30" class="title">SPECIALIZED LOCAL CYBER AI</text>
  <rect class="out" x="24" y="46" width="512" height="288" rx="14"/>
  <text x="40" y="72" class="foot">Offline machine - cyber refs never leave</text>

  <rect class="b" x="56" y="96" width="160" height="64" rx="10"/>
  <text x="136" y="122" text-anchor="middle" class="lab">Cyber PDF corpus</text>
  <text x="136" y="140" text-anchor="middle" class="sub">ISO / NIST / OWASP...</text>

  <line class="line ingest" x1="216" y1="128" x2="258" y2="128"/>
  <text x="224" y="116" class="lbl flow-lbl">manual feed</text>

  <rect class="b" x="262" y="96" width="168" height="64" rx="10"/>
  <text x="346" y="122" text-anchor="middle" class="lab">Specialization</text>
  <text x="346" y="140" text-anchor="middle" class="sub">train / ground on refs</text>

  <path class="line ingest" d="M346 160 V182 H280 V206"/>

  <rect class="hi pulse" x="150" y="206" width="260" height="88" rx="12"/>
  <text x="280" y="238" text-anchor="middle" class="lab">AI Cyber specialist</text>
  <text x="280" y="258" text-anchor="middle" class="sub">local model shaped for cyber work</text>
  <text x="280" y="276" text-anchor="middle" class="sub">methodology-aware answers</text>

  <text x="48" y="318" class="foot">Not generic chat over files - a local cyber specialist.</text>
""",
    "Centinel architecture",
    "Cyber PDFs fed offline to specialize a local AI cyber assistant.",
)

save(
    "centinel",
    "fr",
    """
  <text x="24" y="30" class="title">IA CYBER LOCALE SPÉCIALISÉE</text>
  <rect class="out" x="24" y="46" width="512" height="288" rx="14"/>
  <text x="40" y="72" class="foot">Machine hors-ligne - les refs cyber ne sortent pas</text>

  <rect class="b" x="56" y="96" width="160" height="64" rx="10"/>
  <text x="136" y="122" text-anchor="middle" class="lab">Corpus PDF cyber</text>
  <text x="136" y="140" text-anchor="middle" class="sub">ISO / NIST / OWASP...</text>

  <line class="line ingest" x1="216" y1="128" x2="258" y2="128"/>
  <text x="218" y="116" class="lbl flow-lbl">alimentation manuelle</text>

  <rect class="b" x="262" y="96" width="168" height="64" rx="10"/>
  <text x="346" y="122" text-anchor="middle" class="lab">Spécialisation</text>
  <text x="346" y="140" text-anchor="middle" class="sub">entraînement / ancrage</text>

  <path class="line ingest" d="M346 160 V182 H280 V206"/>

  <rect class="hi pulse" x="150" y="206" width="260" height="88" rx="12"/>
  <text x="280" y="238" text-anchor="middle" class="lab">Spécialiste IA cyber</text>
  <text x="280" y="258" text-anchor="middle" class="sub">modèle local façonné pour le cyber</text>
  <text x="280" y="276" text-anchor="middle" class="sub">réponses orientées méthodo</text>

  <text x="48" y="318" class="foot">Pas un chat générique sur des fichiers - un spécialiste cyber local.</text>
""",
    "Architecture Centinel",
    "PDFs cyber alimentés hors-ligne pour spécialiser une IA cyber locale.",
)

# --- VOICE ---
save(
    "voice",
    "en",
    """
  <text x="24" y="30" class="title">ONE BASELINE / TWO GENAI PROTOTYPES</text>

  <rect class="b" x="200" y="48" width="160" height="36" rx="10"/>
  <text x="280" y="72" text-anchor="middle" class="lab">Caller</text>
  <line class="line" x1="280" y1="84" x2="280" y2="106"/>

  <rect class="hi" x="140" y="106" width="280" height="48" rx="10"/>
  <text x="280" y="128" text-anchor="middle" class="lab">Amazon Connect + Lex</text>
  <text x="280" y="144" text-anchor="middle" class="sub">shared contact-center baseline</text>

  <path class="line" d="M200 154 V170 H150 V186"/>
  <path class="line" d="M360 154 V170 H410 V186"/>

  <rect class="out" x="36" y="186" width="224" height="132" rx="12"/>
  <text x="52" y="210" class="cap">PROTOTYPE A</text>
  <rect class="hi" x="52" y="222" width="192" height="78" rx="10"/>
  <text x="148" y="250" text-anchor="middle" class="lab">Connect-native GenAI</text>
  <text x="148" y="270" text-anchor="middle" class="sub">GenAI inside Connect</text>
  <text x="148" y="286" text-anchor="middle" class="sub">native conversation path</text>

  <rect class="out" x="300" y="186" width="224" height="132" rx="12"/>
  <text x="316" y="210" class="cap">PROTOTYPE B</text>
  <rect class="hi" x="316" y="222" width="192" height="78" rx="10"/>
  <text x="412" y="250" text-anchor="middle" class="lab">Custom Lambda GenAI</text>
  <text x="412" y="270" text-anchor="middle" class="sub">Lambda brain + memory</text>
  <text x="412" y="286" text-anchor="middle" class="sub">Bedrock / managed LLM</text>

  <text x="24" y="342" class="foot">Same entry. Two ways to attach GenAI without rewriting the parcours.</text>
""",
    "GenAI Voice Assist architecture",
    "Shared Connect+Lex baseline with Connect-native and custom Lambda GenAI prototypes.",
)

save(
    "voice",
    "fr",
    """
  <text x="24" y="30" class="title">UNE BASE / DEUX PROTOTYPES GENAI</text>

  <rect class="b" x="200" y="48" width="160" height="36" rx="10"/>
  <text x="280" y="72" text-anchor="middle" class="lab">Appelant</text>
  <line class="line" x1="280" y1="84" x2="280" y2="106"/>

  <rect class="hi" x="140" y="106" width="280" height="48" rx="10"/>
  <text x="280" y="128" text-anchor="middle" class="lab">Amazon Connect + Lex</text>
  <text x="280" y="144" text-anchor="middle" class="sub">socle contact center partagé</text>

  <path class="line" d="M200 154 V170 H150 V186"/>
  <path class="line" d="M360 154 V170 H410 V186"/>

  <rect class="out" x="36" y="186" width="224" height="132" rx="12"/>
  <text x="52" y="210" class="cap">PROTOTYPE A</text>
  <rect class="hi" x="52" y="222" width="192" height="78" rx="10"/>
  <text x="148" y="250" text-anchor="middle" class="lab">GenAI native Connect</text>
  <text x="148" y="270" text-anchor="middle" class="sub">GenAI dans Connect</text>
  <text x="148" y="286" text-anchor="middle" class="sub">parcours conversationnel natif</text>

  <rect class="out" x="300" y="186" width="224" height="132" rx="12"/>
  <text x="316" y="210" class="cap">PROTOTYPE B</text>
  <rect class="hi" x="316" y="222" width="192" height="78" rx="10"/>
  <text x="412" y="250" text-anchor="middle" class="lab">GenAI Lambda custom</text>
  <text x="412" y="270" text-anchor="middle" class="sub">cerveau Lambda + mémoire</text>
  <text x="412" y="286" text-anchor="middle" class="sub">Bedrock / LLM géré</text>

  <text x="24" y="342" class="foot">Même entrée. Deux façons d'ajouter la GenAI sans réécrire le parcours.</text>
""",
    "Architecture GenAI Voice Assist",
    "Socle Connect+Lex partagé, avec prototypes GenAI native Connect et Lambda custom.",
)

# --- MCP ---
save(
    "mcp",
    "en",
    """
  <text x="24" y="30" class="title">OPENWEBUI - MCP - AWS</text>

  <rect class="b" x="32" y="70" width="132" height="64" rx="10"/>
  <text x="98" y="96" text-anchor="middle" class="lab">OpenWebUI</text>
  <text x="98" y="114" text-anchor="middle" class="sub">user prompt / chat</text>
  <line class="line" x1="164" y1="102" x2="206" y2="102"/>

  <rect class="hi pulse" x="210" y="54" width="132" height="96" rx="10"/>
  <text x="276" y="86" text-anchor="middle" class="lab">MCP layer</text>
  <text x="276" y="106" text-anchor="middle" class="sub">Office tools</text>
  <text x="276" y="124" text-anchor="middle" class="sub">pptx / docx / xlsx</text>
  <line class="line" x1="342" y1="102" x2="386" y2="102"/>

  <rect class="cloud" x="390" y="46" width="140" height="168" rx="12"/>
  <text x="408" y="70" class="cap">AWS</text>
  <rect class="b" x="408" y="84" width="104" height="36" rx="8"/>
  <text x="460" y="107" text-anchor="middle" class="lab">Bedrock</text>
  <rect class="b" x="408" y="132" width="104" height="36" rx="8"/>
  <text x="460" y="155" text-anchor="middle" class="lab">S3</text>
  <rect class="b" x="408" y="180" width="104" height="24" rx="8"/>
  <text x="460" y="197" text-anchor="middle" class="sub">+ other services</text>

  <path class="line return" d="M460 214 V278 H352"/>
  <text x="404" y="268" text-anchor="middle" class="lbl flow-lbl">presigned URL (auth-scoped)</text>

  <rect class="hi pulse" x="32" y="250" width="320" height="56" rx="10"/>
  <text x="192" y="274" text-anchor="middle" class="lab">Back to OpenWebUI</text>
  <text x="192" y="292" text-anchor="middle" class="sub">see / download only what you created</text>

  <text x="32" y="338" class="foot">MCP sits between chat UI and AWS - result returns in chat.</text>
""",
    "MCP Office Machine architecture",
    "MCP between OpenWebUI and AWS; auth-scoped presigned URL returns to the user.",
)

save(
    "mcp",
    "fr",
    """
  <text x="24" y="30" class="title">OPENWEBUI - MCP - AWS</text>

  <rect class="b" x="32" y="70" width="132" height="64" rx="10"/>
  <text x="98" y="96" text-anchor="middle" class="lab">OpenWebUI</text>
  <text x="98" y="114" text-anchor="middle" class="sub">prompt / chat utilisateur</text>
  <line class="line" x1="164" y1="102" x2="206" y2="102"/>

  <rect class="hi pulse" x="210" y="54" width="132" height="96" rx="10"/>
  <text x="276" y="86" text-anchor="middle" class="lab">Couche MCP</text>
  <text x="276" y="106" text-anchor="middle" class="sub">Outils Office</text>
  <text x="276" y="124" text-anchor="middle" class="sub">pptx / docx / xlsx</text>
  <line class="line" x1="342" y1="102" x2="386" y2="102"/>

  <rect class="cloud" x="390" y="46" width="140" height="168" rx="12"/>
  <text x="408" y="70" class="cap">AWS</text>
  <rect class="b" x="408" y="84" width="104" height="36" rx="8"/>
  <text x="460" y="107" text-anchor="middle" class="lab">Bedrock</text>
  <rect class="b" x="408" y="132" width="104" height="36" rx="8"/>
  <text x="460" y="155" text-anchor="middle" class="lab">S3</text>
  <rect class="b" x="408" y="180" width="104" height="24" rx="8"/>
  <text x="460" y="197" text-anchor="middle" class="sub">+ autres services</text>

  <path class="line return" d="M460 214 V278 H352"/>
  <text x="404" y="268" text-anchor="middle" class="lbl flow-lbl">URL signée (auth limitée)</text>

  <rect class="hi pulse" x="32" y="250" width="320" height="56" rx="10"/>
  <text x="192" y="274" text-anchor="middle" class="lab">Retour OpenWebUI</text>
  <text x="192" y="292" text-anchor="middle" class="sub">voir / télécharger seulement ce que vous avez créé</text>

  <text x="32" y="338" class="foot">Le MCP s'intercale entre le chat et AWS - le résultat revient dans le chat.</text>
""",
    "Architecture MCP Office Machine",
    "MCP entre OpenWebUI et AWS ; URL signée à portée limitée pour l'utilisateur.",
)

# --- ANALYZER ---
save(
    "analyzer",
    "en",
    """
  <text x="24" y="30" class="title">FULL AI FLOW + N8N</text>

  <rect class="b" x="170" y="48" width="220" height="44" rx="10"/>
  <text x="280" y="68" text-anchor="middle" class="lab">Operator</text>
  <text x="280" y="84" text-anchor="middle" class="sub">asks AI to scan a repo</text>
  <line class="line" x1="280" y1="92" x2="280" y2="116"/>

  <rect class="hi" x="150" y="116" width="260" height="50" rx="10"/>
  <text x="280" y="140" text-anchor="middle" class="lab">Orchestrator AI</text>
  <text x="280" y="156" text-anchor="middle" class="sub">full AI conversation path</text>

  <line class="line" x1="280" y1="166" x2="280" y2="190"/>
  <text x="292" y="184" class="lbl">n8n workflow</text>

  <rect class="b" x="150" y="190" width="260" height="48" rx="10"/>
  <text x="280" y="212" text-anchor="middle" class="lab">n8n automation</text>
  <text x="280" y="228" text-anchor="middle" class="sub">wires AI to analysis steps</text>

  <line class="line stem" x1="280" y1="238" x2="280" y2="296"/>
  <path class="line ingest" d="M280 296 H262"/>
  <path class="line return" d="M280 296 H298"/>

  <rect class="b" x="32" y="270" width="230" height="52" rx="10"/>
  <text x="147" y="294" text-anchor="middle" class="lab">Analysis worker</text>
  <text x="147" y="310" text-anchor="middle" class="sub">scans code / builds report</text>

  <rect class="hi pulse" x="298" y="270" width="230" height="52" rx="10"/>
  <text x="413" y="294" text-anchor="middle" class="lab">Structured report</text>
  <text x="413" y="310" text-anchor="middle" class="sub">only this reaches the AI</text>

  <text x="24" y="348" class="foot">Client view: AI scans the codebase. Model never sees raw source trees.</text>
""",
    "Repo Analyzer architecture",
    "Full AI flow with n8n; worker scans code; only the structured report reaches the model.",
)

save(
    "analyzer",
    "fr",
    """
  <text x="24" y="30" class="title">FLUX IA COMPLET + N8N</text>

  <rect class="b" x="170" y="48" width="220" height="44" rx="10"/>
  <text x="280" y="68" text-anchor="middle" class="lab">Opérateur</text>
  <text x="280" y="84" text-anchor="middle" class="sub">demande à l'IA de scanner un dépôt</text>
  <line class="line" x1="280" y1="92" x2="280" y2="116"/>

  <rect class="hi" x="150" y="116" width="260" height="50" rx="10"/>
  <text x="280" y="140" text-anchor="middle" class="lab">IA orchestratrice</text>
  <text x="280" y="156" text-anchor="middle" class="sub">chemin conversationnel full IA</text>

  <line class="line" x1="280" y1="166" x2="280" y2="190"/>
  <text x="292" y="184" class="lbl">workflow n8n</text>

  <rect class="b" x="150" y="190" width="260" height="48" rx="10"/>
  <text x="280" y="212" text-anchor="middle" class="lab">Automatisation n8n</text>
  <text x="280" y="228" text-anchor="middle" class="sub">relie l'IA aux étapes d'analyse</text>

  <line class="line stem" x1="280" y1="238" x2="280" y2="296"/>
  <path class="line ingest" d="M280 296 H262"/>
  <path class="line return" d="M280 296 H298"/>

  <rect class="b" x="32" y="270" width="230" height="52" rx="10"/>
  <text x="147" y="294" text-anchor="middle" class="lab">Worker d'analyse</text>
  <text x="147" y="310" text-anchor="middle" class="sub">scanne le code / construit le rapport</text>

  <rect class="hi pulse" x="298" y="270" width="230" height="52" rx="10"/>
  <text x="413" y="294" text-anchor="middle" class="lab">Rapport structuré</text>
  <text x="413" y="310" text-anchor="middle" class="sub">seul ceci atteint l'IA</text>

  <text x="24" y="348" class="foot">Vue client : l'IA scanne le code. Le modèle ne voit jamais l'arbre source brut.</text>
""",
    "Architecture Repo Analyzer",
    "Flux IA complet avec n8n ; le worker scanne le code ; seul le rapport structuré atteint le modèle.",
)

# --- CODIUM ---
save(
    "codium",
    "en",
    """
  <text x="24" y="30" class="title">PLANES + FULL HUMAN CONTROL</text>

  <rect class="hi" x="400" y="54" width="136" height="252" rx="12"/>
  <text x="468" y="90" text-anchor="middle" class="lab">Human</text>
  <text x="468" y="110" text-anchor="middle" class="lab">in the loop</text>
  <text x="468" y="148" text-anchor="middle" class="sub">approves</text>
  <text x="468" y="168" text-anchor="middle" class="sub">reviews</text>
  <text x="468" y="188" text-anchor="middle" class="sub">controls</text>
  <text x="468" y="220" text-anchor="middle" class="lbl">every step</text>
  <text x="468" y="252" text-anchor="middle" class="sub">agent never</text>
  <text x="468" y="270" text-anchor="middle" class="sub">acts alone</text>

  <rect class="plane" x="24" y="54" width="352" height="100" rx="14"/>
  <text x="40" y="78" class="cap">INTELLIGENCE PLANE</text>
  <rect class="b" x="44" y="92" width="148" height="48" rx="10"/>
  <text x="118" y="114" text-anchor="middle" class="lab">Agentic planner</text>
  <text x="118" y="130" text-anchor="middle" class="sub">structure / next steps</text>
  <rect class="b" x="208" y="92" width="148" height="48" rx="10"/>
  <text x="282" y="114" text-anchor="middle" class="lab">Reports / method</text>
  <text x="282" y="130" text-anchor="middle" class="sub">OWASP-oriented</text>

  <line class="line" x1="200" y1="154" x2="200" y2="188"/>
  <text x="212" y="176" class="lbl">gated command bridge</text>

  <rect class="plane" x="24" y="188" width="352" height="118" rx="14"/>
  <text x="40" y="212" class="cap">EXECUTION PLANE</text>
  <rect class="hi" x="44" y="228" width="312" height="58" rx="10"/>
  <text x="200" y="254" text-anchor="middle" class="lab">Kali pentest engine</text>
  <text x="200" y="272" text-anchor="middle" class="sub">isolated execution environment</text>

  <text x="24" y="340" class="foot">Human gates planning and execution. No unsupervised offensive actions.</text>
""",
    "Codium Red architecture",
    "Intelligence plane plans; Kali pentest engine executes; human approves, reviews, controls.",
)

save(
    "codium",
    "fr",
    """
  <text x="24" y="30" class="title">PLANS + CONTRÔLE HUMAIN TOTAL</text>

  <rect class="hi" x="400" y="54" width="136" height="252" rx="12"/>
  <text x="468" y="90" text-anchor="middle" class="lab">Humain</text>
  <text x="468" y="110" text-anchor="middle" class="lab">dans la boucle</text>
  <text x="468" y="148" text-anchor="middle" class="sub">approuve</text>
  <text x="468" y="168" text-anchor="middle" class="sub">revue</text>
  <text x="468" y="188" text-anchor="middle" class="sub">contrôle</text>
  <text x="468" y="220" text-anchor="middle" class="lbl">chaque étape</text>
  <text x="468" y="252" text-anchor="middle" class="sub">l'agent n'agit</text>
  <text x="468" y="270" text-anchor="middle" class="sub">jamais seul</text>

  <rect class="plane" x="24" y="54" width="352" height="100" rx="14"/>
  <text x="40" y="78" class="cap">PLAN D'INTELLIGENCE</text>
  <rect class="b" x="44" y="92" width="148" height="48" rx="10"/>
  <text x="118" y="114" text-anchor="middle" class="lab">Planificateur</text>
  <text x="118" y="130" text-anchor="middle" class="sub">structure / prochaines étapes</text>
  <rect class="b" x="208" y="92" width="148" height="48" rx="10"/>
  <text x="282" y="114" text-anchor="middle" class="lab">Rapports / méthodo</text>
  <text x="282" y="130" text-anchor="middle" class="sub">orienté OWASP</text>

  <line class="line" x1="200" y1="154" x2="200" y2="188"/>
  <text x="212" y="176" class="lbl">pont de commandes contrôlé</text>

  <rect class="plane" x="24" y="188" width="352" height="118" rx="14"/>
  <text x="40" y="212" class="cap">PLAN D'EXÉCUTION</text>
  <rect class="hi" x="44" y="228" width="312" height="58" rx="10"/>
  <text x="200" y="254" text-anchor="middle" class="lab">Moteur pentest Kali</text>
  <text x="200" y="272" text-anchor="middle" class="sub">environnement d'exécution isolé</text>

  <text x="24" y="340" class="foot">L'humain valide planification et exécution. Aucune action offensive autonome.</text>
""",
    "Architecture Codium Red",
    "Plan d'intelligence ; moteur pentest Kali ; l'humain approuve, revoit et contrôle.",
)

# Keep unversioned aliases pointing to EN for old links
for stem in ("ronin", "centinel", "voice", "mcp", "analyzer", "codium"):
    src = (OUT / f"arch-{stem}.en.svg").read_text(encoding="utf-8")
    (OUT / f"arch-{stem}.svg").write_text(src, encoding="utf-8", newline="\n")
    print("alias", f"arch-{stem}.svg")
