#!/usr/bin/env python3
"""Confere títulos de anúncio do Mercado Livre: comprimento (até 60), caixa alta, símbolos, emojis, termos promocionais e palavras repetidas.
Uso:  python checar_titulo.py "Título 1" "Título 2"      ou      echo "Título" | python checar_titulo.py
São alertas, não regras oficiais: confira sempre na Ajuda do Mercado Livre."""
import re
import sys

LIMITE = 60
PROMO = ["frete grátis", "frete gratis", "promoção", "promocao", "oferta", "barato", "melhor preço", "melhor preco", "imperdível", "imperdivel",
         "brinde", "últimas unidades", "ultimas unidades", "queima", "liquidação", "liquidacao", "grátis", "gratis", "original"]
SIMBOLOS = re.compile(r"[!*|#@$%&<>{}\[\]~^_=+]")
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐⬆✅❌]")


def checar(t):
    t = t.strip()
    avisos = []
    n = len(t)
    if n > LIMITE:
        avisos.append("passa de %d caracteres (%d)" % (LIMITE, n))
    low = t.lower()
    for p in PROMO:
        if p in low:
            avisos.append("termo promocional ou arriscado: '%s'" % p)
    if SIMBOLOS.search(t):
        avisos.append("símbolos especiais no título")
    if EMOJI.search(t):
        avisos.append("emoji no título")
    letras = [w for w in re.findall(r"[A-Za-zÀ-ÿ]{4,}", t)]
    if letras and sum(1 for w in letras if w.isupper()) >= max(2, len(letras) // 2):
        avisos.append("muita palavra em caixa alta")
    palavras = [w.lower() for w in re.findall(r"[A-Za-zÀ-ÿ0-9]+", t) if len(w) > 2]
    rep = sorted({w for w in palavras if palavras.count(w) > 1})
    if rep:
        avisos.append("palavra repetida: " + ", ".join(rep))
    if re.search(r"\s{2,}", t):
        avisos.append("espaços duplos")
    return n, avisos


def main():
    titulos = sys.argv[1:] or [l for l in sys.stdin.read().splitlines() if l.strip()]
    if not titulos:
        print(__doc__)
        return
    for t in titulos:
        n, av = checar(t)
        print("%s %2d/%d  %s" % ("OK " if not av else "!! ", n, LIMITE, t))
        for a in av:
            print("      - " + a)


if __name__ == "__main__":
    main()
