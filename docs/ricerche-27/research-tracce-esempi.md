# Ricerca: tracce annotate (Hamel Husain) e traiettorie per RL agentico

Data di accesso di tutte le fonti: 2026-09-04. Citazioni brevi (max 2-3 righe) per rispettare il copyright.

## 1. Tracce annotate ed error analysis (Hamel Husain)

### 1a. Traccia annotata a mano — caso reale: NurtureBoss (assistente per affitti di appartamenti)

Il caso "Lucy" di Rechat (https://hamel.dev/blog/posts/evals/) descrive il processo (tool custom in Shiny for Python, verdetto good/bad, dashboard Metabase) ma NON pubblica una traccia annotata con testo delle note. L'esempio annotato REALE e pubblico è quello di NurtureBoss nel Field Guide:

- URL: https://hamel.dev/blog/posts/field-guide/
- Screenshot UI di annotazione (pubblico, riproducibile in slide): https://hamel.dev/blog/posts/field-guide/images/nboss_annotate.png
- Screenshot filtro sessioni: https://hamel.dev/blog/posts/field-guide/images/nboss_filter.png

Come appare la UI (verificato sull'immagine): titolo "LLM Grader", tab Home / Runs / Annotation Queues.
Colonna sinistra: lista "All Text Messages 315" con thread_id, data, spunta verde (pass) o rossa (fail), bottone "Show Unannotated".
Centro: la traccia esplosa in card: "AI Settings & Metadata", "Prompt", "Human: What is your availability" (2/5/25),
"Tool Call — Tool Name: getCommunitiesAvailability {}", "Tool Response", poi risposta AI.
Colonna destra: "Rate Conversation" con due bottoni Good / Bad (binario, non Likert), textarea "Notes: Add your notes here...",
"Add Tags", "Update Annotation", Back / Next (navigazione da tastiera).

Testo reale di note di open coding scritte da Hamel durante demo sui dati NurtureBoss (fonti secondarie che trascrivono il video):
- "Should have handed off to a human or had better lead nurturing." — https://www.aakashg.com/hamel-shreya-ai-evals-step-by-step/
- "told user that it would check on bathrooms but didn't do it. Also did not follow user instructions, and rendered markdown in a text message." — stessa fonte
- "Should have asked follow-up questions because user intent was unclear." (utente: "What's up to four month rent?", l'assistente lo interpreta come domanda su sconti) — https://www.chatprd.ai/how-i-ai/hamel-husains-guide-to-ai-evals-with-error-analysis
- "This is bad UX - I want a widget here with a calendar link, not bullet points the user has to parse." — https://thingsithinkithink.blog/posts/2025/06-21-llm-evals-lesson-2-error-analysis/

Esempio di critica pass/fail con testo (Honeycomb Query Assistant, spreadsheet NLQ / query generata / critique / outcome):
- URL: https://hamel.dev/blog/posts/llm-judge/ (immagine `spreadsheet.png` nella stessa cartella)
- Colonne dichiarate: "1. The NLQ 2. The generated query 3. The critique 4. The outcome (pass or fail)"
- Fail reale: "While the query attempts to find the slowest trace using MAX(duration_ms) and ordering correctly, it fails to group by trace.trace_id."
- Pass reale: "The query correctly filters for traces with an IP address of 10.0.2.90 and counts the occurrences..."
- Accordo giudice-esperto > 90% in tre iterazioni; "I start with around 30 examples and keep going until I do not see any new failure modes."

### 1b. Tabella di error analysis con failure mode e conteggi (open coding → axial coding)

- URL testo: https://hamel.dev/blog/posts/field-guide/ ; immagine: https://hamel.dev/blog/posts/field-guide/images/pivot.png
- Processo, citazione: "each row represented a conversation. We wrote open-ended notes on any undesired behavior."
  poi "we used an LLM to build a taxonomy of common failure modes. Finally, we mapped each row to specific failure mode labels and counted the frequency".
- Aspetto della pivot (verificato sull'immagine): tabella Excel a 2 colonne, header azzurro "Row Labels" / "Count of messages":

  | Failure mode (axial code) | Count of messages |
  |---|---|
  | conversation-flow | 110 |
  | handoff | 70 |
  | rescheduling | 60 |

  Didascalia: "Excel Pivot Tables are a simple tool, but they work!". Le tre categorie spiegano "60%+" dei problemi.
  Descrizioni nel testo: conversation flow (contesto mancante, risposte goffe), handoff (non riconosce quando passare a un umano),
  rescheduling (gestione delle date). Risultato dopo il fix: date handling "from 33% to 95%".
- Una seconda tabella con conteggi (Transfer/handoff 15, Tour scheduling 10, Incorrect information 7) compare solo nella
  trascrizione di terzi https://thingsithinkithink.blog/posts/2025/06-21-llm-evals-lesson-2-error-analysis/ (demo del corso su Braintrust); usare con cautela, non è su hamel.dev.

### 1c. Definizioni di metodo (FAQ del corso AI Evals, Husain & Shankar)
- https://hamel.dev/blog/posts/evals-faq/ e https://hamel.dev/blog/posts/evals-faq/why-is-error-analysis-so-important-in-llm-evals-and-how-is-it-performed.html
- 4 fasi: dataset → open coding (note libere, "akin to journaling") → axial coding ("Categorize the open-ended notes into a 'failure taxonomy'") → iterative refinement.
- Consigli: almeno 30 tracce annotate a mano, ~100 tracce diverse come guardrail, "benevolent dictator" come unico annotatore, pass/fail binario invece di scale 1-5, tool custom ("the single most impactful investment").
- Esempi di failure mode citati nelle FAQ: "persona-tone mismatch", omissione delle "pet policies" nei riassunti immobiliari.

## 2. Traiettorie reali per RL agentico

### 2a. Dataset pubblico: nebius/SWE-agent-trajectories (Hugging Face)
- URL: https://huggingface.co/datasets/nebius/SWE-agent-trajectories ; blog: https://nebius.com/blog/posts/scaling-data-collection-for-training-swe-agents
- Dimensione: 80.036 traiettorie; risolte 13.389 = 16,7% (target=true). Task da nebius/SWE-bench-extra (6.411 istanze) + dev di SWE-bench.
  Modelli: swe-agent-llama-70b (e varianti Qwen-2.5-72b). Licenza CC-BY-4.0. Media passi: 31,3 per risolte, 58,4 per non risolte.
- Campi di una riga: `instance_id`, `model_name`, `target` (bool: issue risolta), `trajectory` (lista JSON di turni
  {role: system|user|ai, text, mask}: "ai" = ragionamento + comando; "user" = osservazione dell'ambiente), `exit_status`, `generated_patch` (diff), `eval_logs` (log pytest).
- Esempio reale abbreviato (riga instance_id=Melevir__cognitive_complexity-15, model=swe-agent-llama-70b, target=True, exit_status=submitted, 43 turni):
  1. Task (user): "ISSUE: Incorrect counting for sequences of binary logical operators ... receive a fundamental increment (B1) but not a nesting increment (B3)."
  2. ai: `search_dir "def process_node_itself("`  → obs: "Found 1 matches ... cognitive_complexity/utils/ast.py"
  3. ai: `open cognitive_complexity/utils/ast.py` → obs: "[File: .../utils/ast.py (92 lines total)] ..."
  4. ai: `edit 88:88 / base_complexity = inner_boolops_amount  # Remove the nesting increment (B3) / end_of_edit`
  5. ai: `pytest` → obs: "test session starts ... " ; poi `edit 125:125 ... == 9`, `pytest`, `submit`
  6. Esito: generated_patch = diff su utils/ast.py (`-base_complexity = inner_boolops_amount * max(increment_by, 1)` / `+base_complexity = inner_boolops_amount`); eval_logs: "20 passed in 0.50s ... All tests passed." → reward 1.
  Contro-esempio nello stesso dataset: riga 0, AnalogJ__lexicon-336, target=False, 93 turni, exit_status "submitted (exit_context)".
- Come ottenere una riga senza scaricare tutto (API pubblica):
  https://datasets-server.huggingface.co/rows?dataset=nebius%2FSWE-agent-trajectories&config=default&split=train&offset=0&length=1

Alternative pubbliche (formato tool-call nativo):
- nebius/SWE-rebench-openhands-trajectories: 67.074 traiettorie, 32.161 risolte (~48%), Qwen3-Coder-480B con OpenHands v0.54; ruoli system/assistant/user/tool, campi `resolved`, `exit_status`, `model_patch`. https://huggingface.co/datasets/nebius/SWE-rebench-openhands-trajectories
- nvidia/Open-SWE-Traces e nvidia/SWE-Zero-openhands-trajectories (stessa struttura OpenHands); SWE-Gym (https://github.com/SWE-Gym/SWE-Gym); tau-bench (https://github.com/sierra-research/tau-bench) per il dominio retail/airline.

### 2b. Formato ufficiale OpenAI Reinforcement Fine-Tuning (dataset JSONL + grader)
- Guida RFT: https://developers.openai.com/api/docs/guides/reinforcement-fine-tuning (redirect da platform.openai.com/docs/guides/reinforcement-fine-tuning)
- Guida grader: https://developers.openai.com/api/docs/guides/graders
- Cookbook con esempio end-to-end: https://cookbook.openai.com/examples/reinforcement_fine_tuning
- Riga JSONL (esempio ufficiale, dominio compliance): array `messages` in formato chat, ultimo messaggio con ruolo user, più campi extra usati dal grader:
  `{"messages":[{"role":"user","content":"Do you have a dedicated security team?"}],"compliant":"yes","explanation":"A dedicated security team follows strict protocols for handling incidents."}`
- Grader (reward function) ufficiale, tipo multi: sub-grader `compliant` = string_check `{"type":"string_check","reference":"{{item.compliant}}","operation":"eq","input":"{{sample.output_json.compliant}}"}`
  + sub-grader `explanation` = score_model (LLM judge, es. gpt-4o) ; combinazione `"calculate_output": "0.5 * compliant + 0.5 * explanation"`.
  Template: `{{item.*}}` = campi della riga del dataset, `{{sample.output_text}}` / `{{sample.output_json.*}}` = output del modello.
- Tipi di grader: string_check (0/1, eq/ne/like/ilike), text_similarity (bleu, rouge, fuzzy_match...), score_model (LLM, range [0,1], pass_threshold), python (`def grade(sample, item): return 1.0`), multi (formula su sub-grader).
- Job: `POST /v1/fine_tuning/jobs` con `"model": "o4-mini-2025-04-16"`, `"method": {"type": "reinforcement", "reinforcement": {...}}`.
  Loop dichiarato: per ogni prompt il sistema campiona più risposte, le passa al grader e applica un aggiornamento policy-gradient verso i punteggi alti.
- Dimensioni consigliate: "Start small—between several dozen and a few hundred examples"; max 50.000 esempi training, 1.000 test. Modelli supportati: solo reasoning (o4-mini-2025-04-16).
- Esempio GSM8K nella stessa guida: riga con `reference_answer: "#### 18"` e grader string_check sull'output finale (utile per slide più semplice).

## Cosa è riproducibile in slide
- Slide 1 (error analysis): screenshot `nboss_annotate.png` (UI Good/Bad + Notes + Tool Call) e la pivot 110/70/60 ridisegnata come tabella; 3-4 note di open coding reali citate sopra.
- Slide 2 (traiettorie RL): la riga nebius riassunta in 6 righe (task → 4 comandi/osservazioni → patch → "20 passed" → target=True) affiancata alla riga JSONL + grader multi di OpenAI RFT con la formula del reward.
