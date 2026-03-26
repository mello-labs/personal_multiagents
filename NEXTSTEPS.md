# NEXT STEPS

Documento de prioridades para a próxima fase do sistema.

A premissa é simples: velocidade agora, arquitetura depois. Pressa não elimina estratégia. Apenas obriga a separar o que gera alavancagem do que só parece sofisticado.

## P0

### Push notifications reais

Objetivo: receber avisos fora da interface web.

Eventos prioritários:

- próximo compromisso em 15 min
- próximo compromisso em 5 min
- bloco atrasado
- bloco reagendado automaticamente
- resumo diário no início da manhã

Canal recomendado para entrega rápida:

- Telegram ou Pushover

Motivo:

- menor atrito
- implementação simples
- entrega confiável mesmo fora do Mac

Evitar nesta fase:

- APNs nativo
- arquitetura excessiva de mensageria
- múltiplos canais ao mesmo tempo

### Agendador de notificações

Objetivo: transformar estado interno em eventos acionáveis.

Necessário:

- job periódico que consulte agenda do dia
- cálculo de janela para “próximo compromisso”
- prevenção de duplicidade por evento
- registro em auditoria de cada envio

Motivo:

- sem isso, o sistema detecta mas não entrega

## P1

### Bridge local para macOS

Objetivo: exibir notificações nativas no Mac.

Abordagem:

- agente local com `launchd`
- uso de `terminal-notifier` ou `osascript`
- polling simples de eventos pendentes vindos do backend

Motivo:

- aproxima a experiência do que o Notion já faz

Risco:

- depende do Mac estar ligado
- aumenta a superfície operacional

### Web Push no dashboard

Objetivo: transformar a interface web em canal ativo.

Abordagem:

- service worker
- inscrição de browser
- envio via Web Push com VAPID

Motivo:

- mantém tudo dentro do produto
- bom caminho para PWA futura

Risco:

- requer permissão de browser
- UX inconsistente entre navegadores

## P2

### Motor de regras para alertas

Objetivo: sair do hardcode e criar governança sobre os avisos.

Exemplos de regras:

- notificar apenas tarefas de prioridade alta
- suprimir alerta se já houver sessão de foco ativa
- elevar severidade após N reagendamentos
- pausar alertas em janela noturna

Motivo:

- notificação sem critério vira poluição

### Preferências por usuário/dispositivo

Objetivo: controlar frequência, canal e tipo de aviso.

Campos desejáveis:

- canal preferido
- horário de silêncio
- lembretes permitidos
- antecedência padrão

## P3

### Sincronização avançada com calendário

Objetivo: enriquecer o contexto dos avisos.

Ideias:

- importar Google Calendar de forma mais agressiva
- diferenciar compromisso externo de bloco interno
- não reagendar automaticamente em cima de reunião real

### Analytics de confiabilidade

Objetivo: medir se o sistema está ajudando ou apenas emitindo ruído.

Métricas úteis:

- alertas enviados
- alertas ignorados
- alertas que geraram ação
- tempo médio até reação
- tarefas reagendadas vs concluídas

## Sugestão de sequência

1. Implementar notificações via Telegram ou Pushover.
2. Criar tabela/estado para deduplicação de avisos enviados.
3. Ligar eventos de agenda e atraso ao canal escolhido.
4. Validar utilidade por alguns dias.
5. Só então decidir entre Web Push e bridge nativa macOS.

## Decisões que precisam de avaliação

- canal principal de notificação: Telegram, Pushover, Slack, Discord ou bridge local
- antecedência padrão para compromisso: 5, 10 ou 15 minutos
- horário de silêncio
- quais eventos merecem push e quais devem ficar apenas na auditoria
- se o auto-reagendamento deve sempre notificar ou apenas em prioridade alta

## Regra estratégica

O erro clássico aqui é tentar parecer “plataforma de notificações” antes de provar utilidade.

Primeiro: entregar aviso confiável.
Depois: sofisticar canal, preferências e inteligência.
