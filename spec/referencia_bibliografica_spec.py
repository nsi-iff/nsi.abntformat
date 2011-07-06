#coding:utf-8

import unittest
from ludibrio import Stub
from should_dsl import should
from nsi.abntformat import ReferenciaBibliografica


class ReferenciaBibliograficaSpec(unittest.TestCase):

    def test_converte_nome_completo_em_citacao(self):
        referencia = ReferenciaBibliografica()
        referencia._monta_nome('Ruhan Ferreira Almeida; Carlos Souza Teste') \
            |should| equal_to ('ALMEIDA, R. F.; TESTE, C. S.')

    def test_gera_referencia_para_trabalho_de_conclusao(self):
        referencia = ReferenciaBibliografica()
        with Stub() as trabalho_conclusao:
            trabalho_conclusao.tipo >> 'trabalho de conclusão'
            trabalho_conclusao.autores >> 'Ian Fantucci'
            trabalho_conclusao.titulo >> 'Contribuição do alerta, da atenção, '\
                'da intenção e da expectativa temporal para o desempenho de '\
                'humanos em tarefas de tempo de reação'
            trabalho_conclusao.subtitulo >> None
            trabalho_conclusao.data_defesa >> '2001'
            trabalho_conclusao.total_folhas >> '130'
            trabalho_conclusao.tipo_trabalho >> 'Tese (Doutorado em Psicologia)'
            trabalho_conclusao.instituicao >> 'Instituto de Psicologia, '\
                                              'Universidade de São Paulo'
            trabalho_conclusao.local_defesa >> 'São Paulo'
        referencia_abnt = referencia.gera_referencia(trabalho_conclusao)
        referencia_abnt |should| equal_to(
            'FANTUCCI, I. Contribuição do alerta, da atenção, da intenção e da'
            ' expectativa temporal para o desempenho de humanos em tarefas de '
            'tempo de reação. 2001. 130 f. Tese (Doutorado em Psicologia) - '
            'Instituto de Psicologia, Universidade de São Paulo, São Paulo.')

    def test_gera_referencia_de_artigo_de_anais_de_evento(self):
        referencia = ReferenciaBibliografica()
        with Stub() as artigo_anais_evento:
            artigo_anais_evento.tipo >> 'artigo de anais de eventos'
            artigo_anais_evento.autores >> 'Antônio Fernandes Bueno Moreira'
            artigo_anais_evento.titulo >> 'Multiculturalismo, Currículo e '\
                                          'Formação de Professores'
            artigo_anais_evento.subtitulo >> None
            artigo_anais_evento.nome_evento >> 'SEMINÁRIO DE EDUCAÇÃO BÁSICA'
            artigo_anais_evento.numero_evento >> '2'
            artigo_anais_evento.ano_evento >> '1998'
            artigo_anais_evento.local_evento >> 'Santa Cruz do Sul'
            artigo_anais_evento.titulo_anais >> 'Anais'
            artigo_anais_evento.local_publicacao >> 'Santa Cruz do Sul'
            artigo_anais_evento.editora >> 'EDUNISC'
            artigo_anais_evento.ano_publicacao >> '1998'
            artigo_anais_evento.pagina_inicial >> '15'
            artigo_anais_evento.pagina_final >> '30'
        referencia_abnt = referencia.gera_referencia(artigo_anais_evento)
        referencia_abnt |should| equal_to(
            'MOREIRA, A. F. B. Multiculturalismo, Currículo e Formação de '
            'Professores. In: SEMINÁRIO DE EDUCAÇÃO BÁSICA, 2., 1998, Santa '
            'Cruz do Sul. Anais. Santa Cruz do Sul: EDUNISC, 1998. P. 15-30.')

    def test_gera_referencia_de_artigo_de_periodico(self):
        referencia = ReferenciaBibliografica()
        with Stub() as artigo_periodico:
            artigo_periodico.tipo >> 'artigo de periodico'
            artigo_periodico.autores >> 'Demerval Saviani'
            artigo_periodico.titulo >> 'A Universidade e a Problemática da '\
                                       'Educação e Cultura'
            artigo_periodico.subtitulo >> None
            artigo_periodico.nome_periodico >> 'Educação Brasileira'
            artigo_periodico.local_publicacao >> 'Brasília'
            artigo_periodico.volume >> '1'
            artigo_periodico.fasciculo >> '3'
            artigo_periodico.pagina_inicial >> '35'
            artigo_periodico.pagina_final >> '58'
            artigo_periodico.data_publicacao >> '1979'
        referencia_abnt = referencia.gera_referencia(artigo_periodico)
        referencia_abnt |should| equal_to(
            'SAVIANI, D. A Universidade e a Problemática da Educação e Cultura.'\
            ' Educação Brasileira, Brasília, v. 1, n. 3, p. 35-58, 1979.')

    def test_gera_referencia_de_periodico_tecnico_cientifico(self):
        referencia = ReferenciaBibliografica()
        with Stub() as periodico_tecnico_cientifico:
            periodico_tecnico_cientifico.tipo >> 'periodico tecnico cientifico'
            periodico_tecnico_cientifico.titulo >> 'EDUCAÇÃO & REALIDADE'
            periodico_tecnico_cientifico.local_publicacao >> 'Porto Alegre'
            periodico_tecnico_cientifico.editora >> 'UFRGS/FACED'
            periodico_tecnico_cientifico.ano_primeiro_volume >> '1975'
            periodico_tecnico_cientifico.ano_ultimo_volume >> None
        referencia_abnt = referencia.gera_referencia(periodico_tecnico_cientifico)
        referencia_abnt |should| equal_to('EDUCAÇÃO & REALIDADE. Porto Alegre:'\
                                          ' UFRGS/FACED, 1975-')

    def test_gera_referencia_de_livro(self):
        referencia = ReferenciaBibliografica()
        with Stub() as livro:
            livro.tipo >> 'livro'
            livro.autores >> 'Marcos Antônio Azevedo; '\
                             'Vinícios Nogueira Almeida Guerra'
            livro.titulo >> 'Mania de bater'
            livro.subtitulo >> 'a punição corporal doméstica de crianças '\
                               'e adolescentes no Brasil'
            livro.traducao >> None
            livro.edicao >> None
            livro.local_publicacao >> 'São Paulo'
            livro.editora >> 'Iglu'
            livro.ano_publicacao >> '2001'
            livro.numero_paginas >> '386'
        referencia_abnt = referencia.gera_referencia(livro)
        referencia_abnt |should| equal_to('AZEVEDO, M. A.; GUERRA, V. N. A. '
            'Mania de bater: a punição corporal doméstica de crianças e '
            'adolescentes no Brasil. São Paulo: Iglu, 2001. 386 p.')

    def test_gera_referencia_de_relatorio_tecnico_cientifico(self):
        referencia = ReferenciaBibliografica()
        with Stub() as relatorio_tecnico_cientifico:
            relatorio_tecnico_cientifico.tipo >> 'relatorio tecnico cientifico'
            relatorio_tecnico_cientifico.autores >> 'Ubiraci Espinelli Souza; '\
                                                    'Silvio Burratino Melhado'
            relatorio_tecnico_cientifico.titulo >> 'Subsídios para a avaliação'\
                ' do custo de mão-de-obra na construção civil'
            relatorio_tecnico_cientifico.local_publicacao >> 'São Paulo'
            relatorio_tecnico_cientifico.instituicao >> 'EPUSP'
            relatorio_tecnico_cientifico.ano_publicacao >> '1991'
            relatorio_tecnico_cientifico.numero_paginas >> '38'
        referencia_abnt = referencia.gera_referencia(relatorio_tecnico_cientifico)
        referencia_abnt |should| equal_to(
            'SOUZA, U. E.; MELHADO, S. B. Subsídios para a avaliação do '
            'custo de mão-de-obra na construção civil. São Paulo: EPUSP, 1991. '
            '38 p.')


if __name__ == '__main__':
    unittest.main()

