# resourcetags
Scripts em python para adicionar tag`s em alguns recursos da AWS baseado nas instâncias EC2

## Requisitos
python 3 instalado
pip para poder instalar o boto3
aws cli para poder configurar os acessos da aws

## Funcionamento

- tag-ebs.py = Adiciona as tags aos volumes que estão associadas a EC2. As tags são adicionadas no volume baseada nas tags que existem no recusro EC2.

- tag-eni-elb.py = Adiciona tags as Network Interfaces(ENI) dos Load Balancers(ELB) baseada nas tags das instâncias(EC2) que estão associadas ao loab balance. As tags são adicionadas nas Interfaces, que tem como base as tags que existem no recusro EC2. Esse script tem uma particularidade pois eu faço uma condicinal onde se as 3 primeiras letras da descrição da minha ENI forem iguais as 3 primeiras letras do nome do meu ELB meu script identifica o recurso(ELB)  e pegas as tags desse recurso e adicona na ENI.

- tag-eni.py = Adiciona tags as Network Interfaces(ENI) das intâncias(EC2). As tags são baseadas nas instâncias que as ENI`s estão associadas.
- tag-snap.py = Adiciona as tags aos snapshots que estão associadas ao volume. As tags são adicionadas no snapshot baseada nas tags que existem no recusro EBS que foram adicinadas rodando o script tag-ebs.py.

Dentro do código vai ter uma área de variáveis que devem ser alteradas de acordo com as tags que deseja aplicar.
O código que não tiver variável não deve ser alterado, devemos somente rodar ele.

Os scripts acima adicionam tags a todos os recursos que encontrarem, os scripts da pasta tag-daily adicionam tags somente nos recursos do dia.

Uma sugestão é que rode os scripts que adicionam todas as tags e depois rode o script que adiciona tags diariamente, com isso fica mais simples colocar tags nos novos recursos.


## Como rodar os scripts

Instalar as dependências:
pip install boto3
pip install datetime
pip install date
pip install botocore

Obs: Descrevi todos os import que tenho no código, pode ser que nem precise fazer todos os install. Faça o teste.

Configurando a AWS:
Depois de ter instalado o AWS Cli rode o comando aws configure e siga os passos na tela.

Rodando o script:

python3 nomedoscript.py

ou

python nomedoscript.py 

A definição python ou pyton3 vai depender de como foi instalado o pytho na sua máquina.

Qualquer dúvida me chama no telegram: @vitorta


OBS: Alguns scripts foram ADAPTADOS e outros foram criados do ZERO.