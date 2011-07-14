#coding:utf-8

class ReferenciaBibliografica:

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
        return '%(autores)s %(titulo)s%(subtitulo)s. %(defesa)s. '\
                '%(folhas)s f. %(tipo)s - %(instituicao)s, %(local)s.' % {
            'autores': self._monta_nome(trabalho_conclusao.autores),
            'titulo': trabalho_conclusao.titulo,
            'subtitulo': self._gerar_subtitulo(trabalho_conclusao),
            'defesa': trabalho_conclusao.data_defesa,
            'folhas': trabalho_conclusao.total_folhas,
            'tipo': trabalho_conclusao.tipo_trabalho,
            'instituicao': trabalho_conclusao.instituicao,
            'local': trabalho_conclusao.local_defesa }

    def _referencia_artigo_anais_evento(self, artigo_anais_evento):
        return '%(autores)s %(titulo)s%(subtitulo)s. In: %(nome_evento)s, ' \
                '%(numero_evento)s., %(ano_evento)s, %(local_evento)s. ' \
                '%(titulo_anais)s. %(local_publicacao)s: %(editora)s, ' \
                '%(ano_publicacao)s. P. %(pagina_inicial)s-%(pagina_final)s.' % {
            'autores': self._monta_nome(artigo_anais_evento.autores),
            'titulo': artigo_anais_evento.titulo,
            'subtitulo': self._gerar_subtitulo(artigo_anais_evento),
            'nome_evento': artigo_anais_evento.nome_evento,
            'numero_evento': artigo_anais_evento.numero_evento,
            'ano_evento': artigo_anais_evento.ano_evento,
            'local_evento': artigo_anais_evento.local_evento,
            'titulo_anais': artigo_anais_evento.titulo_anais,
            'local_publicacao': artigo_anais_evento.local_publicacao,
            'editora': artigo_anais_evento.editora,
            'ano_publicacao': artigo_anais_evento.ano_publicacao,
            'pagina_inicial': artigo_anais_evento.pagina_inicial,
            'pagina_final': artigo_anais_evento.pagina_final }

    def _referencia_artigo_periodico(self, artigo_periodico):
        return '%(autores)s %(titulo)s%(subtitulo)s. %(nome)s, %(local)s, ' \
                'v. %(volume)s, n. %(fasciculo)s, ' \
                'p. %(pagina_inicial)s-%(pagina_final)s, %(data)s.' % {
            'autores': self._monta_nome(artigo_periodico.autores),
            'titulo': artigo_periodico.titulo,
            'subtitulo': self._gerar_subtitulo(artigo_periodico),
            'nome': artigo_periodico.nome_periodico,
            'local': artigo_periodico.local_publicacao,
            'volume': artigo_periodico.volume,
            'fasciculo': artigo_periodico.fasciculo,
            'pagina_inicial': artigo_periodico.pagina_inicial,
            'pagina_final': artigo_periodico.pagina_final,
            'data': artigo_periodico.data_publicacao }

    def _referencia_periodico_tecnico_cientifico(self, periodico_tecnico_cientifico):
        return '%(titulo)s. %(local)s: %(editora)s, ' \
                '%(ano_primeiro)s-%(ano_ultimo)s' % {
            'titulo': periodico_tecnico_cientifico.titulo,
            'local': periodico_tecnico_cientifico.local_publicacao,
            'editora': periodico_tecnico_cientifico.editora,
            'ano_primeiro': periodico_tecnico_cientifico.ano_primeiro_volume,
            'ano_ultimo': periodico_tecnico_cientifico.ano_ultimo_volume or '' }

    def _referencia_livro(self, livro):
        return '%(autores)s %(titulo)s%(subtitulo)s. %(traducao)s%(edicao)s' \
                '%(publicacao)s: %(editora)s, %(ano)s. %(paginas)s p.' % {
            'autores': self._monta_nome(livro.autores),
            'titulo': livro.titulo,
            'subtitulo': self._gerar_subtitulo(livro),
            'traducao': self._gerar_opcional(livro.traducao, '%s. '),
            'edicao': self._gerar_opcional(livro.edicao, '%s. '),
            'publicacao': livro.local_publicacao,
            'editora': livro.editora,
            'ano': livro.ano_publicacao,
            'paginas': livro.numero_paginas }

    def _referencia_relatorio_tecnico_cientifico(self, relatorio_tecnico_cientifico):
        return '%(autores)s %(titulo)s. %(local)s: %(instituicao)s, %(ano)s. ' \
                '%(paginas)s p.' % {
            'autores': self._monta_nome(relatorio_tecnico_cientifico.autores),
            'titulo': relatorio_tecnico_cientifico.titulo,
            'local': relatorio_tecnico_cientifico.local_publicacao,
            'instituicao': relatorio_tecnico_cientifico.instituicao,
            'ano': relatorio_tecnico_cientifico.ano_publicacao,
            'paginas': relatorio_tecnico_cientifico.numero_paginas }

    def _referencia_imagem(self, imagem):
        return '%(autores)s %(titulo)s. %(instituicao)s, %(local)s.' % {
            'autores': self._monta_nome(imagem.autores),
            'titulo': imagem.titulo,
            'instituicao': imagem.instituicao,
            'local': imagem.local }

    def _referencia_objetos_de_aprendizagem(self, objetos_de_aprendizagem):
        return '%(autores)s %(titulo)s. %(instituicao)s.' % {
            'autores': self._monta_nome(objetos_de_aprendizagem.autores),
            'titulo': objetos_de_aprendizagem.titulo,
            'instituicao': objetos_de_aprendizagem.instituicao }

    def _referencia_outros_conteudos(self, outros_conteudos):
        return '%(autores)s %(titulo)s. %(instituicao)s.' % {
            'autores': self._monta_nome(outros_conteudos.autores),
            'titulo': outros_conteudos.titulo,
            'instituicao': outros_conteudos.instituicao }

    def gerar(self, documento):
        conversores = {
            'trabalho de conclusão': self._referencia_trabalho_conclusao,
            'artigo de anais de eventos': self._referencia_artigo_anais_evento,
            'artigo de periodico': self._referencia_artigo_periodico,
            'periodico tecnico cientifico': self._referencia_periodico_tecnico_cientifico,
            'livro':self._referencia_livro,
            'relatorio tecnico cientifico': self._referencia_relatorio_tecnico_cientifico,
            'imagem': self._referencia_imagem,
            'objetos de aprendizagem': self._referencia_objetos_de_aprendizagem,
            'outros conteúdos': self._referencia_outros_conteudos }
        converter = conversores[documento.tipo]
        return converter(documento)

    def _gerar_subtitulo(self, documento):
        return self._gerar_opcional(documento.subtitulo, ': %s')

    def _gerar_opcional(self, texto, string):
        if texto is None:
            return ''
        return string % texto

