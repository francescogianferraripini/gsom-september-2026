# PC AI: 26 — Agentic AI: da LLM ad agenti, offerta e mercato di strumenti agentici, basi concettuali

# Cosa è un agente?

## Cosa li definisce a livello funzionale? 

Che aspettative abbiamo da un agente?

Quale è lo spazio di soluzioni che gli agenti coprono e copriranno?

## Cosa lo definisce a livello tecnico?

Agent = LLM + Harness + System Prompt + Tools + KB + Skills

Harness = Context Initialization and Management + Memory Management + Loop + Tool calling Execution + Skills access + Execution Sandbox + Logging

# LLM: cosa è, perchè funziona, come viene addestrato

* Definizione di modello linguistico, distribuzione dei next token dato il contesto
* Natura autoregressiva - Inner loop fino al token di stop (1° Loop fino al token di stop)
* Perchè funziona
	* Vettori, prodotto scalare come indicatore di una sovrapposizione
	* Embeddings - Lo spazio delle idee. Esempi king-queen e capitali dei paesi
	- Fully connected layers - Fanout (matching concettuale) e compressione tramite sovrapposizione
	- Attention
	- Reverse Embedding (softmax)
	- Context, Complessità quadratica, prefill e KV cache
	- Knowledge intrinseca nei pesi.
	- Riflessione sull'LLM come compressore lossy.
	- MoE
- Come viene addestrato - parte 1: il pretraining
	- Cross entropy loss e gradient descent
	- Cosa abbiamo: il modello linguistico puro
- Come viene addestrato - parte 2: il RL
	- Dalla text completition alla conversazione - RLHF
	- Cosa abbiamo: il modello puramente conversazionale
- Come viene addestrato - parte 3: il RL agentico
	- Tool calling e l'importanza delle traiettorie - GRPO
	- Cosa abbiamo: il modello istruction tuned 

* Rianalisi del loop conversazionale, introduzione al context rot.

* Bonus: multimodality
* Bonus: reasoning

* Elementi economici al contorno.
* Modelli open vs closed
