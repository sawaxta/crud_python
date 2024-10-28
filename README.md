# Sistema de Gerenciamento Acadêmico

Atividade prática da disciplina de Raciocínio Computacional, do curso de Análise e Desenvolvimento de Sistemas da PUC PR.

## 💻 Pré-requisitos

Antes de começar, é necessário atender aos seguintes requisitos:

- **Python 3** instalado no sistema.
- Compatibilidade do código com todos os sistemas operacionais que suportam Python.

## 🚀 Instalação do projeto

Em um terminal de comando, execute:

### Clone do repositório
`
git clone https://github.com/sawaxta/crud_python.git
`

### Execução do projeto

Para executar o programa, utilize o seguinte comando:

`
python 'main.py'
`

## 🔍 Como Usar

Após executar o programa, um menu interativo será exibido, permitindo que você gerencie as diferentes entidades acadêmicas. Aqui está uma breve descrição das opções disponíveis:

### Menu Principal
1. **Gerenciar Estudantes**:
   - **Incluir Estudante**: Insira o nome, idade e matrícula do estudante para adicioná-lo ao sistema.
   - **Listar Estudantes**: Visualize todos os estudantes cadastrados.
   - **Excluir Estudante**: Escolha um estudante da lista e remova-o do sistema.
   - **Alterar Estudante**: Selecione um estudante da lista e atualize seus dados.

2. **Gerenciar Disciplinas**:
   - **Incluir Disciplina**: Adicione uma nova disciplina informando o código e o nome.
   - **Listar Disciplinas**: Veja todas as disciplinas cadastradas.
   - **Excluir Disciplina**: Remova uma disciplina existente.
   - **Alterar Disciplina**: Atualize as informações de uma disciplina selecionada.

3. **Gerenciar Professores**:
   - **Incluir Professor**: Adicione um novo professor inserindo o código, nome e CPF.
   - **Listar Professores**: Exiba todos os professores registrados.
   - **Excluir Professor**: Selecione e remova um professor.
   - **Alterar Professor**: Atualize os dados de um professor existente.

4. **Gerenciar Turmas**:
   - **Incluir Turma**: Cadastre uma nova turma informando o código da turma, código do professor e código da disciplina.
   - **Listar Turmas**: Veja todas as turmas cadastradas.
   - **Excluir Turma**: Remova uma turma selecionada.
   - **Alterar Turma**: Atualize os dados de uma turma existente.

5. **Gerenciar Matrículas**:
   - **Incluir Matrícula**: Insira o código da turma e do estudante para matriculá-lo.
   - **Listar Matrículas**: Visualize todas as matrículas cadastradas.
   - **Excluir Matrícula**: Remova uma matrícula existente.
   - **Alterar Matrícula**: Atualize as informações de uma matrícula.

6. **Sair**: Encerra o programa.

### 📝 Notas Importantes
- **Armazenamento de Dados**: Todos os dados são armazenados em arquivos JSON.
- **Validação de Dados**: Durante as operações de inclusão, exclusão e alteração, o sistema verifica se os dados já existem ou se o índice informado é válido, evitando erros e garantindo a integridade dos dados.
- **Interatividade**: O programa é baseado em um menu interativo que facilita a navegação e o gerenciamento das informações acadêmicas.




