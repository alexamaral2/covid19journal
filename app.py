from flask import Flask, render_template
from estado import Estado
from noticia import Noticia

app = Flask(__name__)

lista_noticias = [
Noticia(0, "Governo do RJ e Prefeitura do Rio começam a fechar postos de testagem de Covid-19","A queda de casos registrados de Covid evou Estado e Prefeitura do Rio a iniciarem o processo de fechamento de pontos de testagem. Segundo dados da Secretaria de Estado de Saúde, o índice de testes com resultados positivos para Covid-19 caiu de 36% na semana entre 16 e 22 de janeiro para 12% na semana entre 30 de janeiro e 5 de fevereiro. Os números mostram um recuo da doença, que provocou um pico de contaminação em janeiro.","11/02/2022", "300", "static/img/news.png","video/video01.mp4",500),
Noticia(1, "Vídeo mostra como o CTVacinas combate a pandemia de covid-19","Desde o início da pandemia da covid-19, o trabalho do CTVacinas, centro de pesquisas em biotecnologia da UFMG, foi acompanhado de perto pela equipe da TV UFMG, núcleo audiovisual do Centro de Comunicação (Cedecom) da UFMG, que percorreu os laboratórios do  Parque Tecnológico de Belo Horizonte (BH-TEC) para registrar as diferentes frentes de atuação. Além de resgatar o trabalho do CT Vacinas no enfrentamento de outras crises sanitárias – por meio do desenvolvimento de imunizantes contra doenças humanas e veterinárias, como dengue, Chagas, malária, influenza e toxoplasmose –, as gravações realizadas desde o início da pandemia, em 2020, destacam o empenho diário dos pesquisadores da UFMG para combater o novo coronavírus. Nas bancadas dos laboratórios, estudantes e pesquisadores trabalharam juntos no desenvolvimento de testes diagnósticos com tecnologia nacional, no suporte à testagem da população, no monitoramento de variantes e na pesquisa de quatro possíveis vacinas, uma delas (a SpiN-TEC) em análise na Agência Nacional de Vigilância Sanitária (Anvisa). O CTVacinas, que será transformado no Centro Nacional de Vacinas, evidencia o papel de destaque da UFMG na busca pela soberania nacional no desenvolvimento de testes de diagnóstico para doenças e na produção de imunizantes com tecnologia brasileira.","09/02/2022","400","static/img/news.png","video/video02.mp4",800),
Noticia(2, "Galinha Pintadinha se vacina contra Covid para incentivar crianças em SP; veja vídeo","Na nova leva de vacinação contra a Covid-19, voltada para crianças de 5 a 11 anos, até a Galinha Pintadinha aproveitou para se imunizar. Após a primeira dose, ela passa a ser a Galinha Vacinadinha.A partir desta terça-feira (18), o personagem infantil protagonizará uma campanha do Governo de São Paulo para incentivar as crianças a se protegerem contra o coronavírus. A imunização desse público no estado começou na sexta (14), e o primeiro a se vacinar foi Davi Seremramiwe Xavante, 8.","19/01/2022","1000","static/img/news.png","video/video03.mp4",50),
Noticia(3, "Sobe para 29 o número de cidades em risco moderado para Covid-19 no ES","O Governo do Espírito Santo anunciou, nesta sexta-feira (11), o novo mapa de risco da Covid-19, que terá vigência desta segunda (14) até o próximo domingo (20).Comparado ao último mapa, em que 21 cidades estavam em risco moderado, agora são 29 municípios nesta classificação. Além de Vitória, Vila Velha, Serra, Cariacica, Guarapari e Viana, na Região Metropolitana, outras 23 cidades do interior também aparecem em amarelo no novo mapa. São elas: Anchieta, Aracruz, Atílio Vivácqua, Barra de São Francisco, Cachoeiro de Itapemirim,Colatina, Ecoporanga, Fundão, Ibatiba, Ibiraçu, Itapemirim, Iúna, Jerônimo Monteiro, João Neiva, Linhares, Marechal Floriano, Muniz Freire, Pedro Canário, Pinheiros, Piúma, Rio Novo do Sul, São José do Calçado e São Mateus. Em pronunciamento feito na noite desta sexta-feira (11), o governador Renato Casagrande (PSB), afirmou que após o número de infectados pela Covid-19 voltar a cair no estado, agora há uma tendência de que as mortes também diminuam.","11/02/2022","10","static/img/news.png","video/video04.mp4",350)

]

lista_estados = [
    Estado(0, "Rio de Janeiro", "RJ" ,[lista_noticias[0]],"static/img/bandeira-rj.png"),
    Estado(1, "São Paulo", "SP" ,[lista_noticias[2]],"static/img/bandeira_sp.jpg"),
    Estado(2, "Minas Gerais", "MG" ,[lista_noticias[1]],"static/img/bandeira-mg.png"),
    Estado(3, "Espirito Santo", "ES" ,[lista_noticias[3]],"static/img/bandeira-es.png")
]

def listarNoticiasCurtidas():
    listaCurtida = []

    for noticia in lista_noticias:
        listaCurtida.append(noticia.get_curtidas())
        listaCurtida.sort(key=int, reverse=True)
        listaDecrescente = listaCurtida[:3]

    listaMaisCurtida = []

    for noticias in lista_noticias:
        for i in listaDecrescente:
            if i == noticias.get_curtidas():
                id = noticias.get_idNoticia()
                titulo = noticias.get_titulo()
                descricao = noticias.get_descricao() 
                publicacao = noticias.get_dataPublicacao()
                curtidas = noticias.get_curtidas()
                img = noticias.get_imgNoticia()
                video = noticias.get_videoNoticia()
                visualizacao = noticias.get_visualizacaoNoticia()

                listaMaisCurtida.append(Noticia(id,titulo,descricao,publicacao,curtidas,img,video,visualizacao))
    return listaMaisCurtida

@app.route('/')
def home():
        return render_template("index.html", noticias = listarNoticiasCurtidas() , estados=lista_estados)

@app.route("/estado/<siglaEstado>")
def exibir_estado(siglaEstado):
        for estado in lista_estados:
                if estado.get_sigla() == siglaEstado:
                    return render_template("estado.html", estado = estado, noticias = listarNoticiasCurtidas())
        return render_template("index.html", estados=lista_estados)
        
@app.route("/estado/<siglaEstado>/noticia/<int:idNoticia>")
def exibir_noticia(siglaEstado,idNoticia):         
        for noticia in lista_noticias:
            if noticia.get_idNoticia() == idNoticia:
                return render_template("noticia.html",estado = lista_estados , noticia = noticia)
        return render_template("estados.html", noticias = lista_noticias[idNoticia])