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
from models.profissionalDao import ProfissionalDAO


class Service:

    @staticmethod
    def _validar_email_cliente(email, cliente_id=None):
        email_normalizado = email.strip().casefold()
        clientes = Service.cliente_listar()
        cliente_atual = next(
            (cliente for cliente in clientes
             if cliente.get_id() == cliente_id),
            None
        )

        if email_normalizado == "admin" and not (
            cliente_atual
            and cliente_atual.get_email().strip().casefold() == "admin"
        ):
            raise ValueError("O e-mail 'admin' é reservado ao administrador.")

        if any(
            cliente.get_id() != cliente_id
            and cliente.get_email().strip().casefold() == email_normalizado
            for cliente in clientes
        ):
            raise ValueError("Já existe um cliente com este e-mail.")

        if any(
            profissional.get_email().strip().casefold() == email_normalizado
            for profissional in Service.profissional_listar()
        ):
            raise ValueError("Já existe um profissional com este e-mail.")

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        Service._validar_email_cliente(cliente.get_email())
        ClienteDAO().inserir(cliente)

    @staticmethod
    def cliente_listar():
        return ClienteDAO().listar()

    @staticmethod
    def cliente_listar_id(id):
        return ClienteDAO().listar_id(id)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        Service._validar_email_cliente(cliente.get_email(), id)
        ClienteDAO().atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        if any(
            horario.get_id_cliente() == id
            for horario in Service.horario_listar()
        ):
            raise ValueError(
                "Não é possível excluir um cliente com horário agendado."
            )
        ClienteDAO().excluir(id)

    @staticmethod
    def cliente_criar_admin():
        for cliente in Service.cliente_listar():
            if cliente.get_email().strip().casefold() == "admin":
                return
        ClienteDAO().inserir(Cliente(0, "admin", "admin", "fone", "1234"))

    @staticmethod
    def cliente_autenticar(email, senha):
        for cliente in Service.cliente_listar():
            if cliente.get_email() == email and cliente.get_senha() == senha:
                return {"id": cliente.get_id(), "nome": cliente.get_nome()}
        return None

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

    @staticmethod
    def _validar_conflito_horario(data, id_profissional, horario_id=None):
        if any(
            horario.get_id() != horario_id
            and horario.get_id_profissional() == id_profissional
            and horario.get_data() == data
            for horario in Service.horario_listar()
        ):
            raise ValueError(
                "Já existe um horário nesta data e hora para este profissional."
            )

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
        Service._validar_conflito_horario(
            horario.get_data(), horario.get_id_profissional()
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
        Service._validar_conflito_horario(
            horario.get_data(), horario.get_id_profissional(), id
        )
        HorarioDAO().atualizar(horario)

    @staticmethod
    def horario_excluir(id):
        horario = Service.horario_listar_id(id)
        if horario is not None and horario.get_id_cliente() not in [0, None]:
            raise ValueError(
                "Não é possível excluir um horário já agendado por um cliente."
            )
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
        horarios = []

        while atual <= data_fim:
            horario = Horario(0, atual)
            Service._validar_conflito_horario(
                horario.get_data(), id_profissional
            )
            horarios.append(atual)
            atual += delta

        for data_horario in horarios:
            Service.horario_inserir(
                data_horario, False, None, None, id_profissional
            )

        return len(horarios)

    @staticmethod
    def horario_visualizar_minha_agenda(id_profissional):
        return Service.horario_listar_agenda_profissional(id_profissional)

    @staticmethod
    def horario_listar_agenda_profissional(id_profissional):
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
    def horario_listar_confirmados_hoje():
        hoje = datetime.date.today()
        horarios = [
            h for h in Service.horario_listar()
            if h.get_data().date() == hoje
            and h.get_confirmado()
            and h.get_id_cliente() not in [0, None]
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

    @staticmethod
    def profissional_inserir(nome, email, especialidade, senha):
        profissional = Profissional(0, nome, email, especialidade, senha)
        Service._validar_email_profissional(profissional.get_email())
        ProfissionalDAO().inserir(profissional)

    @staticmethod
    def cliente_alterar_senha(id, nova_senha):
        cliente = Service.cliente_listar_id(id)
        if cliente:
            cliente.set_senha(nova_senha)
            ClienteDAO().atualizar(cliente)

    @staticmethod
    def profissional_listar():
        return ProfissionalDAO().listar()

    @staticmethod
    def profissional_listar_id(id):
        return ProfissionalDAO().listar_id(id)

    @staticmethod
    def profissional_atualizar(id, nome, email, especialidade, senha):
        profissional = Profissional(id, nome, email, especialidade, senha)
        Service._validar_email_profissional(profissional.get_email(), id)
        ProfissionalDAO().atualizar(profissional)

    @staticmethod
    def profissional_excluir(id):
        if any(
            horario.get_id_profissional() == id
            for horario in Service.horario_listar()
        ):
            raise ValueError(
                "Não é possível excluir um profissional com horário cadastrado."
            )
        ProfissionalDAO().excluir(id)

    @staticmethod
    def _validar_email_profissional(email, profissional_id=None):
        email_normalizado = email.strip().casefold()

        if email_normalizado == "admin":
            raise ValueError("O e-mail 'admin' é reservado ao administrador.")

        if any(
            cliente.get_email().strip().casefold() == email_normalizado
            for cliente in Service.cliente_listar()
        ):
            raise ValueError("Já existe um cliente com este e-mail.")

        if any(
            profissional.get_id() != profissional_id
            and profissional.get_email().strip().casefold()
            == email_normalizado
            for profissional in Service.profissional_listar()
        ):
            raise ValueError("Já existe um profissional com este e-mail.")

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