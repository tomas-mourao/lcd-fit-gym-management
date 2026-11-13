class Colors:
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BLUE = "\033[0;34m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    YELLOW = "\033[1;33m"
    LIGHT_PURPLE = "\033[1;35m"
    END = "\033[0m"


class Membro:
    def __init__(self, id, nome):
        self.__id = int(id)
        self.__nome = nome

        self.__entradas = 0
        self.__subscricao = False

    @property
    def identificacao(self):
        return self.__id

    @property
    def nome(self):
        return str(self.__nome)

    @property
    def entradas(self):
        return self.__entradas

    def gastar_entradas(self):
        self.__entradas -= 1
        return self.__entradas

    @property
    def subscricao(self):
        return self.__subscricao

    def comprar_entradas(self, quantidade):
        self.__entradas += quantidade

    def ativar_subscricao(self):
        self.__subscricao = True
        return f'{Colors.GREEN}Subscrição ativada{Colors.END}'

    def desativar_subscricao(self):
        self.__subscricao = False
        return f'{Colors.RED}Subscrição desativada{Colors.END}'

    def __str__(self):
        if self.__subscricao:
            subscricao_texto = f'{Colors.GREEN}Ativa{Colors.END}'
        else:
            subscricao_texto = f'{Colors.RED}Inativa{Colors.END}'

        return f'{self.__id}: {self.__nome} ({self.__entradas} entradas disponíveis, subscrição {subscricao_texto})'

    def __eq__(self, other):
        if isinstance(other, Membro):
            return self.identificacao == other.identificacao
        else:
            return False


class Aula:
    def __init__(self, nome, instrutor, lotacao):
        self.__nome = nome
        self.__instrutor = instrutor
        self.__lotacao = int(lotacao)

        self.__aula = []

    @property
    def nome(self):
        return self.__nome

    @property
    def instrutor(self):
        return self.__instrutor

    @property
    def lotacao(self):
        return self.__lotacao

    def membro_esta_aula(self, membro):
        return membro in self.__aula

    def entrada_aula(self, membro):
        if self.vagas_disponiveis == 0:
            return f'{Colors.RED}A aula está cheia{Colors.END}'
        elif self.membro_esta_aula(membro):
            return f'{Colors.YELLOW}O membro {membro.nome} já está na aula de {self.__nome}{Colors.END}'
        else:
            self.__aula.append(membro)
            return f'{Colors.GREEN}O membro {membro.nome} entrou na aula de {self.__nome}{Colors.END}'

    def saida_aula(self, membro):
        if membro in self.__aula:
            self.__aula.remove(membro)
            return f'{Colors.LIGHT_PURPLE}O membro {membro.nome} saiu da aula de {self.__nome}{Colors.END}'
        else:
            return f'{Colors.YELLOW}O membro {membro.nome} não está na aula de {self.__nome}{Colors.END}'

    @property
    def participantes_aula(self):
        return self.__aula

    @property
    def vagas_disponiveis(self):
        return self.__lotacao - len(self.__aula)

    @property
    def vagas_ocupadas(self):
        return len(self.__aula)
    def __str__(self):
        return f'{self.__nome}: {self.__instrutor} ({self.vagas_ocupadas}/{self.lotacao})'


class Gym:

    def __init__(self, nome, localizacao, lotacao):
        self.__nome = nome
        self.__localizacao = localizacao
        self.__lotacao = int(lotacao)

        self.__membros = []
        self.__aulas = []

        self.__membros_presentes = []

    @property
    def nome(self):
        return self.__nome

    @property
    def localizacao(self):
        return self.__localizacao

    @property
    def lotacao(self):
        return self.__lotacao

    def listagem_membros(self):
        return self.__membros

    def listagem_aulas(self):
        return self.__aulas


    def novo_membro(self, membro):
        if membro in self.__membros:
            return f'{Colors.LIGHT_PURPLE}O membro {membro.nome} já está inscrito no ginásio {self.__nome}{Colors.END}'
        else:
            self.__membros.append(membro)
            return f'{Colors.GREEN}O membro {membro.nome} foi inscrito no ginásio {self.__nome}{Colors.END}'


    def entradas_ginasio(self, membro):
        if membro not in self.__membros:
            return f'{Colors.YELLOW}O membro {membro.nome} não está inscrito no ginásio {self.__nome}{Colors.END}'
        elif self.vagas_disponiveis_ginasio == 0:
            return f'{Colors.RED}Vagas lotadas no ginásio {self.__nome}{Colors.END}'
        elif self.membro_no_ginasio(membro):
            return f'{Colors.LIGHT_PURPLE}O membro {membro.nome} ja está presente no ginásio {self.__nome}{Colors.END}'
        elif not self.membro_no_ginasio(membro) and self.vagas_disponiveis_ginasio > 0 and not membro.subscricao:
            membro.gastar_entradas()
            self.__membros_presentes.append(membro)
            return f'{Colors.GREEN}O Membro {membro.nome} entrou no ginásio {self.__nome}. Ainda tem {membro.entradas} entradas{Colors.END}'
        else:
            self.__membros_presentes.append(membro)
            return f'{Colors.GREEN}O Membro {membro.nome} entrou no ginásio {self.__nome}{Colors.END}'

    def saidas_ginasio(self, membro):
        if membro not in self.__membros:
            return f'{Colors.RED}O membro {membro.nome} não está inscrito no ginásio {self.__nome}{Colors.END}'
        elif membro not in self.__membros_presentes:
            return f'{Colors.LIGHT_PURPLE}O membro {membro.nome} não está presente no ginásio {self.__nome}{Colors.END}'
        else:
            self.__membros_presentes.remove(membro)
            return f'{Colors.YELLOW}O membro {membro.nome} saiu do ginásio {self.__nome}{Colors.END}'


    @property
    def vagas_disponiveis_ginasio(self):
        return self.__lotacao - len(self.__membros_presentes)

    @property
    def vagas_ocupadas_ginasio(self):
        return len(self.__membros_presentes)

    def membro_no_ginasio(self, membro):
        return membro in self.__membros_presentes

    @property
    def listagem_membros_no_ginasio(self):
        return self.__membros_presentes

    def criar_aula(self, aula):
        if aula in self.__aulas:
            return f'{Colors.YELLOW}A aula de {aula.nome} já foi criada{Colors.END}'
        else:
            self.__aulas.append(aula)
            return f'{Colors.GREEN}A aula de {aula.nome} foi criada{Colors.END}'

    def cancelar_aula(self, aula):
        if aula not in self.__aulas:
            return f'{Colors.LIGHT_PURPLE}A aula de {aula.nome} não foi criada{Colors.END}'
        else:
            self.__aulas.remove(aula)
            return f'{Colors.YELLOW}A aula de {aula.nome} foi cancelada{Colors.END}'


    @property
    def aulas_decorrer(self):
        return self.__aulas

    def __str__(self):
        return f'{self.__nome} @ {self.__localizacao} ({self.vagas_ocupadas_ginasio}/{self.__lotacao})'


def export_file(ginasio, filename='gym.txt'):
    try:
        f = open(filename, 'w')
        f.write(f'{ginasio.nome},{ginasio.localizacao},{ginasio.lotacao}\n')
        for membro in ginasio.listagem_membros():
            f.write(f'{membro.identificacao},{membro.nome},{membro.entradas},{membro.subscricao}\n')
        for aula in ginasio.listagem_aulas():
            f.write(f'{aula.nome},{aula.instrutor},{aula.lotacao}\n')
        f.close()
    except IOError:
        print(f'{Colors.RED}ERRO DE LEITURA/ESCRITA DE FICHEIROS!!{Colors.END}')


def import_file(filename='gym.txt'):
    try:
        f = open(filename, 'r')
        linha = f.read().splitlines()
        f.close()
        nome, localizacao, lotacao = linha[0].strip().split(',')
        ginasio = Gym(nome, localizacao, int(lotacao))
        for line in linha[1:]:
            partes = line.strip().split(',')
            if len(partes) == 4:
                membro_id, membro_nome, membro_entradas, membro_subscricao = partes
                m = Membro(membro_id, membro_nome)
                if int(membro_entradas) > 0:
                    m.comprar_entradas(int(membro_entradas))
                if membro_subscricao == 'True':
                    m.ativar_subscricao()
                ginasio.novo_membro(m)
            elif len(partes) == 3:
                aula_nome, aula_instrutor, aula_lotacao = partes
                a = Aula(aula_nome, aula_instrutor, aula_lotacao)
                ginasio.criar_aula(a)
        return ginasio
    except FileNotFoundError:
        print(f'{Colors.RED}ERRO!! FICHEIRO NÃO ENCONTRADO{Colors.END}')



def menu_principal():
    ginasio = import_file('gym.txt')
    if ginasio is None:
        print(f'{Colors.RED}AVISO: "gym.txt" NÃO ENCONTRADO OU COM ERRO.{Colors.END}')
        return
    else:
        print(f'{Colors.GREEN}GINÁSIO {ginasio.nome} IMPORTADO! {Colors.END}')

    while True:
        print(f'{Colors.BLUE}\n==== Menu principal ==== {Colors.END}')
        print('1. Menu de membro')
        print('2. Menu de gestão')
        print('3. Carregar ginásio ')
        print('4. Exportar ginásio')
        print('0. Sair')
        try:
            op = int(input('Escolhe uma opção: '))
        except ValueError:
            print(f'{Colors.RED}Opção inválida.Escolha uma opção válida {Colors.END}')
            continue

        if op == 1:
            id_membro_str = input('Id: ')
            membro_selecionado= None
            try:
                id_num = int(id_membro_str)
                for membro in ginasio.listagem_membros():
                    if membro.identificacao == id_num:
                        membro_selecionado = membro
                        break
                if membro_selecionado is not None:
                    menu_membro(ginasio, membro_selecionado)
                else:
                    print(f'{Colors.RED}O membro não existe. {Colors.END}')
            except ValueError:
                print(f'{Colors.RED}ERRO.Valor inválido{Colors.END}')

        elif op == 2:
            menu_gestao(ginasio)

        elif op == 3:
            if ginasio.vagas_ocupadas_ginasio > 0:
                print(f'{Colors.RED}O ginásio não está vazio.{Colors.END}')
            else:
                filename = input('Ficheiro: ')
                novo_ginasio = import_file(filename)
                if novo_ginasio is None:
                    print(f'{Colors.RED}Ficheiro inválido.{Colors.END}')
                else:
                    ginasio = novo_ginasio
                    print(f"{Colors.GREEN}Ginásio '{ginasio.nome}' carregado com sucesso. {Colors.END}")

        elif op == 4:
            filename = input('Ficheiro: ')
            if filename == '':
                print(f'{Colors.YELLOW}Nenhum ficheiro indicado{Colors.END}')
            else:
                try:
                    export_file(ginasio, filename)
                    print(f"{Colors.GREEN}Dados exportados com sucesso para '{filename}'.{Colors.END}")
                except FileNotFoundError:
                    print(f'{Colors.RED}Ficheiro inválido.{Colors.END}')

        elif op == 0:
            print(f'{Colors.LIGHT_GRAY}A SAIR DO PROGRAMA{Colors.END}')
            break

        else:
            print(f'{Colors.RED}Opção inválida.{Colors.END}')


def menu_membro(ginasio,membro_atual):
    while True:
        print(f'{Colors.BLUE}\n==== Menu Membro [{membro_atual.nome}] ===={Colors.END}')
        print("1. Consultar estado")
        print("2. Registar entrada")
        print("3. Registar saída")
        print("4. Marcar aula")
        print("5. Comprar entradas")
        print("6. Ativar subscrição")
        print("7. Cancelar subscrição")
        print("0. Voltar")
        try:
            op = int(input('Escolhe uma opção: '))
        except ValueError:
            print(f'{Colors.RED}Opção inválida.Escolha uma opção válida{Colors.END}')
            continue

        if op == 1:
            estado_membro = str(membro_atual)
            if not ginasio.membro_no_ginasio(membro_atual):
                print(estado_membro)
            else:
                membro_em_aula = False
                for aula in ginasio.listagem_aulas():
                    if aula.membro_esta_aula(membro_atual):
                        membro_em_aula = True
                        break
                if membro_em_aula:
                    print(f'{estado_membro} - em aula')
                else:
                    print(f'{estado_membro} - a treinar')

        elif op == 2:
            if ginasio.membro_no_ginasio(membro_atual):
                print(f'{Colors.LIGHT_PURPLE}O membro já está no ginásio.{Colors.END}')
            elif ginasio.vagas_disponiveis_ginasio == 0:
                print(f'{Colors.RED}O ginásio está cheio.')
            elif not membro_atual.subscricao and membro_atual.entradas == 0:
                print(f'{Colors.RED}O membro não tem entradas disponíveis.{Colors.END}')
            else:
                print(ginasio.entradas_ginasio(membro_atual))


        elif op == 3:
            if not ginasio.membro_no_ginasio(membro_atual):
                print(f'{Colors.YELLOW}O membro não está a treinar.{Colors.END}')
            else:
                aula_do_membro = None
                for aula in ginasio.listagem_aulas():
                    if aula.membro_esta_aula(membro_atual):
                        aula_do_membro = aula
                        break
                if aula_do_membro is not None:
                    print(aula_do_membro.saida_aula(membro_atual))
                print(ginasio.saidas_ginasio(membro_atual))

        elif op == 4:
            if not ginasio.membro_no_ginasio(membro_atual):
                print(f'{Colors.RED}O membro não está a treinar.{Colors.END}')
            else:
                nome_instrutor = input("Instrutor: ")
                membro_em_aula = False
                for aula in ginasio.listagem_aulas():
                    if aula.membro_esta_aula(membro_atual):
                        membro_em_aula = True
                        break

                if membro_em_aula:
                    print(f'{Colors.LIGHT_PURPLE}O membro já está numa aula.{Colors.END}')
                else:
                    aula_desejada = None
                    for aula in ginasio.listagem_aulas():
                        if aula.instrutor == nome_instrutor:
                            aula_desejada = aula
                            break

                    if not aula_desejada:
                        print(f'{Colors.RED}A aula não existe.{Colors.END}')
                    elif aula_desejada.vagas_disponiveis == 0:
                        print(f'{Colors.RED} aula está cheia.{Colors.END}')
                    else:
                        print(aula_desejada.entrada_aula(membro_atual))

        elif op == 5:
            try:
                quantidade_str = input("Número de entradas: ")
                quantidade_int = int(quantidade_str)
                if quantidade_int <= 0:
                    print(f'{Colors.RED}Quantidade inválida.{Colors.END}')
                else:
                    membro_atual.comprar_entradas(quantidade_int)
                    print(f'{Colors.LIGHT_PURPLE}Compra efetuada. Total de entradas: {membro_atual.entradas}{Colors.END}')
            except ValueError:
                print(f'{Colors.RED}Quantidade inválida.{Colors.END}')

        elif op == 6:
            if membro_atual.subscricao:
                print (f'{Colors.LIGHT_PURPLE}O membro já tem a subscrição ativa{Colors.END}')
            else:
                print(membro_atual.ativar_subscricao())

        elif op == 7:
            if not membro_atual.subscricao:
                print (f'{Colors.LIGHT_PURPLE}O membro já tem a subscrição inativa{Colors.END}')
            else:
                print(membro_atual.desativar_subscricao())

        elif op == 0:
            break
        else:
            print(f'{Colors.RED}Opção inválida.{Colors.END}')


def menu_gestao(ginasio):
    while True:
        print(f'{Colors.BLUE}\n==== Menu de Gestão ==== {Colors.END}')
        print('1. Registar membro')
        print('2. Listar membros')
        print('3. Listar membros a treinar')
        print('4. Criar aula')
        print('5. Cancelar aula')
        print('6. Listar aulas')
        print('7. Ver aula')
        print('8. Visão global')
        print('0. Voltar')
        try:
            op = int(input('Escolhe uma opção: '))
        except ValueError:
            print(f'{Colors.RED}Opção inválida.Escolha uma opção válida {Colors.END}')
            continue

        if op == 1:
            nome_membro = input('Nome: ').strip()
            if not nome_membro:
                print(f'{Colors.RED}Nome inválido.{Colors.END}')
                break
            elif not nome_membro.replace(' ','').isalpha():
                print(f'{Colors.RED}O nome só pode ter letras{Colors.END}')
                continue

            lista_membros = ginasio.listagem_membros()
            maior_id = 0
            for m in lista_membros:
                if m.identificacao > maior_id:
                    maior_id = m.identificacao
            novo_id = maior_id + 1

            membro_novo = Membro(novo_id, nome_membro)
            print(ginasio.novo_membro(membro_novo))
            print(f'{Colors.GREEN}Membro registado com o id {novo_id}{Colors.END}')

        elif op == 2:
            filtro = input('Filtro: ').strip().lower()
            print(f'{Colors.BLUE}\n ==== Membros registados ==== {Colors.END}')
            encontrar_membro = False
            for membro in ginasio.listagem_membros():
                if filtro in membro.nome.lower():
                    print(membro)
                    encontrar_membro = True
            if not encontrar_membro:
                print(f'{Colors.LIGHT_PURPLE}Nenhum membro encontrado com esse filtro.{Colors.END}')

        elif op == 3:
            print(f'\n{Colors.CYAN} ==== Membros presentes ==== {Colors.END}')
            membros_presentes = ginasio.listagem_membros_no_ginasio
            if not membros_presentes:
                print(f'{Colors.YELLOW}Não há nenhum membro no ginásio{Colors.END}')
            else:
                for membro in membros_presentes:
                    estado_membro = str(membro)
                    membro_em_aula = False
                    for aula in ginasio.listagem_aulas():
                        if aula.membro_esta_aula(membro):
                            membro_em_aula = True
                            break

                    if membro_em_aula:
                        print(f'{estado_membro} - em aula')
                    else:
                        print(f'{estado_membro} - a treinar')

        elif op == 4:
            nome_aula = input('Nome: ')
            instrutor_aula = input('Instrutor: ')
            lotacao_aula_str = input('Lotação: ')

            instrutor_existencia = False
            for aula in ginasio.listagem_aulas():
                if aula.instrutor == instrutor_aula:
                    instrutor_existencia = True
                    break

            if instrutor_existencia:
                print(f'{Colors.YELLOW}O instrutor já tem uma aula.{Colors.END}')
            else:
                try:
                    lotacao_aula_int = int(lotacao_aula_str)
                    if lotacao_aula_int <= 0:
                        print(f'{Colors.RED}Lotação inválida.{Colors.END}')
                    elif lotacao_aula_int > ginasio.lotacao:
                        print(f'{Colors.YELLOW}A lotação da aula não pode ser superior à do ginásio.{Colors.END}')
                    else:
                        aula_nova = Aula(nome_aula, instrutor_aula, lotacao_aula_int)
                        print(ginasio.criar_aula(aula_nova))
                except ValueError:
                    print(f'{Colors.RED}Lotação inválida.{Colors.END}')

        elif op == 5:
            instrutor_aula = input('Instrutor: ')
            aula_a_cancelar = None
            for aula in ginasio.listagem_aulas():
                if aula.instrutor == instrutor_aula:
                    aula_a_cancelar = aula
                    break
            if not aula_a_cancelar:
                print(f'{Colors.RED}A aula não existe.{Colors.END}')
            else:
                participantes_a_remover = list(aula_a_cancelar.participantes_aula)
                for membro in participantes_a_remover:
                    aula_a_cancelar.saida_aula(membro)
                print(ginasio.cancelar_aula(aula_a_cancelar))

        elif op == 6:
            print(f'{Colors.CYAN}\n ==== Aulas Disponíveis ==== {Colors.END}')
            aulas_ginasio = ginasio.listagem_aulas()
            if not aulas_ginasio:
                print(f'{Colors.RED}Nenhuma aula criada.{Colors.END}')
            else:
                for aula in aulas_ginasio:
                    print(aula)

        elif op == 7:
            instrutor_aula = input('Instrutor: ')
            aula_a_ver = None
            for aula in ginasio.listagem_aulas():
                if aula.instrutor == instrutor_aula:
                    aula_a_ver = aula
                    break

            if not aula_a_ver:
                print(f'{Colors.RED}A aula não existe.{Colors.END}')
            else:
                print(f'{Colors.CYAN}\nDetalhes da Aula{Colors.END}')
                print(aula_a_ver)
                print(f'{Colors.LIGHT_PURPLE}\nParticipantes:{Colors.END}')
                participantes = aula_a_ver.participantes_aula
                if not participantes:
                    print(f'{Colors.RED}Nenhum participante nesta aula.{Colors.END}')
                else:
                    for membro in participantes:
                        print(membro)

        elif op == 8:
            print(f'{Colors.CYAN}\nVisão Global {Colors.END}')
            print(ginasio)
            numero_membros = len(ginasio.listagem_membros())
            print(f'{Colors.LIGHT_PURPLE}Número de membros: {numero_membros}{Colors.END}')
            if numero_membros > 0:
                contar_membros_subscricao = 0
                for membro in ginasio.listagem_membros():
                    if membro.subscricao or membro.entradas > 0:
                        contar_membros_subscricao += 1
                perc_membros_subscricao = (contar_membros_subscricao / numero_membros) * 100
                print(f'{Colors.LIGHT_PURPLE}Percentagem de membros ativos: {perc_membros_subscricao:.2f}%{Colors.END}')
            else:
                print(f'{Colors.LIGHT_PURPLE}Percentagem de membros ativos: 0.0%{Colors.END}')
            numero_aulas = len(ginasio.listagem_aulas())
            print(f'{Colors.LIGHT_PURPLE}Número de aulas: {numero_aulas}{Colors.END}')
            if numero_aulas > 0:
                ocupacao_total = 0
                for a in ginasio.listagem_aulas():
                    ocupacao_total += a.vagas_ocupadas
                media_ocupacao = ocupacao_total / numero_aulas
                print(f'{Colors.LIGHT_PURPLE}Ocupação média das aulas: {media_ocupacao:.2f}{Colors.END}')
            else:
                print(f'{Colors.LIGHT_PURPLE}Ocupação média das aulas: 0.0{Colors.END}')

            membros_presentes = ginasio.listagem_membros_no_ginasio
            numero_presentes = len(membros_presentes)
            if numero_presentes > 0:
                countar_membros_a_treinar = 0
                for m in membros_presentes:
                    membro_em_aula = False
                    for aula in ginasio.listagem_aulas():
                        if aula.membro_esta_aula(m):
                            membro_em_aula = True
                            break
                    if not membro_em_aula:
                        countar_membros_a_treinar += 1

                perc_membros_a_treinar = (countar_membros_a_treinar / numero_presentes) * 100
                print(f'{Colors.LIGHT_PURPLE}Percentagem de membros a treinar: {perc_membros_a_treinar:.2f}%{Colors.END}')
            else:
                print(f'{Colors.LIGHT_PURPLE}Percentagem de membros a treinar: 0.00%{Colors.END}')

        elif op == 0:
            print(f'{Colors.YELLOW}\n A sair...{Colors.END}')
            break
        else:
            print(f'{Colors.RED}Opção inválida.Tente uma opção válida{Colors.END}')

menu_principal()