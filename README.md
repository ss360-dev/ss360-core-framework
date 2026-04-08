# SS 360 SAS - Open Source Security & AI Framework

## Overview
This repository contains a subset of the core engineering utilities used by **SS 360 SAS** to power our Cybersecurity as a Service (CSaaS) infrastructure. Our goal is to provide the community with high-performance, asynchronous tools for AI orchestration and security observability.

## Key Components
* **Async-LiteLLM Adapters:** Optimized routing for LiteLLM with a focus on low-latency failover.
* **Semantic Cache Layer:** Integration with **Valkey** to minimize token consumption and redundant LLM calls.
* **Security Telemetry Parsers:** Python modules for structured logging compatible with Promtail, Loki, and Grafana.
* **Zero-Trust Utility:** Scripts for automated Caddy/Cloudflare Tunnel provisioning.

## Tech Stack
* **Language:** Python 3.11+ (Asynchronous/FastAPI)
* **Cache:** Valkey (High-performance Redis alternative)
* **Infrastructure:** Docker / Caddy Server
* **Observability:** Loki / Grafana

## Why we are contributing
At SS 360, we believe that AI security must be proactive. By open-sourcing our orchestration layer, we aim to standardize how AI agents interact with sensitive infrastructure while maintaining strict adherence to Zero Trust principles.

## Getting Started

### Prerequisites
- Python 3.11
- Valkey (or Redis) instance

### Installation
```bash
pip install -r requirements.txt
```

### Running the Gateway
```bash
export VALKEY_HOST=localhost
uvicorn src.main:app --reload
```

## License
Distributed under the MIT License. See `LICENSE` for more information.
