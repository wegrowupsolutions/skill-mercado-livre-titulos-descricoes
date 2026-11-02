# Skill do Claude: títulos e descrições para o Mercado Livre

Uma skill gratuita e de código aberto que ensina o Claude a criar **títulos (até 60 caracteres)**, **descrições em texto simples**, **ficha técnica sugerida** e **termos de busca** para anúncios do Mercado Livre, com checklist de conformidade e um verificador de caracteres.

> Não é oficial do Mercado Livre nem da Anthropic. As regras do Mercado Livre mudam: confira sempre na Ajuda do vendedor. Os resultados do anúncio dependem do produto, do preço, da concorrência e das regras vigentes; a skill não promete vendas.

## O que ela entrega (sempre os 4 blocos)
1. **5 títulos** de até 60 caracteres, com a contagem ao lado, em 5 ângulos (busca, característica, medida, público/uso, compatibilidade).
2. **1 descrição** em texto simples (sem HTML, emoji, links nem contato), com características, especificações, o que vem na embalagem e perguntas frequentes.
3. **Ficha técnica** (atributos que a categoria costuma pedir).
4. **8 a 12 termos de busca** e onde usar cada um.

## Como instalar
**Claude Code (terminal ou aplicativo):** copie a pasta `ml-titulos-descricoes` para `~/.claude/skills/` (no Windows: `C:\Users\SEU_USUARIO\.claude\skills\`). Reabra o Claude Code. Para usar: "crie título e descrição para este produto no Mercado Livre: ..." (ou `/ml-titulos-descricoes`).

**Claude.ai / aplicativo do Claude:** baixe `ml-titulos-descricoes.zip` na página de **Releases** deste repositório (ou compacte você mesmo a pasta `ml-titulos-descricoes`) e envie em *Configurações > Recursos (Capabilities) > Skills* [o nome do menu pode variar conforme a versão do aplicativo e o plano; confira em support.claude.com].

**Sem instalar nada:** abra `prompt-sem-skill.md`, copie o texto, preencha os dados do produto e cole no chat. Nesse caso, confira você mesmo se cada título tem até 60 caracteres.

## Exemplo de uso
```
Crie título e descrição para o Mercado Livre:
Produto: caneca térmica de inox 500 ml, tampa antivazamento, cor preta, parede dupla
Vem na caixa: 1 caneca com tampa
```
Veja resultados de exemplo em `ml-titulos-descricoes/references/exemplos.md`.

## Verificador de títulos (opcional)
```bash
python ml-titulos-descricoes/scripts/checar_titulo.py "Caneca Térmica Inox 500 ml Tampa Antivazamento Preta"
```
Mostra a contagem de caracteres e alerta sobre caixa alta, símbolos, emojis, termos promocionais e palavras repetidas.

## Limites e cuidados
- Não invente dados do produto: a skill marca `[CONFIRMAR]` quando falta informação. Confira tudo antes de publicar.
- Saúde, suplementos e cosméticos: a skill evita promessas de resultado, mas regularização na ANVISA e a política da categoria são responsabilidade do vendedor.
- Limites de título e descrição foram levantados em fontes de terceiros (ver `references/regras-mercado-livre.md`) e podem mudar.

## Licença
MIT. Use, modifique e compartilhe. Sugestões e correções são bem-vindas (abra uma *issue* ou *pull request*).

Criada por Vinicius, do canal [NOME_DO_CANAL] (link na descrição do vídeo).
