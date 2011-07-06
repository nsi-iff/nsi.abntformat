#coding:utf-8

class ReferenciaBibliografica:
    def __init__(self):
        pass

    def _monta_nome(self, autores):
        lista_autores = autores.split(';')
        for i in xrange(len(lista_autores)):
            nome_autor = lista_autores[i].split(' ')
            if nome_autor.__contains__(''):
                nome_autor.remove('')
            nome_abnt = nome_autor.pop(len(nome_autor) - 1).upper() + ','
            for j in xrange(len(nome_autor)):
                nome_abnt += ' ' + nome_autor[j][:1:] + '.'
            lista_autores[i] = nome_abnt
        return "; ".join(lista_autores)

    def _referencia_trabalho_conclusao(self, trabalho_conclusao):
        referencia = self._monta_nome(trabalho_conclusao.autores)
        referencia += ' ' + trabalho_conclusao.titulo
        if trabalho_conclusao.subtitulo != None:
            referencia += ': '
            referencia += trabalho_conclusao.subtitulo
        referencia += '. '
        referencia += trabalho_conclusao.data_defesa + '. '
        referencia += trabalho_conclusao.total_folhas + ' f. '
        referencia += trabalho_conclusao.tipo_trabalho + ' - '
        referencia += trabalho_conclusao.instituicao + ', '
        referencia += trabalho_conclusao.local_defesa + '.'
        return referencia

    def _referencia_artigo_anais_evento(self, artigo_anais_evento):
        referencia = self._monta_nome(artigo_anais_evento.autores)
        referencia += ' ' + artigo_anais_evento.titulo
        if artigo_anais_evento.subtitulo != None:
            referencia += ': '
            referencia += artigo_anais_evento.subtitulo
        referencia += '. In: '
        referencia += artigo_anais_evento.nome_evento + ', '
        referencia += artigo_anais_evento.numero_evento + '., '
        referencia += artigo_anais_evento.ano_evento + ', '
        referencia += artigo_anais_evento.local_evento + '. '
        referencia += artigo_anais_evento.titulo_anais + '. '
        referencia += artigo_anais_evento.local_publicacao + ': '
        referencia += artigo_anais_evento.editora + ', '
        referencia += artigo_anais_evento.ano_publicacao + '. '
        referencia += 'P. ' + artigo_anais_evento.pagina_inicial + '-' + \
            artigo_anais_evento.pagina_final + '.'
        return referencia

    def _referencia_artigo_periodico(self, artigo_periodico):
        referencia = self._monta_nome(artigo_periodico.autores)
        referencia += ' ' + artigo_periodico.titulo
        if artigo_periodico.subtitulo != None:
            referencia += ': '
            referencia += artigo_periodico.subtitulo
        referencia += '. '
        referencia += artigo_periodico.nome_periodico + ', '
        referencia += artigo_periodico.local_publicacao + ', '
        referencia += 'v. ' + artigo_periodico.volume + ', '
        referencia += 'n. ' + artigo_periodico.fasciculo + ', '
        referencia += 'p. ' + artigo_periodico.pagina_inicial + '-' + \
            artigo_periodico.pagina_final + ', '
        referencia += artigo_periodico.data_publicacao + '.'
        return referencia

    def _referencia_periodico_tecnico_cientifico(self, periodico_tecnico_cientifico):
        referencia = periodico_tecnico_cientifico.titulo + '. '
        referencia += periodico_tecnico_cientifico.local_publicacao + ': '
        referencia += periodico_tecnico_cientifico.editora + ', '
        referencia += periodico_tecnico_cientifico.ano_primeiro_volume + '-'
        if periodico_tecnico_cientifico.ano_ultimo_volume != None:
            referencia += periodico_tecnico_cientifico.ano_ultimo_volume + '.'
        return referencia

    def _referencia_livro(self, livro):
        referencia = self._monta_nome(livro.autores)
        referencia += ' ' + livro.titulo
        if livro.subtitulo != None:
            referencia += ': '
            referencia += livro.subtitulo
        referencia += '. '
        if livro.traducao != None:
            referencia += livro.traducao + '. '
        if livro.edicao != None:
            referencia += livro.edicao + '. '
        referencia += livro.local_publicacao + ': '
        referencia += livro.editora + ', '
        referencia += livro.ano_publicacao + '. '
        referencia += livro.numero_paginas + ' p.'
        return referencia

    def _referencia_relatorio_tecnico_cientifico(self, relatorio_tecnico_cientifico):
        referencia = self._monta_nome(relatorio_tecnico_cientifico.autores)
        referencia += ' ' + relatorio_tecnico_cientifico.titulo + '. '
        referencia += relatorio_tecnico_cientifico.local_publicacao + ': '
        referencia += relatorio_tecnico_cientifico.instituicao + ', '
        referencia += relatorio_tecnico_cientifico.ano_publicacao + '. '
        referencia += relatorio_tecnico_cientifico.numero_paginas + ' p.'
        return referencia

    def gera_referencia(self, documento):
        if documento.tipo == 'trabalho de conclusão':
            return self._referencia_trabalho_conclusao(documento)
        elif documento.tipo == 'artigo de anais de eventos':
            return self._referencia_artigo_anais_evento(documento)
        elif documento.tipo == 'artigo de periodico':
            return self._referencia_artigo_periodico(documento)
        elif documento.tipo == 'periodico tecnico cientifico':
            return self._referencia_periodico_tecnico_cientifico(documento)
        elif documento.tipo == 'livro':
            return self._referencia_livro(documento)
        elif documento.tipo == 'relatorio tecnico cientifico':
            return self._referencia_relatorio_tecnico_cientifico(documento)

