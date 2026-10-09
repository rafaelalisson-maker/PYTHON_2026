
import datetime

from models.cliente import Cliente
from models.ClienteDao import ClienteDAO
from models.servico import Servico
from models.servicodao import ServicoDAO
from models.horario import Horario
from models.horariodao import HorarioDAO
from models.atendimento import Atendimento
from models.atendimentoDao import AtendimentoDAO
from models.profissional import Profissional
from models.profissionalDao import profissionalDao


class Service:

    # CLIENTES
    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        ClienteDAO().inserir(Cliente(0, nome, email, fone, senha))

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        ClienteDAO().atualizar(Cliente(id, nome, email, fone, senha))

    @staticmethod
    def cliente_excluir(id):
        ClienteDAO().excluir(id)

    @staticmethod
    def cliente_criar_admin():
        for cliente in Service.cliente_listar():
            if cliente.get_email() == "admin":
                return
        Service.cliente_inserir("admin", "admin", "fone", "1234")

    @staticmethod
    def cliente_autenticar(email, senha):
        for cliente in Service.cliente_listar():
            if cliente.get_email() == email and cliente.get_senha() == senha:
                return {"id": cliente.get_id(), "nome": cliente.get_nome()}
        return None

    # SERVIÇOS
    @staticmethod
    def servico_inserir(descricao, valor):
        ServicoDAO().inserir(Servico(0, descricao, valor))

    @staticmethod
    def servico_listar():
        return ServicoDAO().listar()

    @staticmethod
    def servico_listar_id(id):
        return ServicoDAO().listar_id(id)

    @staticmethod
    def servico_atualizar(id, descricao, valor):
        ServicoDAO().atualizar(Servico(id, descricao, valor))

    @staticmethod
    def servico_excluir(id):
        ServicoDAO().excluir(id)

    # HORÁRIOS
    @staticmethod
    def horario_inserir(
        data, confirmado, id_cliente, id_servico, id_profissional=0
    ):
        horario = Horario(0, data)
        horario.set_confirmado(confirmado)
        horario.set_id_cliente(id_cliente if id_cliente is not None else 0)
        horario.set_id_servico(id_servico if id_servico is not None else 0)
        horario.set_id_profissional(
            id_profissional if id_profissional is not None else 0
        )
        HorarioDAO().inserir(horario)

    @staticmethod
    def horario_listar():
        return HorarioDAO().listar()

    @staticmethod
    def horario_listar_id(id):
        return HorarioDAO().listar_id(id)

    @staticmethod
    def horario_atualizar(
        id, data, confirmado, id_cliente, id_servico, id_profissional=0
    ):
        horario = Horario(id, data)
        horario.set_confirmado(confirmado)
        horario.set_id_cliente(id_cliente if id_cliente is not None else 0)
        horario.set_id_servico(id_servico if id_servico is not None else 0)
        horario.set_id_profissional(
            id_profissional if id_profissional is not None else 0
        )
        HorarioDAO().atualizar(horario)

    @staticmethod
    def horario_excluir(id):
        HorarioDAO().excluir(id)

    @staticmethod
    def horario_listar_disponiveis(id_profissional):
        agora = datetime.datetime.now()
        horarios = [
            h for h in Service.horario_listar()
            if h.get_data() >= agora
            and not h.get_confirmado()
            and h.get_id_cliente() in [0, None]
            and h.get_id_profissional() == id_profissional
        ]
        return sorted(horarios, key=lambda h: h.get_data())

    @staticmethod
    def horario_abrir_minha_agenda(
        data, horario_inicio, horario_fim, intervalo, id_profissional
    ):
        data_inicio = datetime.datetime.strptime(
            data + " " + horario_inicio, "%d/%m/%Y %H:%M"
        )
        data_fim = datetime.datetime.strptime(
            data + " " + horario_fim, "%d/%m/%Y %H:%M"
        )

        if intervalo <= 0:
            raise ValueError("O intervalo deve ser maior que zero.")
        if data_fim < data_inicio:
            raise ValueError("O horário final deve ser posterior ao inicial.")

        delta = datetime.timedelta(minutes=intervalo)
        atual = data_inicio
        quantidade = 0

        while atual <= data_fim:
            Service.horario_inserir(
                atual, False, None, None, id_profissional
            )
            atual += delta
            quantidade += 1

        return quantidade

    @staticmethod
    def horario_visualizar_minha_agenda(id_profissional):
        horarios = [
            h for h in Service.horario_listar()
            if h.get_id_profissional() == id_profissional
        ]
        return sorted(horarios, key=lambda h: h.get_data())

    @staticmethod
    def horario_visualizar_meus_servicos(id_cliente):
        horarios = [
            h for h in Service.horario_listar()
            if h.get_id_cliente() == id_cliente
        ]
        return sorted(horarios, key=lambda h: h.get_data())

    @staticmethod
    def horario_confirmar_servico(id_profissional):
        horarios = [
            h for h in Service.horario_listar()
            if not h.get_confirmado()
            and h.get_id_cliente() not in [0, None]
            and h.get_id_profissional() == id_profissional
        ]
        return sorted(horarios, key=lambda h: h.get_data())

    # ATENDIMENTOS
    @staticmethod
    def atendimento_inserir(
        data, queixa_principal, historico_saude,
        avaliacao, prescricao, id_horario
    ):
        obj = Atendimento(
            0, data, queixa_principal, historico_saude,
            avaliacao, prescricao, id_horario
        )
        AtendimentoDAO().inserir(obj)

    @staticmethod
    def atendimento_listar():
        return AtendimentoDAO().listar()

    @staticmethod
    def atendimento_listar_id(id):
        return AtendimentoDAO().listar_id(id)

    @staticmethod
    def atendimento_atualizar(
        id, data, queixa_principal, historico_saude,
        avaliacao, prescricao, id_horario
    ):
        obj = Atendimento(
            id, data, queixa_principal, historico_saude,
            avaliacao, prescricao, id_horario
        )
        AtendimentoDAO().atualizar(obj)

    @staticmethod
    def atendimento_excluir(id):
        AtendimentoDAO().excluir(id)

    # PROFISSIONAIS
    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha):
        profissionalDao().inserir(
            Profissional(0, nome, email, especialidade, senha)
        )

    @staticmethod
    def cliente_alterar_senha(id, nova_senha):
        cliente = Service.cliente_listar_id(id)
        if cliente:
            cliente.set_senha(nova_senha)
            ClienteDAO().atualizar(cliente)

    @staticmethod
    def profissional_listar():
        return profissionalDao().listar()

    @staticmethod
    def profissional_listar_id(id):
        return profissionalDao().listar_id(id)

    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, senha):
        profissionalDao().atualizar(
            Profissional(id, nome, email, especialidade, senha)
        )

    @staticmethod
    def profissional_excluir(id):
        profissionalDao().excluir(id)

    @staticmethod
    def profissional_autenticar(email, senha):
        for profissional in Service.profissional_listar():
            if (
                profissional.get_email() == email
                and profissional.get_senha() == senha
            ):
                return {
                    "id": profissional.get_id(),
                    "nome": profissional.get_nome()
                }
        return None