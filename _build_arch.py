"""Build EN/FR architecture SVGs with stronger type + arrows."""
from pathlib import Path

OUT = Path(__file__).resolve().parent / "assets"
OUT.mkdir(exist_ok=True)

VW, VH = 560, 560

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
        stroke:#111; stroke-width:2.8; fill:none; marker-end:url(#a);
        stroke-linecap:round; stroke-linejoin:round;
        stroke-dasharray:8 18;
        animation: flow 1.35s linear infinite;
      }
      .line.ingest {
        stroke-dasharray: 6 20;
        animation: flow 1.55s linear infinite;
      }
      .line.return {
        stroke-dasharray: 10 16;
        animation: flow 1.15s linear infinite;
      }
      .line.stem {
        marker-end: none;
        stroke-dasharray: 8 18;
        animation: flow 1.35s linear infinite;
      }
      .line.gate {
        stroke-dasharray: 6 14;
        animation: flow 1.4s linear infinite;
      }
      .hi.pulse {
        animation: node-pulse 2.6s ease-in-out infinite;
      }
      .lbl.flow-lbl {
        animation: lbl-pulse 2.2s ease-in-out infinite;
      }
      .chip { fill:#fff; stroke:#111; stroke-width:1.6; }
      .lbl { font-family:Segoe UI,system-ui,sans-serif; font-size:11px; font-weight:700; fill:#111; }
      .foot { font-family:Segoe UI,system-ui,sans-serif; font-size:11.5px; font-weight:600; fill:#3a3a3a; }
      @keyframes flow {
        to { stroke-dashoffset: -52; }
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
        .line, .line.ingest, .line.return, .line.stem, .line.gate, .hi.pulse, .lbl.flow-lbl { animation: none; }
        .line, .line.ingest, .line.return, .line.stem, .line.gate { stroke-dasharray: none; }
      }
    </style>
  </defs>
""".strip()


def save(stem: str, lang: str, body: str, title: str, desc: str, vh: int | None = None) -> None:
    h = vh if vh is not None else VH
    svg = f"""<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {VW} {h}" role="img" aria-labelledby="t d">
  <title id="t">{title}</title>
  <desc id="d">{desc}</desc>
{DEFS}
  <rect class="bg" width="{VW}" height="{h}"/>
{body}
</svg>
"""
    path = OUT / f"arch-{stem}.{lang}.svg"
    path.write_text(svg, encoding="utf-8", newline="\n")
    print("ok", path.name)


# --- RONIN ---
# Single desktop pipeline; long connectors so dash flow reads clearly
RONIN_H = 720
save(
    "ronin",
    "en",
    """
  <text x="24" y="30" class="title">SPECIALIZED TRANSLATOR · HARD LOCK</text>
  <text x="24" y="50" class="foot">Early specialized AI — one task, one non-negotiable constraint</text>

  <rect class="hi pulse" x="100" y="68" width="360" height="72" rx="12"/>
  <text x="280" y="96" text-anchor="middle" class="cap">KNOWLEDGE BASE</text>
  <text x="280" y="116" text-anchor="middle" class="lab">Glossary / Protected Terms (JSON)</text>
  <text x="280" y="132" text-anchor="middle" class="sub">Product names · acronyms · fixed phrasing</text>

  <line class="line ingest" x1="280" y1="140" x2="280" y2="210"/>
  <text x="300" y="182" class="lbl flow-lbl">Grounds the Lock</text>

  <rect class="b" x="100" y="210" width="360" height="64" rx="12"/>
  <text x="280" y="238" text-anchor="middle" class="lab">Desktop UI</text>
  <text x="280" y="258" text-anchor="middle" class="sub">Written in Python</text>

  <line class="line" x1="280" y1="274" x2="280" y2="344"/>

  <rect class="hi" x="100" y="344" width="360" height="64" rx="12"/>
  <text x="280" y="372" text-anchor="middle" class="lab">Hard Restriction</text>
  <text x="280" y="392" text-anchor="middle" class="sub">Lock glossary terms — must not be rewritten</text>

  <line class="line" x1="280" y1="408" x2="280" y2="478"/>

  <rect class="b" x="100" y="478" width="360" height="64" rx="12"/>
  <text x="280" y="506" text-anchor="middle" class="lab">FastAPI Bridge</text>
  <text x="280" y="526" text-anchor="middle" class="sub">Low-latency translate call</text>

  <line class="line" x1="280" y1="542" x2="280" y2="612"/>

  <rect class="hi" x="100" y="612" width="360" height="52" rx="12"/>
  <text x="280" y="644" text-anchor="middle" class="lab">Local LLM</text>

  <rect class="b" x="100" y="680" width="360" height="28" rx="8"/>
  <text x="280" y="699" text-anchor="middle" class="foot">UI → FastAPI → Model — constraint first, then translate</text>
""",
    "Ronin architecture",
    "Specialized desktop translator: glossary KB, hard lock, FastAPI bridge to a local LLM.",
    vh=RONIN_H,
)

save(
    "ronin",
    "fr",
    """
  <text x="24" y="30" class="title">TRADUCTEUR SPÉCIALISÉ · VERROU DUR</text>
  <text x="24" y="50" class="foot">Première IA spécialisée — une tâche, une contrainte non négociable</text>

  <rect class="hi pulse" x="100" y="68" width="360" height="72" rx="12"/>
  <text x="280" y="96" text-anchor="middle" class="cap">BASE DE CONNAISSANCES</text>
  <text x="280" y="116" text-anchor="middle" class="lab">Glossaire / Termes Protégés (JSON)</text>
  <text x="280" y="132" text-anchor="middle" class="sub">Noms produits · acronymes · formulations figées</text>

  <line class="line ingest" x1="280" y1="140" x2="280" y2="210"/>
  <text x="300" y="182" class="lbl flow-lbl">Ancre le Verrou</text>

  <rect class="b" x="100" y="210" width="360" height="64" rx="12"/>
  <text x="280" y="238" text-anchor="middle" class="lab">Interface Desktop</text>
  <text x="280" y="258" text-anchor="middle" class="sub">Écrite en Python</text>

  <line class="line" x1="280" y1="274" x2="280" y2="344"/>

  <rect class="hi" x="100" y="344" width="360" height="64" rx="12"/>
  <text x="280" y="372" text-anchor="middle" class="lab">Restriction Dure</text>
  <text x="280" y="392" text-anchor="middle" class="sub">Verrouiller le glossaire — à ne pas réécrire</text>

  <line class="line" x1="280" y1="408" x2="280" y2="478"/>

  <rect class="b" x="100" y="478" width="360" height="64" rx="12"/>
  <text x="280" y="506" text-anchor="middle" class="lab">Pont FastAPI</text>
  <text x="280" y="526" text-anchor="middle" class="sub">Appel traduction rapide</text>

  <line class="line" x1="280" y1="542" x2="280" y2="612"/>

  <rect class="hi" x="100" y="612" width="360" height="52" rx="12"/>
  <text x="280" y="644" text-anchor="middle" class="lab">LLM Local</text>

  <rect class="b" x="100" y="680" width="360" height="28" rx="8"/>
  <text x="280" y="699" text-anchor="middle" class="foot">UI → FastAPI → Modèle — contrainte d'abord, puis traduction</text>
""",
    "Architecture Ronin",
    "Traducteur desktop spécialisé : glossaire, verrou dur, pont FastAPI vers un LLM local.",
    vh=RONIN_H,
)

# --- CENTINEL ---
# Tall layout: ~70px connectors so dash flow is readable
CENTINEL_H = 960
save(
    "centinel",
    "en",
    """
  <text x="24" y="28" class="title">SPECIALIZED CYBER MODEL · FROM BASE TO REFS</text>
  <text x="24" y="48" class="foot">Not RAG over PDFs — full training on the frameworks</text>

  <rect class="b" x="100" y="64" width="360" height="56" rx="12"/>
  <text x="280" y="90" text-anchor="middle" class="lab">Hugging Face Base</text>
  <text x="280" y="108" text-anchor="middle" class="sub">Abliterated Qwen3</text>

  <line class="line" x1="280" y1="120" x2="280" y2="190"/>
  <text x="300" y="162" class="lbl flow-lbl">Pull Base</text>

  <rect class="hi pulse" x="100" y="190" width="360" height="80" rx="12"/>
  <text x="280" y="216" text-anchor="middle" class="cap">CYBER REFS CORPUS</text>
  <text x="280" y="238" text-anchor="middle" class="lab">ISO · DORA · GDPR · NIST</text>
  <text x="280" y="256" text-anchor="middle" class="lab">OWASP · PTES</text>

  <line class="line ingest" x1="280" y1="270" x2="280" y2="340"/>
  <text x="300" y="312" class="lbl flow-lbl">Feed Trainer</text>

  <rect class="out" x="72" y="340" width="416" height="360" rx="14"/>
  <text x="88" y="368" class="cap">GOOGLE COLAB · UNSLOTH</text>
  <text x="88" y="386" class="foot">Python notebook — full AI training pipeline</text>

  <rect class="b" x="100" y="406" width="360" height="48" rx="10"/>
  <text x="280" y="436" text-anchor="middle" class="lab">Prepare Dataset</text>
  <line class="line" x1="280" y1="454" x2="280" y2="524"/>
  <rect class="b" x="100" y="524" width="360" height="48" rx="10"/>
  <text x="280" y="554" text-anchor="middle" class="lab">Fine-Tune (Unsloth + LoRA/SFT)</text>
  <line class="line" x1="280" y1="572" x2="280" y2="642"/>
  <rect class="b" x="100" y="642" width="360" height="48" rx="10"/>
  <text x="280" y="672" text-anchor="middle" class="lab">Eval / Export Weights</text>

  <line class="line" x1="280" y1="700" x2="280" y2="770"/>
  <text x="300" y="742" class="lbl flow-lbl">Ship Specialist</text>

  <rect class="hi pulse" x="100" y="770" width="360" height="72" rx="12"/>
  <text x="280" y="800" text-anchor="middle" class="lab">Specialized Cyber AI</text>
  <text x="280" y="822" text-anchor="middle" class="sub">Local model shaped on those refs</text>

  <rect class="b" x="100" y="864" width="360" height="68" rx="10"/>
  <text x="280" y="892" text-anchor="middle" class="foot">HF base + refs → Unsloth on Colab → specialist</text>
  <text x="280" y="914" text-anchor="middle" class="foot">Refs matter — ISO, DORA, GDPR, NIST, OWASP, PTES</text>
""",
    "Centinel architecture",
    "Abliterated Qwen3 from Hugging Face, trained on cyber refs with Unsloth on Google Colab into a specialized cyber AI.",
    vh=CENTINEL_H,
)

save(
    "centinel",
    "fr",
    """
  <text x="24" y="28" class="title">MODÈLE CYBER SPÉCIALISÉ · DE LA BASE AUX REFS</text>
  <text x="24" y="48" class="foot">Pas du RAG sur des PDF — entraînement complet sur les référentiels</text>

  <rect class="b" x="100" y="64" width="360" height="56" rx="12"/>
  <text x="280" y="90" text-anchor="middle" class="lab">Base Hugging Face</text>
  <text x="280" y="108" text-anchor="middle" class="sub">Abliterated Qwen3</text>

  <line class="line" x1="280" y1="120" x2="280" y2="190"/>
  <text x="300" y="162" class="lbl flow-lbl">Récupérer la Base</text>

  <rect class="hi pulse" x="100" y="190" width="360" height="80" rx="12"/>
  <text x="280" y="216" text-anchor="middle" class="cap">CORPUS DE REFS CYBER</text>
  <text x="280" y="238" text-anchor="middle" class="lab">ISO · DORA · RGPD · NIST</text>
  <text x="280" y="256" text-anchor="middle" class="lab">OWASP · PTES</text>

  <line class="line ingest" x1="280" y1="270" x2="280" y2="340"/>
  <text x="300" y="312" class="lbl flow-lbl">Alimenter le Trainer</text>

  <rect class="out" x="72" y="340" width="416" height="360" rx="14"/>
  <text x="88" y="368" class="cap">GOOGLE COLAB · UNSLOTH</text>
  <text x="88" y="386" class="foot">Notebook Python — pipeline d'entraînement IA complet</text>

  <rect class="b" x="100" y="406" width="360" height="48" rx="10"/>
  <text x="280" y="436" text-anchor="middle" class="lab">Préparer le Dataset</text>
  <line class="line" x1="280" y1="454" x2="280" y2="524"/>
  <rect class="b" x="100" y="524" width="360" height="48" rx="10"/>
  <text x="280" y="554" text-anchor="middle" class="lab">Fine-Tune (Unsloth + LoRA/SFT)</text>
  <line class="line" x1="280" y1="572" x2="280" y2="642"/>
  <rect class="b" x="100" y="642" width="360" height="48" rx="10"/>
  <text x="280" y="672" text-anchor="middle" class="lab">Éval / Export des Poids</text>

  <line class="line" x1="280" y1="700" x2="280" y2="770"/>
  <text x="300" y="742" class="lbl flow-lbl">Livrer le Spécialiste</text>

  <rect class="hi pulse" x="100" y="770" width="360" height="72" rx="12"/>
  <text x="280" y="800" text-anchor="middle" class="lab">IA Cyber Spécialisée</text>
  <text x="280" y="822" text-anchor="middle" class="sub">Modèle local façonné sur ces refs</text>

  <rect class="b" x="100" y="864" width="360" height="68" rx="10"/>
  <text x="280" y="892" text-anchor="middle" class="foot">Base HF + refs → Unsloth sur Colab → spécialiste</text>
  <text x="280" y="914" text-anchor="middle" class="foot">Les refs comptent — ISO, DORA, RGPD, NIST, OWASP, PTES</text>
""",
    "Architecture Centinel",
    "Abliterated Qwen3 depuis Hugging Face, entraîné sur des refs cyber avec Unsloth sur Google Colab en IA cyber spécialisée.",
    vh=CENTINEL_H,
)

# --- VOICE ---
# Tall fork + shared AI restrictions (no PII / guide-only / isolated from live bot)
VOICE_H = 820
save(
    "voice",
    "en",
    """
  <text x="24" y="28" class="title">ONE BASELINE / TWO GENAI PROTOTYPES</text>
  <text x="24" y="48" class="foot">Same entry — GenAI attaches without rewriting the parcours</text>

  <rect class="b" x="190" y="68" width="180" height="48" rx="12"/>
  <text x="280" y="98" text-anchor="middle" class="lab">Caller</text>

  <line class="line" x1="280" y1="116" x2="280" y2="186"/>

  <rect class="hi" x="120" y="186" width="320" height="68" rx="12"/>
  <text x="280" y="216" text-anchor="middle" class="lab">Amazon Connect + Lex</text>
  <text x="280" y="236" text-anchor="middle" class="sub">Shared Contact-Center Baseline</text>

  <path class="line" d="M200 254 V330 H148 V400"/>
  <path class="line" d="M360 254 V330 H412 V400"/>
  <text x="280" y="318" text-anchor="middle" class="lbl flow-lbl">Fork GenAI Attach</text>

  <rect class="out" x="28" y="400" width="240" height="168" rx="14"/>
  <text x="44" y="428" class="cap">PROTOTYPE A</text>
  <rect class="hi" x="48" y="444" width="200" height="104" rx="12"/>
  <text x="148" y="484" text-anchor="middle" class="lab">Connect-native GenAI</text>
  <text x="148" y="508" text-anchor="middle" class="sub">GenAI inside Connect</text>
  <text x="148" y="528" text-anchor="middle" class="sub">Native conversation path</text>

  <rect class="out" x="292" y="400" width="240" height="168" rx="14"/>
  <text x="308" y="428" class="cap">PROTOTYPE B</text>
  <rect class="hi" x="312" y="444" width="200" height="104" rx="12"/>
  <text x="412" y="484" text-anchor="middle" class="lab">Custom Lambda GenAI</text>
  <text x="412" y="508" text-anchor="middle" class="sub">Lambda Brain + Memory</text>
  <text x="412" y="528" text-anchor="middle" class="sub">Bedrock / Managed LLM</text>

  <path class="line" d="M148 568 V620"/>
  <path class="line" d="M412 568 V620"/>
  <text x="280" y="602" text-anchor="middle" class="lbl flow-lbl">Both Bound By</text>

  <rect class="hi pulse" x="28" y="620" width="504" height="100" rx="14"/>
  <text x="280" y="650" text-anchor="middle" class="cap">AI RESTRICTIONS · HARD LOCK</text>
  <text x="280" y="676" text-anchor="middle" class="lab">No Personal Data Access</text>
  <text x="280" y="698" text-anchor="middle" class="sub">Explain / guide only · no data files · isolated from live scripted bot</text>

  <rect class="b" x="28" y="744" width="504" height="52" rx="10"/>
  <text x="280" y="766" text-anchor="middle" class="foot">Connect+Lex stays; GenAI plugs in as A or B — privacy constraint is non-negotiable</text>
  <text x="280" y="784" text-anchor="middle" class="foot">Staging / Terraform isolation so the live channel is never burned</text>
""",
    "GenAI Voice Assist architecture",
    "Shared Connect+Lex baseline, two GenAI prototypes, hard AI restrictions: no personal-data access.",
    vh=VOICE_H,
)

save(
    "voice",
    "fr",
    """
  <text x="24" y="28" class="title">UNE BASE / DEUX PROTOTYPES GENAI</text>
  <text x="24" y="48" class="foot">Même entrée — la GenAI se greffe sans réécrire le parcours</text>

  <rect class="b" x="190" y="68" width="180" height="48" rx="12"/>
  <text x="280" y="98" text-anchor="middle" class="lab">Appelant</text>

  <line class="line" x1="280" y1="116" x2="280" y2="186"/>

  <rect class="hi" x="120" y="186" width="320" height="68" rx="12"/>
  <text x="280" y="216" text-anchor="middle" class="lab">Amazon Connect + Lex</text>
  <text x="280" y="236" text-anchor="middle" class="sub">Socle Contact Center Partagé</text>

  <path class="line" d="M200 254 V330 H148 V400"/>
  <path class="line" d="M360 254 V330 H412 V400"/>
  <text x="280" y="318" text-anchor="middle" class="lbl flow-lbl">Bifurcation GenAI</text>

  <rect class="out" x="28" y="400" width="240" height="168" rx="14"/>
  <text x="44" y="428" class="cap">PROTOTYPE A</text>
  <rect class="hi" x="48" y="444" width="200" height="104" rx="12"/>
  <text x="148" y="484" text-anchor="middle" class="lab">GenAI Native Connect</text>
  <text x="148" y="508" text-anchor="middle" class="sub">GenAI dans Connect</text>
  <text x="148" y="528" text-anchor="middle" class="sub">Parcours conversationnel natif</text>

  <rect class="out" x="292" y="400" width="240" height="168" rx="14"/>
  <text x="308" y="428" class="cap">PROTOTYPE B</text>
  <rect class="hi" x="312" y="444" width="200" height="104" rx="12"/>
  <text x="412" y="484" text-anchor="middle" class="lab">GenAI Lambda Custom</text>
  <text x="412" y="508" text-anchor="middle" class="sub">Cerveau Lambda + Mémoire</text>
  <text x="412" y="528" text-anchor="middle" class="sub">Bedrock / LLM Géré</text>

  <path class="line" d="M148 568 V620"/>
  <path class="line" d="M412 568 V620"/>
  <text x="280" y="602" text-anchor="middle" class="lbl flow-lbl">Les Deux Sous</text>

  <rect class="hi pulse" x="28" y="620" width="504" height="100" rx="14"/>
  <text x="280" y="650" text-anchor="middle" class="cap">RESTRICTIONS IA · VERROU DUR</text>
  <text x="280" y="676" text-anchor="middle" class="lab">Aucun Accès aux Données Personnelles</text>
  <text x="280" y="698" text-anchor="middle" class="sub">Expliquer / guider seulement · pas de fichiers de données · isolé du bot scripté live</text>

  <rect class="b" x="28" y="744" width="504" height="52" rx="10"/>
  <text x="280" y="766" text-anchor="middle" class="foot">Connect+Lex reste ; GenAI en A ou B — contrainte privacy non négociable</text>
  <text x="280" y="784" text-anchor="middle" class="foot">Staging / isolation Terraform pour ne jamais brûler le canal live</text>
""",
    "Architecture GenAI Voice Assist",
    "Socle Connect+Lex, deux prototypes GenAI, restrictions IA dures : aucun accès aux données personnelles.",
    vh=VOICE_H,
)

# --- MCP ---
# Chat → big secured OWUI → MCP → AWS; return elbow back to OWUI entry with user-scoped URL
MCP_H = 820
save(
    "mcp",
    "en",
    """
  <text x="24" y="28" class="title">OPENWEBUI · MCP · AWS</text>
  <text x="24" y="48" class="foot">Chat asks for a PPT — agent acts via MCP, Bedrock works in AWS, file returns to the same entry</text>

  <rect class="b" x="120" y="68" width="320" height="52" rx="12"/>
  <text x="280" y="92" text-anchor="middle" class="lab">User Chat Request</text>
  <text x="280" y="110" text-anchor="middle" class="sub">e.g. “Generate a PPT…”</text>

  <line class="line" x1="280" y1="120" x2="280" y2="178"/>

  <rect class="hi pulse" x="88" y="178" width="384" height="112" rx="14"/>
  <text x="280" y="210" text-anchor="middle" class="cap">OPENWEBUI · SECURED ENTRY</text>
  <text x="280" y="236" text-anchor="middle" class="lab">Auth / Session-Bound Chat</text>
  <text x="280" y="258" text-anchor="middle" class="sub">Only the signed-in user reaches this flow</text>
  <text x="280" y="276" text-anchor="middle" class="sub">Download lands back here — same chat entry</text>

  <line class="line" x1="280" y1="290" x2="280" y2="360"/>
  <text x="300" y="332" class="lbl flow-lbl">Agent Thinks → Calls Tools</text>

  <rect class="hi" x="100" y="360" width="360" height="80" rx="12"/>
  <text x="280" y="388" text-anchor="middle" class="lab">MCP Layer (FastMCP)</text>
  <text x="280" y="410" text-anchor="middle" class="sub">Office tools — pptx / docx / xlsx</text>
  <text x="280" y="428" text-anchor="middle" class="sub">Orchestrates generation outside the chat</text>

  <line class="line ingest" x1="280" y1="440" x2="280" y2="510"/>
  <text x="300" y="482" class="lbl flow-lbl">Into AWS</text>

  <rect class="cloud" x="88" y="510" width="384" height="148" rx="14"/>
  <text x="104" y="538" class="cap">AWS ENVIRONMENT</text>
  <rect class="b" x="112" y="556" width="160" height="72" rx="10"/>
  <text x="192" y="586" text-anchor="middle" class="lab">Bedrock</text>
  <text x="192" y="608" text-anchor="middle" class="sub">AI reasoning / gen</text>
  <rect class="b" x="292" y="556" width="160" height="72" rx="10"/>
  <text x="372" y="586" text-anchor="middle" class="lab">S3</text>
  <text x="372" y="608" text-anchor="middle" class="sub">Store Office file</text>

  <path class="line return" d="M280 658 V720 H40 V234 H88"/>
  <text x="56" y="470" class="lbl flow-lbl" transform="rotate(-90 56 470)">Presigned URL → OWUI Entry</text>
  <text x="200" y="744" text-anchor="middle" class="sub">User-scoped — only that requester can download</text>

  <rect class="b" x="100" y="748" width="360" height="48" rx="10"/>
  <text x="280" y="770" text-anchor="middle" class="foot">OWUI security + per-user presigned URL</text>
  <text x="280" y="786" text-anchor="middle" class="foot">Same chat entry · bounded delivery</text>
""",
    "MCP Office Machine architecture",
    "Secured OpenWebUI chat → MCP Office tools → Bedrock/S3 in AWS → user-scoped presigned URL back to the OWUI entry.",
    vh=MCP_H,
)

save(
    "mcp",
    "fr",
    """
  <text x="24" y="28" class="title">OPENWEBUI · MCP · AWS</text>
  <text x="24" y="48" class="foot">Le chat demande un PPT — l'agent agit via MCP, Bedrock dans AWS, fichier revient à l'entrée</text>

  <rect class="b" x="120" y="68" width="320" height="52" rx="12"/>
  <text x="280" y="92" text-anchor="middle" class="lab">Demande Chat Utilisateur</text>
  <text x="280" y="110" text-anchor="middle" class="sub">ex. « Génère un PPT… »</text>

  <line class="line" x1="280" y1="120" x2="280" y2="178"/>

  <rect class="hi pulse" x="88" y="178" width="384" height="112" rx="14"/>
  <text x="280" y="210" text-anchor="middle" class="cap">OPENWEBUI · ENTRÉE SÉCURISÉE</text>
  <text x="280" y="236" text-anchor="middle" class="lab">Auth / Chat Lié à la Session</text>
  <text x="280" y="258" text-anchor="middle" class="sub">Seul l'utilisateur connecté entre dans ce flux</text>
  <text x="280" y="276" text-anchor="middle" class="sub">Le téléchargement revient ici — même entrée chat</text>

  <line class="line" x1="280" y1="290" x2="280" y2="360"/>
  <text x="300" y="332" class="lbl flow-lbl">L'Agent Réfléchit → Outils</text>

  <rect class="hi" x="100" y="360" width="360" height="80" rx="12"/>
  <text x="280" y="388" text-anchor="middle" class="lab">Couche MCP (FastMCP)</text>
  <text x="280" y="410" text-anchor="middle" class="sub">Outils Office — pptx / docx / xlsx</text>
  <text x="280" y="428" text-anchor="middle" class="sub">Orchestre la génération hors du chat</text>

  <line class="line ingest" x1="280" y1="440" x2="280" y2="510"/>
  <text x="300" y="482" class="lbl flow-lbl">Vers AWS</text>

  <rect class="cloud" x="88" y="510" width="384" height="148" rx="14"/>
  <text x="104" y="538" class="cap">ENVIRONNEMENT AWS</text>
  <rect class="b" x="112" y="556" width="160" height="72" rx="10"/>
  <text x="192" y="586" text-anchor="middle" class="lab">Bedrock</text>
  <text x="192" y="608" text-anchor="middle" class="sub">Raisonnement / gén. IA</text>
  <rect class="b" x="292" y="556" width="160" height="72" rx="10"/>
  <text x="372" y="586" text-anchor="middle" class="lab">S3</text>
  <text x="372" y="608" text-anchor="middle" class="sub">Stocke le fichier Office</text>

  <path class="line return" d="M280 658 V720 H40 V234 H88"/>
  <text x="56" y="470" class="lbl flow-lbl" transform="rotate(-90 56 470)">URL Signée → Entrée OWUI</text>
  <text x="200" y="744" text-anchor="middle" class="sub">Borné utilisateur — seul le demandeur peut télécharger</text>

  <rect class="b" x="100" y="748" width="360" height="48" rx="10"/>
  <text x="280" y="770" text-anchor="middle" class="foot">Sécu OWUI + URL signée par utilisateur</text>
  <text x="280" y="786" text-anchor="middle" class="foot">Même entrée chat · livraison bornée</text>
""",
    "Architecture MCP Office Machine",
    "Chat OpenWebUI sécurisé → outils MCP Office → Bedrock/S3 dans AWS → URL signée bornée vers l'entrée OWUI.",
    vh=MCP_H,
)

# --- ANALYZER ---
# Any chat → n8n workflows (4 chips) → MCP scan detail → Spec sheet only back
# Thesis: AI orchestrates · MCP executes · source stays out of the model
ANALYZER_H = 1160
save(
    "analyzer",
    "en",
    """
  <text x="24" y="28" class="title">REPO ANALYZER · QUALITY + SECURITY SCAN</text>
  <text x="24" y="48" class="foot">Any chat asks to scan a repo — n8n workflows orchestrate, MCP analyzes, Spec sheet returns</text>

  <rect class="b" x="100" y="68" width="360" height="64" rx="12"/>
  <text x="280" y="94" text-anchor="middle" class="lab">Any AI Chat</text>
  <text x="280" y="116" text-anchor="middle" class="sub">“Scan this repo…” · OWUI · local · cloud</text>

  <line class="line" x1="280" y1="132" x2="280" y2="210"/>
  <text x="300" y="178" class="lbl flow-lbl">Repo URL / Ref</text>

  <rect class="out" x="48" y="210" width="464" height="230" rx="14"/>
  <text x="68" y="242" class="cap">N8N WORKFLOWS · AI-WIRED</text>
  <text x="280" y="266" text-anchor="middle" class="sub">GitHub · GitLab · Bitbucket — AI picks &amp; chains the jobs</text>

  <rect class="chip" x="76" y="286" width="176" height="52" rx="8"/>
  <text x="164" y="318" text-anchor="middle" class="lbl">1 · Ingest URL</text>
  <path class="line stem" d="M252 312 H284"/>
  <rect class="chip" x="284" y="286" width="204" height="52" rx="8"/>
  <text x="386" y="318" text-anchor="middle" class="lbl">2 · Call MCP Scan</text>

  <path class="line stem" d="M386 338 V356 H164 V374"/>

  <rect class="chip" x="76" y="374" width="176" height="52" rx="8"/>
  <text x="164" y="406" text-anchor="middle" class="lbl">3 · Aggregate Scores</text>
  <path class="line stem" d="M252 400 H284"/>
  <rect class="hi pulse" x="284" y="374" width="204" height="52" rx="8"/>
  <text x="386" y="406" text-anchor="middle" class="lbl">4 · Emit Spec Sheet</text>

  <line class="line" x1="280" y1="440" x2="280" y2="510"/>
  <text x="300" y="482" class="lbl flow-lbl">Inside Step 2 · MCP Detail</text>

  <rect class="out" x="56" y="510" width="448" height="320" rx="14"/>
  <text x="72" y="538" class="cap">MCP ANALYSIS PIPELINE · AST-AWARE</text>

  <rect class="b" x="88" y="558" width="384" height="56" rx="10"/>
  <text x="280" y="582" text-anchor="middle" class="lab">Tree-sitter · Code Tree First</text>
  <text x="280" y="602" text-anchor="middle" class="sub">Any language · then drill level by level as needed</text>

  <line class="line ingest" x1="280" y1="614" x2="280" y2="660"/>

  <rect class="b" x="88" y="660" width="384" height="56" rx="10"/>
  <text x="280" y="684" text-anchor="middle" class="lab">Commit-Timed Scans</text>
  <text x="280" y="704" text-anchor="middle" class="sub">Project start · +2 months · +1 year — same repo, time slices</text>

  <line class="line ingest" x1="280" y1="716" x2="280" y2="762"/>

  <rect class="hi pulse" x="88" y="762" width="384" height="48" rx="10"/>
  <text x="280" y="792" text-anchor="middle" class="lab">Cyclomatic Complexity + Security Signals</text>

  <line class="line return" x1="280" y1="830" x2="280" y2="900"/>
  <text x="300" y="872" class="lbl flow-lbl">Report Only → Chat</text>

  <rect class="hi pulse" x="88" y="900" width="384" height="88" rx="12"/>
  <text x="280" y="928" text-anchor="middle" class="lab">Spec Sheet / Structured Report</text>
  <text x="280" y="950" text-anchor="middle" class="sub">What this project is · quality &amp; security view</text>
  <text x="280" y="970" text-anchor="middle" class="sub">Dev-usable deliverable — model never sees raw source</text>

  <rect class="b" x="88" y="1012" width="384" height="120" rx="10"/>
  <text x="280" y="1042" text-anchor="middle" class="foot">Pattern: AI orchestrates · n8n workflows · MCP executes</text>
  <text x="280" y="1064" text-anchor="middle" class="foot">Source stays out of the model · Spec sheet is the contract</text>
  <text x="280" y="1086" text-anchor="middle" class="foot">Ingest → Scan → Aggregate → Emit</text>
  <text x="280" y="1108" text-anchor="middle" class="foot">Tree-sitter · Cyclomatic Complexity · Multi-forge</text>
""",
    "Repo Analyzer architecture",
    "Any AI chat into n8n workflows; MCP Tree-sitter scan with commit timelines and cyclomatic/security scoring; Spec sheet only returns to the chat.",
    vh=ANALYZER_H,
)

save(
    "analyzer",
    "fr",
    """
  <text x="24" y="28" class="title">REPO ANALYZER · SCAN QUALITÉ + SÉCURITÉ</text>
  <text x="24" y="48" class="foot">Un chat demande un scan — workflows n8n orchestrent, MCP analyse, Spec sheet revient</text>

  <rect class="b" x="100" y="68" width="360" height="64" rx="12"/>
  <text x="280" y="94" text-anchor="middle" class="lab">N'importe Quel Chat IA</text>
  <text x="280" y="116" text-anchor="middle" class="sub">« Scan ce dépôt… » · OWUI · local · cloud</text>

  <line class="line" x1="280" y1="132" x2="280" y2="210"/>
  <text x="300" y="178" class="lbl flow-lbl">URL / Réf Dépôt</text>

  <rect class="out" x="48" y="210" width="464" height="230" rx="14"/>
  <text x="68" y="242" class="cap">WORKFLOWS N8N · CÂBLÉS PAR L'IA</text>
  <text x="280" y="266" text-anchor="middle" class="sub">GitHub · GitLab · Bitbucket — l'IA choisit et enchaîne les jobs</text>

  <rect class="chip" x="76" y="286" width="176" height="52" rx="8"/>
  <text x="164" y="318" text-anchor="middle" class="lbl">1 · Ingérer URL</text>
  <path class="line stem" d="M252 312 H284"/>
  <rect class="chip" x="284" y="286" width="204" height="52" rx="8"/>
  <text x="386" y="318" text-anchor="middle" class="lbl">2 · Appeler Scan MCP</text>

  <path class="line stem" d="M386 338 V356 H164 V374"/>

  <rect class="chip" x="76" y="374" width="176" height="52" rx="8"/>
  <text x="164" y="406" text-anchor="middle" class="lbl">3 · Agréger Scores</text>
  <path class="line stem" d="M252 400 H284"/>
  <rect class="hi pulse" x="284" y="374" width="204" height="52" rx="8"/>
  <text x="386" y="406" text-anchor="middle" class="lbl">4 · Émettre Spec Sheet</text>

  <line class="line" x1="280" y1="440" x2="280" y2="510"/>
  <text x="300" y="482" class="lbl flow-lbl">Dans l'Étape 2 · Détail MCP</text>

  <rect class="out" x="56" y="510" width="448" height="320" rx="14"/>
  <text x="72" y="538" class="cap">PIPELINE D'ANALYSE MCP · SENSIBLE AST</text>

  <rect class="b" x="88" y="558" width="384" height="56" rx="10"/>
  <text x="280" y="582" text-anchor="middle" class="lab">Tree-sitter · Arbre du Code D'abord</text>
  <text x="280" y="602" text-anchor="middle" class="sub">Toute langue · puis descente niveau par niveau</text>

  <line class="line ingest" x1="280" y1="614" x2="280" y2="660"/>

  <rect class="b" x="88" y="660" width="384" height="56" rx="10"/>
  <text x="280" y="684" text-anchor="middle" class="lab">Scans Datés par Commit</text>
  <text x="280" y="704" text-anchor="middle" class="sub">Début projet · +2 mois · +1 an — mêmes dépôts, tranches de temps</text>

  <line class="line ingest" x1="280" y1="716" x2="280" y2="762"/>

  <rect class="hi pulse" x="88" y="762" width="384" height="48" rx="10"/>
  <text x="280" y="792" text-anchor="middle" class="lab">Complexité Cyclomatique + Signaux Sécu</text>

  <line class="line return" x1="280" y1="830" x2="280" y2="900"/>
  <text x="300" y="872" class="lbl flow-lbl">Rapport Seul → Chat</text>

  <rect class="hi pulse" x="88" y="900" width="384" height="88" rx="12"/>
  <text x="280" y="928" text-anchor="middle" class="lab">Spec Sheet / Rapport Structuré</text>
  <text x="280" y="950" text-anchor="middle" class="sub">Ce qu'est le projet · vue qualité &amp; sécurité</text>
  <text x="280" y="970" text-anchor="middle" class="sub">Livrable utile au dev — le modèle ne voit jamais le source brut</text>

  <rect class="b" x="88" y="1012" width="384" height="120" rx="10"/>
  <text x="280" y="1042" text-anchor="middle" class="foot">Pattern : l'IA orchestre · workflows n8n · le MCP exécute</text>
  <text x="280" y="1064" text-anchor="middle" class="foot">Le source reste hors du modèle · la Spec sheet est le contrat</text>
  <text x="280" y="1086" text-anchor="middle" class="foot">Ingérer → Scanner → Agréger → Émettre</text>
  <text x="280" y="1108" text-anchor="middle" class="foot">Tree-sitter · Complexité Cyclomatique · Multi-forge</text>
""",
    "Architecture Repo Analyzer",
    "Chat IA quelconque vers workflows n8n ; scan MCP Tree-sitter avec timelines de commits et scoring cyclomatique/sécurité ; seule la Spec sheet revient au chat.",
    vh=ANALYZER_H,
)

# --- CODIUM ---
# IDE+AI → methodology KB → human gate → container engine (Kali/Python/HTTP/VPN) → report
# Local engine, cloud-ready; every action needs pentester approval; no exploit detail on diagram
CODIUM_H = 1080
save(
    "codium",
    "en",
    """
  <text x="24" y="28" class="title">CODIUM RED · AI PENTEST ASSISTANT</text>
  <text x="24" y="48" class="foot">IDE + AI drives a local Kali engine — every action waits for human approval</text>

  <rect class="hi" x="88" y="68" width="384" height="72" rx="12"/>
  <text x="280" y="96" text-anchor="middle" class="lab">IDE + Connected AI</text>
  <text x="280" y="118" text-anchor="middle" class="sub">Cursor-like workspace · target any web app</text>

  <line class="line" x1="280" y1="140" x2="280" y2="210"/>
  <text x="300" y="182" class="lbl flow-lbl">Plans Against Target</text>

  <rect class="b" x="72" y="210" width="416" height="88" rx="12"/>
  <text x="280" y="238" text-anchor="middle" class="lab">AI Restrictions + Methodology KB</text>
  <text x="280" y="260" text-anchor="middle" class="sub">Dictionary fed with PTES · MITRE ATT&amp;CK · CVE docs</text>
  <text x="280" y="280" text-anchor="middle" class="sub">Bounded agent — method over freestyle</text>

  <line class="line gate" x1="280" y1="298" x2="280" y2="368"/>
  <text x="300" y="340" class="lbl flow-lbl">Propose Action</text>

  <rect class="hi pulse" x="72" y="368" width="416" height="72" rx="12"/>
  <text x="280" y="396" text-anchor="middle" class="lab">Pentester Approval Gate</text>
  <text x="280" y="418" text-anchor="middle" class="sub">Every step · approve · review · deny — agent never acts alone</text>

  <line class="line" x1="280" y1="440" x2="280" y2="510"/>
  <text x="300" y="482" class="lbl flow-lbl">Approved → Engine</text>

  <rect class="out" x="48" y="510" width="464" height="250" rx="14"/>
  <text x="68" y="540" class="cap">CONTAINER ENGINE · LOCAL · CLOUD-READY</text>
  <text x="280" y="562" text-anchor="middle" class="sub">Isolated execution behind the IDE</text>

  <rect class="chip" x="72" y="580" width="196" height="56" rx="8"/>
  <text x="170" y="604" text-anchor="middle" class="lbl">Kali CLI + Tools</text>
  <text x="170" y="622" text-anchor="middle" class="sub">Pentest toolkit</text>
  <rect class="chip" x="292" y="580" width="196" height="56" rx="8"/>
  <text x="390" y="604" text-anchor="middle" class="lbl">Python Playground</text>
  <text x="390" y="622" text-anchor="middle" class="sub">AI writes &amp; runs code</text>

  <rect class="chip" x="72" y="652" width="196" height="56" rx="8"/>
  <text x="170" y="676" text-anchor="middle" class="lbl">HTTP Server</text>
  <text x="170" y="694" text-anchor="middle" class="sub">Stand up listeners</text>
  <rect class="chip" x="292" y="652" width="196" height="56" rx="8"/>
  <text x="390" y="676" text-anchor="middle" class="lbl">Stealth VPN</text>
  <text x="390" y="694" text-anchor="middle" class="sub">Quiet path to target</text>

  <line class="line ingest" x1="280" y1="760" x2="280" y2="830"/>
  <text x="300" y="802" class="lbl flow-lbl">Connect · Code · Assess</text>

  <rect class="hi pulse" x="72" y="830" width="416" height="88" rx="12"/>
  <text x="280" y="858" text-anchor="middle" class="lab">Findings Report</text>
  <text x="280" y="880" text-anchor="middle" class="sub">Structured engagement report when the run completes</text>
  <text x="280" y="900" text-anchor="middle" class="sub">Back to the IDE — human still owns the call</text>

  <rect class="b" x="72" y="942" width="416" height="108" rx="10"/>
  <text x="280" y="972" text-anchor="middle" class="foot">Pattern: IDE + AI plan · container engine executes</text>
  <text x="280" y="994" text-anchor="middle" class="foot">Human gate on every action · methodology-bound</text>
  <text x="280" y="1016" text-anchor="middle" class="foot">Local first · integrable in a cloud environment</text>
""",
    "Codium Red architecture",
    "IDE with AI assistant, methodology KB, human approval gate, Kali container engine with Python/HTTP/VPN, findings report.",
    vh=CODIUM_H,
)

save(
    "codium",
    "fr",
    """
  <text x="24" y="28" class="title">CODIUM RED · ASSISTANT PENTEST IA</text>
  <text x="24" y="48" class="foot">IDE + IA pilotent un moteur Kali local — chaque action attend l'approbation humaine</text>

  <rect class="hi" x="88" y="68" width="384" height="72" rx="12"/>
  <text x="280" y="96" text-anchor="middle" class="lab">IDE + IA Connectée</text>
  <text x="280" y="118" text-anchor="middle" class="sub">Espace type Cursor · cibler toute appli web</text>

  <line class="line" x1="280" y1="140" x2="280" y2="210"/>
  <text x="300" y="182" class="lbl flow-lbl">Planifie Contre la Cible</text>

  <rect class="b" x="72" y="210" width="416" height="88" rx="12"/>
  <text x="280" y="238" text-anchor="middle" class="lab">Restrictions IA + Base Méthodo</text>
  <text x="280" y="260" text-anchor="middle" class="sub">Dictionnaire nourri de PTES · MITRE ATT&amp;CK · CVE</text>
  <text x="280" y="280" text-anchor="middle" class="sub">Agent borné — méthode avant freestyle</text>

  <line class="line gate" x1="280" y1="298" x2="280" y2="368"/>
  <text x="300" y="340" class="lbl flow-lbl">Propose une Action</text>

  <rect class="hi pulse" x="72" y="368" width="416" height="72" rx="12"/>
  <text x="280" y="396" text-anchor="middle" class="lab">Porte d'Approbation Pentester</text>
  <text x="280" y="418" text-anchor="middle" class="sub">Chaque étape · approuver · revoir · refuser — l'agent n'agit jamais seul</text>

  <line class="line" x1="280" y1="440" x2="280" y2="510"/>
  <text x="300" y="482" class="lbl flow-lbl">Approuvé → Moteur</text>

  <rect class="out" x="48" y="510" width="464" height="250" rx="14"/>
  <text x="68" y="540" class="cap">MOTEUR CONTENEUR · LOCAL · PRÊT CLOUD</text>
  <text x="280" y="562" text-anchor="middle" class="sub">Exécution isolée derrière l'IDE</text>

  <rect class="chip" x="72" y="580" width="196" height="56" rx="8"/>
  <text x="170" y="604" text-anchor="middle" class="lbl">Kali CLI + Outils</text>
  <text x="170" y="622" text-anchor="middle" class="sub">Boîte à outils pentest</text>
  <rect class="chip" x="292" y="580" width="196" height="56" rx="8"/>
  <text x="390" y="604" text-anchor="middle" class="lbl">Playground Python</text>
  <text x="390" y="622" text-anchor="middle" class="sub">L'IA écrit &amp; exécute</text>

  <rect class="chip" x="72" y="652" width="196" height="56" rx="8"/>
  <text x="170" y="676" text-anchor="middle" class="lbl">Serveur HTTP</text>
  <text x="170" y="694" text-anchor="middle" class="sub">Lève des listeners</text>
  <rect class="chip" x="292" y="652" width="196" height="56" rx="8"/>
  <text x="390" y="676" text-anchor="middle" class="lbl">VPN Discret</text>
  <text x="390" y="694" text-anchor="middle" class="sub">Chemin calme vers la cible</text>

  <line class="line ingest" x1="280" y1="760" x2="280" y2="830"/>
  <text x="300" y="802" class="lbl flow-lbl">Connecter · Coder · Évaluer</text>

  <rect class="hi pulse" x="72" y="830" width="416" height="88" rx="12"/>
  <text x="280" y="858" text-anchor="middle" class="lab">Rapport de Findings</text>
  <text x="280" y="880" text-anchor="middle" class="sub">Rapport d'engagement structuré en fin de run</text>
  <text x="280" y="900" text-anchor="middle" class="sub">Retour à l'IDE — l'humain garde la décision</text>

  <rect class="b" x="72" y="942" width="416" height="108" rx="10"/>
  <text x="280" y="972" text-anchor="middle" class="foot">Pattern : IDE + IA planifient · le moteur conteneur exécute</text>
  <text x="280" y="994" text-anchor="middle" class="foot">Porte humaine sur chaque action · borné par la méthodo</text>
  <text x="280" y="1016" text-anchor="middle" class="foot">Local d'abord · intégrable dans un environnement cloud</text>
""",
    "Architecture Codium Red",
    "IDE avec assistant IA, base méthodo, porte d'approbation humaine, moteur conteneur Kali avec Python/HTTP/VPN, rapport de findings.",
    vh=CODIUM_H,
)

for stem in ("ronin", "centinel", "voice", "mcp", "analyzer", "codium"):
    src = (OUT / f"arch-{stem}.en.svg").read_text(encoding="utf-8")
    (OUT / f"arch-{stem}.svg").write_text(src, encoding="utf-8", newline="\n")
    print("alias", f"arch-{stem}.svg")
