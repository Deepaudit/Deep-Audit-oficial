# 🛡️ Deep Audit Oficial
> **Framework de Auditoria Ofensiva focado em Web & Networks**

![GitHub License](https://img.shields.io/github/license/Deepaudit/Deep-Audit-oficial?color=blue)
![Focus](https://img.shields.io/badge/Focus-Web%20%26%20Network-red)

O **Deep Audit** é um projeto de segurança cibernética focado na análise profunda de aplicações e infraestruturas. Este repositório serve como portfólio e laboratório para testes de vulnerabilidades críticas.

---

## 🎯 Especialidades & Foco

Este projeto documenta metodologias e ferramentas para:

### 🌐 Web Security (OWASP Top 10)
- **Injection:** Foco em SQLi e **XPath Injection** (ambiente de teste incluso).
- **Broken Access Control:** Exploração de falhas de permissão e IDOR.
- **Business Logic:** Análise de falhas no fluxo lógico das aplicações.

### 🔍 Reconnaissance (Recon)
- Mapeamento de superfície de ataque e subdomínios.
- Identificação de serviços e tecnologias (Fingerprinting).
- Auditoria de infraestrutura de redes e monitoramento.

---

## 📂 Estrutura do Repositório

| Arquivo/Pasta | Função |
| :--- | :--- |
| `index.html` | Dashboard principal da interface Deep Audit. |
| `login.php` | Laboratório vulnerável para estudos de XPath Injection. |
| `usuarios.xml` | Banco de dados XML utilizado no laboratório. |
| `xpath_fuzzer.py` | Script em Python para automação de testes de injeção. |

---

## 🧪 Como Executar o Laboratório
Para testar a vulnerabilidade de XPath Injection presente neste projeto:

1. **Inicie o servidor local:**
   ```bash
   php -S localhost:8000
Execute o Fuzzer em Python:

Bash
python3 xpath_fuzzer.py
⚖️ Aviso Legal (Disclaimer)
Este repositório é destinado exclusivamente para fins educacionais e de pesquisa de segurança autorizada. O uso dessas técnicas sem autorização expressa é ilegal. O autor não se responsabiliza pelo uso indevido deste material.

Desenvolvido por Pablo Eliezer Pesquisador de Segurança e Auditor de Sistemas
