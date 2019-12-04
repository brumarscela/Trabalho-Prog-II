from peewee import *
import os
import datetime

arq = '/home/aluno/Documentos/trab_prog/trabprog.db'
db = SqliteDatabase(arq)

class BaseModel(Model):
    class Meta:
        database = db


class Pessoa(BaseModel):
    nome = CharField()
    cpf = IntegerField()
    data_nasc = DateField()


class Paciente(BaseModel):
    enfermidade = CharField()
    quantidade_consultas = []
    pessoa = ForeignKeyField(Pessoa)


class Atendente(BaseModel):
    carga_horaria = IntegerField()
    salario = FloatField()
    pessoa = ForeignKeyField(Pessoa)


class Psicologo(BaseModel):
    carga_horaria = IntegerField()
    salario = FloatField()
    dias_disp = CharField()
    pessoa = ForeignKeyField(Pessoa)


class Horario(BaseModel):
    dia = DateTimeField()
    dias_disp = ForeignKeyField(Psicologo)


class FormaPagamento(BaseModel):
    a_vista = FloatField()
    parcelado = FloatField()
    convenio = CharField()


class Local(BaseModel):
    aluguel = FloatField()
    endereco = CharField()
    telefone = IntegerField()


class Consulta(BaseModel):
    tipo_consulta = CharField()
    hora = ForeignKeyField(Horario)
    espaco = ForeignKeyField(Local)
    paciente = ForeignKeyField(Paciente)
    medico = ForeignKeyField(Psicologo)
    pag = ForeignKeyField(FormaPagamento)

class Propaganda(BaseModel):
    preco_radio = FloatField()
    preco_televisao = FloatField()
    preco_redes_sociais = FloatField()
    preco_site = FloatField()


class Contabilidade(BaseModel):
    entrada_dinheiro = FloatField()
    gasto_salario = FloatField()
    gasto_energia = FloatField()
    gasto_internet = FloatField()
    gasto_propaganda = ForeignKeyField(Propaganda)
    gasto_aluguel = ForeignKeyField(Local)


if __name__ == "__main__":
    if os.path.exists(arq):
        os.remove(arq)


    db.connect()
    db.create_tables([Pessoa, Paciente, Atendente, Psicologo, Horario, FormaPagamento, Local, Consulta, Propaganda, Contabilidade]) 


    p3 = Pessoa.create(nome = "Tiago", cpf = 10955578999, data_nasc = "08/07/2001")
    p2 = Pessoa.create(nome = "Múcio", cpf = 10865888999, data_nasc = "10/06/2002")
    p1 = Pessoa.create(nome = "Bruna", cpf = 10865378989, data_nasc = "05/06/2001")
    pac = Paciente.create(enfermidade = "TOC", quantidade_consultas = 5, pessoa = p3)
    at = Atendente.create(carga_horaria = 6, salario = 3000, pessoa = p2)
    psi = Psicologo.create(carga_horaria = 10, salario = 9000, dias_disp = "seg, ter, qua, qui, sex, sab", pessoa = p1)
    h = Horario.create(dia = datetime.datetime(2019, 12, 5, 14, 30), dias_disp = psi)
    pagamento = FormaPagamento.create(a_vista = 300, parcelado = 0, convenio = 0)
    loc = Local.create(aluguel = 3000, endereco = "rua XV de Novembro - Centro", telefone = 33384050)
    c1 = Consulta.create(tipo_consulta = "semanal", hora = h, espaco = loc, paciente = p3, medico = psi, pag = pagamento)
    prop = Propaganda.create(preco_radio = 300, preco_televisao = 3000, preco_redes_sociais = 300, preco_site = 3000)
    cont = Contabilidade.create(entrada_dinheiro = 100000, gasto_salario = 12000, gasto_energia = 300, gasto_internet = 80, gasto_aluguel = loc, gasto_propaganda = prop)


    print(
        "Nome: " + p3.nome + "\n", "CPF: " + str(p3.cpf) + "\n", "Data de nascimento: " + str(p3.data_nasc) + "\n" + "\n",
        "Nome: " + p2.nome + "\n", "CPF: " + str(p2.cpf) + "\n", "Data de nascimento: " + str(p2.data_nasc) + "\n" + "\n",
        "Nome: " + p1.nome + "\n", "CPF: " + str(p1.cpf) + "\n", "Data de nascimento: " + str(p1.data_nasc) + "\n" + "\n",
        "Enfermidade: " + str(pac.enfermidade) + "\n", "Quantidade de consultas: " + str(pac.quantidade_consultas) + "\n", "Função: " + str(pac.pessoa) + "\n" + "\n",
        "Carga horária: " + str(at.carga_horaria) + "\n", "Salário: " + str(at.salario) + "\n", "Função: " + str(at.pessoa) + "\n" + "\n",
        "Carga horária: " + str(psi.carga_horaria) + "\n", "Salário: " + str(psi.salario) + "\n", "Dias disponiveis: " + str(psi.dias_disp), "Função: " + str(psi.pessoa) + "\n" + "\n",
        "Dia: " + str(h.dia) + "\n", "Dias disponíveis: " + str(h.dias_disp) + "\n" + "\n",
        "Pagamento a vista: " + str(pagamento.a_vista) + "\n", "Pagamento Parcelado: " + str(pagamento.parcelado) + "\n", "Pagamento convênio: " + str(pagamento.convenio) + "\n" + "\n",
        "Valor do aluguel: " + str(loc.aluguel) + "\n", "Endereço: " + str(loc.endereco) + "\n", "Telefone: " + str(loc.telefone) + "\n" + "\n",
        "Tipo de consulta: " + c1.tipo_consulta + "\n", "Hora: " + str(c1.hora) + "\n", "Espaço: " + str(c1.espaco) + "\n", "Paciente: " + str(c1.paciente) + "\n", "Médico: " + str(c1.medico) + "\n", "Pagamento: " + str(c1.pag) + "\n" + "\n",
        "Preço rádio: " + str(prop.preco_radio) + "\n", "Preço televisão: " + str(prop.preco_televisao) + "\n", "Preço redes sociais: " + str(prop.preco_redes_sociais) + "\n", "Preço site: " + str(prop.preco_site) + "\n" + "\n",
        "Caixa: " + str(cont.entrada_dinheiro) + "\n", "Gasto com salário: " + str(cont.gasto_salario) + "\n", "Gasto com energia elétrica: " + str(cont.gasto_energia) + "\n", "Gasto com internet: " + str(cont.gasto_internet) + "\n", "Gasto com aluguel: " + str(cont.gasto_aluguel) + "\n", "Gasto com propaganda: " + str(cont.gasto_propaganda) + "\n" + "\n")
