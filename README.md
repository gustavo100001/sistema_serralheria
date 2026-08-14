# Sistema Metal

Sistema de gerenciamento desenvolvido em **Python** para auxiliar profissionais de serralheria na organização de ferramentas, cortes e orçamentos.

> **Status:** Em desenvolvimento — versão `v0.2`

---

## Sobre o projeto

O Sistema Metal surgiu da ideia de transformar tarefas comuns da rotina de uma serralheria em funcionalidades simples dentro de um sistema.

O projeto está sendo desenvolvido de forma incremental, começando pela implementação da lógica principal em Python e evoluindo posteriormente para persistência de dados, banco de dados e novas funcionalidades.

Atualmente, o sistema funciona através do terminal.

---

## Funcionalidades

### Cadastro e login

* Cadastro de usuários;
* Login através de CPF e senha;
* Validação básica dos dados inseridos.

> Atualmente, os usuários são armazenados apenas em memória e os dados são perdidos quando o programa é encerrado.

### Checklist de ferramentas

* Lista de ferramentas utilizadas na obra;
* Conferência das ferramentas disponíveis;
* Identificação de ferramentas que estão faltando.

### Organização de cortes

* Registro dos tamanhos dos cortes em centímetros;
* Validação das entradas;
* Apresentação dos cortes registrados durante a execução.

### Cálculo de materiais e serviço

* Cadastro dos materiais utilizados;
* Registro dos respectivos valores;
* Cálculo do custo total dos materiais;
* Cálculo do valor de venda conforme a regra de mão de obra implementada;
* Aceita `,` ou `.` como separador decimal.

---

## Tecnologias

* **Python 3.12**
* Bibliotecas padrão do Python

Não são utilizadas bibliotecas externas na versão atual.

---

## Como executar

### Pré-requisitos

* Python 3.12 ou superior;
* Git, caso queira clonar o repositório.

### Clonando o projeto

```bash
git clone https://github.com/gustavo100001/sistema-metal.git
```

Entre na pasta do projeto:

Execute o programa:

---

## Próximos passos

* [ ] Implementar persistência dos usuários em banco de dados
* [ ] Integrar SQL ao sistema
* [ ] Implementar operações CRUD
* [ ] Permitir consultar dados registrados anteriormente
* [ ] Calcular o total de centímetros cortados
* [ ] Registrar e contabilizar barras de metal utilizadas
* [ ] Permitir definir a porcentagem da mão de obra
* [ ] Ampliar o cadastro de ferramentas
* [ ] Melhorar as validações de entrada
* [ ] Melhorar a organização e estrutura do código
* [ ] Criar uma interface gráfica

---

## Objetivo do projeto

Além de buscar solucionar problemas relacionados à rotina de uma serralheria, o Sistema Metal está sendo desenvolvido como uma forma de aplicar conhecimentos de programação em um projeto construído do zero.

A proposta é acompanhar a evolução do sistema desde uma aplicação simples em Python até uma aplicação mais completa, com persistência de dados, banco de dados, operações CRUD e uma interface própria.

---

## Autor

**Gustavo Peixoto de Faria**

GitHub: **gustavo100001**
