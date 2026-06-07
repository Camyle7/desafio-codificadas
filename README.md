# Desafio Codeforces — Mentoria Codificadas | Além do Código
 
## Sobre este repositório
 
Este repositório contém minha resolução para o desafio de programação proposto na mentoria, utilizando problemas da plataforma [Codeforces](https://codeforces.com/) com auxílio de Inteligência Artificial.
 
---
 
## Problemas escolhidos
 
| # | Nome do problema | Link | Dificuldade |
|---|-----------------|------|-------------|
| 1 | Absolute Cinema | [Ver no Codeforces](https://codeforces.com/problemset/problem/2229/B) | 800 |

---
 
## Problema 1 — [Absolute Cinema]
 
### O que o problema pede?
O problema mostra dois arrays *a* e *b* de tamanho *n*. A operação pede para que escolha um índice *i* e trocar a[i] com b[i], trocar elementos na mesma posição. O objetivo é maximizar: max(a) + soma(b).
 
 
### Como eu resolvi?
Temos dois arrays que podem ser trocados a[i] com b[i] em qualquer posição sem alterar o valor da soma. Nisso para uma posição j que tinha máximo de a, queremos a[j] grande. E para todas as outras posições, queremos a[i] pequeno (para minimizar sum(a)). Então para cada posição J máxima, colocamos max(a[j], b[j]) em a[j]. E para as posições i diferentes de J colocamos min(a[i], b[i]) em a[i].
 
 
### Código
```python

```import sys 
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list (map(int, input().split()))
    b = list (map(int, input().split()))

    S_total = sum(a) + sum(b)
    mins = [min(a[i], b[i]) for i in range(n)]
    sum_mins = sum(mins)
    best = max(mins)

    print(S_total - sum_mins + best)

t = int(input())
for _ in range(t):
    solve()
 

 

```
 
---
 

 
 

```
```
 


---
 
## IA utilizada
 
**Qual IA você usou?**

Claude.
 
**Como a IA te ajudou?**

Me ajudou a interpretar o problema, procurar uma solução para o problema e corrigir erros no código.
---
 
## Reflexão
 
### Dificuldades encontradas
A parte de escrever o código foi a mais difícil, já que não tenho conhecimento sobre a linguagem phyton.
<>
 
 
### O que aprendi
Aprendi a como usar uma IA para ajudar na resolução de um problema em programação por etapas. Desde achar uma estratégia até em corrigir erros de sintaxe.
<>
 
 
### Como foi a experiência?
Gostei bastante da experiência, tive contato e utilizei a linguagem phyton que é uma linguagem que tenho muito interesse em aprender e também conheci a plataforma da codeforces que tenho certeza que vai me ajudar bastante durante os meus estudos.
