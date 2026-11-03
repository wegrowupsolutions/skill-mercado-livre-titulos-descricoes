# Skill do Claude: títulos e descrições para o Mercado Livre

Uma skill **gratuita e de código aberto** (licença MIT) que ensina o Claude a criar anúncios do Mercado Livre do jeito certo, sempre. Você passa os dados do produto e recebe:

1. **5 títulos** de até 60 caracteres, com a contagem ao lado, em 5 ângulos (busca direta, característica forte, medida, público e uso, compatibilidade).
2. **1 descrição** em texto simples (sem HTML, emoji, link, contato ou preço), com características, especificações, o que vem na embalagem e perguntas frequentes.
3. **Ficha técnica sugerida** (os atributos que a categoria costuma pedir).
4. **8 a 12 termos de busca**, como o comprador digita, e onde usar cada um.

Antes de entregar, a skill passa por um checklist. Se faltar um dado (medida, garantia, material), ela **não inventa**: escreve `[CONFIRMAR]` no lugar.

> **Aviso:** projeto independente. Não é oficial do Mercado Livre nem da Anthropic. As regras do Mercado Livre mudam, então confira sempre na Ajuda do vendedor. A skill melhora a qualidade do texto, mas **não promete venda nem posição na busca**. O Claude pode errar: leia e confira tudo antes de publicar.

---

## Baixar

- **Mais fácil:** vá em [**Releases**](../../releases/latest) e baixe `ml-titulos-descricoes.zip`.
- **Ou:** clique em **Code > Download ZIP** neste repositório. Dentro, a pasta da skill é `ml-titulos-descricoes`.

## Instalar (escolha um caminho)

### Caminho 1: Claude Code (terminal ou aplicativo)
1. Copie a pasta `ml-titulos-descricoes` (a pasta inteira) para a pasta de skills do seu usuário:
   - Windows: `C:\Users\SEU_USUARIO\.claude\skills\`
   - Mac e Linux: `~/.claude/skills/`
2. Reabra o Claude Code.
3. Peça: `Crie título e descrição para este produto no Mercado Livre: ...` (ou chame pelo nome: `/ml-titulos-descricoes`).

O caminho final precisa ficar assim: `.claude/skills/ml-titulos-descricoes/SKILL.md`.

### Caminho 2: Claude no site ou aplicativo (Claude.ai)
1. Baixe `ml-titulos-descricoes.zip` na página de Releases.
2. Abra as configurações do Claude e procure a área de **Skills** (pode aparecer em *Configurações > Recursos*; o nome do menu varia conforme a versão e o plano. Confira em [support.claude.com](https://support.claude.com)).
3. Envie o arquivo `.zip` e ative a skill.
4. Em uma conversa nova, cole os dados do produto.

### Caminho 3: sem instalar nada
Abra o arquivo [`prompt-sem-skill.md`](prompt-sem-skill.md), copie o texto, troque os dados do produto no final e cole no chat de qualquer Claude. É a mesma lógica, mas sem a verificação automática: **confira você mesmo** se cada título tem até 60 caracteres.

---

## Como usar

Cole os dados do produto. Quanto mais fato verdadeiro, melhor o resultado:

```
Crie título e descrição para o Mercado Livre:
Produto: caneca térmica de inox 500 ml, tampa antivazamento, cor preta, parede dupla
Marca: (se tiver)
Medidas e material: (o que você sabe)
Vem na caixa: 1 caneca com tampa
Para quem é: uso diário, carro e escritório
```

Se algo faltar, a skill pergunta ou marca `[CONFIRMAR]`. Depois:

1. Escolha 1 dos 5 títulos e confira a contagem.
2. Preencha os `[CONFIRMAR]` com o que está na caixa ou na embalagem do produto.
3. Copie a descrição (texto simples) para o anúncio.
4. Preencha a ficha técnica com os atributos sugeridos.
5. Confira medidas, material e garantia contra o produto que está na sua mão.
6. Abra a Ajuda do vendedor e confira as regras da sua categoria antes de publicar.

Mais exemplos em [`ml-titulos-descricoes/references/exemplos.md`](ml-titulos-descricoes/references/exemplos.md).

### Verificador de títulos (opcional)
Precisa de Python 3 instalado.

```bash
python ml-titulos-descricoes/scripts/checar_titulo.py "Caneca Térmica Inox 500 ml Tampa Antivazamento Preta"
```

Mostra a contagem de caracteres (`OK` ou `!!`) e avisa de: passou de 60, caixa alta, símbolos, emoji, termos promocionais (por exemplo "promoção", "frete grátis", "original") e palavra repetida. São alertas da skill, não regra oficial.

---

## O que tem neste repositório

```
ml-titulos-descricoes/        <- a skill (copie esta pasta)
  SKILL.md                    instruções do Claude
  references/
    regras-mercado-livre.md   regras e limites, com data de conferência
    exemplos.md               exemplos de resultado
  scripts/
    checar_titulo.py          verificador de caracteres
prompt-sem-skill.md           versão para colar no chat
LICENSE
```

## Limites e cuidados

- **Não invente dados do produto.** A skill marca `[CONFIRMAR]` quando falta informação. Confira tudo antes de publicar.
- **Saúde, suplementos e cosméticos:** a skill descreve ingrediente e uso sem prometer efeito, mas o registro na ANVISA e a política da categoria são responsabilidade do vendedor.
- **Os limites** (60 caracteres no título, texto simples na descrição) foram levantados em fontes de terceiros, não na documentação oficial. Veja `references/regras-mercado-livre.md`. Se achar que mudou, abra uma *issue*.

## Perguntas frequentes

**A skill faz meu anúncio aparecer na busca?** Não. Ela ajuda a evitar erros básicos e a organizar o texto. Venda e posição dependem de produto, preço, concorrência e das regras do Mercado Livre.

**Funciona para outros marketplaces?** Foi feita para o Mercado Livre. Os princípios servem para outros, mas os limites e as regras mudam.

**Posso mudar a skill?** Pode. A licença é MIT: use, modifique e compartilhe.

**Encontrei um erro ou uma regra desatualizada.** Abra uma *issue* ou um *pull request* aqui no repositório.

## Licença

MIT. Veja [`LICENSE`](LICENSE).

---

Criada por Vinicius, do canal [@viniciusarmstrong](https://www.youtube.com/@viniciusarmstrong). Vídeo explicando como usar: link na descrição do canal.
